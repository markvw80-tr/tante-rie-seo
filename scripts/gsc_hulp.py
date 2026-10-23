#!/usr/bin/env python3
"""Gedeelde hulpfuncties voor de nulmeting en de migratiemonitor (Tante Rie).

Alleen lezen uit Search Console via ~/.claude/skills/seo/scripts/gsc_query.py.
"""
import json
import os
import subprocess
import sys
from urllib.parse import urlparse

GSC_DIR = os.path.expanduser("~/.claude/skills/seo/scripts")
DATA = "/Users/markvanwijk/Tante Rie SEO/data/gsc/"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def fetch(start, end, dims, out_path=None):
    """Haal rijen op via gsc_query.py (subprocess); sla optioneel de ruwe JSON op."""
    env = dict(os.environ, PYTHONWARNINGS="ignore")
    p = subprocess.run(
        [sys.executable, "gsc_query.py", "--start-date", start, "--end-date", end,
         "--dimensions", dims, "--limit", "25000", "--json"],
        cwd=GSC_DIR, env=env, capture_output=True, text=True)
    try:
        data = json.loads(p.stdout)
    except ValueError:
        raise RuntimeError("gsc_query.py gaf geen JSON: " + p.stderr[-400:])
    if data.get("error"):
        raise RuntimeError(str(data["error"]))
    if out_path:
        with open(out_path, "w") as f:
            json.dump(data, f, indent=1)
    return data


def split_url(url):
    """Geeft (variant, pad, heeft_parameters). variant is bv. 'https://tanterie.nl'."""
    u = urlparse(url)
    variant = f"{u.scheme}://{u.netloc}"
    pad = u.path.rstrip("/") or "/"
    return variant, pad, bool(u.query)


HOME_VARIANTEN = [
    "http://www.tanterie.nl", "https://www.tanterie.nl",
    "http://tanterie.nl", "https://tanterie.nl",
    "http://webshop.tanterie.nl", "https://webshop.tanterie.nl",
]


def homepage_per_variant(page_rows):
    """Homepage per URL-variant (zonder parameters). page_rows: rijen met dimensie page."""
    out = {v: {"clicks": 0, "impressions": 0, "pos_w": 0.0} for v in HOME_VARIANTEN}
    param = {"clicks": 0, "impressions": 0}
    for r in page_rows:
        variant, pad, par = split_url(r["keys"][0])
        if pad != "/":
            continue
        if par:
            param["clicks"] += r["clicks"]
            param["impressions"] += r["impressions"]
            continue
        o = out.setdefault(variant, {"clicks": 0, "impressions": 0, "pos_w": 0.0})
        o["clicks"] += r["clicks"]
        o["impressions"] += r["impressions"]
        o["pos_w"] += r["position"] * r["impressions"]
    for o in out.values():
        o["position"] = round(o["pos_w"] / o["impressions"], 1) if o["impressions"] else None
        del o["pos_w"]
    return out, param


def https_aandeel(varianten):
    """Aandeel van https://tanterie.nl/ in de homepage (alle varianten samen)."""
    tot_c = sum(v["clicks"] for v in varianten.values())
    tot_i = sum(v["impressions"] for v in varianten.values())
    h = varianten.get("https://tanterie.nl", {"clicks": 0, "impressions": 0})
    return {
        "impressions": h["impressions"], "impressions_totaal": tot_i,
        "aandeel_impressions": round(100 * h["impressions"] / tot_i, 1) if tot_i else None,
        "clicks": h["clicks"], "clicks_totaal": tot_c,
        "aandeel_clicks": round(100 * h["clicks"] / tot_c, 1) if tot_c else None,
    }


TRACK = ["bunzlau servies", "theewinkel", "thee uit twente", "tea"]


def posities_trackwoorden(qp_rows):
    """Per trackingzoekwoord en URL (variant + pad, zonder parameters) de gewogen positie."""
    res = {k: {} for k in TRACK}
    for r in qp_rows:
        q, url = r["keys"][0].lower().strip(), r["keys"][1]
        if q not in res:
            continue
        variant, pad, par = split_url(url)
        key = variant + pad if pad != "/" else variant + "/"
        o = res[q].setdefault(key, {"clicks": 0, "impressions": 0, "pos_w": 0.0})
        o["clicks"] += r["clicks"]
        o["impressions"] += r["impressions"]
        o["pos_w"] += r["position"] * r["impressions"]
    for q in res:
        for o in res[q].values():
            o["position"] = round(o["pos_w"] / o["impressions"], 1) if o["impressions"] else None
            del o["pos_w"]
    return res


def laatste_volledige_dag(vandaag, achterstand=2):
    """Bepaal via de date-dimensie de laatste dag met data (GSC loopt 2 tot 3 dagen achter)."""
    from datetime import date, timedelta
    d = date.fromisoformat(vandaag)
    data = fetch((d - timedelta(days=14)).isoformat(), d.isoformat(), "date")
    dagen = sorted(r["keys"][0] for r in data["rows"])
    return dagen[-1] if dagen else None
