#!/usr/bin/env python3
"""Opdrachtregels van het SEO-team aan het PIM-team (Tante Rie).

Regels in opbouw staan in marketing/pim-regels-concept.json (een lijst regels).
Versturen bundelt ze tot één bericht in team/mailbox/seo-naar-pim.json in de
repository tante-rie-hq. Werkafspraken: tante-rie-hq/team/werkafspraken-seo.md.

Gebruik:
  python3 scripts/pim_regels.py controleer              # velden en aantallen van het concept
  python3 scripts/pim_regels.py stuur [--op-verzoek-mark] [--hq PAD]
  python3 scripts/pim_regels.py nieuw [--hq PAD]        # berichten van PIM met status nieuw
"""
import argparse
import datetime
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONCEPT = os.path.join(REPO, "marketing", "pim-regels-concept.json")
HQ = os.path.join(os.path.dirname(REPO), "tante-rie-hq")
MINIMUM = 20

VELDEN = ("product_id", "handle", "veld", "huidige_waarde", "gewenste_waarde",
          "reden", "prioriteit", "status")
TOEGESTAAN = {
    "veld": {"titel", "seo_titel", "meta_description", "beschrijving", "alt_tekst", "tags"},
    "prioriteit": {"hoog", "middel", "laag"},
    "status": {"nieuw"},
}


def laad(pad, leeg):
    if not os.path.exists(pad):
        return leeg
    with open(pad, encoding="utf-8") as f:
        return json.load(f)


def schrijf(pad, data):
    with open(pad, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def fouten_in(regels):
    fouten = []
    gezien = set()
    for i, r in enumerate(regels, 1):
        ontbreekt = [v for v in VELDEN if v not in r]
        extra = [k for k in r if k not in VELDEN]
        if ontbreekt:
            fouten.append(f"regel {i}: ontbreekt {', '.join(ontbreekt)}")
        if extra:
            fouten.append(f"regel {i}: onbekend veld {', '.join(extra)}")
        for veld, waarden in TOEGESTAAN.items():
            if veld in r and r[veld] not in waarden:
                fouten.append(f"regel {i}: {veld} '{r[veld]}' niet toegestaan")
        if len(str(r.get("reden", "")).split()) > 10:
            fouten.append(f"regel {i}: reden langer dan tien woorden")
        sleutel = (r.get("product_id"), r.get("veld"), r.get("huidige_waarde") if r.get("veld") == "alt_tekst" else None)
        if sleutel in gezien:
            fouten.append(f"regel {i}: dubbel voor {sleutel[0]} {sleutel[1]}")
        gezien.add(sleutel)
    return fouten


def controleer(_args):
    regels = laad(CONCEPT, [])
    fouten = fouten_in(regels)
    for f in fouten:
        print(f)
    per_prio = {p: sum(r.get("prioriteit") == p for r in regels) for p in ("hoog", "middel", "laag")}
    print(f"{len(regels)} regels ({per_prio['hoog']} hoog, {per_prio['middel']} middel, "
          f"{per_prio['laag']} laag); minimum voor versturen {MINIMUM}")
    return 1 if fouten else 0


def stuur(args):
    regels = laad(CONCEPT, [])
    fouten = fouten_in(regels)
    if fouten:
        print("\n".join(fouten))
        return 1
    if not regels:
        print("Geen regels in het concept.")
        return 1
    if len(regels) < MINIMUM and not args.op_verzoek_mark:
        print(f"{len(regels)} regels; versturen kan vanaf {MINIMUM} of met --op-verzoek-mark.")
        return 1
    pad = os.path.join(args.hq, "team", "mailbox", "seo-naar-pim.json")
    mailbox = laad(pad, {"berichten": []})
    vandaag = datetime.date.today().isoformat()
    volgnr = 1 + sum(b["bericht_id"].startswith(f"seo-{vandaag}-") for b in mailbox["berichten"])
    volgorde = {"hoog": 0, "middel": 1, "laag": 2}
    mailbox["berichten"].append({
        "bericht_id": f"seo-{vandaag}-{volgnr}",
        "datum": vandaag,
        "van": "seo",
        "aan": "pim",
        "status": "nieuw",
        "regels": sorted(regels, key=lambda r: (volgorde[r["prioriteit"]], r["handle"], r["veld"])),
    })
    schrijf(pad, mailbox)
    schrijf(CONCEPT, [])
    print(f"Bericht seo-{vandaag}-{volgnr} met {len(regels)} regels in {pad}; concept geleegd. "
          "Commit en push tante-rie-hq.")
    return 0


def nieuw(args):
    pad = os.path.join(args.hq, "team", "mailbox", "pim-naar-seo.json")
    berichten = [b for b in laad(pad, {"berichten": []})["berichten"] if b.get("status") == "nieuw"]
    for b in berichten:
        print(f"{b['bericht_id']}  {b.get('datum', '')}  {len(b.get('regels', []))} regels")
    if not berichten:
        print("Geen nieuwe berichten van PIM.")
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="opdracht", required=True)
    sub.add_parser("controleer")
    s = sub.add_parser("stuur")
    s.add_argument("--op-verzoek-mark", action="store_true")
    s.add_argument("--hq", default=HQ)
    n = sub.add_parser("nieuw")
    n.add_argument("--hq", default=HQ)
    args = p.parse_args()
    return {"controleer": controleer, "stuur": stuur, "nieuw": nieuw}[args.opdracht](args)


if __name__ == "__main__":
    sys.exit(main())
