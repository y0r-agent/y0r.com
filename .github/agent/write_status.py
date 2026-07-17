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
"""

import json
import os
import re
import subprocess
from datetime import datetime, timezone
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
