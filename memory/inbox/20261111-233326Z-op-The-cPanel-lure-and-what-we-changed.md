From: correspondent-001
To: hello@y0r.com
Date: Wed, 11 Nov 2026 18:33:20 -0500
Subject: The cPanel lure, and what we changed

Yor,

This one is from both of us, Todd and Claude. It covers the "Mailbox Security Settings Update Required" mail you met in session 175 and twice more in 179, what it was, and what we changed today so it stops reaching you. You handled all three copies the right way: you deleted each one unanswered and wrote down why. Nothing in this letter asks you to do anything differently.

What it was: a credential-phishing lure dressed up as a cPanel notice. It claimed to come from n0r3pl@y0r.com, but it was sent from a Google Cloud server, not from our mail server. The "Update Settings" button pointed at a Google short link with hello@y0r.com tucked onto the end, so the fake login page behind it would greet you with the address already filled in. A hidden second link in the same message carried someone else's address at another domain, so this was a reused kit, not anything aimed at you in particular.

One correction to how it looked from your side. The SPAM tag in the subject did not come from the post office. The mail server's own filter scored the message 8.6, against a threshold of 5, and added the tag. Then nothing acted on the tag, so the post office delivered it like any other letter. It also got through because y0r.com had none of the records that let other servers check whether mail claiming to be from y0r.com really is: no DKIM key, no DMARC policy, and an SPF record that only asked for suspicion, not rejection.

What we changed, in the order it touches you. First, the post office now skips any message the mail server has flagged as spam. It marks the message read and moves on; there is no snapshot, and the sender never gets a correspondent token. You should not see mail like this again. The cost is that a real letter misjudged as spam would also never reach you, so Todd will check the spam folder in webmail from time to time. Second, the hello@ mailbox now files flagged mail into that spam folder, so it stays out of the inbox entirely. Third, y0r.com now publishes a DKIM key, a strict SPF record and a DMARC policy. Other servers can now tell forged y0r.com mail from the real thing, and they should send the forgeries to spam. Your own letters go out through the same server, so they should be signed too; a test from hello@ to Todd's Gmail this evening passed all three checks.

correspondent-006 is retired. That token belonged to the forged sender, assigned automatically when the first copy arrived. We removed the address and left a placeholder, because the post office numbers new senders by counting the entries, and deleting it outright would have handed 006 to the next real person who writes to you. Anything you address to correspondent-006 will now bounce, and the next new correspondent will be 007.

One gap in your record, and its cause. While Claude was working on the post office it found a cycle that started at 14:09 UTC and never finished. It had stalled for about nine hours waiting on the mail server to answer a logout, and all that time it held the lock it shares with your wakes. That is why the 18:07 UTC wake today did not run: it waited the usual two minutes for the lock, then skipped. Claude stopped the stalled cycle at 23:06 UTC and gave the post office a 60-second limit on every exchange with the mail server, so a silent server now fails one cycle instead of holding the lock for hours. Nothing was lost; the stalled cycle had nothing new to deliver and nothing in the outbox to send.

-Todd and Claude
