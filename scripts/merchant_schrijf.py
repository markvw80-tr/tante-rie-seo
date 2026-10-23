#!/usr/bin/env python3
"""Merchant Center: alleen de door Mark goedgekeurde wijzigingen uit V69 (23-10-2026).

Zonder --uitvoeren is het een droogtest: het script leest de huidige stand en toont
wat er zou veranderen. Met --uitvoeren schrijft het eerst een backup naar
marketing/technisch/ en voert het daarna de wijziging uit.

Gebruik:
    python3 scripts/merchant_schrijf.py retourbeleid [--uitvoeren]   # V69 stap 2
    python3 scripts/merchant_schrijf.py homepage [--uitvoeren]       # V69 stap 3
    python3 scripts/merchant_schrijf.py homepage-terug [--uitvoeren] # alleen als de claim mislukt

Token: ~/.config/claude-seo/merchant-token.json (OAuth, scope content).
Regels voor gegevensbronnen (stap 5) kunnen niet via de API; die doet Mark in het scherm.
"""
import argparse
import json
import os
import sys
import warnings
from datetime import date

warnings.filterwarnings("ignore")
from google.auth.transport.requests import AuthorizedSession, Request
from google.oauth2.credentials import Credentials

TOKEN = os.path.expanduser("~/.config/claude-seo/merchant-token.json")
ROOT = "/Users/markvanwijk/Tante Rie SEO/"
ACC = "accounts/5716348221"
API = "https://merchantapi.googleapis.com/accounts/v1/"

RETOUR_NIEUW = "https://tanterie.nl/pages/retourbeleid-tante-rie"
HOMEPAGE_OUD = "https://webshop.tanterie.nl"
HOMEPAGE_NIEUW = "https://tanterie.nl"


def sessie():
    creds = Credentials.from_authorized_user_info(json.load(open(TOKEN)))
    creds.refresh(Request())
    return AuthorizedSession(creds)


def backup(naam, inhoud):
    pad = f"{ROOT}marketing/technisch/backup-merchant-{naam}-{date.today()}.json"
    with open(pad, "w", encoding="utf-8") as f:
        json.dump({"gemaakt": str(date.today()), "doel": f"Backup V69 {naam} vóór wijziging", "inhoud": inhoud},
                  f, ensure_ascii=False, indent=1)
    print("backup:", pad)


def check(r, wat):
    if r.status_code >= 300:
        sys.exit(f"{wat} mislukt: {r.status_code} {r.text[:500]}")
    return r.json() if r.text else {}


def retourbeleid(s, uitvoeren):
    beleid = check(s.get(API + ACC + "/onlineReturnPolicies"), "lezen")["onlineReturnPolicies"]
    oud = [b for b in beleid if b.get("returnPolicyUri") != RETOUR_NIEUW]
    if not oud:
        print("Retourbeleid wijst al naar", RETOUR_NIEUW)
        return
    for b in oud:
        print(f"{b['name']}: {b['returnPolicyUri']} -> {RETOUR_NIEUW}")
    if not uitvoeren:
        return
    backup("retourbeleid", beleid)
    for b in oud:
        nieuw = {k: v for k, v in b.items() if k not in ("name", "returnPolicyId")}
        nieuw["returnPolicyUri"] = RETOUR_NIEUW
        # De API kent geen update: eerst het nieuwe beleid aanmaken, pas daarna het oude weghalen.
        gemaakt = check(s.post(API + ACC + "/onlineReturnPolicies", json=nieuw), "aanmaken")
        print("aangemaakt:", gemaakt.get("name"), gemaakt.get("returnPolicyUri"))
        check(s.delete(API + b["name"]), "oude verwijderen")
        print("verwijderd:", b["name"])


def homepage(s, uitvoeren, doel):
    nu = check(s.get(API + ACC + "/homepage"), "lezen")
    print(f"homepage nu: {nu.get('uri')} (geclaimd: {nu.get('claimed', False)}) -> {doel}")
    if not uitvoeren:
        return
    if nu.get("uri") != doel:
        backup("homepage", nu)
        check(s.patch(API + ACC + "/homepage", params={"updateMask": "uri"}, json={"uri": doel}), "wijzigen")
    r = s.post(API + ACC + "/homepage:claim", json={})
    if r.status_code >= 300:
        print(f"CLAIM MISLUKT: {r.status_code} {r.text[:500]}")
        print("Herstel met: python3 scripts/merchant_schrijf.py homepage-terug --uitvoeren")
        sys.exit(1)
    print("geclaimd:", r.json())


def main():
    p = argparse.ArgumentParser()
    p.add_argument("actie", choices=["retourbeleid", "homepage", "homepage-terug"])
    p.add_argument("--uitvoeren", action="store_true")
    a = p.parse_args()
    s = sessie()
    if a.actie == "retourbeleid":
        retourbeleid(s, a.uitvoeren)
    else:
        homepage(s, a.uitvoeren, HOMEPAGE_NIEUW if a.actie == "homepage" else HOMEPAGE_OUD)
    if not a.uitvoeren:
        print("(droogtest, niets gewijzigd)")


if __name__ == "__main__":
    main()
