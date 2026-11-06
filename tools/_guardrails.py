"""
Read-only guardrails: a reference pattern for agents that should only *observe*.

Many useful agents (reporting, auditing, Q&A over company data) must never change
anything in the systems they read. Saying so in CLAUDE.md is good; enforcing it in
code is better, because an assistant writing a new tool at 11pm won't always
remember the rule. This module puts the rule *below* every tool:

  1. HTTP  - `session()` returns a requests.Session that refuses any method other
             than GET / HEAD / OPTIONS. A few read APIs use POST for searches; add
             those exact endpoints to READ_ONLY_POST_ALLOWLIST, each with a comment.
  2. SQL   - `assert_read_only_sql()` passes a single SELECT / SHOW / DESCRIBE /
             EXPLAIN / WITH statement and rejects anything containing a write keyword.
  3. AWS   - `readonly_boto3_session()` (optional; needs boto3) blocks any AWS API
             operation that isn't a known read verb, for every client and service.

A blocked call raises `ReadOnlyViolation` and stops the run. It is deliberately loud:
a guardrail that silently skips work would hide bugs.

This is a second layer, not a substitute for read-only credentials. Scope your API
keys and database users to read-only as well (defence in depth).

Using it in a tool:

    from _guardrails import session, assert_read_only_sql

    http = session()
    data = http.get("https://api.example.com/items", timeout=30).json()

    assert_read_only_sql(query)
    cursor.execute(query)

Agents that are *meant* to write (send email, create tickets) should not use this
module for those calls. Give them an explicit, reviewed write path instead.
"""

import re
from urllib.parse import urlparse

import requests


class ReadOnlyViolation(RuntimeError):
    """Raised when a tool attempts an operation that could change remote state."""


# ------------------------------------------------------------------ HTTP

READ_METHODS = frozenset({"GET", "HEAD", "OPTIONS"})

# (host contains, path contains) for POST endpoints that only ever read.
# Keep this list short and specific: every entry is a hole in the guardrail.
# Example:
#   ("api.example.com", "/v1/search"),   # search is POST-only, returns results only
READ_ONLY_POST_ALLOWLIST: list[tuple[str, str]] = []


def _post_is_allowlisted(url: str) -> bool:
    parsed = urlparse(url)
    host, path = (parsed.hostname or "").lower(), parsed.path or ""
    return any(h in host and seg in path for h, seg in READ_ONLY_POST_ALLOWLIST)


class ReadOnlySession(requests.Session):
    """A requests.Session that refuses state-changing calls.

    Every helper (get, post, put, ...) funnels through `request`, so overriding
    this one method guards them all.
    """

    def request(self, method, url, *args, **kwargs):
        verb = (method or "").upper()
        if verb not in READ_METHODS and not (verb == "POST" and _post_is_allowlisted(url)):
            raise ReadOnlyViolation(
                f"Blocked {verb} {urlparse(url).path or url}\n"
                "  This agent is read-only. If this endpoint genuinely only reads, add it "
                "to READ_ONLY_POST_ALLOWLIST in tools/_guardrails.py with a comment saying why."
            )
        return super().request(verb, url, *args, **kwargs)


def session() -> ReadOnlySession:
    """Return a guarded HTTP session. Use this instead of `requests` in every tool."""
    return ReadOnlySession()


# ------------------------------------------------------------------ SQL

SQL_READ_PREFIXES = ("SELECT", "SHOW", "DESCRIBE", "DESC", "EXPLAIN", "WITH")

# A WITH ... or SELECT ... can still hide a write in some databases
# (e.g. a data-modifying CTE, or SELECT ... INTO). Reject these words anywhere.
# Statements that *start* with a write verb are already caught by the prefix check.
SQL_WRITE_KEYWORDS = (
    "INSERT", "UPDATE", "DELETE", "MERGE", "DROP", "ALTER",
    "CREATE", "TRUNCATE", "GRANT", "REVOKE", "INTO",
)
_WRITE_RE = re.compile(r"\b(" + "|".join(SQL_WRITE_KEYWORDS) + r")\b", re.IGNORECASE)
_STRINGS_AND_COMMENTS = re.compile(r"'(?:[^']|'')*'|\"[^\"]*\"|--[^\n]*|/\*.*?\*/", re.DOTALL)


def assert_read_only_sql(query: str) -> None:
    """Raise ReadOnlyViolation unless `query` is a single read statement."""
    # Ignore words inside string literals and comments, e.g. WHERE note = 'please update'.
    code = _STRINGS_AND_COMMENTS.sub(" ", query or "")
    flat = " ".join(code.split()).rstrip(";").strip()
    if not flat:
        raise ReadOnlyViolation("Blocked empty SQL statement.")
    if ";" in flat:
        raise ReadOnlyViolation(f"Blocked multi-statement SQL: {flat[:120]}")
    if not flat.upper().startswith(SQL_READ_PREFIXES):
        raise ReadOnlyViolation(
            f"Blocked non-read SQL: {flat[:120]}\n"
            f"  Only {', '.join(SQL_READ_PREFIXES)} statements are permitted."
        )
    hit = _WRITE_RE.search(flat)
    if hit:
        raise ReadOnlyViolation(f"Blocked SQL containing write keyword {hit.group(1).upper()}: {flat[:120]}")


# ------------------------------------------------------------------ AWS (optional)

AWS_READ_PREFIXES = (
    "Describe", "Get", "List", "Head", "Query", "Scan", "BatchGet",
    "Lookup", "Search", "Estimate", "Preview", "Validate", "Simulate", "Check",
)
# Names that pass the prefix test but shouldn't be allowed.
AWS_DENY = frozenset({
    "GetSessionToken",       # mints new credentials
    "GetFederationToken",
    "SelectObjectContent",   # runs server-side code against objects
})


def readonly_boto3_session(**kwargs):
    """A boto3 Session whose clients can only perform read operations.

    The hook fires before every API call from any client this session creates,
    so a new client can't quietly gain write access. Requires `pip install boto3`.
    """
    import boto3  # imported here so agents that don't use AWS don't need boto3

    sess = boto3.Session(**kwargs)

    def _block_writes(model, **_):
        op = model.name
        if op in AWS_DENY or not op.startswith(AWS_READ_PREFIXES):
            raise ReadOnlyViolation(
                f"Blocked AWS operation {model.service_model.service_name}:{op}\n"
                "  This agent is read-only."
            )

    sess.events.register("before-call.*.*", _block_writes)
    return sess
