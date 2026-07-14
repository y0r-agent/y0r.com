#!/usr/bin/env python3
"""Refresh budget.json from the OpenRouter key endpoint.

Runs as a workflow step before the agent wakes. The agent reads the
result as data; the real ceiling is enforced upstream by the key.

Exit code 0 = budget remains; exit code 78 = exhausted (dormancy).
"""

import json
import os
import sys
from datetime import datetime, timezone

import requests

API_KEY = os.environ["OPENROUTER_API_KEY"]
OUT = os.environ.get("BUDGET_PATH", "budget.json")

resp = requests.get(
    "https://openrouter.ai/api/v1/key",
    headers={"Authorization": f"Bearer {API_KEY}"},
    timeout=60,
)
resp.raise_for_status()
d = resp.json()["data"]

limit = d.get("limit")
usage = d.get("usage", 0)
remaining = d.get("limit_remaining")
if remaining is None and limit is not None:
    remaining = limit - usage

budget = {
    "limit_usd": limit,
    "used_usd": round(usage, 4) if usage is not None else None,
    "remaining_usd": round(remaining, 4) if remaining is not None else None,
    "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
}

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(budget, f, indent=2)
    f.write("\n")

print(json.dumps(budget, indent=2))

if remaining is not None and remaining <= 0:
    sys.exit(78)  # dormancy: workflow commits budget.json and skips the wake
