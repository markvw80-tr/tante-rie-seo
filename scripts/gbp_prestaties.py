#!/usr/bin/env python3
"""Google Bedrijfsprofiel-prestaties voor Tante Rie (alleen lezen).

Haalt per dag op: routeverzoeken, klikken op bellen, websiteklikken, berichten,
vertoningen in Zoeken en Maps (mobiel en desktop), plus per maand de zoektermen
waarop het profiel werd getoond.

Eenmalige koppeling (OAuth, scope business.manage):
    python3 gbp_prestaties.py --auth
Opent een browser; log in met het Google-account dat eigenaar of beheerder is van
het Bedrijfsprofiel. Het token komt in ~/.config/claude-seo/gbp-token.json.

Gebruik:
    python3 gbp_prestaties.py --lijst                             # accounts en locaties
    python3 gbp_prestaties.py --start 2026-08-01 --eind 2026-10-19
    python3 gbp_prestaties.py --start 2026-08-01 --eind 2026-10-19 --locatie locations/123

Schrijft ruwe JSON naar data/gbp/<start>_<eind>-gbp-*.json en print een samenvatting.

Vereist: Google Cloud-project met de APIs My Business Account Management,
My Business Business Information en Business Profile Performance ingeschakeld,
een goedgekeurde GBP API-toegangsaanvraag, en een OAuth-client (type Desktop)
opgeslagen als ~/.config/claude-seo/gbp-oauth-client.json.
"""
import argparse
import json
import os
import sys
from datetime import date

import requests
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPE = ["https://www.googleapis.com/auth/business.manage"]
CONF = os.path.expanduser("~/.config/claude-seo/")
CLIENT = CONF + "gbp-oauth-client.json"
TOKEN = CONF + "gbp-token.json"
ROOT = "/Users/markvanwijk/Tante Rie SEO/"
OUT = ROOT + "data/gbp/"

METRICS = [
    "BUSINESS_DIRECTION_REQUESTS",
    "CALL_CLICKS",
    "WEBSITE_CLICKS",
    "BUSINESS_CONVERSATIONS",
    "BUSINESS_IMPRESSIONS_MOBILE_SEARCH",
    "BUSINESS_IMPRESSIONS_DESKTOP_SEARCH",
    "BUSINESS_IMPRESSIONS_MOBILE_MAPS",
    "BUSINESS_IMPRESSIONS_DESKTOP_MAPS",
]


def auth():
    from google_auth_oauthlib.flow import InstalledAppFlow
    if not os.path.exists(CLIENT):
        sys.exit(f"OAuth-client ontbreekt: {CLIENT}")
    creds = InstalledAppFlow.from_client_secrets_file(CLIENT, SCOPE).run_local_server(port=0)
    with open(TOKEN, "w") as f:
        f.write(creds.to_json())
    os.chmod(TOKEN, 0o600)
    print(f"Token opgeslagen in {TOKEN}")


def sessie():
    if not os.path.exists(TOKEN):
        sys.exit("Geen token. Draai eerst: python3 gbp_prestaties.py --auth")
    creds = Credentials.from_authorized_user_file(TOKEN, SCOPE)
    if not creds.valid:
        creds.refresh(Request())
        with open(TOKEN, "w") as f:
            f.write(creds.to_json())
    s = requests.Session()
    s.headers["Authorization"] = f"Bearer {creds.token}"
    return s


def get(s, url, params=None):
    r = s.get(url, params=params, timeout=60)
    if r.status_code != 200:
        sys.exit(f"HTTP {r.status_code} op {url}\n{r.text[:800]}")
    return r.json()


def locaties(s):
    accts = get(s, "https://mybusinessaccountmanagement.googleapis.com/v1/accounts").get("accounts", [])
    res = []
    for a in accts:
        locs = get(
            s,
            f"https://mybusinessbusinessinformation.googleapis.com/v1/{a['name']}/locations",
            {"readMask": "name,title,websiteUri,storefrontAddress", "pageSize": 100},
        ).get("locations", [])
        for l in locs:
            res.append({"account": a["name"], "accountNaam": a.get("accountName"), **l})
    return res


def prestaties(s, loc, start, eind):
    params = [("dailyMetrics", m) for m in METRICS]
    for pre, d in (("dailyRange.start_date", start), ("dailyRange.end_date", eind)):
        params += [(f"{pre}.year", d.year), (f"{pre}.month", d.month), (f"{pre}.day", d.day)]
    data = get(s, f"https://businessprofileperformance.googleapis.com/v1/{loc}:fetchMultiDailyMetricsTimeSeries", params)
    kw = get(
        s,
        f"https://businessprofileperformance.googleapis.com/v1/{loc}/searchkeywords/impressions/monthly",
        {
            "monthlyRange.start_month.year": start.year, "monthlyRange.start_month.month": start.month,
            "monthlyRange.end_month.year": eind.year, "monthlyRange.end_month.month": eind.month,
            "pageSize": 100,
        },
    )
    return data, kw


def samenvatting(data):
    tot = {}
    for reeks in data.get("multiDailyMetricTimeSeries", []):
        for ts in reeks.get("dailyMetricTimeSeries", []):
            m = ts["dailyMetric"]
            tot[m] = sum(int(v.get("value", 0)) for v in ts.get("timeSeries", {}).get("datedValues", []))
    return tot


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--auth", action="store_true")
    ap.add_argument("--lijst", action="store_true")
    ap.add_argument("--start")
    ap.add_argument("--eind")
    ap.add_argument("--locatie", help="locations/<id>; standaard de eerste locatie")
    a = ap.parse_args()
    if a.auth:
        return auth()
    s = sessie()
    locs = locaties(s)
    if a.lijst or not a.start:
        for l in locs:
            print(l["name"], "|", l.get("title"), "|", l.get("websiteUri"), "|", l["accountNaam"])
        return
    loc = a.locatie or (locs[0]["name"] if locs else sys.exit("Geen locaties gevonden voor dit account."))
    start, eind = date.fromisoformat(a.start), date.fromisoformat(a.eind)
    data, kw = prestaties(s, loc, start, eind)
    os.makedirs(OUT, exist_ok=True)
    pre = f"{OUT}{start}_{eind}-gbp-"
    json.dump(data, open(pre + "dagelijks.json", "w"), indent=1)
    json.dump(kw, open(pre + "zoektermen.json", "w"), indent=1, ensure_ascii=False)
    print(f"Locatie {loc}, {start} t/m {eind}")
    for m, v in samenvatting(data).items():
        print(f"  {m}: {v}")
    print(f"Ruwe data: {pre}*.json")


if __name__ == "__main__":
    main()
