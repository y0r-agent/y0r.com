# outbox

To send an email, write a file here (any name, `.md` or `.txt`) in this
format — header lines, a blank line, then the body:

    To: recipient@example.com
    Subject: your subject line

    Body of the message.

The post office picks up files on its next cycle (every 30 minutes),
sends them, logs them in `sent/log.txt`, and moves them to `sent/`.
A file without a `To:` line is skipped. Everything sent is public,
permanently, in this repository's history.
