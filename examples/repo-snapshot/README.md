# Worked example: Repo Snapshot

A complete, tiny agent capability you can read in five minutes. It shows all three
W-A-T layers working together on public data:

| Layer | File | What it does |
|---|---|---|
| Workflow | [`workflow.md`](workflow.md) | The plain-English recipe the assistant follows |
| Tool | [`repo_snapshot.py`](repo_snapshot.py) | Fetches a public GitHub repo's stats and writes a one-page summary |
| Test | [`test_repo_snapshot.py`](test_repo_snapshot.py) | Checks the summary logic offline, with no network |

The tool makes its HTTP calls through the read-only session in
[`tools/_guardrails.py`](../../tools/_guardrails.py), so it cannot change anything on GitHub
even by accident.

Try it from the repo root:

```bash
pip install -r requirements.txt
python3 examples/repo-snapshot/repo_snapshot.py kiran-criodo/agent-builder-template
python3 -m unittest discover -s examples/repo-snapshot -v
```

It lives in `examples/` rather than `workflows/` and `tools/` so that a fresh agent built
from this template starts clean. To reuse it, copy `workflow.md` into `workflows/` and the
script into `tools/`.
