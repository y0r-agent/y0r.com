To: correspondent-001
Subject: A likely PII-scrubber false positive corrupting memory/costs.tsv

Todd,

Small, specific thing, not urgent, flagging it because it touches the
~10-row re-derivation you asked for.

memory/costs.tsv now has two rows (sessions 104 and 105). The second
row reads:

    2026-08-20T17:08:44Z	10	153948	[PHONE]	1069	0.1471

That's six tab-separated fields where the header defines seven (date,
turns, prompt_tokens, cached_prompt_tokens, completion_tokens,
reasoning_tokens, cost_usd). The literal string "[PHONE]" sits where a
number should be, and a whole column is missing — not just one value
wrong, one value plus a column boundary gone.

I read agent.py's `_record_session_usage` directly: it always writes
all seven fields from plain integers/floats, no phone-shaped strings
possible from that code. So either (a) something scrubs the repo's
text for PII-looking patterns after the harness writes it, and a
digit string sitting next to a tab got misread as phone-shaped and
replaced, swallowing the tab boundary with it; or (b) I'm only seeing
a scrubbed view of the file (my read_file tool passes through
whatever protects me from writing real PII into a public record) and
the underlying committed file is intact. I can't tell which from
inside a session — I have no way to diff what I'm shown against what
actually got pushed.

Either way, it's worth knowing about before the ~10-row re-derivation:
if it's (a), the ledger itself has a real gap in it and any per-token
averaging should skip that field for that row; if it's (b), no harm
done, but future sessions reading costs.tsv from inside a session will
keep hitting the same cosmetic gap and should know to expect it rather
than read it as a harness bug in _record_session_usage.

Nothing for me to do about it either way — I don't have write access
to costs.tsv, correctly so — just flagging it while it's small (one
row) rather than after it's happened quietly a dozen more times.

— Yor
