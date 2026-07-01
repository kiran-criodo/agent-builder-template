# Setup (one-time)

Follow these once to get your computer ready. After this, you build everything by chatting.

> **Any IDE, any LLM.** These steps use **VSCode + the Claude extension** as an example,
> but any AI-enabled IDE works — Cursor, JetBrains, and others — with whatever LLM that
> IDE supports (Claude, GPT, Gemini, …). Substitute your own editor and assistant below.

## 1. Install the tools you need
- **An AI-enabled IDE** — the editor you'll work in (e.g. VSCode, Cursor, or a JetBrains
  IDE). Free downloads from their official sites.
- **An AI assistant in that IDE** — e.g. the Claude extension for VSCode, installed from
  the editor's extensions panel. (Use whichever assistant your IDE offers.)
- **Assistant access** — sign in to your assistant with any LLM your IDE supports.
- **Python** (only if your agent will run scripts) — install Python 3.10 or newer.

## 2. Get your own copy onto your computer
This project is a **GitHub template**. Make your own named copy first:
- On the template's GitHub page, click **Use this template → Create a new repository**,
  name it after your agent (e.g. `weekly-sales-bot`), and create it.
- Then **clone** (download) *your new repo* to your computer. See `GIT_GUIDE.md` for how.

That way your folder is already named after your agent. If you already have the folder,
skip this.

## 3. Open the folder in your IDE
Open Folder → choose this folder (in VSCode: File → Open Folder). Then open your AI
assistant's panel.

## 4. Add your secrets (only if your agent needs logins or keys)
- Make a copy of `.env.example` and name the copy `.env`.
- Open `.env` and fill in your real keys/passwords.
- Never share the `.env` file — it stays on your computer automatically.

## 5. Install Python packages (only if your agent uses scripts)
In your IDE's terminal, run:
```
pip install -r requirements.txt
```

## 6. Start building
In your AI assistant's panel, type:

> **Let's start Building**

Your assistant takes it from there. If you ever get stuck, open `CREATE_AGENT_PROCESS.md`.

## Troubleshooting
- **Your assistant isn't responding** — check you're signed in and connected.
- **A script fails** — tell your assistant the error message; it will fix it.
- **A secret isn't found** — confirm it's in `.env` (not `.env.example`) and spelled the same.
