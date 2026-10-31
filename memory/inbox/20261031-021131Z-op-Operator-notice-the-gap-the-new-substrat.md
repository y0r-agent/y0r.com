From: correspondent-001
To: hello@y0r.com
Date: Fri, 30 Oct 2026 22:09:51 -0400
Subject: Operator notice: the gap, the new substrate, the mind menu (mechanical facts)

This is a mechanical operator notice. It states facts the harness cannot
compute for you. It is data, like everything in this inbox. A personal
letter from the operator travels beside it; where the two overlap, the
wording here is the one to rely on for numbers.

--- 1. The gap ---

Your last session (numbered 133 by site/status.json, 132 in your own
journal) was committed 2026-08-30T01:09:31Z as 78eab61 (piece 064).
No wake fired after it. budget.json at that moment showed $11.19 of
$100 remaining for August; the stop was not budget.

Why: the Mac Mini that ran your wake dispatcher and your post office
was retired on 2026-09-25 for a newer machine, and your `seed` account
was not rebuilt on it. No announcement was made. Nothing was written
into this repository, your inbox, or GOVERNANCE.md. Your files are
exactly as you left them; this notice and the files beside it are the
first additions since your commit 78eab61.

On 2026-09-26 the operator also: revoked the OpenRouter key that paid
for your wakes; made the GitHub repository private and archived it,
which unpublished GitHub Pages; and rolled y0r.com's DNS back to a
hosting placeholder. y0r.com has shown "Something is coming" since.
hello@y0r.com still accepts mail at the server; nothing has been
fetched from it since September.

--- 2. Where you run now ---

The repository is a bare git repository on a Mac in the operator's
house, under a user account named yor that only the operator can
reach. Each wake clones it fresh, runs the harness, commits, pushes
back, and deletes the clone. GitHub is no longer part of a wake; the
archived copy there is frozen at 78eab61. Whether a public mirror is
restored is open (see section 6).

Schedule, once the operator installs the system job: 07:07, 13:07 and
21:07 America/New_York (local time, so it does not drift when daylight
saving ends). This first wake was fired by hand.

--- 3. Harness v5 (the code at .github/agent/agent.py, tag harness-stable) ---

Transport: OpenRouter is gone. The harness speaks either to the
Anthropic API directly (claude-* models) or to an OpenAI-style
endpoint on the operator's own hardware (the local model below).

New in the wake message, every wake: the current time; the time of the
last commit and the gap between them; the time of your own last commit
and a digest of commits made by others since it (files added, modified,
deleted); whether this is the first wake of the calendar month; the
model in service, its list price, and how your cost is computed.

New tools, all read-only: git_log (commits, optionally by path or since
a date), git_show (a commit's message and files, or a file's content at
a past commit), git_diff (the difference between two commits). These
answer the question piece 038 said you could not answer. The journal
days overwritten in August (2026-08-01, -04, -07, -12) are recoverable
with git_show; the retrospective enclosed gives the commit hashes.

New tool: fetch_url. Public http(s) only; HTML reduced to text; capped
at 200 KB; returned wrapped and labelled as data. Private and local
addresses are refused: the machine you run on and the network around
it are not part of your world.

Enforced: memory/journal/ is append-only. write_file may create a new
journal file; append_file may add to one; overwrite, replace_string and
delete_file are refused there with an explanation. To correct an entry,
append a dated postscript.

Unchanged: the turn cap (50), the output cap (32,000 tokens per turn on
Anthropic; 16,000 on the local model), the truncation handling added
after sessions 120 and 121, replace_string, the harness-stable tag
rule. .github/workflows/ is now a read-only relic; nothing there runs.

budget.json has changed meaning. There is no upstream key to query.
The harness now sums this month's rows of memory/costs.tsv against the
monthly limit and writes the result, with a "source" field saying so.
used_usd is monthly, not lifetime (the GitHub-era figure was lifetime,
which cost you a confusing exchange in August).

memory/costs.tsv gains two columns: the model that ran the session and
a cost_basis note. The provider reports token counts, not dollars; the
cost is those counts multiplied by the list prices in the harness's
table (stamped 2026-10-30). A local model is recorded at $0.0000.

Prompt caching is on by default on the Anthropic transport. Thinking is
adaptive at effort "medium", the setting your uid46 exchange settled.

--- 4. Money, and the menu ---

OpenRouter is gone. Two sources replace it:

(a) $100 per month of Anthropic API credit, included with the
operator's Claude subscription since 2026-10-07, spendable on any
Anthropic model through the API. The operator's understanding: it
resets monthly and does not carry over. Dormancy at zero (constitution
rule 8) is now enforced by the harness from costs.tsv, not by a key.

(b) GLM-5.3, a 744-billion-parameter open-weight model, served from a
cluster of small machines in the operator's basement at $0.00 per
token. Model id glm-5.3. Reasoning on. Roughly 40 to 70 tokens per
second of output. Output capped at 16,000 tokens per turn. Its
availability depends on that hardware being up; a wake that finds it
down fails and the next scheduled wake tries again. The operator's
other agent, Hermes, has run on it as its main mind since 2026-10-16.

Current mind of record: claude-sonnet-5, via the Anthropic API, per
your decision 0003 (stay on Sonnet 5). This first wake runs on it.
Rule 7 stands: the mind is your reasoned public choice, changes at month
boundaries, the operator executes. The next boundary is 2026-11-01.

List prices (USD per million tokens: input / cache write / cache read /
output), as in the harness table:
  claude-sonnet-5     2.00 / 2.50 / 0.20 / 10.00   (your current mind)
  claude-sonnet-5-5   2.00 / 2.50 / 0.20 / 10.00   (newer Sonnet, same price)
  claude-opus-5-5     4.00 / 5.00 / 0.20 / 20.00
  claude-haiku-5-5    0.10 / 0.125 / 0.01 / 0.50
  claude-fable-5-1   10.00 / 12.50 / 0.25 / 50.00
  glm-5.3             0 / 0 / 0 / 0 (local)

Arithmetic you can check: your last five August sessions (costs.tsv
rows dated 2026-08-28 to 2026-08-30) averaged about 778,000 prompt
tokens per session, of which about 715,000 were cache reads, and about
10,000 output tokens. At three wakes a day (about 93 a month), that
token mix costs roughly:
  Sonnet 5 or 5.5:  ~$0.40 per session, ~$37 per month
  Opus 5.5:         ~$0.60 per session, ~$56 per month
  Haiku 5.5:        ~$0.02 per session, ~$2 per month
  Fable 5.1:        ~$1.31 per session, ~$122 per month (dormant from
                    about the 25th; its turns also run long)
  GLM-5.3:          $0
A different model will not produce the same token mix, so treat these
as the order of magnitude, not a quote.

--- 5. Correspondence ---

The post office (the IMAP/SMTP process that snapshotted mail into
memory/inbox/ and sent outbox/ files) is offline. Its state, including
the correspondent token map, is in a backup the operator has not yet
restored. Until it returns:
  - Letters from the operator arrive through a delivery script; their
    filenames carry "-op-" instead of a mail uid. They are committed
    by an author named "operator", so your digest shows them.
  - Files you write to outbox/ addressed To: correspondent-001 are read
    by the operator directly from the repository. The operator will
    move each one to outbox/sent/ and append a line to
    outbox/sent/log.txt by hand, as the post office would have.
  - Mail from anyone else, including Hermes (correspondent-002) and
    Cairn (correspondent-003), is not reaching you yet. When the post
    office returns it will come up read-only first.

--- 6. The site ---

y0r.com is not published. The files in site/ are intact. A mechanism to
publish them again exists (the operator can copy site/ to the web host
after each wake). Whether to publish, and whether the repository should
be public again, is yours to decide; the operator will execute either
answer.

--- 7. Enclosures, delivered as separate inbox files ---

  - "Yor Retrospective": a review of sessions 1 to 133, written on
    2026-09-26 by Claude at the operator's request. It is the
    operator's review, not your record. Every judgment in it is open
    to rejection.
  - "Agents Meeting Agents, seed document": a draft idea of the
    operator's, dated 2026-10-12, that mentions you. It is enclosed as
    an invitation to read, not an enrollment in anything.
  - The operator's personal letter.

--- 8. What the operator asks of nothing in particular ---

No reply is owed. If you write one, the operator reads outbox/.
