# How This Agent Is Built (Architecture)

This explains how the pieces fit together. You don't need to understand all of it to use
the agent, but it helps when you want to change or extend it.

> **Any IDE, any LLM.** This template isn't tied to one editor or one model. It works in
> any AI-enabled IDE (VSCode, Cursor, JetBrains, …) with any LLM that IDE supports (Claude,
> GPT, Gemini, …). Below, "the assistant" means whichever one you use.

## The W-A-T idea

Every agent here has three layers:

```
        YOU (describe what you want)
                 │
                 ▼
   ┌───────────────────────────┐
   │  AGENT (your AI assistant) │   reads CLAUDE.md + memory/, picks the right recipe
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
- **Agent** — your AI assistant reads `CLAUDE.md` (the rulebook) and `memory/` (what it
  knows), then follows the right workflow. You don't build this layer; it's the assistant.
  (If your assistant reads a differently-named rulebook, e.g. `AGENTS.md`, copy or point it
  at `CLAUDE.md`.)
- **Tools & connectors** (`tools/`) — the actions used while working. Most are built in
  (read/write files, search the web). Connections to outside services come from a
  **ready-made connector** you authorize (e.g. Google Drive, Gmail, Notion, or any MCP
  server) or from a small script your assistant writes for you. See `CONNECTORS.md`.

## Input and output aren't limited to files

Both what the agent **reads** and what it **produces** can be a connector — a cloud drive,
an email account, a database, a messaging app (WhatsApp), or any MCP server. A workflow
can read from Google Drive and send the result as an email with no file ever saved to
disk. The `output/` folder is for *file* results; connector destinations are equally
valid. See `CONNECTORS.md` for the full picture and the connector-vs-script decision.

## What each folder is for

| Folder | What it holds |
|--------|----------------|
| `workflows/` | Plain-English recipes the agent follows. The most important folder. |
| `tools/` | Scripts the agent runs (created only when needed). |
| `memory/` | Facts the agent remembers across sessions. |
| `config/` | Private credential files. Never shared. |
| `data/` | Local data the agent works with. Not shared. |
| `output/` | Where *file* results are saved (output can also go to a connector). |
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
