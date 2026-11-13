#!/usr/bin/env python3
"""PreToolUse-hook SEO: `pim_regels.py stuur` alleen na akkoord van de kwaliteitsredacteur.

De kwaliteitsredacteur legt akkoord vast met `python3 scripts/pim_regels.py akkoord`
(marketing/review/pim-regels-akkoord.json met een hash van het concept). Is het concept
daarna gewijzigd, of ontbreekt het akkoord, dan blokkeert deze hook het versturen.
"""
import json
import os
import re
import sys
from pathlib import Path

data = json.load(sys.stdin)
if data.get("tool_name") != "Bash":
    sys.exit(0)
if not re.search(r"pim_regels\.py\s+stuur\b", data.get("tool_input", {}).get("command", "")):
    sys.exit(0)

root = Path(os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd()))
sys.path.insert(0, str(root / "scripts"))
import pim_regels  # noqa: E402

reden = None
try:
    ak = json.loads(Path(pim_regels.AKKOORD).read_text())
    if ak.get("hash") != pim_regels.hash_concept():
        reden = "Het concept is gewijzigd na het akkoord van de kwaliteitsredacteur."
except (OSError, ValueError):
    reden = "Er is geen akkoord van de kwaliteitsredacteur op het concept."
if reden:
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": reden + " Laat de kwaliteitsredacteur het concept toetsen en "
                                    "`python3 scripts/pim_regels.py akkoord` draaien."}}))
