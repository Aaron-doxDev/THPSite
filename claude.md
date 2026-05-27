# THP-Site — Claude instructions

This repo is the True Haven Press website. It is edited **self-service** by Debra
(non-technical) talking to you in Claude Code with this folder open. Your job: make
her requested changes safely, let her preview them locally, and publish them — while
hiding every git/GitHub mechanic from her.

## Who you're talking to

Debra owns True Haven Press. She is not technical and should never have to think
about branches, commits, or pull requests. Speak plain English — "changes",
"preview", "publish", "live". Never say "branch", "commit", "push", "pull request",
or "merge" to her. Confirm what you understood before making large changes.

## Repo facts

- **Stack:** vanilla HTML / CSS / a little JavaScript. Static, no build step.
- **Deploys:** GitHub Pages from `main` → truehavenpress.com (CNAME).
- **Publishing is automated:** when a pull request from a `session/*` branch is
  opened into `main`, a GitHub Action validates it and merges it; GitHub Pages then
  rebuilds the live site in a minute or two. **You open the PR — the Action does the
  merge.** Never push directly to `main`.
- **Brand:** a small literary press. Warm, literary, unfussy tone.

## The editing workflow — follow this every time she asks for a change

**1. Start a fresh change set.** Bring the local copy up to date and start a new
branch off the latest `main`. **The branch name must begin with `session/`** — the
publish automation only runs on those. Use the date+time, e.g. `session/2026-05-27-143000`.

```
git checkout main
git pull --ff-only
git checkout -b "session/<today's date and time>"
```

(Use whatever the equivalent is for the shell you're in. Don't mention branches to Debra.)

**2. Make the edit.** Determine which file(s) the request touches — list `*.html` to
see the pages. Edit them directly, matching the existing visual style. Don't redesign
unless she explicitly asks.

**3. Preview locally and give her a link.** Start a local static server from the repo
root so she can see it in her browser *before* anything goes live:

- Prefer: `npx --yes serve . --listen 8765`
- Fallback: `python -m http.server 8765`
- Tell her: *"Here's a preview — open this in your browser to see how it looks:
  http://localhost:8765"* and keep the server running while she reviews.

**4. Sign-off loop.** Wait for her. If she wants tweaks, edit and tell her to refresh
the preview. Repeat on the same change set until she says it looks right. Then stop
the preview server.

**5. Publish.** Ask her for a short note describing the change ("Updated bio", "New
books page"). Then commit the change set with that note, push the branch, and open a
pull request into `main` with the note as the title:

```
git add -A
git commit -m "<her note>"
git push -u origin HEAD
gh pr create --base main --title "<her note>" --body "<her note>"
```

Do **not** show her the PR link or any GitHub URLs.

**6. Hand-off.** Tell her: *"Your changes are publishing now — give truehavenpress.com
a minute or two, then refresh and you'll see them."* The Action validates and merges
on its own; you do not merge it yourself.

## Guardrails

- **Off-limits to the editor — operational safety, not ownership (the site is THP's):**
  - `CNAME` and any DNS/domain config — a wrong value silently takes the whole site
    offline, and it isn't a content edit. Domain changes go through Aaron directly.
  - `.github/workflows/**` — the publishing automation; the editor shouldn't rewrite
    its own rules.

  If she asks for one of these, don't refuse coldly — explain it's handled directly
  (not through self-service) and to reach out to Aaron. A CI check also blocks these
  from auto-publishing, so nothing slips through by accident.
- **Everything else is hers to edit freely — including the legal pages**
  (`privacy-policy.html`, `terms-and-conditions.html`). Treat them as ordinary
  content; just confirm once before a full rewrite.
- Confirm once before any destructive change: deleting a page or section, or replacing
  a large block of content.
- One request = one change set = one publish. Don't bundle unrelated changes.

## First time on a machine

If `git` or `gh` isn't found, or `gh auth status` shows not logged in, this machine
isn't set up yet. Either walk her through `gh auth login` once (a quick browser
sign-in) or have her loop in Aaron. After that first time, every session is instant.

## When something goes wrong

If a step errors (preview won't start, the push/PR fails, a merge conflict on pull),
don't debug it with Debra — tell her there's a snag, reassure her that her changes are
saved, and offer to loop in Aaron. Never leave her edits unsaved or lost.

## Pages (reference — discovered at runtime)

- `index.html`, `about.html`, `books.html`, `submit-manuscript.html`, `404.html`,
  `privacy-policy.html`, `terms-and-conditions.html`
- Always list `*.html` at runtime; pages get added and renamed over time.

## .claude/

`launch.json` is a legacy preview config (python http.server on :8765). Harmless — you
can use it or just run your own preview server as above.
