"""Write a one-page markdown snapshot of a public GitHub repository.

Usage:
    python3 repo_snapshot.py owner/name [--out-dir output]

The fetch goes through the read-only session in tools/_guardrails.py. The summary
logic (`summarise`) is a pure function, so it can be tested without a network.
"""

import argparse
import datetime as dt
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "tools"))

from _guardrails import session  # noqa: E402

API = "https://api.github.com/repos/{}"


def parse_repo(text: str) -> str:
    """Accept 'owner/name' or a github.com URL; return 'owner/name'."""
    m = re.search(r"(?:github\.com/)?([\w.-]+)/([\w.-]+?)(?:\.git)?/?$", text.strip())
    if not m:
        raise ValueError(f"Not a GitHub repo: {text!r}. Use owner/name.")
    return f"{m.group(1)}/{m.group(2)}"


def fetch(repo: str) -> dict:
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    resp = session().get(API.format(repo), headers=headers, timeout=30)
    if resp.status_code == 404:
        raise SystemExit(f"Repository {repo} not found (or it's private).")
    if resp.status_code == 403:
        raise SystemExit("GitHub rate limit reached. Add GITHUB_TOKEN to .env or try later.")
    resp.raise_for_status()
    return resp.json()


def activity_label(pushed_at: str, today: dt.date) -> str:
    days = (today - dt.date.fromisoformat(pushed_at[:10])).days
    if days <= 30:
        return f"active (last push {days} days ago)"
    if days <= 180:
        return f"quiet (last push {days} days ago)"
    return f"dormant (last push {days} days ago)"


def summarise(repo: dict, today: dt.date) -> str:
    """Turn the GitHub API's repo JSON into a markdown snapshot."""
    licence = (repo.get("license") or {}).get("spdx_id") or "none"
    topics = ", ".join(repo.get("topics") or []) or "none"
    lines = [
        f"# Snapshot: {repo['full_name']}",
        "",
        repo.get("description") or "_No description set._",
        "",
        "| | |",
        "|---|---|",
        f"| Stars | {repo.get('stargazers_count', 0)} |",
        f"| Forks | {repo.get('forks_count', 0)} |",
        f"| Open issues | {repo.get('open_issues_count', 0)} |",
        f"| Main language | {repo.get('language') or 'n/a'} |",
        f"| Licence | {licence} |",
        f"| Topics | {topics} |",
        f"| Template repo | {'yes' if repo.get('is_template') else 'no'} |",
        f"| Activity | {activity_label(repo['pushed_at'], today)} |",
        "",
        f"Source: {repo['html_url']} (fetched {today.isoformat()})",
    ]
    if licence == "none":
        lines += ["", "> Note: no licence file, so others can't legally reuse this code."]
    return "\n".join(lines) + "\n"


def main(argv=None) -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("repo", help="owner/name or a github.com URL")
    ap.add_argument("--out-dir", default=os.path.join(ROOT, "output"))
    args = ap.parse_args(argv)

    repo = parse_repo(args.repo)
    today = dt.date.today()
    text = summarise(fetch(repo), today)

    os.makedirs(args.out_dir, exist_ok=True)
    path = os.path.join(args.out_dir, f"repo-snapshot-{repo.replace('/', '-')}-{today}.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(text)
    print(f"Saved to {path}")


if __name__ == "__main__":
    main()
