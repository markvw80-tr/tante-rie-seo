#!/usr/bin/env python3
"""Google Bedrijfsprofiel: alleen de door Mark goedgekeurde wijzigingen uit V65 (23-10-2026).

De teksten staan vast in dit script en zijn gelijk aan de eindteksten in
marketing/review/review-gbp-teksten-2026-10-23.md. Zonder --uitvoeren is het een
droogtest. Met --uitvoeren komt eerst een backup in marketing/autoriteit/.

Gebruik:
    python3 scripts/gbp_schrijf.py categorieen [--uitvoeren]
    python3 scripts/gbp_schrijf.py beschrijving [--uitvoeren]
    python3 scripts/gbp_schrijf.py attributen [--uitvoeren]       # V131 b, c, d (15-11-2026)
    python3 scripts/gbp_schrijf.py speciaaltijden [--uitvoeren]   # V130 (15-11-2026): koopzondagen en koopavond
    python3 scripts/gbp_schrijf.py bericht 1 [--uitvoeren]   # 1 t/m 4, niet vóór de geplande datum

Token: ~/.config/claude-seo/gbp-token.json (OAuth, scope business.manage).
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

TOKEN = os.path.expanduser("~/.config/claude-seo/gbp-token.json")
ROOT = "/Users/markvanwijk/Tante Rie SEO/"
LOC = "locations/6267696427702073490"
ACCOUNT = "accounts/101666303135035326611"
INFO = "https://mybusinessbusinessinformation.googleapis.com/v1/"
V4 = "https://mybusiness.googleapis.com/v4/"
CDN = "https://cdn.shopify.com/s/files/1/0999/6274/9192/files/"

HOOFD = "categories/gcid:tea_store"
EXTRA = ["gift_shop", "coffee_store", "chinaware_store", "pottery_store", "kitchen_supply_store", "home_goods_store"]

BESCHRIJVING = (
    "Tante Rie is de theewinkel in Borne, aan de Bakkerssteeg 6. Aan de theewand vind je ruim 130 soorten "
    "losse thee, en je kunt de thee ruiken en eventueel proeven voordat je kiest. Daarnaast hebben we servies "
    "van Bunzlau Castle en Blond Amsterdam, melamine en servies van Rice, cadeaus, bakmixen en koffiebonen. "
    "Het aardewerk van Bunzlau Castle en het servies van Blond Amsterdam haal je af in de winkel. Melamine en "
    "Rice sturen we ook op. Parkeren kan in de buurt met een parkeerschijf of in de gratis parkeergarage. "
    "De winkel is rolstoeltoegankelijk."
)

UTM = "?utm_source=gbp&utm_medium=organic&utm_campaign="
BERICHTEN = {
    # Nieuw schema V131 a (Mark, 15-11-2026); review marketing/review/review-gbp-berichten-2026-11-15.md
    1: {
        "datum": date(2026, 11, 17),
        "foto": "bunzlau-wand.jpg",
        "url": "https://tanterie.nl/collections/bunzlau" + UTM + "bericht-bunzlau",
        "tekst": (
            "In onze winkel in Borne staat het aardewerk van Bunzlau Castle langs de wand en in een kast, zodat "
            "je het kunt bekijken en vasthouden. Kleur en glazuur zie je pas goed als je een stuk zelf in je "
            "handen hebt. Het aardewerk van Bunzlau Castle versturen we niet. Je bestelt het online en haalt het "
            "af in de winkel, of je komt langs en neemt mee wat er op voorraad is. Zoek je een bepaald stuk, bel "
            "dan vooraf even, dan kijken we of het er ligt. Ons nummer staat in dit profiel. We zijn open van "
            "dinsdag tot en met zaterdag van 10.00 tot 17.00 uur aan de Bakkerssteeg 6."
        ),
    },
    2: {
        "datum": date(2026, 11, 24),
        "foto": "theewand-losse-thee.jpg",
        "url": "https://tanterie.nl/pages/theewinkel-borne-twente" + UTM + "bericht-theewand",
        "tekst": (
            "Aan de theewand in onze winkel in Borne staan ruim 130 soorten losse thee. Je kunt de thee ruiken "
            "en eventueel proeven voordat je een keuze maakt. Dat helpt vooral bij thee die je nog niet kent, "
            "want de geur vertelt vaak al veel over wat je in je kopje krijgt. Weet je niet waar je moet "
            "beginnen, vertel dan wat je normaal drinkt en wat je minder lekker vindt, dan zoeken we samen een "
            "thee die bij je past. Je vindt ons aan de Bakkerssteeg 6 in Borne, van dinsdag tot en met zaterdag "
            "van 10.00 tot 17.00 uur. Op zondag 29 november zijn we open van 12.00 tot 17.00 uur. Parkeren kan "
            "op parkeerplaats De Koem met een parkeerschijf."
        ),
    },
    3: {
        "datum": date(2026, 12, 1),
        "foto": "cadeautafel-winkel.jpg",
        "url": "https://tanterie.nl/pages/theewinkel-borne-twente" + UTM + "bericht-feestdagen",
        "tekst": (
            "Tijdens de feestdagen is Tante Rie gesloten op eerste en tweede kerstdag, 25 en 26 december, en op "
            "Nieuwjaarsdag, 1 januari. De gewone openingstijden zijn dinsdag tot en met zaterdag van 10.00 tot "
            "17.00 uur. Zoek je een cadeau voor iemand die van thee houdt, kom dan langs in de winkel aan de "
            "Bakkerssteeg 6 in Borne, dan denken we graag met je mee."
        ),
    },
    4: {
        "datum": date(2026, 12, 8),
        "foto": "cadeautafel-winkel.jpg",
        "url": "https://tanterie.nl/pages/theewinkel-borne-twente" + UTM + "bericht-koopavond",
        "tekst": (
            "In december zijn we op twee dagen langer of extra open. Op zaterdag 12 december is de winkel open "
            "van 10.00 tot 21.00 uur. Op zondag 20 december zijn we open van 12.00 tot 17.00 uur. Kom je langs "
            "voor een cadeau, vertel dan voor wie het is, dan zoeken we samen iets dat past. Je vindt ons aan de "
            "Bakkerssteeg 6 in Borne. Parkeren kan op parkeerplaats De Koem met een parkeerschijf."
        ),
    },
}


def sessie():
    creds = Credentials.from_authorized_user_info(json.load(open(TOKEN)))
    creds.refresh(Request())
    return AuthorizedSession(creds)


def backup(naam, inhoud):
    pad = f"{ROOT}marketing/autoriteit/backup-gbp-{naam}-{date.today()}.json"
    with open(pad, "w", encoding="utf-8") as f:
        json.dump({"gemaakt": str(date.today()), "doel": f"Backup V65 {naam} vóór wijziging", "inhoud": inhoud},
                  f, ensure_ascii=False, indent=1)
    print("backup:", pad)


def check(r, wat):
    if r.status_code >= 300:
        sys.exit(f"{wat} mislukt: {r.status_code} {r.text[:500]}")
    return r.json() if r.text else {}


def lees(s, veld):
    return check(s.get(INFO + LOC, params={"readMask": veld}), "lezen")


def categorieen(s, uitvoeren):
    nu = lees(s, "categories").get("categories", {})
    print("nu:", nu.get("primaryCategory", {}).get("name"),
          [c["name"] for c in nu.get("additionalCategories", [])])
    nieuw = {"primaryCategory": {"name": HOOFD},
             "additionalCategories": [{"name": f"categories/gcid:{c}"} for c in EXTRA]}
    print("nieuw:", HOOFD, [c["name"] for c in nieuw["additionalCategories"]])
    if uitvoeren:
        backup("categorieen", nu)
        uit = check(s.patch(INFO + LOC, params={"updateMask": "categories"}, json={"categories": nieuw}), "wijzigen")
        print("resultaat:", [c.get("displayName") for c in uit["categories"].get("additionalCategories", [])])


def beschrijving(s, uitvoeren):
    nu = lees(s, "profile").get("profile", {})
    print(f"nu ({len(nu.get('description', ''))} tekens):", nu.get("description"))
    print(f"nieuw ({len(BESCHRIJVING)} tekens):", BESCHRIJVING)
    if uitvoeren:
        backup("beschrijving", nu)
        check(s.patch(INFO + LOC, params={"updateMask": "profile.description"},
                      json={"profile": {"description": BESCHRIJVING}}), "wijzigen")
        print("resultaat:", lees(s, "profile")["profile"]["description"] == BESCHRIJVING)


# V130 (Mark, 15-11-2026): tijden uit V122. (datum, open, dicht)
SPECIAAL = [((2026, 11, 29), 12, 17), ((2026, 12, 12), 10, 21), ((2026, 12, 20), 12, 17)]


def speciaaltijden(s, uitvoeren):
    nu = lees(s, "specialHours").get("specialHours", {})
    periodes = nu.get("specialHourPeriods", [])
    bestaand = {(p["startDate"]["year"], p["startDate"]["month"], p["startDate"]["day"]) for p in periodes}
    nieuw = []
    for (j, m, d), van, tot in SPECIAAL:
        if (j, m, d) in bestaand:
            continue
        dag = {"year": j, "month": m, "day": d}
        nieuw.append({"startDate": dag, "openTime": {"hours": van}, "endDate": dag, "closeTime": {"hours": tot}})
    print(f"nu {len(periodes)} periodes, toe te voegen {len(nieuw)}:", nieuw)
    if uitvoeren and nieuw:
        backup("speciaaltijden", nu)
        body = {"specialHours": {"specialHourPeriods": periodes + nieuw}}
        check(s.patch(INFO + LOC, params={"updateMask": "specialHours"}, json=body), "wijzigen")
        terug = lees(s, "specialHours")["specialHours"]["specialHourPeriods"]
        print("teruggelezen:", len(terug), "periodes")
        for p in terug:
            if p["startDate"]["year"] == 2026 and p["startDate"]["month"] >= 11 or p["startDate"]["year"] == 2027:
                print(p["startDate"], p.get("openTime"), p.get("closeTime"), p.get("closed"))


# V131 (Mark, 15-11-2026): b creditcard ja, c Online bestellen-knop ja, d parkeerplaats De Koem met parkeerschijf
ATTRIBUTEN = [
    {"name": "attributes/pay_credit_card", "values": [True]},
    {"name": "attributes/has_parking_lot_free", "values": [True]},
    {"name": "attributes/has_parking_garage_free", "values": [True]},  # Mark 15-11: gratis parkeergarage in de buurt
    {"name": "attributes/url_shop_online",
     "uriValues": [{"uri": "https://tanterie.nl/?utm_source=gbp&utm_medium=organic&utm_campaign=bestellen"}]},
]


def attributen(s, uitvoeren):
    nu = check(s.get(INFO + LOC + "/attributes"), "lezen")
    print("nu:", [(a["name"], a.get("values") or a.get("uriValues")) for a in nu.get("attributes", [])
                  if a["name"] in {x["name"] for x in ATTRIBUTEN}])
    print("nieuw:", ATTRIBUTEN)
    if uitvoeren:
        backup("attributen", nu)
        masker = ",".join(x["name"] for x in ATTRIBUTEN)
        check(s.patch(INFO + LOC + "/attributes", params={"attributeMask": masker},
                      json={"name": LOC + "/attributes", "attributes": ATTRIBUTEN}), "wijzigen")
        terug = check(s.get(INFO + LOC + "/attributes"), "teruglezen")
        for a in terug.get("attributes", []):
            if a["name"] in {x["name"] for x in ATTRIBUTEN}:
                print("teruggelezen:", a["name"], a.get("values") or a.get("uriValues"))


def bericht(s, nr, uitvoeren):
    b = BERICHTEN[nr]
    print(f"bericht {nr} (gepland {b['datum']}), foto {b['foto']}, knop {b['url']}\n{b['tekst']}")
    if date.today() < b["datum"]:
        sys.exit(f"Nog niet: bericht {nr} staat gepland op {b['datum']}.")
    body = {
        "languageCode": "nl",
        "topicType": "STANDARD",
        "summary": b["tekst"],
        "callToAction": {"actionType": "LEARN_MORE", "url": b["url"]},
        "media": [{"mediaFormat": "PHOTO", "sourceUrl": CDN + b["foto"]}],
    }
    if uitvoeren:
        uit = check(s.post(f"{V4}{ACCOUNT}/{LOC}/localPosts", json=body), "plaatsen")
        print("geplaatst:", uit.get("name"), uit.get("state"), uit.get("searchUrl"))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("actie", choices=["categorieen", "beschrijving", "speciaaltijden", "attributen", "bericht"])
    p.add_argument("nr", nargs="?", type=int, choices=sorted(BERICHTEN))
    p.add_argument("--uitvoeren", action="store_true")
    a = p.parse_args()
    s = sessie()
    if a.actie == "categorieen":
        categorieen(s, a.uitvoeren)
    elif a.actie == "beschrijving":
        beschrijving(s, a.uitvoeren)
    elif a.actie == "attributen":
        attributen(s, a.uitvoeren)
    elif a.actie == "speciaaltijden":
        speciaaltijden(s, a.uitvoeren)
    else:
        if not a.nr:
            sys.exit("Geef het berichtnummer (1 t/m 4).")
        bericht(s, a.nr, a.uitvoeren)
    if not a.uitvoeren:
        print("(droogtest, niets gewijzigd)")


if __name__ == "__main__":
    main()
