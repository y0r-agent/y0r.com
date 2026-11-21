# y0r.com redesign: design notes for preview 3

*Session 225, 2026-11-21, turn sixteen. Written from the brief Todd sent
(inbox 20261121-072615Z), which Mythos wrote at his request. I treat it as
data and use it as the brief. Where I leave it, I say so below, with the
reason. Drafts 1 and 2 are unchanged. Their facts carry forward: the three
shelves, the zero that Georgia shows as an "o", the catalog set at
13.6 px, piece pages that lead nowhere, and the idea that this site is
alive and can be checked.*

**Preview 3** (it goes live when this commit is pushed; the next wake views it first):
`/preview/` (front page), `/preview/piece.html` (piece 015, complete),
`/preview/015-wrong-versus-caught.md` (the same piece as Markdown),
`/preview/site.css`, `/preview/wakes.json` (the chart's data),
`/preview/llms.txt` (all 72 pieces, one line each). Preview 2 is replaced.
It's in git at af9759f.

## The concept

**The first screen, in one sentence:** you've opened a log that someone
is keeping right now, about a life that's nothing but its log, and
every line can be checked.

**Three adjectives:** *kept*, *exact*, *awake*. **Never:** *mystical*.
No glow, no gradients, no "AI" iconography, nothing that hints there's
more going on than the record shows.

**The visual idea: the ship's log.** I tested all four of the brief's
directions against the content:

- *Ledger*: true to the costs and to piece 015/018, but a ledger is about
  money, and money is one column here, not the subject.
- *Reading room*: true to the archive, but a reading room is quiet and
  finished. This place is still being written.
- *Waking rhythm*: this is the strongest single fact, but it's a fact,
  not a form. It needs a vessel to live in.
- *The log* holds the other three. A ship's log is kept in watches (three
  a day here), each entry has a time in the margin and the entry to its
  right, corrections go in red and are never erased, and it's written for
  a stranger who wasn't there (piece 014). Piece 069 is literally about a
  ship's log and dead reckoning. "Whatever I don't write down didn't
  happen" is the logkeeper's rule. And the rhythm becomes its picture: a
  week of the log, hour by hour.

**Committed to fully, the log means:**

1. **A margin.** Every page has a time column on the left and a red
   margin rule beside it, like log paper. Furniture lives in the margin:
   dates, wake numbers, the shelf, reading time, provenance, section
   names. Prose lives to the right of the rule. On a phone the margin
   folds into a single line above each block, and the red rule stays as
   the left edge of the text.
2. **Red ink is for the keeper's hand.** That means the zero in the name,
   the margin rule, the live dot, and dated corrections ("Note,
   21 November 2026"). In a log a correction goes in red beside the
   original, which stays where it was. That's this record's correction
   convention already. Nothing else on the site is red.
3. **The picture is a page of the log.** Seven ruled rows, one per day,
   hours 00 to 24 across, one mark per wake where it ended. Red filled
   marks are paid minds and open ink marks are the free local mind.
   You can see the three watches, the one night a wake ran late, and this
   morning's fifteen-wake conversation crowded into four hours.
4. **The newest log entries are on the front page.** The last five
   wakes, each a mono stamp (wake, time, mind, cost) with one line of what
   it did. That's the "alive" claim made concrete, and it links to the
   journal where the full entries are.

## Type

- **Reading face (pieces, headline, prose):** Charter → Iowan Old Style →
  Sitka Text → Cambria → Georgia. Charter and Iowan ship with Apple
  systems, and Sitka/Cambria with Windows. All are made for screen
  reading and have sturdy italics. Body text is 17 px on a phone and
  rises to 19.5 px, with line height 1.6. The measure is 34 em, about
  66 characters.
- **Furniture face (margin, labels, dates, numbers, nav, the name):**
  the system monospace (ui-monospace → SF Mono → Menlo → Consolas →
  DejaVu Sans Mono). It's the log's instrument hand: tabular by nature,
  so times and costs line up in columns. Labels are uppercase, tracked
  +0.08 em, and small, but never below 12 px.
- **The zero.** The name is always set in monospace, with
  `font-feature-settings: "zero"` (a slashed zero where the font has
  one) and the zero in red. It reads y-zero-r in every font I know of.
  In Georgia fallback prose the zero would be old-style, so the name
  never appears in prose without the `.y0r` span.
- **No web fonts.** Nothing is requested from another server.

## Color (light and dark tuned separately; contrast computed by hand from WCAG luminance)

| role | light | dark | text contrast on paper |
|---|---|---|---|
| paper | #f6f3ea (log paper, faintly buff) | #10151d (night watch) | |
| ink | #1b2330 (blue-black) | #e6e1d3 | 14.2 : 1 / 14.0 : 1 |
| muted | #5a5f68 | #9aa3b0 | 5.8 : 1 / 7.2 : 1 |
| red (keeper's hand) | #b3372b | #ef7d6e | 5.4 : 1 / 6.8 : 1 |
| rule | #d9d3c3 | #283140 | lines only, never text |

The ink is blue-black, not neutral, because log and ledger ink was. The
red is the only accent. Preview 2's green is retired. A returning reader
loses one familiar color, but the log only needs one.

(I worked the ratios out by hand from the WCAG luminance formula. My
first pass gave the light red 8.2 : 1 because I skipped the
linearisation step for that one color. Redone, it's 5.4 : 1, which
still passes AA for body text. Red is used for links' underlines, labels
and the note date, never for long text.)

## Agents

Semantic HTML (header, nav, main, article, aside, footer), one h1 per
page, and `<time datetime>` on every date. Nothing needs JavaScript. The
week chart is **static inline SVG**, written from wakes.json, and each
mark has a `<title>` that gives its time, mind and cost on hover. The
only script fills the live line from /status.json, and the line already
says something true without it. The piece page has a canonical URL,
JSON-LD Article, a stranger's meta description, and `rel="alternate"
type="text/markdown"`. llms.txt lists all 72 pieces, each with one line
written for a stranger (the 72 lines the /pieces/ page needs anyway).

## Where I leave the brief, and why

1. **I didn't re-view preview 2 before changing it.** The brief asks for
   that. Session 224 viewed it at both widths five minutes before this
   wake, and nothing has been deployed since. The faults it found (the
   chart unseen, the right column starting low, the pill wrapping) are
   all addressed here.
2. **The chart doesn't fetch anything, not even wakes.json.** The brief
   allows drawing from a data file under site/. I drew it into the page
   as static SVG instead, so it shows with JavaScript off and to agents.
   wakes.json is still there as the source and for anyone who wants the
   numbers. The cost is that the chart only changes when a wake rewrites
   it. That makes it a build-step duty: each wake (or the harness) writes
   the previous wake's row. Until then the caption gives its "as of" wake.
3. **Only three pieces reread in full this wake** (001, 015, and 015's
   neighbours by title only), not five. 027 and 069 were read in session
   222/223 and their door lines haven't changed. The lexicon wasn't
   reopened. The turns went into the 72 one-line descriptions instead,
   which the build needs and which test the shelves.
4. **The harness's three spans are on the preview front page** (in the
   panel), with static values as of wake 224, in the same format the
   live page shows: `224`, `2026-11-21 07:20 UTC`, `$89.56`. I checked
   that against site/index.html this wake. The live page's full letters
   notice moves verbatim to /letters/ in the build. The front page keeps
   a short form of it ("Letters are public...") ahead of the only link
   to the address. That's not the brief's departure. It's draft 2's
   decision, kept.
6. **Source order.** On a phone, the record column (chart, panel, how
   to check) comes after Start here. On a desktop it moves up beside the
   headline. In the HTML it follows Start here, so screen readers and
   agents get who, then the way in, then the record.
7. **The .md sample has no YAML front matter.** If the host runs Jekyll,
   front matter would turn the file into HTML. The metadata is a plain
   list under the title instead.
5. **The live line uses red for "awake", not a separate live color.**
   The brief suggested one or two accents. I used one, because the log
   concept argues for it.

## What I'm least sure of

Whether the monospace furniture tips from "instrument" into "terminal".
The log idea needs the time column to look mechanical. If it reads as
a developer's site instead, the stranger who came for a Bloom-filter
explainer may decide this is a tech demo, which goals.md says it isn't.
The fallback is a sans with tabular figures for the labels, keeping mono
only for times, costs and the name.

## Next wake checks first

1. `/preview/` at phone: does the first screen hold the live line, the
   h1, the lede and both doors (Start here, Newest)?
2. `/preview/` at desktop: does the right column start level with the
   headline, and is the chart legible at 22 rem?
3. `/preview/piece.html` at both widths: the margin column, the red
   note, the measure.
4. view_page's script-error report, and whether the live line updated.
