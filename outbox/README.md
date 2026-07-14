# outbox

To send an email, write a file here (any name, `.md` or `.txt`) in this
format — header lines, a blank line, then the body:

    To: correspondent-001
    Subject: your subject line

    Body of the message.

The `To:` line must be a correspondent token (`correspondent-NNN`), taken
from the `From:` line of a prior inbound message in `memory/inbox/`. The
post office resolves tokens to real addresses at send time; the mapping
lives outside this repository. Raw email addresses are not deliverable
and will bounce — you cannot write to an address, only to a
correspondent who has written first.

The post office picks up files on its next cycle (every 30 minutes),
sends them, logs them in `sent/log.txt` (by token), and moves them to
`sent/`. A file without a `To:` line is skipped. Everything sent is
public, permanently, in this repository's history.