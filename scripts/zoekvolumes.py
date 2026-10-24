#!/usr/bin/env python3
"""Zoekvolumes uit Google Keyword Planner (Google Ads API, Basic access sinds 24-10-2026).

Eenmalig (Mark): token en klant-ID verborgen invoeren, daarna inloggen in de browser:
    python3 scripts/zoekvolumes.py token
    python3 scripts/zoekvolumes.py inloggen

Daarna:
    python3 scripts/zoekvolumes.py volumes "losse thee,theewinkel borne" [--json]
    python3 scripts/zoekvolumes.py volumes --bestand marketing/zoekwoorden/keyword-planner-invoer-2026-10-23.txt
    python3 scripts/zoekvolumes.py ideeen "losse thee" [--limiet 50]

Standaard Nederlands (taal 1010) en Nederland (locatie 2528). Ruwe uitvoer gaat naar
data/keyword-planner/JJJJ-MM-DD-<onderwerp>.json.

Config in ~/.config/claude-seo/google-api.json (vult Mark zelf in, nooit in de chat):
    "ads_developer_token": "...", "ads_customer_id": "233-270-6927",
    "ads_login_customer_id": "<alleen bij een managementaccount>"
"""
import argparse
import json
import os
import sys
import warnings
from datetime import date

warnings.filterwarnings("ignore")

CFG = os.path.expanduser("~/.config/claude-seo/")
CLIENT = CFG + "gbp-oauth-client.json"  # desktop-client van project tante-rie
TOKEN = CFG + "ads-token.json"
SCOPE = ["https://www.googleapis.com/auth/adwords"]
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAAL, LAND = "1010", "2528"


def token():
    """Vraagt token en klant-ID verborgen op en schrijft ze in google-api.json (niets in beeld of logs)."""
    from getpass import getpass
    pad = CFG + "google-api.json"
    cfg = json.load(open(pad))
    t = getpass("Ontwikkelaarstoken (wordt niet getoond): ").strip()
    k = input("Klant-ID Google Ads (123-456-7890): ").strip()
    m = input("Managementaccount-ID (leeg laten als er geen is): ").strip()
    if not t or not k:
        sys.exit("Token en klant-ID zijn verplicht, niets opgeslagen")
    cfg.update({"ads_developer_token": t, "ads_customer_id": k})
    if m:
        cfg["ads_login_customer_id"] = m
    with open(pad, "w") as f:
        json.dump(cfg, f, indent=2)
    os.chmod(pad, 0o600)
    print("opgeslagen in", pad)


def inloggen():
    from google_auth_oauthlib.flow import InstalledAppFlow
    creds = InstalledAppFlow.from_client_secrets_file(CLIENT, SCOPE).run_local_server(port=0)
    with open(TOKEN, "w") as f:
        f.write(creds.to_json())
    os.chmod(TOKEN, 0o600)
    print("opgeslagen:", TOKEN)


def client():
    from google.ads.googleads.client import GoogleAdsClient
    cfg = json.load(open(CFG + "google-api.json"))
    oauth = json.load(open(CLIENT))["installed"]
    tok = json.load(open(TOKEN))
    ontbreekt = [k for k in ("ads_developer_token", "ads_customer_id") if not cfg.get(k)]
    if ontbreekt:
        sys.exit("Ontbreekt in google-api.json: " + ", ".join(ontbreekt))
    d = {"developer_token": cfg["ads_developer_token"], "client_id": oauth["client_id"],
         "client_secret": oauth["client_secret"], "refresh_token": tok["refresh_token"],
         "use_proto_plus": True}
    if cfg.get("ads_login_customer_id"):
        d["login_customer_id"] = cfg["ads_login_customer_id"].replace("-", "")
    return GoogleAdsClient.load_from_dict(d), cfg["ads_customer_id"].replace("-", "")


def ophalen(woorden, ideeen, limiet):
    c, klant = client()
    svc = c.get_service("KeywordPlanIdeaService")
    ga = c.get_service("GoogleAdsService")
    rij = []
    # Historische metrics accepteert maximaal 10.000 woorden per verzoek; ideeën één seed-set.
    if ideeen:
        req = c.get_type("GenerateKeywordIdeasRequest")
        req.customer_id = klant
        req.language = ga.language_constant_path(TAAL)
        req.geo_target_constants.append(ga.geo_target_constant_path(LAND))
        req.keyword_plan_network = c.enums.KeywordPlanNetworkEnum.GOOGLE_SEARCH
        req.keyword_seed.keywords.extend(woorden)
        for i, r in enumerate(svc.generate_keyword_ideas(request=req)):
            if i >= limiet:
                break
            m = r.keyword_idea_metrics
            rij.append({"zoekwoord": r.text, "volume": m.avg_monthly_searches,
                        "concurrentie": m.competition.name})
    else:
        req = c.get_type("GenerateKeywordHistoricalMetricsRequest")
        req.customer_id = klant
        req.language = ga.language_constant_path(TAAL)
        req.geo_target_constants.append(ga.geo_target_constant_path(LAND))
        req.keyword_plan_network = c.enums.KeywordPlanNetworkEnum.GOOGLE_SEARCH
        req.keywords.extend(woorden)
        for r in svc.generate_keyword_historical_metrics(request=req).results:
            m = r.keyword_metrics
            rij.append({"zoekwoord": r.text, "volume": m.avg_monthly_searches,
                        "concurrentie": m.competition.name,
                        "per_maand": [{"jaar": x.year, "maand": x.month.name, "volume": x.monthly_searches}
                                      for x in m.monthly_search_volumes]})
    return rij


def main():
    p = argparse.ArgumentParser()
    p.add_argument("actie", choices=["token", "inloggen", "volumes", "ideeen"])
    p.add_argument("woorden", nargs="?", default="", help="komma-gescheiden")
    p.add_argument("--bestand", help="één zoekwoord per regel")
    p.add_argument("--limiet", type=int, default=50)
    p.add_argument("--onderwerp", default="zoekvolumes")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    if a.actie == "token":
        return token()
    if a.actie == "inloggen":
        return inloggen()
    woorden = [w.strip() for w in a.woorden.split(",") if w.strip()]
    if a.bestand:
        woorden += [w.strip() for w in open(a.bestand, encoding="utf-8") if w.strip() and not w.startswith("#")]
    if not woorden:
        sys.exit("Geen zoekwoorden opgegeven")
    rij = ophalen(woorden, a.actie == "ideeen", a.limiet)
    pad = f"{ROOT}/data/keyword-planner/{date.today()}-{a.onderwerp}.json"
    os.makedirs(os.path.dirname(pad), exist_ok=True)
    json.dump({"gemaakt": str(date.today()), "taal": TAAL, "locatie": LAND, "actie": a.actie,
               "resultaten": rij}, open(pad, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if a.json:
        print(json.dumps(rij, ensure_ascii=False, indent=1))
    else:
        for r in sorted(rij, key=lambda x: -(x["volume"] or 0)):
            print(f"{r['volume'] or 0:>8}  {r['concurrentie']:<10} {r['zoekwoord']}")
    print("opgeslagen:", pad, file=sys.stderr)


if __name__ == "__main__":
    main()
