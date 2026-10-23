#!/usr/bin/env python3
"""Rekent de nulmeting uit de ruwe exports data/gsc/2026-10-21-nulmeting-*.json en schrijft
markdown-tabellen en een JSON naar het opgegeven uitvoerpad. Alleen lezen.

Gebruik: python3 nulmeting_tabellen.py <uitvoer.json>
"""
import json
import re
import sys
import collections
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gsc_hulp as g
import zoekwoord_clusters as zc

P = "2026-10-21-nulmeting-"
MD = "/Users/markvanwijk/Tante Rie SEO/marketing/zoekwoorden/clusters-2026-10-21.md"


def rows(per, naam):
    return json.load(open(g.DATA + f"{P}{per}-{naam}.json"))["rows"]


def nl(x, dec=0):
    s = f"{x:,.{dec}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def tot(rs):
    c = sum(r["clicks"] for r in rs)
    i = sum(r["impressions"] for r in rs)
    pw = sum(r["position"] * r["impressions"] for r in rs)
    return {"clicks": c, "impressions": i, "ctr": 100 * c / i if i else 0, "position": pw / i if i else 0}


def groep_van(q):
    naam, soort = zc.classify(q)
    if naam == "Merk: Tante Rie":
        return "Merk"
    if naam.startswith("Merk (vermoedelijk)"):
        return "Vermoedelijk merk"
    if naam.startswith("Irrelevant: RI&E"):
        return "RI&E ('rie' los)"
    if naam.startswith("Irrelevant: andere"):
        return "Andere 'tante'"
    if naam.startswith("Spam"):
        return "Spam"
    return "Non-brand"


def query_totalen(per):
    """Per zoekopdracht gesommeerd over apparaten (uit de query,device-export)."""
    q = collections.defaultdict(lambda: {"clicks": 0, "impressions": 0, "pw": 0.0})
    for r in rows(per, "querydevice"):
        o = q[r["keys"][0]]
        o["clicks"] += r["clicks"]
        o["impressions"] += r["impressions"]
        o["pw"] += r["position"] * r["impressions"]
    return q


def toppagina(per):
    best = {}
    for r in rows(per, "querypage"):
        q, u = r["keys"]
        if q not in best or r["impressions"] > best[q][0]:
            best[q] = (r["impressions"], g.split_url(u)[1])
    return {q: v[1] for q, v in best.items()}


def hoofdzoekwoorden():
    res = {}
    for line in open(MD):
        if line.startswith("| ") and "/" in line and "vert., pos." in line:
            cel = [c.strip() for c in line.split("|")]
            m = re.match(r"(.+?) \((\d[\d\.]*) vert\., pos\. ([\d,]+)\)", cel[2])
            if m:
                res[cel[1]] = m.group(1)
    return res


def clusters(per, hoofd):
    qt = query_totalen(per)
    tp = toppagina(per)
    cl = collections.defaultdict(lambda: {"clicks": 0, "impressions": 0, "pw": 0.0})
    for q, o in qt.items():
        naam, soort = zc.classify(q, tp.get(q))
        if soort != "non-brand":
            continue
        c = cl[naam]
        c["clicks"] += o["clicks"]; c["impressions"] += o["impressions"]; c["pw"] += o["pw"]
    out = {}
    for naam, c in cl.items():
        hz = hoofd.get(naam)
        hq = qt.get(hz.lower()) if hz else None
        out[naam] = {
            "clicks": c["clicks"], "impressions": c["impressions"],
            "ctr": 100 * c["clicks"] / c["impressions"] if c["impressions"] else 0,
            "position": c["pw"] / c["impressions"] if c["impressions"] else 0,
            "hoofd": hz,
            "hoofd_pos": (hq["pw"] / hq["impressions"]) if hq and hq["impressions"] else None,
            "hoofd_impr": hq["impressions"] if hq else 0,
            "hoofd_clicks": hq["clicks"] if hq else 0,
        }
    return out


def pagina_totalen(per):
    """Per genormaliseerd pad: host en parameters genegeerd (parameters apart geteld)."""
    d = collections.defaultdict(lambda: {"clicks": 0, "impressions": 0, "pw": 0.0, "par_c": 0, "par_i": 0})
    for r in rows(per, "page"):
        v, pad, par = g.split_url(r["keys"][0])
        o = d[pad]
        o["clicks"] += r["clicks"]; o["impressions"] += r["impressions"]; o["pw"] += r["position"] * r["impressions"]
        if par:
            o["par_c"] += r["clicks"]; o["par_i"] += r["impressions"]
    for o in d.values():
        o["position"] = o["pw"] / o["impressions"] if o["impressions"] else 0
        o["ctr"] = 100 * o["clicks"] / o["impressions"] if o["impressions"] else 0
    return d


DOEL = [
    ("2", "/collections/rice"), ("2", "/products/rice-j"), ("2", "/products/rice-a"), ("2", "/products/rice-r"), ("2", "/products/rice-l"),
    ("3", "/pages/theewinkel-borne-twente"),
    ("4", "/collections/joeff"), ("4", "/pages/muuss-van-joeff-de-wand-die-met-je-meebeweegt"),
    ("4", "/collections/nfc-natural-flower-cards"), ("4", "/collections/thee-bewaarblikken"),
    ("5", "/products/pineut-watertwist-carafe-strawberry-hibiscus"),
    ("5", "/products/pineut-watertwist-carafe-strawberry-hibiscus-kopie"),
    ("5", "/products/pineut-watertwist-carafe-citrus-mint-verbena-kopie"),
    ("5", "/products/pineut-watertwist-carafe-iced-tea-mango-green-tea-kopie"),
    ("5", "/products/pineut-watertwist-carafe-sangria-red-wine-bio-kopie"),
    ("5", "/products/pineut-cake-pouchbag-lemon-poppy-cake"), ("5", "/products/pineut-cake-pouchbag-lemon-poppy-cake-kopie"),
    ("6", "/collections/bunzlau"), ("6", "/blogs/nieuws/een-kijkje-bij-bunzlau-nieuwe-seizoensfavorieten-en-een-leuk-nieuwtje"),
    ("6", "/pages/serviezen"),
    ("7", "/pages/blond-amsterdam-servies"), ("7", "/collections/blond"),
    ("8", "/products/earl-grey"), ("8", "/products/beste-van-borne"),
    ("9", "/pages/zakelijk"),
    ("10", "/"), ("10", "/collections/bunzlau"), ("10", "/products/earl-grey"),
]


def md_tabel(kop, rijen):
    return "\n".join(["| " + " | ".join(kop) + " |", "|" + "|".join(["---"] + ["---:"] * (len(kop) - 1)) + "|"] + ["| " + " | ".join(r) + " |" for r in rijen])


def main(out):
    res = {}
    hoofd = hoofdzoekwoorden()
    for per in ("huidig", "vorigemaand"):
        r = {}
        r["totaal"] = tot(rows(per, "date"))
        r["apparaat"] = {x["keys"][0]: x for x in rows(per, "device")}
        # merk / non-brand (query-export: zonder geanonimiseerde zoekopdrachten)
        gr = collections.defaultdict(lambda: {"clicks": 0, "impressions": 0, "pw": 0.0})
        grd = collections.defaultdict(lambda: collections.defaultdict(lambda: {"clicks": 0, "impressions": 0}))
        for x in rows(per, "querydevice"):
            gn = groep_van(x["keys"][0])
            o = gr[gn]; o["clicks"] += x["clicks"]; o["impressions"] += x["impressions"]; o["pw"] += x["position"] * x["impressions"]
            dd = grd[gn][x["keys"][1]]; dd["clicks"] += x["clicks"]; dd["impressions"] += x["impressions"]
        r["groepen"] = {k: dict(v, position=v["pw"] / v["impressions"] if v["impressions"] else 0) for k, v in gr.items()}
        r["groepen_apparaat"] = {k: {a: dict(b) for a, b in v.items()} for k, v in grd.items()}
        r["query_dekking"] = tot(rows(per, "querydevice"))
        v, par = g.homepage_per_variant(rows(per, "page"))
        r["home"] = v; r["home_param"] = par; r["home_aandeel"] = g.https_aandeel(v)
        r["clusters"] = clusters(per, hoofd)
        pt = pagina_totalen(per)
        r["pagina"] = {pad: {k: o[k] for k in ("clicks", "impressions", "ctr", "position", "par_c", "par_i")} for pad, o in pt.items()}
        prod = [o for pad, o in pt.items() if pad.startswith("/products/")]
        r["producten"] = {"paden": len(prod), "clicks": sum(o["clicks"] for o in prod),
                          "impressions": sum(o["impressions"] for o in prod),
                          "par_c": sum(o["par_c"] for o in prod), "par_i": sum(o["par_i"] for o in prod)}
        r["track"] = g.posities_trackwoorden(rows(per, "querypage"))
        # pagina per apparaat
        pdv = collections.defaultdict(lambda: collections.defaultdict(lambda: {"clicks": 0, "impressions": 0}))
        for x in rows(per, "pagedevice"):
            _, pad, _ = g.split_url(x["keys"][0])
            o = pdv[pad][x["keys"][1]]; o["clicks"] += x["clicks"]; o["impressions"] += x["impressions"]
        r["pagina_apparaat"] = {p: {a: dict(b) for a, b in v.items()} for p, v in pdv.items() if p in ("/", "/collections/bunzlau", "/products/earl-grey")}
        res[per] = r
    json.dump(res, open(out, "w"), indent=1, default=str)
    print("ok", out)


if __name__ == "__main__":
    main(sys.argv[1])
