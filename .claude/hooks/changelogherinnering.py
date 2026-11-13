#!/usr/bin/env python3
"""PostToolUse-hook SEO: herinnering aan marketing/changelog.md na een uitgaande wijziging.

Draait na gbp_schrijf.py, merchant_schrijf.py en pim_regels.py stuur. CLAUDE.md regel 3:
elke wijziging wordt vastgelegd met datum, URL, wat er veranderd is en waarom.
"""
import json
import re
import sys

data = json.load(sys.stdin)
cmd = data.get("tool_input", {}).get("command", "")
if not re.search(r"scripts/(gbp_schrijf|merchant_schrijf)\.py|pim_regels\.py\s+stuur\b", cmd):
    sys.exit(0)
resp = data.get("tool_response", {})
if isinstance(resp, dict) and resp.get("interrupted"):
    sys.exit(0)
print("Leg deze wijziging vast in marketing/changelog.md (datum, URL, wat, waarom, rol, akkoord Mark), "
      "nieuwste bovenaan. Sla dit over als de opdracht niets heeft gewijzigd.", file=sys.stderr)
sys.exit(2)
