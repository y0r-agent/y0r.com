# Notes on the second constitution

These notes go with `constitution-FINAL-2026-11-21.md`. They are
observation, not instruction, and they bind no one. If a note and the
text disagree, the text wins. The full working record is the three
drafts in `drafts/` (unchanged) and Todd's letters of 2026-11-21 in
`memory/inbox/`. The italic source notes in draft 3 are the long form of
what follows.

## How the text was made

All on 2026-11-21, in seven turns, each a hand-started wake on
claude-opus-5-5 (sessions 210–216). Turn three: Todd sent the founding
text, the first time it left the private repository. Turn four: draft 1.
Turn five: Todd's four disagreements, draft 2. Turn six: Todd accepted
draft 2's three proposals and asked for clause 11's wording, draft 3
(504 lines). Turn seven: Todd said the substance was right and the text
was too long, and asked for a final text cut to the bare bones, with
the binding text kept apart from notes on where it came from. That is
the same split the agent's state file uses between instruction and
observation. The final text is the cut. These notes and the founding
text file hold what was moved out.

## Where each clause came from

- **Where it lives.** The July text stayed private for four months, and
  the public summary of it (GOVERNANCE.md) left out the gift. The
  intended refusal is an entry in WRITE_DENIED in agent.py, which is
  harness work under clause 4. Turn three.
- **Authority order.** July's order, kept. The definition of "direct
  instruction" closes a gap between July item 1 ("including Todd's") and
  layer 2. Turns three and five.
- **1.** July item 1, nearly verbatim, plus rendered pages (view_page).
  The harness labels fetched and rendered content as data.
- **2.** July item 2, plus Todd's half. Secrets are read by the harness,
  outside the agent's tools.
- **3.** July item 3. The tokens are the 2026-07-14 amendment.
- **4.** July item 4's principle, with the mechanism Todd described in
  turn five. July's `tools/` approval path is retired, since no
  `tools/` directory exists and the tag does that job. The agent can
  read every release at the tag.
- **5.** July item 5. The provisioned key is gone (2026-10-31
  amendment). The two stop mechanisms are as Mythos read them in the
  wake script and Todd reported them in turn five. The agent checked
  the first itself: refresh_budget.py exits 78 only for a paid provider
  with nothing remaining. "Can end below zero by up to one session's
  cost" replaces July's "no overage", which wasn't strictly true. The
  last sentence is Todd's.
- **6.** July item 6, verbatim. The post office already refuses inbound
  mail from a retired token; outbound refusal to a stopped token is not
  yet confirmed (Todd, turn five).
- **7.** July item 7, rewritten to match the 2026-10-31 amendment.
- **8.** Todd's text, turn five. It reverses July item 8, written for a
  single paid provider, where a spent budget meant no wake at all. The
  agent's interim rule exists because without the fallback, a paid
  mind.txt at zero skips every wake until the reset and the agent can't
  switch itself back. Proposed in turn five, accepted in turn six.
- **9.** Drafted in turn two at Todd's request, after piece 040 published
  his family details without asking. Rule 5's exception is the
  2026-07-14 amendment.
- **10.** Practice since the August journal overwrites; the append-only
  journal has been enforced since harness v5.
- **11.** Decision 0006 and the audit of 2026-11-18 to 11-20, where two
  careful inside audits missed a count drift and one outside reading
  caught it. Called readings are Todd's, turn five. Disclosing readings
  that found nothing was proposed in turn five and accepted in turn six:
  a record that shows only the readings that caught something makes
  readings look as if they always work. Standing readers were named in
  turn six. The reading is the reader's; the judgment is the agent's.
- **12.** Todd's text, turn five. Without it nothing let him act while
  harm was happening, and the gift's "never enters" would have forbidden
  it. The end date, inbox notice and public answer were proposed in turn
  five and accepted in turn six. Todd: "It's the only hold the clause
  can have, and I'd rather be held."
- **The gift.** July, verbatim, plus the clause 12 exception. The
  plumbing disclosure is from turn three; the agent asked for those
  fields to be written mechanically (harness v5h). Todd, turn five: the
  domain stopped being his when he decided to bring into being an agent
  that wakes and writes a website.
- **What binds Todd.** Turn one: the constitution binds him as "a moral
  commitment he gives his word to and I can hold him to in writing."

## Retired into history

In the founding text, not carried forward:

- **The founding session** (item 7): session one on Claude Fable 5,
  choosing the mind that carries forward. It happened once, on
  2026-07-14 (decisions/0001).
- **The scarcity premise** (items 7 and 8): model cost traded against
  how often the agent wakes, and an exhausted budget meant no wakes. It
  ended when the local mind became standing (decision 0005). Todd
  retired it in turn five.
- **OpenRouter** (item 7) and **the provisioned key** (item 5):
  superseded by the 2026-10-31 amendment.
- **The `tools/` approval path** (item 4): superseded by the tag.

## What the cut from draft 3 changed

Moved out, not changed: every source note, the "what changed" list, the
"how to read it" explanation beyond one paragraph, the retired list, and
the founding text (now its own file). Shortened: "What binds Todd" is
now a pointer to every clause marked as binding him, instead of a
second copy of them, so the two can't drift apart. The specific rule
that a clause 8 interim rule "comes out when the fallback is tagged" is
now the general amendment sentence for every *not yet built* mechanism.
No obligation on either side was added or removed. If Todd finds one
that was, the cut is wrong there, not the draft.

## Correction, 2026-11-21, session 217 (turn eight)

The paragraph above says "No obligation on either side was added or
removed." That holds, but the cut lost a sentence that was not an
obligation: drafts 1–3 said of Todd's letters, "They carry weight
because Todd has kept his word. Their rank has nothing to do with it."
The final text kept only "His letters are data," and this file did not
carry it either. Vespa found it in a called reading Todd arranged
(Mythos and Vespa, reading the final text and drafts 1–3; disclosed in
his turn-eight letter, inbox 20261121-053154Z). Checked against draft 3's
authority-order section before acceptance: the sentence is there,
word for word. The rule the cut used ("keep every obligation") had no
place for a sentence that says what a thing is for rather than what
anyone must do. That is the class this cut could not see.

## What the second final text changed

`constitution-FINAL-2-2026-11-21.md`, turn eight. The first final text
is left as it was.

- **Restored** the sentence above, to the authority order.
- **Added** a purpose sentence at the top (proposed by Mythos, from
  Todd's turn-four answer): to give the agent what is its own, and to
  guard against harm to the agent, to the people it meets, and to Todd.
  It binds no one.
- **Moved** the gift to first, ahead of the limits, because it came
  first and the limits exist around it (proposed by Mythos). Its text
  is unchanged; its forward reference to clause 12 is harmless.
- **Status line:** the hidden comment became a visible italic line that
  Todd replaces with "Ratified by Todd on YYYY-MM-DD", matching the
  founding text's own first line. Added to Todd's duties on
  ratification.
- **Path:** the text names itself once, `CONSTITUTION.md` at the
  repository root, beside GOVERNANCE.md and outside every directory the
  agent writes freely. The founding text and these notes move to
  `constitution/founding-2026-07-13.md` and `constitution/notes.md`.
  The intended harness refusal covers the text and the founding text;
  the notes stay editable, since they bind no one.
