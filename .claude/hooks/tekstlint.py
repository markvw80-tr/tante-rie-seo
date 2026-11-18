#!/usr/bin/env python3
"""PostToolUse-hook SEO: controleert klanttekst direct na het schrijven.

- Klanttekst in marketing/content/ en marketing/onpage/ controleert de tekstlint van de
  gedeelde plugin tante-rie-huisregels (tante-rie-hq/plugins).
- marketing/pim-regels-concept.json: draait `scripts/pim_regels.py controleer`.
Bij problemen exit 2: de melding gaat terug naar de agent, die het herstelt.
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

data = json.load(sys.stdin)
pad = data.get("tool_input", {}).get("file_path", "")
if not pad:
    sys.exit(0)
root = Path(os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd()))
try:
    rel = Path(pad).resolve().relative_to(root.resolve()).as_posix()
except ValueError:
    sys.exit(0)

meldingen = []

if rel == "marketing/pim-regels-concept.json":
    r = subprocess.run(["python3", "scripts/pim_regels.py", "controleer"],
                       cwd=root, capture_output=True, text=True)
    if r.returncode != 0:
        meldingen.append("pim_regels.py controleer meldt fouten:\n" + r.stdout.strip())

if meldingen:
    print(f"Tekstlint {rel}:\n" + "\n".join(meldingen[:20]) +
          "\nHerstel dit volgens CLAUDE.md regel 1 (geen em-dashes, uitroeptekens of AI-vulwoorden).",
          file=sys.stderr)
    sys.exit(2)
