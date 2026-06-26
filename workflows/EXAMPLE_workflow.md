# EXAMPLE Workflow (a template — copy this format for your own workflows)

> A "workflow" is a recipe in plain English. Claude reads it and follows the steps.
> Copy this file, rename it to describe the task (e.g. `weekly-report.md`), and fill in
> each section. Delete this example once you have your own.

## Purpose
<!-- One sentence: what does this workflow accomplish? -->
Example: Produce a short weekly summary of a topic and save it as a file.

## When to use
<!-- What the user might say to trigger this. -->
Example: "Give me this week's summary", "weekly report".

## Inputs
<!-- What information or access this workflow needs to run. -->
- Example: the topic or area to summarize.
- Example: the date range (defaults to the last 7 days).

## Steps
<!-- Number the steps in plain English. Be specific but don't write code. -->
1. Ask the user for anything missing (e.g. the topic), if not already provided.
2. Gather the needed information (e.g. search the web, read a file in `resources/`).
3. Summarize the findings into a clear, short write-up.
4. Save the result to `output/` (see "Output" below).
5. Show the user a short preview and the file location.

## Output
<!-- Exactly what gets produced and where it is saved. -->
- A markdown file saved to `output/`, named like `weekly-summary-<date>.md`.

## Validation (check before showing results)
<!-- How to confirm the result is correct, not just present. -->
- The summary actually addresses the requested topic.
- The file was saved to `output/`.
- Nothing was made up; if information was missing, the user was asked rather than guessed.
