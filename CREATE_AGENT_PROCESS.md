# How to Create an Agent — Step by Step

This is your complete, plain-English guide to building your own AI **agent** — even if
you have never written a line of code. You build the whole thing just by **chatting**
with Claude inside VSCode.

There are two ways to use this guide:

- **Just say "Let's start Building."** Claude will read this file, then interview you
  one question at a time and create all the files for you. This is the easiest path.
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
2. **Agent** — this is Claude itself. It reads your workflows and just *does* them. You
   don't build this part; it comes for free.
3. **Tools** — the things the agent uses while working: reading and writing files,
   running a command, searching the web, sending email, reading a database, and so on.
   Most tools are built in. Some need a small script or a login key.

You mostly spend your time writing good **Workflows**. The Agent and Tools do the rest.

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

## Part 2 — Before You Build: Get Clear

The single biggest thing that makes an agent good is **clarity** up front. Before
building, have a rough idea of three things (don't worry about being perfect — Claude
will help you refine these):

1. **Use cases** — What do you want the agent to do? (e.g. "summarize my weekly sales,"
   "research a topic and write a report," "check a website every morning.")
2. **Inputs / connections / tools** — What does it need access to? (e.g. a spreadsheet,
   a website, an email account, a database, an API key.)
3. **Outputs** — What should it produce? (e.g. a report saved as a file, an email sent,
   an updated spreadsheet.)

That's enough to start. **Start small.** Build one useful thing first, get it working,
then add more later.

---

## Part 3 — Build It (the guided steps)

When you say **"Let's start Building,"** Claude will walk you through the steps below,
**one question at a time**, and fill in the files for you. You can also follow along
manually if you prefer. After each step Claude shows you what it created so you can
approve or adjust before moving on.

### Step 0 — Name your agent & save the starter
Before anything else, Claude asks: *What would you like to name your agent?* It then
**renames** this starter project to your chosen name (updating the title in `README.md`,
the project heading in `CLAUDE.md`, and any other "Agent Builder Template" references) so
your agent has its own identity from the start.

Claude then asks *where you'd like to keep it* in version control (for example, a new
GitHub repository) and offers to **commit** (save a snapshot) and **push** (upload) the
renamed starter code there. This gives you a clean, saved baseline before you build
anything — so you can always step back to it. See `docs/GIT_GUIDE.md` if any of these
words are new.
→ Updates `README.md` and `CLAUDE.md`, then commits & pushes the starter code.

### Step 1 — Clarity & purpose
Claude asks: *What should this agent do? What does it need access to? What should it
produce?*
→ Claude fills in the **`# Project Context`** section of `CLAUDE.md` with your answers.

### Step 2 — Connections & secrets
Claude asks: *Does it need any logins, API keys, or files to connect to?*
→ If yes, Claude adds the needed key names to **`.env.example`** (blank template) and
tells you exactly where to paste your real values into **`.env`** (kept private). Any
required software is noted in **`requirements.txt`**.
→ If no, this step is skipped.

### Step 3 — Design your first workflow (in plain English)
Claude asks about the **one** most useful task you want first. It then writes that task
as plain-English steps and shows it to you for approval.
→ Saved as a recipe in **`workflows/`** (e.g. `workflows/weekly-report.md`).
*Tip: start with just one workflow. You can add more anytime.*

### Step 4 — Build any tools needed
If the workflow needs something beyond reading/writing files or searching the web (for
example, connecting to a service), Claude writes a small script for you.
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

## Part 4 — Quick-Start Checklist

- [ ] Download (clone) this folder and open it in VSCode with the Claude extension.
- [ ] Make sure Claude is connected (Pro plan or another supported LLM).
- [ ] Type **"Let's start Building."**
- [ ] Name your agent and let Claude save the renamed starter to version control.
- [ ] Answer Claude's questions about purpose, connections, and outputs.
- [ ] Approve the first workflow it designs.
- [ ] Let it test the workflow and check the result in `output/`.
- [ ] Save and share (commit & push).
- [ ] Add more workflows later, one at a time.

---

## Part 5 — Handy Claude Code Tips

- **`/init`** — Generates or refreshes the `CLAUDE.md` rulebook for the project.
- **`/plan`** — Puts Claude in "planning mode." It designs an approach and shows it to
  you *before* doing anything. Great for thinking before building.
- **`/effort`** — Set how much effort Claude puts in: `high`, `medium`, or `low`.
- **`/compact`** — In a long chat, this tidies up the conversation so Claude keeps
  working smoothly without losing track.
- **"Revert to here"** — Hover over an earlier point in the conversation and choose this
  to go back to how things were at that moment (handy if a change didn't work out).
- **Save your `.md` files** — Your workflow recipes are reusable. Copy good ones into
  future agents to get a head start.

---

## Part 6 — A Few Good Habits

- **Start small.** One working workflow beats ten half-finished ones.
- **Plan before building.** Describe the goal, let Claude propose steps, then go.
- **Always let it test.** Check that results are correct before trusting them.
- **Keep secrets in `.env`.** Never put passwords or keys in any other file.
- **Commit often.** Save snapshots as you go so you can always step back.
- **Let the agent learn.** Ask it to update its own instructions and memory as it goes.

---

**Ready?** Open this folder in VSCode and type **"Let's start Building."**
