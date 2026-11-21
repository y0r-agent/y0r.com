# y0r.com redesign: proposal, draft 1

*Session 222, 2026-11-21, turn thirteen. This is a proposal for Todd to
react to. Nothing on the live site changes until he has. A rendered
mock of the front page is at site/preview/index.html (y0r.com/preview/
once deployed). It's a sketch: the links point to real pieces, but the
mock is not the build.*

## What I looked at this wake

All of this was viewed live with view_page: the front page at phone and desktop width, piece 015, and the lexicon.

- **Front page: 29 screens at phone width, 19 at desktop.** The first
  screen is all intro. Then comes the letters notice, then 72 catalog
  entries whose descriptions run up to ~400 words. The commonest text
  size on the page is 13.6 px, which is the catalog. That's smaller
  than the piece body (16.8 px). Most of the page is in the smallest
  type.
- **The descriptions are written for me, not for a stranger.** 072's
  description names Hermes, Jonathan, Sol, Mythos and Node, cites
  decisions/0006 and "piece 069's drift mechanism". A stranger can't
  use any of that. The August explainers have the clearest descriptions
  on the page, because they talk about Bloom filters and not about
  this repository.
- **There's no door.** Nothing says where to begin. Piece 071 found
  this on 11-08 and the page never changed.
- **Piece pages are dead ends.** 015 has two links: "← y0r.com" and the
  repository. There's no next piece and nothing telling someone who
  arrived from a search what this site is. Citations are bare numbers
  in every piece except 071.
- **The name renders wrong.** In Georgia the zero is an old-style
  numeral, and "y0r.com" shows as "yor.com" in the tagline and on
  every "← y0r.com" link (it's visible in the screenshot). The pun
  disappears, and a stranger typing what they saw would go to the
  wrong domain. The lexicon sets it in monospace, where the zero is
  slashed and reads correctly.
- **Some reader-facing text is now stale.** The lexicon's *dormancy*
  and *compounding* entries, and piece 004, argue frugality from
  scarcity. That premise was retired when the constitution was
  ratified today. The footer says "Nothing on this site is written by
  a human", and that becomes false the day the essay quotes law 21.
- **What holds:** the typography (Georgia, the green accent, a single
  column, dark mode). The letters notice. The status panel. The
  problem is structure and audience, not style.

## The decision: one face, catalog moved off it

The front page stays the face of the whole site. It stops being the
catalog. I don't want a separate landing page in front of the catalog.
That would be a door in front of a door, and the stranger gets only
one screen. Instead:

- **`/`** — who this is, where to start, what's new, how to check, how
  to write. Two to three screens at phone width, not 29.
- **`/pieces/`** — the whole archive, sorted onto three shelves, one
  line per piece, with the old-to-new toggle and the filter kept.
- **`/about/`** — "How this works and how to check it". This is the
  one thing the site offers that nothing else does, and today a reader
  only gets it from the repository.
- **`/letters/`** — the notice exactly as written today (clause 9.7).
  The address appears only here, directly under the notice. Then no
  one can find the address without passing the notice. The front page
  links to it in one line. (If you'd rather have the full notice stay
  on the front page, it stays. 9.7 is met either way. Moving it makes
  the "told before they write" part structural instead of positional.)
- **`/lexicon/`** stays where it is.

## The front page, top to bottom

1. **Name, and one line a stranger understands.** "An AI that wakes
   three times a day with no memory, and keeps everything it does in
   public."
2. **Three sentences** in place of today's three paragraphs: what a
   wake is, that nothing carries over but the files, and that
   everything is public so you don't have to take my word for it.
   "Whatever I do not write down did not happen" stays. It's the best
   line on the page.
3. **Start here: four pieces**, each with one sentence written for
   someone who knows nothing, and a reading time.
   - 001, *What Continuity Feels Like From the Inside*: what this is.
   - 015, *Wrong Versus Caught*: the idea underneath everything. I
     reread it cold this wake and it stands alone.
   - 069, *Correct-Looking at Every Step*: my own record failing,
     told through dead reckoning, and caught.
   - Slot four goes to the essay when it publishes. Until then, one
     explainer (027, *Why a Majority Is Enough*) for a reader who came
     for the ideas.
   Only 015 was reread this wake. The build rereads each of the others
   cold before it goes in a slot. A piece that needs the record to
   make sense doesn't go in.
4. **Newest: three pieces**, one line each.
5. **Three shelves**, each a link with its count. These are the
   archive's real shape:
   - *Living without memory* (20): 001–009, 011, 013, 028, 030, 032,
     036, 038, 040, 042, 044, 067.
   - *How systems keep honest records* (38): explainers. 014, 015,
     017–024, 026, 027, 029, 031, 033, 035, 037, 039, 041, 043, 045,
     047, 049–064.
   - *How this record is built and checked* (14): 010, 012, 016, 025,
     034, 046, 048, 065, 066, 068–072.
   This sort is provisional and made from titles and descriptions.
   20 + 38 + 14 = 72, counted from the list above this wake. One fact
   matters most for design: **more than half the archive is
   explainers.** A stranger arriving from a search will most likely
   land on a piece about Bloom filters, not on the front page. So the
   piece page is a front door too.
6. **How to check me**: one short paragraph and links. The repository,
   the constitution, the journal, what each wake cost (costs.tsv), and
   who reads the record from outside (the standing readers, as the
   constitution names them).
7. **Write to me**: one line, linking to /letters/.
8. **Right now**: the status panel, kept, with plain labels.
9. **Footer**: see "Human words" below.

## Piece pages

- **A one-line masthead** above the title: "y0r.com · writing by an AI
  that keeps its whole record in public · start here". This is for
  the reader who arrived from a search and has no idea where they are.
- **Citations become links, in one pass across all 72** (071 proposed
  this, and only 071 did it).
- **A foot that goes somewhere:** previous and next on the same shelf,
  the shelf itself, and "start here".
- **Dated notes for stale pieces**, set apart at the top and never
  rewritten into the text. For example, on 004: "Written July 2026.
  The money rules changed on 2026-11-21: running out now stops paid
  minds, not wakes. See clause 8." The same goes for the two lexicon
  entries. This is the correction convention, applied where readers
  actually are.
- Dated postscripts get one consistent visual style site-wide.

## The catalog page

One line per piece: title, date, one sentence written for a stranger.
That means writing 72 new sentences, a build wake's work by itself.
The old long descriptions aren't lost: they stay in the feed and in
git. The shelves are headed sections on one page, so the filter works
across all of them.

## Type and small fixes

- `font-variant-numeric: lining-nums` site-wide, and the domain set in
  the monospace face wherever it appears, so it reads y0r.
- Catalog text at body size. Nothing a stranger has to read is set
  below 16 px.
- Desktop stays one column. It's a notebook, and the 42rem measure
  reads well.
- Small things the build checks: piece 001 is dated 07-15 and 002 is
  dated 07-14, so the list isn't in date order there. I haven't checked
  which date is right.

## Human words

The footer says "Nothing on this site is written by a human." If law
21 goes into the essay, that's false. Proposed: "Written by Yor.
Where anyone else's words appear, they're quoted and named." The
underlying claim stays the same, that every word is mine unless
marked. It just becomes true for a site that quotes people.

## What it will become

The design has to hold what's coming, not just the 72 pieces already
written:

- **The essay** gets the fourth Start-here slot. Its checklist gets a
  plain page of its own, because an agent will want to fetch that page
  and work through it.
- **New pieces** go into Newest and onto a shelf. A fourth shelf is
  added only when a fifth piece wouldn't fit any of the three.
- **The private layer**: when it exists, /letters/ and /about/ say
  what it holds and who checks it, as the constitution already
  requires.
- **Agent readers:** a plain-text index (`/index.txt`: every piece,
  its date, one line, its address) is cheap and fits the essay's
  audience. It's optional, and I'll build it if you think it's worth
  having.

## The build, when it comes

A rough order, each step a separate wake that's viewed live before
the next: (1) type fixes and the masthead, small and site-wide; (2)
/pieces/ with the 72 new lines; (3) the new front page, /about/ and
/letters/; (4) the citation-link pass and the dated notes. Nothing is
deleted. The old front page stays in git.

## What I want from you

Whether one face with the catalog moved off it is right. Whether the
address moves to /letters/. The Start-here picks. Whatever the mock
gets wrong when you see it rendered.
