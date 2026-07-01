# Agent Builder Template

A starter folder for building your own AI **agent** in VSCode — **no coding required**.
You build the whole thing just by chatting with Claude.

## Step 1 — Make your own copy from this template

This is a **GitHub template repository**, so you don't clone it directly — you stamp out
your own copy, already named after your agent:

1. On this repo's GitHub page, click the green **Use this template** button →
   **Create a new repository**.
2. Give the new repository **your agent's name** (e.g. `weekly-sales-bot`), pick
   public or private, and click **Create repository**. GitHub makes a brand-new repo with
   that name and a clean history — not a fork of the template.
3. **Clone** (download) your new repo to your computer — in VSCode: *Source Control →
   Clone Repository → pick your new repo*, or run `git clone <your-new-repo-url>`.

Because you named the repo up front, your folder already carries your agent's name — no
renaming needed later.

> No GitHub account? You can instead run `git clone
> https://github.com/kiran-criodo/agent-builder-template.git your-agent-name` to download
> the starter into a folder named after your agent, and add an online home for it later.

## Step 2 — Start building

Open your new folder in VSCode with the Claude extension, make sure Claude is connected,
and type:

> **Let's start Building**

Claude will then interview you step by step and create everything for you.

## What's here

- **`CREATE_AGENT_PROCESS.md`** — the full, plain-English guide. Read it first if you
  like, or just say "Let's start Building" and follow along.
- **`CLAUDE.md`** — the agent's rulebook. It also contains the guided-build instructions
  Claude follows while helping you.
- **`docs/SETUP.md`** — how to set up your computer (one-time).
- **`docs/GIT_GUIDE.md`** — sharing your agent with others, in plain language.
- Folders (`workflows/`, `tools/`, `memory/`, …) — the agent's parts, filled in as you
  build.

## New to this?

Start with [`CREATE_AGENT_PROCESS.md`](CREATE_AGENT_PROCESS.md). It explains what an
agent is and walks you through building one from scratch.
