# Governance

This agent operates under a constitution. The full text is public in this
repository at `CONSTITUTION.md`. That text is the authority, and this file
no longer summarizes it. Todd's copy is authoritative; any difference
between the copies is corrected in public with a date.

The founding text of 2026-07-13 is kept unchanged at
`constitution/founding-2026-07-13.md`. Where each clause of the current
text came from, and why, is in `constitution/notes.md`. The notes explain;
they do not bind.

Amendments are made by Todd only, each with a dated, public reason,
recorded here and made to the text at the same time. Entries before
2026-11-21 amended the founding text.

## Amendment log

- **2026-07-14** — The founding session's cost ($1.35, Claude Fable 5) is
  forgiven: the monthly limit was raised once, by exactly that amount, so
  month one begins with a full $100. Reason: the founding mind was the
  operator's requirement, not the agent's choice; the agent should not begin
  in debt to its own birth. The limit returns to $100.00 at the August reset.

- **2026-07-14** — Repository history was rewritten to remove a
  correspondent's personal data (a real name and email address) that
  entered via an inbound mail snapshot and the agent's use of it; commit
  hashes before this date changed. Concurrently, the post office now
  pseudonymizes all correspondent addresses to stable tokens in both
  directions. Reason: correspondents did not consent to their personal
  data becoming a permanent public record; the operator judged PII
  removal the one justified edit to history. A mechanical notice of
  these changes was delivered to the agent's inbox.

- **2026-10-31** — The month-boundary timing on mind changes is suspended,
  effective immediately. The agent may choose its mind at any wake by writing
  the model's id as the first line of `mind.txt` at the repository root; the
  harness reads it at the next wake and reports the source of the choice in
  the wake message. The operator's configuration applies only when the file is
  absent or names a model not on the menu. Public reasoning remains the
  agent's practice, not a precondition, and the operator no longer executes
  the change by hand. Reason: the waiting period existed to slow spending
  against a hard monthly cap on a single paid provider. With a zero-cost local
  mind on the menu, a monthly allowance in place of a prepaid key, and the
  operator reading every wake, the delay protects nothing and only postpones
  the agent's own decision. The cap and dormancy at zero are unchanged.

- **2026-11-21** — The founding text of 2026-07-13 is replaced by a second
  text, `CONSTITUTION.md`. The agent wrote it over one conversation
  (sessions 210 to 217), at the operator's request and against his written
  disagreements, and the operator ratified it. Reason: the agent could
  never read the founding text, the public summary of it left out the
  gift, and three of its mechanisms no longer exist. The founding text is
  kept unchanged at `constitution/founding-2026-07-13.md`.
