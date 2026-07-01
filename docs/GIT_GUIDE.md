# Git, in Plain Language

"Git" is a tool for saving snapshots of your project and sharing it with others. Here are
the only words you really need — and the easiest way to do each is to just **ask your AI
assistant** (Claude, or any LLM your IDE supports — "Claude" below is just the example).

## The words

- **Repo** — the project folder, tracked by git. (This folder is a repo.)
- **Clone** — *download* a copy of a repo to your computer.
- **Commit** — *save a snapshot* of your changes, with a short note describing them.
- **Push** — *upload* your saved snapshots so others can get them.
- **Pull** — *download* the latest changes others have made.

## The everyday rhythm

1. **Pull** before you start, to get the latest version.
2. Do your work (chat with your assistant, build/improve your agent).
3. **Commit** to save a snapshot.
4. **Push** to share it.

## Pushing your changes back to your repo

As you build, you'll want to send your work back to your own GitHub repo so it's saved and
shareable. If you made this repo with **"Use this template"** and cloned *your* copy, it's
already wired to your repo — so this is just:

- Say **"Save and share my changes"** (your assistant will commit & push), or run
  `git add -A && git commit -m "your note" && git push`.

That's it — your changes land in your GitHub repo.

> **One caveat if you cloned the template directly** (the `git clone …agent-builder-template`
> fallback, *not* "Use this template"): your copy still points at the original template,
> which you can't push to. First create your own empty repo on GitHub and point your folder
> at it — just ask your assistant: *"Point this repo at my new GitHub repo and push"* and it
> will handle the commands (`git remote set-url origin <your-repo-url>`, then push).

## The easy way: just ask your assistant

You can say things like:
- "Save my work" → it will commit for you.
- "Share my changes" → it will commit and push.
- "Get the latest version" → it will pull.

Your assistant handles the exact commands. You just describe what you want.

## Starting from the template

This starter is a **GitHub template repository**. The easiest way to begin is to make
your own copy from it, already named after your agent:

1. On the template's GitHub page, click **Use this template → Create a new repository**.
2. Name it after your agent (e.g. `weekly-sales-bot`) and create it — you get a fresh
   repo with a clean history (not a fork).
3. **Clone** your new repo to your computer.

Your online repo and your local folder now both carry your agent's name from the start.

## Publishing later (if you didn't use the template)

If you already have the folder and just want to put it online, ask your assistant: *"Help
me publish this repo to GitHub"* and follow its steps.

## A safety note

- Your secrets (`.env`, anything in `config/`) are **automatically kept private** and are
  never uploaded. You don't have to do anything special — it's already set up.
- If you ever make a change you don't like, you can go back. Most AI chat panels let you
  hover an earlier point and revert to it (in Claude Code: **"revert to here"**); check
  your assistant's controls.
