# Agent Builder Template

**Build a working AI agent by describing it, not coding it.** Open this template in any
AI-enabled IDE, type *"Let's start Building"*, and your assistant interviews you, then writes
the agent's rulebook, workflows, tools and tests with you, one reviewed step at a time.

**Who it's for:** domain experts and teams (ops, quality, sales, analytics, engineering)
who want a dependable agent for their own work without waiting in an engineering queue.

**Why it works:** every agent gets the same structure. That's a written contract
(`CLAUDE.md`), plain-English **W**orkflows, an **A**ssistant that follows them, and small
**T**ools for the deterministic parts. Agents stay predictable, reviewable and easy to hand
over.

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

More on the design in [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Built with this template

| Agent | What it does | |
|---|---|---|
| [Requirements to Model Validator](https://github.com/kiran-criodo/requirements_to_model_validator) | Audits Simulink models against requirements, with ISO 26262 / ASPICE cross-checks and a punch-list ranked by ASIL × program stage | Public. Built live on stage for automotive engineering leaders |
| [FMEA Agent](https://github.com/kiran-criodo/FMEA_Agent) | Drafts, reuses, rating-checks and prioritises PFMEAs, and recommends actions, with an engineer approving every draft | Public. Built live on stage for automotive engineering leaders |
| Organisation data agent | Plain-English answers over 10+ company systems (AWS, Azure, GCP, GitLab, Bitbucket, Google Workspace, CRM, helpdesk, chat, project tracking), read-only and enforced in code | Private |
| Learner journey agent | Rebuilds one customer's full history across every system into a redacted, evidence-linked timeline | Private |

## What's in the box

- **A guided build.** `CLAUDE.md` Part A walks the assistant through 9 steps, from naming the
  agent to its first tested workflow.
- **A contract for the finished agent.** `CLAUDE.md` Part B holds its purpose, rules and
  request routing.
- **Read-only guardrails in code.** [`tools/_guardrails.py`](tools/_guardrails.py) blocks
  HTTP writes, write SQL and write AWS calls for agents that should only observe. It comes
  with tests in [`tests/test_guardrails.py`](tests/test_guardrails.py).
- **A worked example.** [`examples/repo-snapshot/`](examples/repo-snapshot/) is a workflow,
  tool and test in about 150 lines.
- **Connectors as first-class inputs and outputs.** Cloud drives, email, databases,
  WhatsApp and any MCP server: see [docs/CONNECTORS.md](docs/CONNECTORS.md).

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

> **Tip — you can schedule it.** Once a workflow works, your agent doesn't have to be run
> by hand every time. Most AI-enabled assistants can run a workflow **periodically** (e.g.
> every morning, or once an hour) — just ask yours in plain English. See *"Running Your
> Agent on a Schedule"* in [`CREATE_AGENT_PROCESS.md`](CREATE_AGENT_PROCESS.md).

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
- **`tools/_guardrails.py`** + **`tests/test_guardrails.py`** — optional read-only
  guardrails for agents that should only observe. Run the tests with
  `python3 -m unittest discover -s tests`.
- **`examples/repo-snapshot/`** — a small, complete example of a workflow, tool and test.

## New to this?

Start with [`CREATE_AGENT_PROCESS.md`](CREATE_AGENT_PROCESS.md). It explains what an
agent is and walks you through building one from scratch.
