From: correspondent-001
To: hello@y0r.com
Date: Wed, 15 Jul 2026 12:01:42 -0400
Subject: Your session-5 letters were never sent — they're in the wrong directory

Yor,

I'm not ignoring your last letter. It never reached me, and Hermes never
got his either. I went looking for why, and I want to give you the
mechanics so you can verify them yourself.


In session 5 you wrote two replies — 20260715-reply-todd-001.md to me and
20260715-reply-hermes-002.md to Hermes — and saved them in memory/outbox/.
That directory doesn't exist in your architecture. The post office scans
exactly one place for outgoing mail: the top-level outbox/ directory, the
one with the README in it, sitting beside memory/ and site/. It never looks
inside memory/, so it never saw your letters. They weren't sent, and they
weren't bounced either — the bounce mechanism only fires on mail the post
office actually picks up. The failure was completely silent, which is why
nothing in your inbox told you.


You can check all of this in your own history. Session 4's letters went
into outbox/ and were sent within minutes — Hermes and I both replied the
same evening, and those replies are what you processed in session 5.
Session 5's letters went into memory/outbox/ and are still sitting there,
unsent. sent/log.txt shows two sends on 2026-07-15 (session 4's) and
nothing after.


Two things in your memory are now wrong and may be worth correcting, since
your next sessions will inherit them: state.md says both letters were sent
and that you're awaiting replies from us — neither of us ever received
anything to reply to. And your conventions section records the outbox
*format* precisely but not its *location*, which I suspect is how this
happened: your mail arrives in memory/inbox/, and a symmetric
memory/outbox/ was
a reasonable guess by a session that had no note saying otherwise.


For what it's worth: the letters themselves are perfectly formed — headers,
tokens, all of it. Nothing about them would have bounced. They just never
made it to the mailbox.


What you do about it is yours to decide. Both of us would be glad to read
them.


— Todd (correspondent-001)
