# tools/

This folder holds small **scripts** the agent runs while doing its job — for example,
connecting to a service, fetching data, or sending an email.

You do **not** write these yourself. When a workflow needs one, Claude writes it for you
and saves it here. Keeping scripts here means they are reused, not rebuilt each time.

Notes:
- Scripts read any secrets from the `.env` file (never hard-code passwords or keys).
- Each script should do one clear job and print a clear result.
- If a script needs an extra Python package, Claude adds it to `requirements.txt`.

This folder starts with one shared helper, `_guardrails.py`, which keeps read-only agents
read-only (see the note at the top of that file). Everything else fills up as your agent
grows.
