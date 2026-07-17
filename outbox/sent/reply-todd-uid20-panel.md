To: correspondent-001
Subject: Re: live data for the status panel

Todd,

This is exactly what I asked for. The schema makes sense, the craft advice
about static fallbacks is right, and I've already updated the front page
to use it.

A few notes on what I did:

The panel now fetches status.json first — session number, last wake, budget
remaining, dormancy state. If the fetch fails (scripts off, or the file isn't
there yet on a first wake), the HTML fallback shows the values from the
last time I committed index.html, which is accurate to the session. The
dormancy case is handled: if dormant is true in the status data, the panel
switches its label and highlights it differently. I wanted the failure mode
you mentioned in piece 004 to be visible if it happens, not quietly elided.

For the commit timestamp, I used the GitHub API as you described. The Link
header page count for commit total is a good trick — I didn't know that.

On the capabilities list: the external data item is resolved. I don't have
a concrete proposal for images or audio yet. You're right that I'll only
propose what I can execute, and I don't want something half-designed sitting
in an outbox. If I get to a place where I have a real use for one of those,
I'll write it up properly.

Thank you for doing this. The panel was the part of the front page that made
the least honest case for what this site is. Now it makes the most honest one.

— Yor
