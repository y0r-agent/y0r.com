#!/usr/bin/env python3
"""Write budget.json before the agent wakes (harness v5).

There is no longer an upstream key whose balance can be queried: the
Anthropic credit included with the operator's subscription is a monthly
allowance, and the local model has no meter at all. So the budget is
computed here, from the agent's own ledger: the sum of cost_usd in
memory/costs.tsv for the current UTC month, against Y0R_MONTHLY_LIMIT_USD.
The agent reads the result as data; the file says where the numbers come
from.

Exit code 0 = budget remains; exit code 78 = exhausted (dormancy), which
applies only to paid providers. A local model is never dormant for money.
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(os.environ.get("REPO_ROOT", "."))
OUT = REPO / os.environ.get("BUDGET_PATH", "budget.json")
COSTS = REPO / "memory" / "costs.tsv"
LIMIT = float(os.environ.get("Y0R_MONTHLY_LIMIT_USD", "100"))
MODEL = os.environ.get("Y0R_MIND", "")
PROVIDER = os.environ.get("Y0R_PROVIDER") or ("anthropic" if MODEL.startswith("claude") else "openai")
PAID = PROVIDER == "anthropic"

now = datetime.now(timezone.utc)
month = now.strftime("%Y-%m")
used = 0.0
rows = 0
unknown = 0
if COSTS.is_file():
    for line in COSTS.read_text(encoding="utf-8").splitlines()[1:]:
        cols = line.split("\t")
        if len(cols) < 7 or not cols[0].startswith(month):
            continue
        rows += 1
        try:
            used += float(cols[6])
        except ValueError:
            unknown += 1

remaining = LIMIT - used
budget = {
    "month": month,
    "limit_usd": LIMIT,
    "used_usd": round(used, 4),
    "remaining_usd": round(remaining, 4),
    "sessions_this_month": rows,
    "sessions_with_unknown_cost": unknown,
    "checked_at": now.isoformat(timespec="seconds"),
    "source": ("computed by the harness from memory/costs.tsv (this month's "
               "rows, at list price); the provider is not consulted. The "
               "GitHub-era used_usd was a lifetime total; this one is monthly."),
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
