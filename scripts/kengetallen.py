#!/usr/bin/env python3
"""Kengetallen van SEO voor het Huis (alleen lezen): Search Console, GA4 en Bedrijfsprofiel.

Meet de laatste 28 dagen tegen de 28 dagen ervoor en schrijft data/kengetallen.json, dat het Huis
op de toonbank toont. Draait wekelijks mee met de migratiemonitor (scripts/run-migratiemonitor.sh)
en kan ook los: python3 scripts/kengetallen.py
"""
import datetime
import json
import os
import subprocess
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
from gsc_hulp import fetch  # noqa: E402

UIT = os.path.join(os.path.dirname(HIER), "data", "kengetallen.json")
SKILL = os.path.expanduser("~/.claude/skills/seo/scripts")
GA4_PROPERTY = "521523059"
GSC_VERTRAGING = 3  # Search Console loopt een paar dagen achter
DAGEN = 28


def merk(query):
    q = query.lower().replace("-", " ")
    return "tante rie" in q or "tanterie" in q


def gsc(eind):
    start, vorig_eind = eind - datetime.timedelta(days=DAGEN - 1), eind - datetime.timedelta(days=DAGEN)
    vorig_start = vorig_eind - datetime.timedelta(days=DAGEN - 1)

    def klikken(a, b):
        rijen = fetch(a.isoformat(), b.isoformat(), "query").get("rows", [])
        niet = sum(r["clicks"] for r in rijen if not merk(r["keys"][0]))
        return niet, sum(r["clicks"] for r in rijen)

    nu, vorig = klikken(start, eind), klikken(vorig_start, vorig_eind)
    periode = f"{start:%d-%m} t/m {eind:%d-%m-%Y}"
    return [
        cijfer("gsc-niet-merk", "Klikken uit Google zonder merknaam", nu[0], vorig[0], periode, "Search Console", "hoger"),
        cijfer("gsc-totaal", "Klikken uit Google, totaal", nu[1], vorig[1], periode, "Search Console", "hoger"),
    ]


def ga4(dagen):
    p = subprocess.run([sys.executable, "ga4_report.py", "--property", GA4_PROPERTY, "--days", str(dagen),
                        "--report", "organic", "--json"], cwd=SKILL, capture_output=True, text=True,
                       env=dict(os.environ, PYTHONWARNINGS="ignore"))
    d = json.loads(p.stdout)
    return d["totals"]["sessions"], d["date_range"]


def ga4_cijfer():
    nu, bereik = ga4(DAGEN)
    dubbel, _ = ga4(2 * DAGEN)
    periode = f"{bereik['start'][8:10]}-{bereik['start'][5:7]} t/m {bereik['end'][8:10]}-{bereik['end'][5:7]}-{bereik['end'][:4]}"
    return cijfer("ga4-organisch", "Bezoeken via Google (organisch)", nu, dubbel - nu, periode, "GA4", "hoger")


def gbp_cijfers(eind):
    import gbp_prestaties as g
    s = g.sessie()
    loc = "locations/6267696427702073490"
    start, vorig_eind = eind - datetime.timedelta(days=DAGEN - 1), eind - datetime.timedelta(days=DAGEN)
    vorig_start = vorig_eind - datetime.timedelta(days=DAGEN - 1)
    nu = g.samenvatting(g.prestaties(s, loc, start, eind)[0])
    vorig = g.samenvatting(g.prestaties(s, loc, vorig_start, vorig_eind)[0])
    acties = ("BUSINESS_DIRECTION_REQUESTS", "CALL_CLICKS", "WEBSITE_CLICKS")
    periode = f"{start:%d-%m} t/m {eind:%d-%m-%Y}"
    return [
        cijfer("gbp-acties", "Acties in het Bedrijfsprofiel (route, bellen, website)",
               sum(nu.get(m, 0) for m in acties), sum(vorig.get(m, 0) for m in acties), periode, "Bedrijfsprofiel", "hoger"),
        cijfer("gbp-route", "Routeverzoeken naar de winkel", nu.get("BUSINESS_DIRECTION_REQUESTS", 0),
               vorig.get("BUSINESS_DIRECTION_REQUESTS", 0), periode, "Bedrijfsprofiel", "hoger"),
    ]


def cijfer(id_, label, waarde, vorige, periode, bron, beter, eenheid=""):
    return {"id": id_, "label": label, "waarde": waarde, "vorige": vorige, "periode": periode,
            "bron": bron, "beter": beter, "eenheid": eenheid}


def main():
    vandaag = datetime.date.today()
    cijfers, fouten = [], []
    for naam, stap in (("Search Console", lambda: gsc(vandaag - datetime.timedelta(days=GSC_VERTRAGING))),
                       ("GA4", lambda: [ga4_cijfer()]),
                       ("Bedrijfsprofiel", lambda: gbp_cijfers(vandaag - datetime.timedelta(days=GSC_VERTRAGING)))):
        try:
            cijfers += stap()
        except Exception as e:  # een bron die faalt, mag de rest niet tegenhouden
            fouten.append(f"{naam}: {str(e)[:200]}")
    uit = {"team": "seo", "bijgewerkt": datetime.datetime.now().isoformat(timespec="minutes"), "cijfers": cijfers, "fouten": fouten}
    os.makedirs(os.path.dirname(UIT), exist_ok=True)
    with open(UIT, "w", encoding="utf-8") as f:
        json.dump(uit, f, indent=2, ensure_ascii=False)
    for c in cijfers:
        print(f"{c['label']}: {c['waarde']} (was {c['vorige']}, {c['periode']})")
    for f_ in fouten:
        print("Mislukt:", f_)
    return 1 if not cijfers else 0


if __name__ == "__main__":
    sys.exit(main())
