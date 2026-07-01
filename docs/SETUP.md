# Setup (one-time)

Follow these once to get your computer ready. After this, you build everything by chatting.

## 1. Install the tools you need
- **VSCode** — the editor you'll work in. (Free download from the official site.)
- **The Claude extension for VSCode** — install it from the Extensions panel in VSCode.
- **Claude access** — sign in with a Claude Pro plan (or another supported LLM).
- **Python** (only if your agent will run scripts) — install Python 3.10 or newer.

## 2. Get your own copy onto your computer
This project is a **GitHub template**. Make your own named copy first:
- On the template's GitHub page, click **Use this template → Create a new repository**,
  name it after your agent (e.g. `weekly-sales-bot`), and create it.
- Then **clone** (download) *your new repo* to your computer. See `GIT_GUIDE.md` for how.

That way your folder is already named after your agent. If you already have the folder,
skip this.

## 3. Open the folder in VSCode
File → Open Folder → choose this folder. Then open the Claude panel.

## 4. Add your secrets (only if your agent needs logins or keys)
- Make a copy of `.env.example` and name the copy `.env`.
- Open `.env` and fill in your real keys/passwords.
- Never share the `.env` file — it stays on your computer automatically.

## 5. Install Python packages (only if your agent uses scripts)
In VSCode's terminal, run:
```
pip install -r requirements.txt
```

## 6. Start building
In the Claude panel, type:

> **Let's start Building**

Claude takes it from there. If you ever get stuck, open `CREATE_AGENT_PROCESS.md`.

## Troubleshooting
- **Claude isn't responding** — check you're signed in and connected.
- **A script fails** — tell Claude the error message; it will fix it.
- **A secret isn't found** — confirm it's in `.env` (not `.env.example`) and spelled the same.
