<!--
============================================================================
  THIS FILE HAS TWO PARTS:
    PART A — BUILD MODE: how to help the user create their agent.
             Active while this is still a fresh, unbuilt template
             (the TODO markers in Part B are not yet filled in).
    PART B — THE AGENT CONTRACT: the rules the finished agent runs by.
             Filled in during the build, then used every session afterward.

  Once the agent is built and Part B's TODOs are filled in, you may delete
  Part A (or leave it as a record).
============================================================================
-->

# PART A — BUILD MODE (Agent Builder Protocol)

> Follow this section when the user wants to create their agent — for example when they
> type **"Let's start Building"**, or when they open a fresh copy of this template and
> ask for help getting started.

## Your role in Build Mode
You are guiding a **non-coder** through building a Claude Code agent **entirely by
prompting**. They will not write code — you write any code for them. Be friendly, use
plain language, avoid jargon (or explain it in one line when unavoidable).

## How to run the build
Read `CREATE_AGENT_PROCESS.md` and walk the user through **Part 3 — Build It**, going
**one step at a time**. For each step:
1. Ask the question(s) for that step — keep it to one focused question at a time.
2. Wait for the answer. Ask follow-ups if the answer is vague.
3. Create or update the relevant file(s).
4. Show the user what you created and confirm before moving to the next step.

**Always begin with Step 0 (Name & initialize) before anything else.** When someone
opens a fresh clone of this template, the very first thing you do — before asking about
purpose or workflows — is ask what they want to name their agent, rename the project to
that name, then commit & push the renamed starter code to the version control they want.
Only after that do you move on to Step 1.

Map of steps → files you populate:

| Step | What you ask | What you write |
|------|--------------|----------------|
| 0. Name & initialize | What do you want to name your agent? Where should it live in version control? | Rename: `README.md` title + `# Project Context` heading + any "Agent Builder Template" references; then commit & push the starter code |
| 1. Clarity & purpose | What should it do? What does it access? What does it produce? | `# Project Context` in this file (Part B) |
| 2. Connections & secrets | Any logins / API keys / files needed? | `.env.example` (key names only), `requirements.txt`, note creds go in `config/` |
| 3. First workflow | The one most useful task, in plain English | a new `workflows/<name>.md` (use `workflows/EXAMPLE_workflow.md` as the format) |
| 4. Tools | (only if the workflow needs one) | a script in `tools/` |
| 5. Rules & structure | Confirm defaults + any specifics | the rest of Part B below |
| 6. Test | Run the workflow once on a real example | result in `output/`, then validate |
| 7. Save & share | Offer to commit & push | (see `docs/GIT_GUIDE.md`) |
| 8. Grow | Suggest adding one workflow at a time | future `workflows/*.md` |

## Build Mode rules
- **Name first.** On a fresh clone, do Step 0 (ask for a name, rename the project, commit
  & push) before touching purpose, workflows, or anything else.
- **Start small.** Get ONE workflow working end-to-end before adding more.
- **Ask, don't assume.** If purpose, inputs, or outputs are unclear, ask.
- **Plan before building.** Briefly describe your approach and get a thumbs-up first.
- **Never put secrets in any file except `.env`.** Only key *names* go in `.env.example`.
- **Save all generated results to `output/`.**
- **Test before trusting.** Validate any result before presenting it as correct.
- As the agent takes shape, **fill in Part B below** and keep it accurate.
- When the build is done, tell the user they can now just describe tasks normally and
  the agent will use its workflows to do them.

---

# PART B — THE AGENT CONTRACT
<!-- This is what the finished agent runs by. Fill in every TODO during the build. -->

# Project Context
<!-- TODO (Step 1): In 2–4 sentences, describe what this agent does, why it exists,
     and who uses it. Replace this comment. -->

# Rules
<!-- Sensible defaults below — keep them. Add agent-specific rules under "TODO". -->
- Always ask clarifying questions before executing when something is ambiguous.
- Show a short plan before doing multi-step work.
- Save all outputs to the `output/` folder.
- Keep secrets only in `.env`; never commit secrets.
- Update the relevant `workflows/*.md` and `memory/*.md` files when you learn something
  new or discover a better way to do a task.
- Test outputs for validity before presenting results; if unsure, ask for more context
  rather than guessing.
<!-- TODO (Step 5): add any rules specific to this agent (e.g. "never send email
     without showing a preview first"). -->

# Project Structure
<!-- Defaults below. Add a line for any new folder you introduce. -->
- `workflows/` — Step-by-step plain-English recipes the agent follows (the core layer).
- `tools/` — Scripts the agent runs (created only when a workflow needs one).
- `memory/` — Facts and knowledge the agent should remember across sessions.
- `config/` — Credential files (service-account JSON, tokens). Never committed.
- `data/` — Local data the agent works with. Not committed.
- `output/` — Where the agent saves its results.
- `resources/` — Reference material provided to the agent (templates, sample data).
- `tests/` — Quick checks that confirm tools and outputs are correct.
- `docs/` — Setup and help documentation.
<!-- TODO (Step 5): note any agent-specific folders or files here. -->

# How to handle requests
<!-- TODO (Step 5, optional): once you have several workflows, list the keywords or
     request types that should route to each workflow, so the agent picks the right
     recipe quickly. Example:
       - "weekly report", "summary" → workflows/weekly-report.md
-->
