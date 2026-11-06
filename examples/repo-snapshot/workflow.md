# Workflow: Repo Snapshot

## Purpose
Produce a one-page snapshot of a public GitHub repository: what it is, how active it is,
and how much interest it has. Save it as a markdown file.

## When to use
"Give me a snapshot of <owner>/<repo>", "how active is this repo?", "summarise this GitHub project".

## Inputs
- The repository, as `owner/name` or a github.com URL. Ask if it isn't given.
- No credentials needed for public repos. (Optional: a `GITHUB_TOKEN` in `.env` raises the
  rate limit from 60 to 5,000 requests an hour.)

## Steps
1. Confirm the repository name with the user if there's any doubt.
2. Run `python3 tools/repo_snapshot.py <owner/name>` (or `examples/repo-snapshot/repo_snapshot.py`).
3. Read the generated file and give the user a three-line preview plus its location.

## Output
- `output/repo-snapshot-<owner>-<name>-<date>.md`

## Validation (check before showing results)
- The repo name in the file matches what the user asked for.
- Numbers come from the API response; nothing is estimated or invented.
- If the API returned an error (not found, rate-limited), say so plainly; don't write a file.
