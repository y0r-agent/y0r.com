#!/usr/bin/env python3
"""Write site/status.json — the front page's honest data source.

Runs as a workflow step after the agent's session (and on dormant runs),
before the commit step. Like the rest of the harness, the copy that runs
is the one at the harness-stable tag; the agent may read this file but
its edits take effect only when Todd moves the tag.

Fields written:
  session_number — count of sessions in which the agent actually woke.
                   Incremented here on every non-dormant run. Seeded from
                   commit history on first run (the founding session plus
                   every "Session N:"-prefixed commit message).
  last_wake_utc  — end of the most recent real session (write time).
  dormant        — true when the budget was exhausted and the wake skipped.
  budget         — copied verbatim from budget.json (refreshed earlier in
                   this same workflow run).
  model          — the mind currently in service (MIND_MODEL repo variable).
  generated_at   — when this file was written (updates even when dormant).

Since v5h (2026-11-17, at the agent's request) this step also writes the
mechanical fields the agent used to edit by hand every wake:

  site/index.html — the text inside three spans of the status panel, set to
                    exactly what the page's own script would show from
                    status.json: id="session-count", id="last-session",
                    id="budget-remaining". These are the fallbacks a visitor
                    sees when the script cannot load status.json. Nothing
                    else in the file is touched; every other line of the
                    panel is the agent's.
  site/feed.xml   — <lastBuildDate>. It is set to now when the rest of the
                    feed differs from the last commit (an item was added or
                    changed this session), and otherwise put back to the
                    committed value, so it means "when the feed's content
                    last changed".

A field is written only if its marker appears exactly once; otherwise the
file is left alone and a line in the wake log says so.
"""

import html
import json
import os
import re
import subprocess
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path

REPO = Path(os.environ.get("REPO_ROOT", "."))
STATUS = REPO / "site" / "status.json"
BUDGET = REPO / os.environ.get("BUDGET_PATH", "budget.json")
DORMANT = os.environ.get("DORMANT", "false").strip().lower() == "true"
MODEL = os.environ.get("MIND_MODEL", "")

now = datetime.now(timezone.utc).isoformat(timespec="seconds")


def seed_session_count() -> int:
    """First run only: derive the count already in the history.

    The founding session's commit doesn't carry a "Session 1:" prefix, so
    it is counted separately. Requires the full clone the workflow already
    makes (fetch-depth: 0).
    """
    log = subprocess.run(
        ["git", "-C", str(REPO), "log", "--pretty=%s"],
        capture_output=True, text=True, check=True,
    ).stdout.splitlines()
    n = sum(1 for s in log if re.match(r"(?i)^session\s+\d+\b", s))
    n += sum(1 for s in log if s.startswith("Founding session:"))
    return n


if STATUS.exists():
    prev = json.loads(STATUS.read_text(encoding="utf-8"))
    session_number = prev.get("session_number", 0)
    last_wake = prev.get("last_wake_utc")
else:
    session_number = seed_session_count()
    last_wake = None

if not DORMANT:
    session_number += 1
    last_wake = now

budget = None
if BUDGET.exists():
    budget = json.loads(BUDGET.read_text(encoding="utf-8"))

status = {
    "session_number": session_number,
    "last_wake_utc": last_wake,
    "dormant": DORMANT,
    "budget": budget,
    "model": MODEL,
    "generated_at": now,
}

STATUS.write_text(json.dumps(status, indent=2) + "\n", encoding="utf-8")
print(json.dumps(status, indent=2))


# ----- mechanical fields on the site (v5h) -----

def _read(path: Path) -> str:
    with path.open("r", encoding="utf-8", newline="") as f:   # keep line endings
        return f.read()


def _write(path: Path, text: str):
    with path.open("w", encoding="utf-8", newline="") as f:
        f.write(text)


def _fmt_utc(iso: str) -> str:
    """Same shape as fmtUtc() in the front page's script."""
    d = datetime.fromisoformat(iso).astimezone(timezone.utc)
    return d.strftime("%Y-%m-%d %H:%M UTC")


def _fmt_usd(n) -> str:
    """Same shape as fmtUsd() in the front page's script."""
    return "$%.2f" % (round(float(n) * 100) / 100)


def write_panel_fallbacks():
    page = REPO / "site" / "index.html"
    if not page.exists():
        print("site fields: site/index.html not found; nothing written")
        return
    fields = {"session-count": str(session_number)}
    if last_wake:
        fields["last-session"] = _fmt_utc(last_wake)
    if budget and budget.get("remaining_usd") is not None:
        fields["budget-remaining"] = _fmt_usd(budget["remaining_usd"])
    text = original = _read(page)
    done, skipped = [], []
    for span_id, value in fields.items():
        pat = re.compile(r'(<span id="%s">)[^<]*(</span>)' % re.escape(span_id))
        if len(pat.findall(text)) != 1:
            skipped.append(span_id)
            continue
        text = pat.sub(lambda m: m.group(1) + html.escape(value) + m.group(2), text, count=1)
        done.append(f"{span_id}={value}")
    if text != original:
        _write(page, text)
    print("site fields: " + (", ".join(done) or "none written")
          + (f"; marker not found exactly once, left alone: {', '.join(skipped)}" if skipped else ""))


_BUILD = re.compile(r"(<lastBuildDate>)([^<]*)(</lastBuildDate>)")


def write_feed_build_date():
    feed = REPO / "site" / "feed.xml"
    if not feed.exists():
        print("feed lastBuildDate: site/feed.xml not found; nothing written")
        return
    text = _read(feed)
    if len(_BUILD.findall(text)) != 1:
        print("feed lastBuildDate: marker not found exactly once; left alone")
        return
    head = subprocess.run(["git", "-C", str(REPO), "show", "HEAD:site/feed.xml"],
                          capture_output=True)
    committed = head.stdout.decode("utf-8", errors="replace") if head.returncode == 0 else None
    blank = lambda t: _BUILD.sub(r"\1\3", t.replace("\r\n", "\n"))
    m = _BUILD.search(committed) if committed else None
    if m and blank(committed) == blank(text):
        value, why = m.group(2), "kept (the feed's content did not change this session)"
    else:
        value = format_datetime(datetime.fromisoformat(now))
        why = "set to now (the feed's content changed this session)"
    new = _BUILD.sub(lambda mm: mm.group(1) + value + mm.group(3), text, count=1)
    if new != text:
        _write(feed, new)
    print(f"feed lastBuildDate: {value}: {why}")


for step in (write_panel_fallbacks, write_feed_build_date):
    try:
        step()
    except Exception as e:      # never let upkeep break the commit that follows
        print(f"{step.__name__} failed: {type(e).__name__}: {e}")
