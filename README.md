# Agent Builder Template

A starter folder for building your own AI **agent** in any AI-enabled code editor —
**no coding required**. You build the whole thing just by chatting with an AI assistant.

> **Works with any IDE and any LLM.** Use whatever AI-enabled IDE you like — VSCode,
> Cursor, JetBrains, and others — with whatever LLM that IDE supports (Claude, GPT,
> Gemini, and more). This guide uses **Claude in VSCode** as the running example; wherever
> you see "Claude" or "VSCode," substitute your own assistant and editor. The agent's
> rulebook lives in `CLAUDE.md`; if your assistant reads a different filename (for example
> `AGENTS.md`), copy or point it at that file.

## Step 1 — Make your own copy from this template

This is a **GitHub template repository**, so you don't clone it directly — you stamp out
your own copy, already named after your agent:

1. On this repo's GitHub page, click the green **Use this template** button →
   **Create a new repository**.
2. Give the new repository **your agent's name** (e.g. `weekly-sales-bot`), pick
   public or private, and click **Create repository**. GitHub makes a brand-new repo with
   that name and a clean history — not a fork of the template.
3. **Clone** (download) your new repo to your computer — via your IDE's *Clone
   Repository* command (in VSCode: *Source Control → Clone Repository*), or run
   `git clone <your-new-repo-url>`.

Because you named the repo up front, your folder already carries your agent's name — no
renaming needed later.

> No GitHub account? You can instead run `git clone
> https://github.com/kiran-criodo/agent-builder-template.git your-agent-name` to download
> the starter into a folder named after your agent, and add an online home for it later.

## Step 2 — Start building

Open your new folder in your AI-enabled IDE (e.g. VSCode with the Claude extension),
make sure the AI assistant is connected, and type:

> **Let's start Building**

Your assistant will then interview you step by step and create everything for you.

## What's here

- **`CREATE_AGENT_PROCESS.md`** — the full, plain-English guide. Read it first if you
  like, or just say "Let's start Building" and follow along.
- **`CLAUDE.md`** — the agent's rulebook. It also contains the guided-build instructions
  your assistant follows while helping you. (If your assistant reads a different filename,
  such as `AGENTS.md`, copy or point it at this file.)
- **`docs/SETUP.md`** — how to set up your computer (one-time).
- **`docs/CONNECTORS.md`** — connecting your agent to outside services (cloud drive,
  email, databases, WhatsApp, MCP servers) for input *and* output.
- **`docs/GIT_GUIDE.md`** — sharing your agent with others, in plain language.
- Folders (`workflows/`, `tools/`, `memory/`, …) — the agent's parts, filled in as you
  build.

## New to this?

Start with [`CREATE_AGENT_PROCESS.md`](CREATE_AGENT_PROCESS.md). It explains what an
agent is and walks you through building one from scratch.
