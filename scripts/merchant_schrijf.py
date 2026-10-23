#!/usr/bin/env python3
"""Merchant Center: alleen de door Mark goedgekeurde wijzigingen uit V69 (23-10-2026).

Zonder --uitvoeren is het een droogtest: het script leest de huidige stand en toont
wat er zou veranderen. Met --uitvoeren schrijft het eerst een backup naar
marketing/technisch/ en voert het daarna de wijziging uit.

Gebruik:
    python3 scripts/merchant_schrijf.py retourbeleid [--uitvoeren]   # V69 stap 2
    python3 scripts/merchant_schrijf.py homepage [--uitvoeren]       # V69 stap 3
    python3 scripts/merchant_schrijf.py homepage-terug [--uitvoeren] # alleen als de claim mislukt
    python3 scripts/merchant_schrijf.py tweede-account [--uitvoeren] # V70: feed uit, claim intrekken op 5819585029
    python3 scripts/merchant_schrijf.py afhalen [--alleen shopify_ZZ_<id>] [--uitvoeren]  # A4

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
ACC2 = "accounts/5819585029"  # tweede account met automatische feed (V70)
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
        nieuw["label"] = "Retourbeleid tanterie.nl"
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


def tweede_account(s, uitvoeren):
    """V70: automatische feed uit en websiteclaim intrekken op het tweede account."""
    feed = check(s.get(API + ACC2 + "/autofeedSettings"), "feed lezen")
    hp = check(s.get(API + ACC2 + "/homepage"), "homepage lezen")
    print(f"{ACC2}: automatische feed aan={feed.get('enableProducts')}, "
          f"website {hp.get('uri')} geclaimd={hp.get('claimed', False)}")
    if not uitvoeren:
        return
    backup("tweede-account", {"autofeedSettings": feed, "homepage": hp})
    if feed.get("enableProducts"):
        uit = check(s.patch(API + ACC2 + "/autofeedSettings", params={"updateMask": "enableProducts"},
                            json={"enableProducts": False}), "feed uitzetten")
        print("automatische feed aan:", uit.get("enableProducts", False))
    if hp.get("claimed"):
        uit = check(s.post(API + ACC2 + "/homepage:unclaim", json={}), "claim intrekken")
        print("claim ingetrokken:", uit)


DS = "https://merchantapi.googleapis.com/datasources/v1/"
PI = "https://merchantapi.googleapis.com/products/v1/"
PRIMAIR = ["10606676973", "10706837209"]  # Shopify App API NL en BE
AFHALEN_NAAM = "Alleen afhalen (team)"
AFHALEN_TSV = ROOT + "marketing/technisch/aanvullende-bron-alleen-afhalen-2026-10-23.tsv"


def afhalen(s, uitvoeren, alleen):
    """A4: aanvullende bron die alleen-afhalen varianten uitsluit van Shopping en gratis webvermeldingen."""
    bronnen = check(s.get(DS + ACC + "/dataSources"), "bronnen lezen").get("dataSources", [])
    supp = next((b for b in bronnen if b.get("displayName") == AFHALEN_NAAM), None)
    ids = [r.split("\t")[0] for r in open(AFHALEN_TSV).read().splitlines()[1:]]
    if alleen:
        ids = [i for i in ids if i.startswith(alleen)]
    print(f"aanvullende bron: {supp['name'] if supp else 'nog niet aanwezig'}; varianten: {len(ids)}")
    if not uitvoeren:
        return
    if not supp:
        supp = check(s.post(DS + ACC + "/dataSources", json={
            "displayName": AFHALEN_NAAM, "supplementalProductDataSource": {}}), "bron aanmaken")
        print("aangemaakt:", supp["name"])
    for pid in PRIMAIR:
        prim = next(b for b in bronnen if b["dataSourceId"] == pid)
        backup(f"primaire-bron-{pid}", prim)
        regel = prim["primaryProductDataSource"].get("defaultRule", {"takeFromDataSources": [{"self": True}]})
        bron = regel.get("takeFromDataSources", [])
        if not any(b.get("supplementalDataSourceName") == supp["name"] for b in bron):
            bron = bron + [{"supplementalDataSourceName": supp["name"]}]
            check(s.patch(DS + prim["name"], params={"updateMask": "primaryProductDataSource.defaultRule"},
                          json={"primaryProductDataSource": {"defaultRule": {"takeFromDataSources": bron}}}),
                  f"koppelen aan {pid}")
            print("gekoppeld aan", pid)
    fout = 0
    for n, offer in enumerate(ids, 1):
        for label in ["EUR_107259592968", "EUR_114053906696"]:
            r = s.post(PI + ACC + "/productInputs:insert", params={"dataSource": supp["name"]}, json={
                "offerId": offer, "contentLanguage": "nl", "feedLabel": label,
                "productAttributes": {"excludedDestinations": ["SHOPPING_ADS", "FREE_LISTINGS"]}})
            if r.status_code >= 300:
                fout += 1
                if fout <= 3:
                    print("fout:", offer, label, r.status_code, r.text[:300])
        if n % 200 == 0:
            print(n, "varianten verwerkt", flush=True)
    print(f"klaar: {len(ids)} varianten, {fout} fouten")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("actie", choices=["retourbeleid", "homepage", "homepage-terug", "tweede-account", "afhalen"])
    p.add_argument("--alleen", help="alleen offerIds die hiermee beginnen (test)")
    p.add_argument("--uitvoeren", action="store_true")
    a = p.parse_args()
    s = sessie()
    if a.actie == "retourbeleid":
        retourbeleid(s, a.uitvoeren)
    elif a.actie == "tweede-account":
        tweede_account(s, a.uitvoeren)
    elif a.actie == "afhalen":
        afhalen(s, a.uitvoeren, a.alleen)
    else:
        homepage(s, a.uitvoeren, HOMEPAGE_NIEUW if a.actie == "homepage" else HOMEPAGE_OUD)
    if not a.uitvoeren:
        print("(droogtest, niets gewijzigd)")


if __name__ == "__main__":
    main()
