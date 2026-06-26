# How This Agent Is Built (Architecture)

This explains how the pieces fit together. You don't need to understand all of it to use
the agent, but it helps when you want to change or extend it.

## The W-A-T idea

Every agent here has three layers:

```
        YOU (describe what you want)
                 │
                 ▼
   ┌───────────────────────────┐
   │   AGENT  (Claude itself)   │   reads CLAUDE.md + memory/, picks the right recipe
   └───────────────────────────┘
        │                     │
        ▼                     ▼
 ┌──────────────┐     ┌──────────────────┐
 │  WORKFLOWS   │     │      TOOLS        │
 │ plain-English│     │ scripts + built-in│
 │   recipes    │     │ actions (files,   │
 │ (the core)   │     │ web, email, data) │
 └──────────────┘     └──────────────────┘
```

- **Workflows** (`workflows/`) — plain-English recipes. This is where most of your agent's
  intelligence lives. Start with one; add more over time.
- **Agent** — Claude reads `CLAUDE.md` (the rulebook) and `memory/` (what it knows), then
  follows the right workflow. You don't build this layer; it's Claude.
- **Tools** (`tools/`) — the actions used while working. Most are built in (read/write
  files, search the web). Some need a small script, which Claude writes for you.

## What each folder is for

| Folder | What it holds |
|--------|----------------|
| `workflows/` | Plain-English recipes the agent follows. The most important folder. |
| `tools/` | Scripts the agent runs (created only when needed). |
| `memory/` | Facts the agent remembers across sessions. |
| `config/` | Private credential files. Never shared. |
| `data/` | Local data the agent works with. Not shared. |
| `output/` | Where results are saved. |
| `resources/` | Reference material you provide (templates, sample data). |
| `tests/` | Quick checks that results are correct. |
| `docs/` | Setup and help documents (you're reading one). |

## Where secrets live

- `.env` — your real keys and passwords. **Private, never shared.**
- `.env.example` — a blank template listing which keys are needed. Safe to share.
- `config/` — credential files (e.g. a downloaded key file). Private, never shared.

## How it's shared

Everything is one folder tracked by **git**. You **commit** (save snapshots) and **push**
(upload) it so others can **clone** (download) and use it. Improvements flow both ways.
See `GIT_GUIDE.md`.

<!-- TODO: as your agent grows, note here anything special about how it works —
     e.g. which services it connects to, or any unusual steps. -->
