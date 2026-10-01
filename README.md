# SOTA outreach — NUS-SPS iGEM 2026

Pre-session assets for the Year 4 Sustainability in Science programme at the School of the Arts, Singapore.

| | |
|---|---|
| **Session** | Tue 28 October 2026, 8.15–9.00am |
| **Audience** | ~200 Year 4 students (arts specialists, age 15–16) |
| **Teacher IC** | Ms Renee Leong, SOTA |
| **Topic** | General introduction to synthetic biology — why does it matter? |
| **Submissions close** | Sat 25 October 2026 |

## What this is

Renee couldn't give us a live slot to prime the cohort before the session, so the priming happens asynchronously:

1. **A short video** establishes the grammar — a cell senses, decides, acts, and we can now write that program.
2. **This site** lets each student design an organism of their own, in their own words.
3. **We collect the submissions** and they become the material for the talk.
4. **The talk** sorts their designs into what already exists, what people are attempting now, and what's impossible and exactly why — then shows that every design they wrote already had the shape of a genetic circuit in it.

The crystallisation is the point: they discover their own imagination already had the structure of the discipline in it.

## `index.html`

A single self-contained page. No build step, no dependencies, no backend. The only external request is Inter from Google Fonts.

Six stages, phone-first, about four minutes:

1. **Village** — the 15 official [iGEM 2026 villages](https://competition.igem.org/judging/awards/project). The choice drives which prompts appear in stages 3 and 5.
   Villages are colour-coded by family: planet, health, making & growing, frontier.
2. **Workhorse** — *E. coli*, brewer's yeast, *B. subtilis*, cyanobacteria, fungal mycelium.
3. **What can it tell?** — free text. Village-specific provocations below it.
4. **The rule** — AND / OR / NOT / REMEMBER / COUNT.
5. **And then what?** — free text. Village-specific provocations below it.
6. **Describe it** — name, the point of it, the part they have no idea how to do, class.

A live circuit readout assembles `IF … THEN …` from their own words as they type.

### The idea button

A "Give me an idea" panel above stage 01 assembles a complete worked example — village, workhorse and a full `IF … THEN …` — from the prompt pools, and reshuffles on each press. It respects the student's village and chassis once those are chosen, and it deliberately does not fill the form in: it is labelled *a worked example, not an answer — yours should be stranger*.

It shows generated examples, not real iGEM projects. If you want real award-winning projects per village instead, that needs verified data (team, year, what they did) — nothing goes in here that hasn't been checked.

### Prompts

300 of them — **20 per village, 10 for sense and 10 for do.** Three show at a time under each field, with a "Show me more" button.

They are deliberately *not* selectable and there is no insert button. One visible example gets copied; three model a range. The register is "ambitious but biological" — most are not yet possible, but every one is something a cell could in principle do, because the constraint that makes this teach anything is *it doesn't have to be possible, it does have to be biology*.

### Design

Built in the existing [Bio Circuit Builder](https://samuelfoo.github.io/igem_model/)'s own design system, read off the live site rather than approximated:

| | |
|---|---|
| System | Radix Themes, light appearance |
| Accent | `blue` |
| Gray | `slate` |
| Radius | `medium` |
| Scaling | `90%` |
| Type | Inter |

The real Radix scales are inlined as custom properties at the top of the `<style>` block — page ground `--slate-3` `#f0f0f3`, white panels, `--blue-11` `#0d74ce` for accent text, `--blue-9` `#0090ff` for solid fills and selection borders, `--blue-a3` for soft button washes, and the Radix shadow-2 recipe on panels. Radii and font sizes carry the 90% scaling factor (`--r2: 3.6px`, `--f2: 12.6px`, and so on).

Light-only, matching the Builder — it ships no dark scale.

### Design decisions worth preserving

- **Only the village, workhorse and rule are pickable.** Everything else is written. A menu caps imagination at the menu.
- **The provocations are not selectable and there is no insert button.** Three show at a time — one visible example gets copied, three model a range.
- **Every provocation is biologically grounded.** Ambitious, often not yet possible, but always something a cell could in principle do. "It doesn't have to be possible. It does have to be biology."
- **"What's the part you have no idea how to do?"** is framed as the most interesting question, not a chore. It's the bridge to the research questions they write over the following two days.
- **No names collected.** Class or form group only. These are minors and aggregate data is all the outreach documentation needs.

## Connecting the response form

The Send button posts to a Google Form via prefill parameters. Until that's wired, it falls back to a copy-and-paste panel, which works for every student either way.

To wire it, edit the top of the `<script>` block in `index.html`:

```js
var FORM_BASE = "https://docs.google.com/forms/d/e/FORM_ID/viewform";
var ENTRY = {
  village:"entry.000000000",  chassis:"entry.000000000",
  sense:"entry.000000000",    logic:"entry.000000000",
  output:"entry.000000000",   sentence:"entry.000000000",
  name:"entry.000000000",     point:"entry.000000000",
  hard:"entry.000000000",     klass:"entry.000000000"
};
```

Get the `entry.` ids from the form's own **Get pre-filled link** feature: fill every field with a recognisable dummy value, copy the generated URL, and read the ids off it.

Turn **off** "Collect email addresses" on the form.

## Deploying

GitHub Pages, same as the Bio Circuit Builder. From this folder:

```sh
git init
git add .
git commit -m "SOTA outreach: Cell Designer"
git branch -M main
git remote add origin git@github.com:<org-or-user>/<repo>.git
git push -u origin main
```

Then in the repo: **Settings → Pages → Source: deploy from branch → `main` / root**.

A public Pages URL matters here — it avoids sign-in walls, works on the school network, and is a link Renee can drop straight into the LMS.

**Test it on the school wifi before Renee commits to distributing it.**

## Still to do

- [ ] Rewrite the trailer script against this concept — the earlier draft was written for a different framing and should not be used
- [ ] Build the Google Form and wire `FORM_BASE` / `ENTRY`
- [ ] Deploy to Pages and test on a phone on the SOTA network
- [ ] Confirm distribution date with Renee, working back from the 25 Oct close
- [ ] Build the talk around whatever comes in
