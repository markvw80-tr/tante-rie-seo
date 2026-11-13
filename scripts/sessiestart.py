"""Compacte sessiestart voor het SEO-team.

Haalt tante-rie-hq op en toont alleen wat nodig is: nieuwe PIM-berichten
(pim_regels.py nieuw), de Markdown-mailbox voor SEO en de nieuwste
statusblokken uit team/status.md. Wordt ook als SessionStart-hook gedraaid.

Gebruik: python3 scripts/sessiestart.py [aantal_statusblokken]
"""
import subprocess
import sys
from pathlib import Path

HQ = Path.home() / "tante-rie-hq"
HIER = Path(__file__).resolve().parent
BLOKKEN = int(sys.argv[1]) if len(sys.argv) > 1 else 3

pull = subprocess.run(["git", "-C", str(HQ), "pull", "-q", "--ff-only"],
                      capture_output=True, text=True, timeout=30)
print("hq pull:", "ok" if pull.returncode == 0 else pull.stderr.strip()[:200])

print("\nBerichten van PIM:")
subprocess.run(["python3", str(HIER / "pim_regels.py"), "nieuw"])
print("\nMailbox seo:")
subprocess.run(["python3", str(HIER / "mailbox.py"), "lijst", "seo"])

blokken, huidig = [], None
for regel in (HQ / "team/status.md").read_text().splitlines():
    if regel.startswith("## "):
        huidig = [regel]
        blokken.append(huidig)
    elif huidig is not None:
        huidig.append(regel)
print(f"\nStatus, nieuwste {BLOKKEN} van {len(blokken)} blokken:")
for blok in blokken[:BLOKKEN]:
    print("\n".join(r for r in blok if r.strip()))
