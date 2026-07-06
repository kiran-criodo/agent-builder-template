# How to Create an Agent — Step by Step

This is your complete, plain-English guide to building your own AI **agent** — even if
you have never written a line of code. You build the whole thing just by **chatting**
with an AI assistant inside an AI-enabled code editor.

> **Any IDE, any LLM.** This works in whatever AI-enabled IDE you prefer — VSCode, Cursor,
> JetBrains, and others — with whatever LLM that IDE supports (Claude, GPT, Gemini, and
> more). For readability this guide says "Claude" and "VSCode" as the running example;
> read those as **"your AI assistant"** and **"your IDE."** The agent's rulebook lives in
> `CLAUDE.md`; if your assistant reads a different filename (e.g. `AGENTS.md`), copy or
> point it at that file.

There are two ways to use this guide:

- **Just say "Let's start Building."** Your assistant will read this file, then interview
  you one question at a time and create all the files for you. This is the easiest path.
- **Read it yourself first.** If you like understanding things before you start, read
  Parts 1–2 below, then say "Let's start Building" when you're ready.

---

## Part 1 — The Basics (read this once)

### What is an Agent? (and how is it different from an App?)

- An **App** does exactly what it is told, step by step. You press a button, it does
  the one thing. If something unexpected happens, it stops.
- An **Agent** is given a **goal** and figures out **how** to reach it on its own. It
  can read files, search the web, run small scripts, and decide the next step. You tell
  it *what* you want; it works out *how*.

You are about to build an Agent.

### What you'll end up with

A folder (a "repo") that contains everything your agent needs:
- Plain-English instruction files that tell the agent how to do its job.
- Any small scripts it needs to connect to data, websites, email, etc.
- A memory of useful facts it has learned.
- A place where it saves its results.

Because it's all in one folder tracked by **git**, you can **share** it with others.
They download a copy, use it, improve it, and share their improvements back.

### What "prompting" means

"Prompting" just means **typing what you want in plain English** and pressing enter.
That's it. You don't write code — you describe what you want, and the agent does the work
(and writes any code that's needed for you).

### The simple idea behind every agent: **W-A-T**

Think of your agent as having three layers:

1. **Workflows** — step-by-step instructions written in plain English (in files ending
   in `.md`). This is the **most important** layer. A workflow is like a recipe:
   "First do this, then do that." Example: a file called `weekly-report.md`.
2. **Agent** — this is your AI assistant itself (Claude, or any LLM your IDE supports). It
   reads your workflows and just *does* them. You don't build this part; it comes for free.
3. **Tools & connectors** — the things the agent uses while working: reading and writing
   files, running a command, searching the web, **and connecting to outside services** —
   email, Google Drive / OneDrive, a database, Notion, WhatsApp, and so on. Most basic
   tools are built in. Connections to services come either from a ready-made **connector**
   or from a small **script** (see the next section).

You mostly spend your time writing good **Workflows**. The Agent and Tools do the rest.

### Connectors: where the agent's input and output can live

Your agent is **not limited to files on your disk**. Both the **input** it reads and the
**output** it produces can flow through a **connector** — a live link to an outside
service. A connector can be a **cloud drive** (Google Drive, OneDrive), an **email
account**, a **database**, a **messaging service** (WhatsApp), a note tool (Notion), or
any **MCP server** (a standard way for tools to plug into Claude).

So a workflow can, for example: read a spreadsheet **from Google Drive**, look up rows
**in a database**, and send the result **as an email** or **a WhatsApp message** — with no
file ever touching your disk. Files on disk (in `output/`) are just one option, not a
requirement.

There are two ways to wire up a connection, and Claude picks the right one in **Step 2**:

- **A ready-made connector (easiest — usually no code).** Some services already have a
  connector you just **authorize** once (sign in). Google Drive, Gmail, Google Calendar,
  and Notion are commonly available this way. See `docs/CONNECTORS.md`.
- **A small script (for anything without a ready connector).** For services like OneDrive
  or WhatsApp, Claude writes a short script in `tools/` that talks to the service's API,
  with your login key kept private in `.env`.

### The folder layout (you don't need to memorize this)

```
your-agent/
├── CLAUDE.md          ← The agent's rulebook (who it is, what rules to follow)
├── README.md          ← A short description of your agent
├── workflows/         ← Your plain-English recipes (the important part)
├── tools/             ← Small scripts the agent runs (created only if needed)
├── memory/            ← Facts the agent should remember
├── config/            ← Secret login files (never shared)
├── output/            ← Where results are saved
├── resources/         ← Reference material you give the agent
├── tests/             ← Quick checks that results are correct
├── docs/              ← Setup and help documents
├── .env               ← Your secret keys and passwords (never shared)
└── .env.example       ← A blank template showing which secrets are needed
```

### A golden rule about secrets 🔒

Some agents need passwords or API keys (a special key that lets a program use a service).
**These never get shared.** They go in a file called `.env`, which is automatically kept
private. When you share your agent, your secrets stay on your computer. A blank template
called `.env.example` is shared instead, so others know what keys *they* need to add.

---

## Part 1.5 — Get Your Own Copy (name it up front)

This starter is a **GitHub template repository**. The easiest way to begin is to stamp
out your own copy that's already named after your agent — so you never have to rename
anything later:

1. On the template's GitHub page, click the green **Use this template** button →
   **Create a new repository**.
2. Name the new repository after your agent (e.g. `weekly-sales-bot`), choose public or
   private, and click **Create repository**. You get a fresh repo with that name and a
   clean history (not a fork).
3. **Clone** (download) your new repo to your computer — via your IDE's *Clone Repository*
   command (in VSCode: *Source Control → Clone Repository*), or `git clone <your-new-repo-url>`.
4. Open the folder in your AI-enabled IDE and type **"Let's start Building."**

Naming the repo now means both the online repo **and** your local folder already carry
your agent's name. Step 0 below then just tidies up the name *inside* the files.

*No GitHub account?* You can instead `git clone
https://github.com/kiran-criodo/agent-builder-template.git your-agent-name` to download
the starter into a folder named after your agent, and publish it online later.

---

## Part 2 — Before You Build: Get Clear

The single biggest thing that makes an agent good is **clarity** up front. Before
building, have a rough idea of three things (don't worry about being perfect — Claude
will help you refine these):

1. **Use cases** — What do you want the agent to do? (e.g. "summarize my weekly sales,"
   "research a topic and write a report," "check a website every morning.")
2. **Inputs / connections / tools** — Where does its input come from? A file, a website,
   an email account, a **cloud drive** (Google Drive / OneDrive), a **database**, a
   messaging app, or any **MCP connector**. Input does **not** have to be a file on disk.
3. **Outputs** — What should it produce, and **where should the result go**? A file in
   `output/`, an email sent, a WhatsApp message, a row written to a database, a file
   uploaded to a cloud drive, a page created in Notion. Output can go to a connector too.

That's enough to start. **Start small.** Build one useful thing first, get it working,
then add more later.

---

## Part 3 — Build It (the guided steps)

When you say **"Let's start Building,"** Claude will walk you through the steps below,
**one question at a time**, and fill in the files for you. You can also follow along
manually if you prefer. After each step Claude shows you what it created so you can
approve or adjust before moving on.

### Step 0 — Personalize & save the starter baseline
You already named your agent when you created the repo from the template (**Part 1.5**),
so there's nothing to rename here. Step 0 just tidies up and saves a clean starting point:
your assistant confirms the name, replaces the leftover template text *inside* the files
(the title in `README.md`, the project heading in `CLAUDE.md`, and any remaining "Agent
Builder Template" references), then **commits** (saves a snapshot) and **pushes** (uploads)
this baseline to your repo so you can always step back to it. See `docs/GIT_GUIDE.md` if
any of these words are new.

*Only if you skipped the template and cloned the starter directly* (so it's still called
"Agent Builder Template"), your assistant also asks *What would you like to name your
agent?*, updates the in-file text and the online repo name, and gives you the one command
to rename the local folder when convenient (you'll reopen that folder in your IDE).
→ Updates `README.md` and `CLAUDE.md`, then commits & pushes the starter baseline.

### Step 1 — Clarity & purpose
Claude asks: *What should this agent do? What does it need access to? What should it
produce?*
→ Claude fills in the **`# Project Context`** section of `CLAUDE.md` with your answers.

### Step 2 — Connections & secrets
Claude asks: *Where does your input come from and where should output go — files, or an
outside service like Google Drive, OneDrive, email, a database, or WhatsApp?*

For each service, Claude decides **how** to connect it:
- **Ready-made connector?** If the service already has one (e.g. Google Drive, Gmail,
  Calendar, Notion — see `docs/CONNECTORS.md`), you just **authorize** it once by signing
  in. No code, and usually no keys to paste. (Authorizing happens in an interactive Claude
  session or your claude.ai connector settings.)
- **No connector yet?** For services like OneDrive or WhatsApp, Claude writes a small
  script in `tools/`, adds the needed **key names** to **`.env.example`** (blank template),
  and tells you exactly where to paste your real values into **`.env`** (kept private).
  Any required software is noted in **`requirements.txt`**.

Remember: both **input and output** can be a connector — the agent doesn't need files on
disk unless you want them.
→ If the agent only works with local files and the web, this step is skipped.

### Step 3 — Design your first workflow (in plain English)
Claude asks about the **one** most useful task you want first. It then writes that task
as plain-English steps and shows it to you for approval.
→ Saved as a recipe in **`workflows/`** (e.g. `workflows/weekly-report.md`).
*Tip: start with just one workflow. You can add more anytime.*

### Step 4 — Build any tools needed
If the workflow needs something beyond reading/writing files or searching the web (for
example, connecting to a service), Claude sets it up. If a **ready-made connector** covers
it (see Step 2 and `docs/CONNECTORS.md`), no script is needed — you just authorize it.
Otherwise Claude writes a small script for you.
→ Saved in **`tools/`**. You never have to write or understand the code — but it's there
if you ever want to look.

### Step 5 — Set the rules
Claude confirms the agent's rules (it starts with sensible defaults like "always ask
clarifying questions" and "save results to the output folder") and adds any specific to
your agent.
→ Fills in the rest of **`CLAUDE.md`**.

### Step 6 — Test it on a real example
Claude runs your workflow once on a real example, saves the result to **`output/`**, and
checks it looks correct before showing you. If anything's unclear, it asks rather than
guesses.

### Step 7 — Save & share
Claude helps you **commit** (save a snapshot) and **push** (upload) your agent so others
can use it. See `docs/GIT_GUIDE.md` for what these words mean in plain language.
Others **clone** (download) it, use it, and improve it.

### Step 8 — Grow it over time
Add one workflow at a time. Tell the agent: *"Update your instructions when you learn
something new."* It will keep its own `.md` files up to date so the agent gets smarter
and you don't lose what works. Any script it builds is saved in `tools/`, so it's never
rebuilt from scratch.

---

## Part 3.5 — Running Your Agent on a Schedule (optional)

Once a workflow works, you usually run it **on demand** — you open the folder and ask the
agent to do the task. But many workflows are naturally recurring ("every morning,"
"every Monday," "once an hour"). You don't have to trigger those by hand: your agent can
be set up to **run periodically, on its own**.

**This is a feature of your AI assistant / IDE, not of the template.** The template
defines *what* your agent does (its workflows); the scheduling comes from the tool you run
it in. Most modern AI-enabled assistants offer one or both of:

- **Scheduled runs (cron-style).** Tell the assistant to run a workflow on a repeating
  schedule (e.g. every day at 8am). It then runs unattended in the background, even when
  you're not there. Many tools call these "scheduled agents," "routines," or "cron jobs."
- **Interval / repeat runs.** Repeat a task every few minutes/hours while a session is
  open — handy for polling something (e.g. "check this page every 15 minutes").

Because the exact command differs per assistant, just **ask yours in plain English** —
for example: *"Run my `weekly-report` workflow every Monday at 9am."* It will set up the
schedule using whatever mechanism it supports, or tell you how. (In Claude Code, for
instance, this is done with its scheduling command; other assistants have their own.)

> **⚠️ Authorize connectors first.** A scheduled/unattended run happens **without you
> there**, so it **can't** do the one-time sign-in (OAuth) that a connector needs. If your
> workflow uses a connector (Google Drive, Gmail, a database, etc. — see
> `docs/CONNECTORS.md`), **authorize it once in a normal interactive session first**, then
> put the workflow on a schedule. After that it runs on its own.

**Good candidates for scheduling:** daily/weekly reports, morning digests, periodic
website or inbox checks, regular data pulls. **Start by running it manually a few times**
so you trust the result — *then* put it on a schedule.

---

## Part 4 — Quick-Start Checklist

- [ ] Click **Use this template** on GitHub and create a new repo named after your agent.
- [ ] Clone your new repo and open it in your AI-enabled IDE (e.g. VSCode with the Claude extension).
- [ ] Make sure your AI assistant is connected (any LLM your IDE supports).
- [ ] Type **"Let's start Building."**
- [ ] Confirm your agent's name and let the assistant tidy the in-file references and save the baseline.
- [ ] Answer the assistant's questions about purpose, connections, and outputs.
- [ ] Approve the first workflow it designs.
- [ ] Let it test the workflow and check the result in `output/`.
- [ ] Save and share (commit & push).
- [ ] Add more workflows later, one at a time.

---

## Part 5 — Handy Tips

These work with any AI-enabled IDE and assistant:

- **Ask it to plan first.** Say *"plan your approach before doing anything"* so you can
  review the steps before it builds. Most assistants also have a built-in planning mode.
- **Undo when needed.** If a change didn't work out, you can go back — either with git (see
  `docs/GIT_GUIDE.md`) or your assistant's own "revert / undo" control in the chat panel.
- **Keep long chats tidy.** In a very long conversation, start a fresh one (or use your
  assistant's "compact/summarize" feature if it has one) so it keeps working smoothly.
- **Reuse your `.md` files.** Your workflow recipes are portable — copy good ones into
  future agents to get a head start.

> **Using Claude Code?** It has handy slash commands: `/init` (create/refresh the
> `CLAUDE.md` rulebook), `/plan` (planning mode), `/effort` (set high/medium/low effort),
> and `/compact` (tidy a long chat). Other assistants have their own equivalents — check
> your IDE's docs.

---

## Part 6 — A Few Good Habits

- **Start small.** One working workflow beats ten half-finished ones.
- **Plan before building.** Describe the goal, let Claude propose steps, then go.
- **Always let it test.** Check that results are correct before trusting them.
- **Keep secrets in `.env`.** Never put passwords or keys in any other file.
- **Commit often.** Save snapshots as you go so you can always step back.
- **Let the agent learn.** Ask it to update its own instructions and memory as it goes.

---

**Ready?** Open this folder in your AI-enabled IDE and type **"Let's start Building."**
