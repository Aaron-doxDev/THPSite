# THP-Site — Claude instructions

All website-content changes for True Haven Press are handled through the
**`site-self-service`** skill in the [truehavenpress-marketplace](https://github.com/TrueHavenPress/truehavenpress-marketplace)
plugin. That skill owns the editing workflow: it pulls latest `main`, creates
a session branch, edits HTML, previews locally, and opens a pull request when
published. **Do not push directly to `main`** from this repo.

If you arrived here without the skill installed: ask Aaron, or follow the
onboarding prompt he sent.

## Repo-specific facts

- **Stack:** vanilla HTML / CSS / a little JavaScript. Static, no build step.
- **Deploys:** GitHub Pages from `main` to `truehavenpress.com` (CNAME).
- **Brand:** True Haven Press — a small literary press. Tone is warm, literary, unfussy.

## Pages (live as of 2026-05-24)

- `index.html`, `about.html`, `books.html`, `submit-manuscript.html`, `404.html`
- Legal: `privacy-policy.html`, `terms-and-conditions.html`
- The skill discovers pages at runtime via `ls *.html`, so this list is reference only — adding/renaming pages doesn't require updating this file.

## Do not touch (under any circumstances)

- `CNAME` and any DNS / domain config
- `.github/workflows/**` — none today; if any are added, Aaron owns them
- `privacy-policy.html` and `terms-and-conditions.html` — legal copy; only edit on explicit request and confirmation

## What lives in `.claude/`

`launch.json` is a legacy preview-server config (Python http.server on port 8765). The `site-self-service` skill doesn't use it — the skill launches its own preview via `npx serve`. The file is harmless to leave.
