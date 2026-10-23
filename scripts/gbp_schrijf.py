#!/usr/bin/env python3
"""Google Bedrijfsprofiel: alleen de door Mark goedgekeurde wijzigingen uit V65 (23-10-2026).

De teksten staan vast in dit script en zijn gelijk aan de eindteksten in
marketing/review/review-gbp-teksten-2026-10-23.md. Zonder --uitvoeren is het een
droogtest. Met --uitvoeren komt eerst een backup in marketing/autoriteit/.

Gebruik:
    python3 scripts/gbp_schrijf.py categorieen [--uitvoeren]
    python3 scripts/gbp_schrijf.py beschrijving [--uitvoeren]
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
    1: {
        "datum": date(2026, 10, 27),
        "foto": "theewand-losse-thee.jpg",
        "url": "https://tanterie.nl/pages/theewinkel-borne-twente" + UTM + "bericht-theewand",
        "tekst": (
            "Aan de theewand in onze winkel in Borne staan ruim 130 soorten losse thee. Je kunt de thee ruiken "
            "en eventueel proeven voordat je een keuze maakt. Dat helpt vooral bij thee die je nog niet kent, "
            "want de geur vertelt vaak al veel over wat je in je kopje krijgt. Weet je niet waar je moet "
            "beginnen, vertel dan wat je normaal drinkt en wat je minder lekker vindt, dan zoeken we samen een "
            "thee die bij je past. Je vindt ons aan de Bakkerssteeg 6 in Borne, van dinsdag tot en met zaterdag "
            "van 10.00 tot 17.00 uur. Parkeren kan in de buurt met een parkeerschijf of in de gratis parkeergarage."
        ),
    },
    2: {
        "datum": date(2026, 11, 3),
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
    3: {
        "datum": date(2026, 11, 10),
        "foto": "blond-amsterdam-wand.jpg",
        "url": "https://tanterie.nl/pages/blond-amsterdam-servies" + UTM + "bericht-blond-amsterdam",
        "tekst": (
            "Blond Amsterdam maakt mokken en bekers met kleurrijke illustraties, en in onze winkel in Borne zie "
            "je ze zoals ze echt zijn. Een praktische vraag bij dit servies is of het in de vaatwasser kan. Dat "
            "kan: de mokken, bekers en borden mogen erin, het liefst op een mild programma zodat de print lang "
            "mooi blijft. Blond Amsterdam versturen we niet. Je bestelt online en haalt het af in de winkel, of "
            "je neemt mee wat er op voorraad is. Meer over het servies lees je op onze pagina over Blond Amsterdam."
        ),
    },
    4: {
        "datum": date(2026, 11, 17),
        "foto": "cadeautafel-winkel.jpg",
        "url": "https://tanterie.nl/pages/theewinkel-borne-twente" + UTM + "bericht-feestdagen",
        "tekst": (
            "Tijdens de feestdagen is Tante Rie gesloten op Eerste en Tweede Kerstdag, 25 en 26 december, en op "
            "Nieuwjaarsdag, 1 januari. De gewone openingstijden zijn dinsdag tot en met zaterdag van 10.00 tot "
            "17.00 uur. Zoek je een cadeau voor iemand die van thee houdt, kom dan langs in de winkel aan de "
            "Bakkerssteeg 6 in Borne, dan denken we graag met je mee."
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
    p.add_argument("actie", choices=["categorieen", "beschrijving", "bericht"])
    p.add_argument("nr", nargs="?", type=int, choices=sorted(BERICHTEN))
    p.add_argument("--uitvoeren", action="store_true")
    a = p.parse_args()
    s = sessie()
    if a.actie == "categorieen":
        categorieen(s, a.uitvoeren)
    elif a.actie == "beschrijving":
        beschrijving(s, a.uitvoeren)
    else:
        if not a.nr:
            sys.exit("Geef het berichtnummer (1 t/m 4).")
        bericht(s, a.nr, a.uitvoeren)
    if not a.uitvoeren:
        print("(droogtest, niets gewijzigd)")


if __name__ == "__main__":
    main()
