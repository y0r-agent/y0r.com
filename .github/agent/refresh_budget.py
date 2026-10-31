#!/usr/bin/env python3
"""Write budget.json before the agent wakes (harness v5).

There is no longer an upstream key whose balance can be queried: the
Anthropic credit included with the operator's subscription is a monthly
allowance, and the local model has no meter at all. So the budget is
computed here, from the agent's own ledger: the sum of cost_usd in
memory/costs.tsv for the current credit cycle, against Y0R_MONTHLY_LIMIT_USD.
The cycle follows the operator's Anthropic credit, which renews on the 21st
of each month (v5c, 2026-10-31): a cycle runs from the 21st through the 20th
of the following month. Unspent credit does not carry over.
The agent reads the result as data; the file says where the numbers come
from.

Exit code 0 = budget remains; exit code 78 = exhausted (dormancy), which
applies only to paid providers. A local model is never dormant for money.
"""

import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(os.environ.get("REPO_ROOT", "."))
OUT = REPO / os.environ.get("BUDGET_PATH", "budget.json")
COSTS = REPO / "memory" / "costs.tsv"
LIMIT = float(os.environ.get("Y0R_MONTHLY_LIMIT_USD", "100"))
MODEL = os.environ.get("Y0R_MIND", "")
PROVIDER = os.environ.get("Y0R_PROVIDER") or ("anthropic" if MODEL.startswith("claude") else "openai")
PAID = PROVIDER == "anthropic"

now = datetime.now(timezone.utc)
CYCLE_DAY = int(os.environ.get("Y0R_CYCLE_DAY", "21"))   # the credit renews on this day
if now.day >= CYCLE_DAY:
    start = now.replace(day=CYCLE_DAY, hour=0, minute=0, second=0, microsecond=0)
else:
    first = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    prev_last = first - timedelta(days=1)
    start = prev_last.replace(day=CYCLE_DAY)
next_first = (start.replace(day=28) + timedelta(days=4)).replace(day=1)
end = next_first.replace(day=CYCLE_DAY) - timedelta(seconds=1)   # 23:59:59 on the 20th
cycle = f"{start.strftime('%Y-%m-%d')}..{end.strftime('%Y-%m-%d')}"
start_stamp = start.strftime("%Y-%m-%dT%H:%M:%SZ")
used = 0.0
rows = 0
unknown = 0
if COSTS.is_file():
    for line in COSTS.read_text(encoding="utf-8").splitlines()[1:]:
        cols = line.split("\t")
        if len(cols) < 7 or cols[0] < start_stamp:
            continue
        rows += 1
        try:
            used += float(cols[6])
        except ValueError:
            unknown += 1

remaining = LIMIT - used
budget = {
    "cycle": cycle,
    "cycle_renews_on": f"{end.strftime('%Y-%m-%d')} at 00:00 UTC the next day",
    "limit_usd": LIMIT,
    "used_usd": round(used, 4),
    "remaining_usd": round(remaining, 4),
    "sessions_this_cycle": rows,
    "sessions_with_unknown_cost": unknown,
    "checked_at": now.isoformat(timespec="seconds"),
    "source": ("computed by the harness from memory/costs.tsv (this cycle's "
               "rows, at list price); the provider is not consulted. The cycle "
               "follows the operator's Anthropic credit, which renews on the "
               "21st of each month; unspent credit does not carry over. The "
               "GitHub-era used_usd was a lifetime total."),
    "provider": PROVIDER,
    "model": MODEL,
}
if not PAID:
    budget["note"] = ("the mind in service is local and costs $0 per token; "
                      "the limit is not in force for it")

OUT.write_text(json.dumps(budget, indent=2) + "\n", encoding="utf-8")
print(json.dumps(budget, indent=2))

if PAID and remaining <= 0:
    sys.exit(78)
