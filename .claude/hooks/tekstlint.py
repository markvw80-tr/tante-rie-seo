#!/usr/bin/env python3
"""PostToolUse-hook SEO: controleert klanttekst direct na het schrijven.

- marketing/content/*.md en marketing/onpage/*.md: geen gedachtestreepjes,
  geen uitroeptekens, geen AI-vulwoorden (lijst uit PIM lint_nl_copy.py).
  Tabelregels, citaten en codeblokken worden overgeslagen (daar staan oude
  waarden of voorbeelden).
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
elif re.match(r"marketing/(content|onpage)/.+\.md$", rel):
    filler = ["ontdek", "geniet van", "perfect voor elk moment", "de ultieme",
              "unieke combinatie", "kortom", "al met al", "of je nu",
              "laat je verrassen", "must-have", "in de wereld van"]
    lint = Path.home() / "Tante Rie PIM/scripts/lint_nl_copy.py"
    if lint.exists():
        m = re.search(r"FILLER\s*=\s*\[(.*?)\]", lint.read_text(), re.S)
        if m:
            filler = re.findall(r'"([^"]+)"', m.group(1)) or filler
    in_code = False
    for nr, regel in enumerate(Path(pad).read_text().split("\n"), 1):
        if regel.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code or regel.lstrip().startswith(("|", ">")):
            continue
        schoon = re.sub(r"(?<=\d)–(?=\d)", "", regel)
        schoon = re.sub(r"!\[|!=", "", schoon)
        if "—" in schoon or "–" in schoon:
            meldingen.append(f"regel {nr}: gedachtestreep")
        if "!" in schoon:
            meldingen.append(f"regel {nr}: uitroepteken")
        laag = regel.lower()
        for w in filler:
            if w in laag:
                meldingen.append(f"regel {nr}: vulwoord '{w}'")

if meldingen:
    print(f"Tekstlint {rel}:\n" + "\n".join(meldingen[:20]) +
          "\nHerstel dit volgens CLAUDE.md regel 1 (geen em-dashes, uitroeptekens of AI-vulwoorden).",
          file=sys.stderr)
    sys.exit(2)
