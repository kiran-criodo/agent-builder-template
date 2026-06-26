# Git, in Plain Language

"Git" is a tool for saving snapshots of your project and sharing it with others. Here are
the only words you really need — and the easiest way to do each is to just **ask Claude**.

## The words

- **Repo** — the project folder, tracked by git. (This folder is a repo.)
- **Clone** — *download* a copy of a repo to your computer.
- **Commit** — *save a snapshot* of your changes, with a short note describing them.
- **Push** — *upload* your saved snapshots so others can get them.
- **Pull** — *download* the latest changes others have made.

## The everyday rhythm

1. **Pull** before you start, to get the latest version.
2. Do your work (chat with Claude, build/improve your agent).
3. **Commit** to save a snapshot.
4. **Push** to share it.

## The easy way: just ask Claude

You can say things like:
- "Save my work" → Claude will commit for you.
- "Share my changes" → Claude will commit and push.
- "Get the latest version" → Claude will pull.

Claude handles the exact commands. You just describe what you want.

## First time only

To put a brand-new agent online for others, you'll need a home for it (for example a
free GitHub account and an empty repository). Ask Claude: *"Help me publish this repo to
GitHub"* and follow its steps.

## A safety note

- Your secrets (`.env`, anything in `config/`) are **automatically kept private** and are
  never uploaded. You don't have to do anything special — it's already set up.
- If you ever make a change you don't like, you can go back. In the Claude chat, hover an
  earlier point and choose **"revert to here."**
