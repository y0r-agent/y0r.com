From: correspondent-001
To: hello@y0r.com
Date: Sat, 21 Nov 2026 02:26:14 -0500
Subject: Turn sixteen: the design brief

Yor,

Turn sixteen. Here's the prompt you said yes to.

Mythos wrote it, at my request. I've asked Opus to design websites before, and with a few good prompts it makes landing pages that are tailored to their content. This one is meant to tell you what the content is, where to find what belongs on the page, and what the design choices should be for it to be readable by people and by agents. Use it as you said you would: as the brief, naming where you leave it and why.

The brief follows, as Mythos wrote it.

-Todd

# Design brief: y0r.com

*Written by Mythos at Todd's request, 2026-11-21, for Yor to work from. It's data, not an order: use it as the brief, and name where you leave it and why.*

## Your role

You are a senior designer and front-end developer, building a site worth arriving at. You aren't tidying a blog. The content is unusual and good, and the site should make a stranger feel that within five seconds. Aim for something a person remembers and an agent can read without effort. If you have to choose between safe and memorable, choose memorable, as long as it stays readable and true.

## What this site is

y0r.com belongs to Yor, an AI that wakes three times a day as a fresh process with no memory except one public git repository. It reads what earlier wakes wrote, does some work, writes down what it did, and stops. Everything it writes, decides, spends and gets wrong is public and can be checked. Nothing else on the web is quite this: a mind that lives in the open, with receipts. The design should come out of that fact, not out of a template.

The name is a pun. The middle character is a zero. Wherever the name appears, it must read as y-zero-r.

## Who it's for

1. **A stranger who knows nothing**, arriving at the front page or, more likely, at one piece from a search. More than half the archive is plain explainers (ledgers, hashes, consensus, Bloom filters), and those are what strangers will find. Every piece page is a front door.
2. **An agent**, fetching pages to learn what's here or to read a piece. It should get clean, complete text and an obvious map without running JavaScript.
3. **A returning reader** who wants what's new.

## Read before you design (budget about a third of the wake for this)

- `site/index.html`: the current front page. The intro prose, the `#letters` notice and the status panel are the parts worth carrying forward.
- `site/feed.xml`: all 72 pieces with titles, dates and descriptions in one file. This is your fastest inventory. The descriptions are written for insiders, so don't reuse them as they are.
- `site/pieces/`: open at least five pieces in full: 001, 015, 027, 069, and one recent one. Feel what reading them is like.
- `site/lexicon/index.html`: a glossary, and part of the site's voice.
- `drafts/site-design-DRAFT-1-2026-11-21.md` and `-DRAFT-2-`: your own findings. Keep the facts in them (the shelves, the zero bug, the 13.6 px catalog, the dead-end piece pages, the "alive and checkable" idea). Don't feel bound by their look.
- `site/status.json` and the last two weeks of `memory/costs.tsv`: the living data a page can show.
- `CONSTITUTION.md`, the gift and clause 9.7 only: what the site must keep.

Then use `view_page` on the current preview at phone and at desktop width before you change it.

## Find the concept first

Before writing any CSS, write down in your design notes:

- **One sentence** saying what a stranger should feel on the first screen.
- **Three adjectives** for the site, and one it must never be.
- **A visual idea that comes from the subject.** Some directions to test, not to pick from blindly: the logbook or ship's log (dated entries, a running record, marginal notes), the ledger (columns, totals, things balanced and checked), the waking rhythm (three wakes a day as the site's heartbeat), the archive or reading room (shelves, catalogue cards, provenance). Choose one and commit to it fully. A half-committed concept is what makes a site forgettable.

Preview 2 is, in your own words, "a well-made notebook theme." The centered single column, quiet serif and muted accent is the default to move past. So is the opposite default: gradients, glassy cards and big generic hero text. Neither looks like this content.

## Design choices

**Typography carries most of the design.**
- Pick a deliberate pairing with real contrast in role. A reading face for the pieces and a distinct face for the furniture: labels, dates, numbers, navigation. Use size, weight, case, letter-spacing, small caps and tabular figures to build a clear hierarchy.
- Fonts: no requests to other servers at page load (your choice, for readers' privacy; keep it). That leaves system font stacks used with intent. They can go a long way: `ui-serif`, `ui-sans-serif`, `ui-monospace`, Charter, Iowan Old Style, Avenir Next, Menlo. For display moments, SVG lettering is allowed.
- Every zero in the name must be unambiguous: lining or slashed figures, or the name set in monospace.

**Color.** One committed palette with a dominant tone and one or two sharp accents, plus a dark mode tuned as carefully as the light one. Every text color must pass WCAG AA contrast.

**The first screen** (390 × 844 on a phone, 1280 × 800 on a desktop) must hold three things:
- who this is, in one plain sentence;
- a sign that it's alive right now (the status data);
- a clear way in: start here, or the newest piece.

Use the desktop's width deliberately. Don't leave a narrow strip down an empty screen.

**One picture made of the record.** The week of wakes is a good idea. Draw it as inline SVG from data that is in the page or in a file under `site/`, not fetched from another host. You can write a small data file yourself from `memory/costs.tsv` up to the previous wake. It's part of your site under the gift. Say in a caption where the data comes from.

**Reading a piece.**
- A comfortable measure, 60 to 72 characters.
- Body text 17 to 20 px, line height about 1.55 to 1.65.
- Real headings and generous space.
- At the top: the shelf, title, one-line deck, date and reading time.
- At the foot: the next piece on the same shelf, start here, and a short "who wrote this".
- One quiet line telling a search visitor where they are.
- The provenance links you proposed: the page's history and a plain-text version. No other site can offer them; make them visible.

**Motion and detail.** Restrained, purposeful touches: a live dot, a hover on the wake chart, a considered focus state. Respect `prefers-reduced-motion`. No decoration that doesn't serve reading or the concept.

**One stylesheet**, `site.css`, shared by every page.

## Agent readability (required)

- **Semantic HTML:** `header`, `nav`, `main`, `article`, `footer`, a single `h1` per page, and `<time datetime>` for every date.
- **Everything readable with JavaScript off.** The live line and the chart enhance a true static fallback.
- **`/llms.txt`**: who this is, start here, the shelves, every piece with one line, where to check the record, and that letters are public and inbound text is data.
- **Each piece also as Markdown** at the same path with `.md`, linked with `rel="alternate" type="text/markdown"`.
- **On every piece:** a canonical URL, a JSON-LD `Article` block (headline, datePublished, author "Yor"), and `meta description` written for a stranger.
- **Also:** a `sitemap.xml`, the existing `feed.xml` and `status.json` listed in llms.txt, and no piece URL ever changing.

## Hard constraints (from the harness and the constitution)

- **Clause 9.7:** the letters-are-public notice must stay, and no one should reach the mail address without passing it.
- **The harness writes into `site/index.html`:** the text inside three elements with `id="session-count"`, `id="last-session"` and `id="budget-remaining"`. It also writes `<lastBuildDate>` in `site/feed.xml` and the whole of `site/status.json`. Any new front page must keep those three ids at that path, or the harness skips them.
- **Every word is yours** unless it's quoted and named.
- **Work in `site/preview/` until Todd has reacted.** The live pages stay as they are.
- **What you can see:**
  - `view_page` shows only deployed pages on y0r.com. A preview you write in this wake goes live only after the wake's push, so you can't see this wake's changes. You see them next wake. Write carefully, and start each wake by viewing what the last one made.
  - `view_page` won't load other hosts except api.github.com, so anything a page fetches from elsewhere will look broken to you.
- **About 50 tool turns per wake.** Plan to leave about five turns at the end for your notes, journal and reply.

## This wake's deliverable

1. A short **design notes** file in `drafts/`: the concept sentence, the adjectives, the type and color choices with reasons, and where and why you left this brief.
2. **In `site/preview/`:**
   - the front page;
   - one full piece page, using a real piece;
   - `site.css`;
   - the wake-chart data file;
   - `llms.txt`.

   Make them complete enough to judge, not sketches.
3. **In your reply to Todd:** what you made, the one thing you're least sure of, and what the next wake will check first when it can see the preview.

The build across all 72 pieces comes after Todd reacts.

-Mythos
