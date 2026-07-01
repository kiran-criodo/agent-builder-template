# Connectors — Plugging Your Agent Into Outside Services

Your agent is **not limited to files on your computer**. Both the **input** it reads and
the **output** it produces can come from — or go to — an outside service. That service
might be a **cloud drive**, an **email account**, a **database**, a **messaging app**, a
notes tool, or any **MCP server**.

This page explains the two ways to connect, what's available out of the box, and how the
agent decides which to use.

---

## The two ways to connect

**1. A ready-made connector (easiest — usually no code)**
Some services already have a connector the agent can use. You just **authorize** it once
by signing in; after that, the agent reads and writes through it. No scripts, and usually
no keys to paste anywhere.

**2. A small script in `tools/` (for anything without a ready connector)**
For services that don't have a drop-in connector, the agent writes a short script that
calls the service's API. Your login key/token goes in **`.env`** (kept private, never
shared) and its *name* goes in **`.env.example`** so others know what they'd need.

> **What's an MCP server?** MCP (Model Context Protocol) is an open standard for plugging a
> tool or service into an AI assistant — supported by Claude and a growing number of other
> assistants/IDEs. Many ready-made connectors are MCP servers under the hood. If a service
> offers an MCP server, that's the clean "ready-made connector" path.

---

## Input *and* output can both be connectors

A workflow doesn't need any file on disk. For example, an agent could:

- read a spreadsheet **from Google Drive**,
- enrich it with rows **from a database**,
- and send the result **as an email** or **a WhatsApp message**.

Saving to the `output/` folder is just *one* option for output — not a requirement.

---

## Commonly available ready-made connectors

These are typically available to authorize (sign in once). **Which connectors exist and
where you turn them on depends on your assistant/IDE.** For Claude, check your **claude.ai
connector settings**, or `claude mcp` / `/mcp` in an interactive Claude Code session; other
assistants have their own connector/MCP settings.

| Service | Typical use |
|---|---|
| **Google Drive** | Read/write files and spreadsheets in Drive |
| **Gmail** | Read and send email |
| **Google Calendar** | Read/create calendar events |
| **Notion** | Read/write pages and databases |

> **Authorizing needs an interactive session.** The sign-in (OAuth) flow can't run in a
> non-interactive/automated session. Authorize the connector once in an interactive session
> of your assistant (for Claude: an interactive Claude Code session or your claude.ai
> connector settings); after that the agent uses it normally.

---

## Services that use a script (`tools/` + a key in `.env`)

When there's no ready connector, the agent writes a script. Common examples:

| Service | How it connects | What you provide |
|---|---|---|
| **OneDrive** | Microsoft Graph API | Register an app in Azure; put the token/keys in `.env` |
| **Email (any provider)** | SMTP (send) / IMAP (read) | Host, username, app password in `.env` |
| **Databases** (Postgres, MySQL, etc.) | Official DB driver | Connection string / credentials in `.env` |
| **WhatsApp** | WhatsApp Business API (Meta) or Twilio | Business number + API token in `.env` — see caveat below |

**⚠️ WhatsApp caveat.** There is **no official API for a personal WhatsApp account**.
Sending/receiving programmatically requires the **WhatsApp Business API** (via Meta or a
provider like Twilio) — a business phone number and API credentials. Plan for that setup
if WhatsApp is part of your workflow.

---

## How the agent chooses (Step 2 of the build)

During **Step 2 — Connections & secrets**, for each service the agent:

1. Checks for a **ready-made connector / MCP server**. If one exists → use it, and have
   you authorize it. No code.
2. Otherwise → write a small script in **`tools/`**, add the key *name* to
   **`.env.example`**, and tell you where to paste the real value into **`.env`**. Note
   any required software in **`requirements.txt`**.

Secrets **only** ever live in `.env` (or `config/` for credential files) — never in any
file that gets shared. See `docs/GIT_GUIDE.md`.
