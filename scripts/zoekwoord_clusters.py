#!/usr/bin/env python3
"""Zoekwoordclusters uit Search Console-exports (Tante Rie).

Leest data/gsc/2026-10-21-queries-90d.json en -query-page-90d.json (alleen lezen),
deelt zoekopdrachten in clusters in en schrijft een JSON met resultaten naar
de scratch-/uitvoermap (standaard data/gsc/../../scripts/_clusters_out.json is NIET gebruikt;
uitvoer gaat naar het pad dat als eerste argument wordt gegeven).

Gebruik: python3 zoekwoord_clusters.py <uitvoer.json>
"""
import json
import re
import sys
import collections
from urllib.parse import urlparse

BASE = "/Users/markvanwijk/Tante Rie SEO/data/gsc/"
DATUM = "2026-10-21"

# ---------------------------------------------------------------- merk
BRAND_RE = re.compile(r"tante[\s\-]?rie\b|tanterie|tante[\s\-]?riet\b|tante[\s\-]?rikie|tantrie|tante ri\b|\bt rie\b|tante rie")
BRAND_AMBIG_RE = re.compile(r"^tante$|^tantes? (servies|serviezen)$|^tante (servies|thee|tee|theelepel|r)$|^tante thee")
# RI&E (risico-inventarisatie): irrelevant verkeer op het losse woord "rie"
RIE_RE = re.compile(r"(^|\s)(rie|ri&e|ri en e)(\s|$|\.)|rie\.nl|risico inventarisatie")
SPAM_RE = re.compile(r"bokep|sex|ngentod|threesome|porn")

# ---------------------------------------------------------------- clusters
# (naam, intentie, doelpagina, regex) - eerste treffer wint
CLUSTERS = [
    ("Bunzlau Castle en Bunzlau servies", "leveranciersmerk", "/collections/bunzlau",
     r"bunzlau|bunslau|bunzlaucastle|boleslawiec|bolesławiec"),
    ("Pools aardewerk en pools servies (generiek)", "informatief/vergelijkend", "/collections/bunzlau",
     r"pools (aardewerk|servies)|pools steengoed|poolse (mok|servies)"),
    ("Muuss en Joeff (wanddecoratie)", "leveranciersmerk", "/collections/joeff",
     r"muuss|joeff|joefs|galerijwand|luminlique"),
    ("Rice DK en Rice by Rice", "leveranciersmerk", "/collections/rice",
     r"\brice\b|ricedk|ricebyrice|rice by rice|byrice"),
    ("Blond Amsterdam servies", "leveranciersmerk", "/pages/blond-amsterdam-servies",
     r"blond|mazagran"),
    ("Natural Flower Cards", "leveranciersmerk", "/collections/nfc-natural-flower-cards",
     r"natural ?flower|nfc\b"),
    ("Pineut Water Twist en Delfts blauw waterfles", "leveranciersmerk/product", "/products/waterfles-delfts-blauw",
     r"pineut|water ?twist|watertwist|delfts blauw|water scoop|waterfles|drinkfles"),
    ("Sterrenmunt", "informatief/product", "/products/sterrenmunt",
     r"sterrenmunt|sterrenmix"),
    ("Thee voor bedrijven, kantoor en horeca (zakelijk)", "transactioneel zakelijk", "/pages/zakelijk",
     r"kantoor|horeca|zakelijk|bedrijven|hotel|restaurant|wederverkoop|op het werk|op werk|op de werkvloer|catering|werkplek|voorziening|leverancier|inkopen|sportkantine"),
    ("Theewinkel (generiek en lokaal)", "transactioneel/lokaal", "/pages/theewinkel-borne-twente",
     r"theewinkel|thee winkel|theehuis|tea shop|theeshop|thee shop|kruidenwinkel|kookwinkel|winkel borne|winkels borne|thee uit twente|telvrije|winkel twente|servies winkel|winkel in borne|borne winkel|toko borne|beste van borne|winkels in borne"),
    ("Thee bewaarblik en theeblikken", "transactioneel", "/collections/thee-bewaarblikken",
     r"bewaarblik|theeblik|thee blik|blikjes|blikken|theedoos|thee koker|theekoker|\bblik\b|thee-blik"),
    ("Proefpakket en kennismaken met thee", "transactioneel", "/collections/proefpakketten",
     r"proef|sample|kennismaken|thee pakket|pakketten|theepakket"),
    ("Koude thee, cold brew en ijsthee", "informatief/transactioneel", "/pages/cold-brew-thee",
     r"koude thee|cold ?brew|koud water|ijsthee|ijs thee|iced tea|handybrew|thee voor koud"),
    ("Thee cadeau en theegeschenk", "transactioneel", "/pages/thee-cadeau",
     r"cadeau|geschenk|kado|geef|giftset|gift|moederdag"),
    ("Thee accessoires (zeefje, schep, maatlepel, toren)", "transactioneel", "/collections/thee-accessoires",
     r"accessoire|zeef|schep|lepel|maatschepje|thee toren|theefilter|filter|infuser|theepot|thee pot|theekan|theeservies|teeli|thee verpakken|thee display|thee organizer|thee opbergen|thee dienblad|thee plateau|thee schaaltjes|thee doosjes|thee tubes|thee ei\b|thee eitje|thee kan|waterkoker|thermosfles|kop thee|presentatie|thee kopjes|theekopjes"),
    ("Servies, mokken en bekers (generiek)", "transactioneel/vergelijkend", "/pages/serviezen",
     r"servies|serviezen|\bmok\b|mokken|melk ?mok|tumbler|beker|kop en schotel|ontbijtbord|petit four|\bbord\b|borden|kommen|waterglas|\bglas\b|porselein|koffiekopjes|koffie ?kop"),
    ("Taart, bakmixen en bakken", "transactioneel", "/collections/bakmixen",
     r"baking|dubai cake|bakmix|cake|taart|brownie|pannenkoek|koek|bakken|bakset|bakzolder|bakwinkel|bak winkel"),
    ("Groene, witte en oolong thee en matcha", "transactioneel/informatief", "/collections/groene-thee",
     r"groene|groen thee|green thee|matcha|sencha|japans|japanse|jasmijn|gunpowder|chinese thee|pai mu tan|witte thee|oolong|gele thee"),
    ("Zwarte thee (assam, ceylon, earl grey)", "transactioneel/informatief", "/collections/zwarte-thee",
     r"zwarte|assam|ceylon|darjeeling|earl grey|pu erh|keemun|lapsang|engelse thee|english breakfast"),
    ("Rooibos en honeybush", "transactioneel/informatief", "/collections/rooibos",
     r"rooibos|honeybush"),
    ("Vruchtenthee en fruitige thee", "transactioneel/informatief", "/collections/vruchtenthee",
     r"vruchten ?thee|fruitige|fruit thee|aardbei|hibiscus|cranberry|mango|ananas|kokos thee|kersen|framboos|bessen|vlierbes|citroen|bananen|pompoen"),
    ("Kruidenthee (kamille, munt, gember, salie)", "informatief/transactioneel", "/collections/kruidenthee",
     r"kruiden ?thee|kamille|munt|salie|gember|ginger|kurkuma|valeriaan|venkel|fenegriek|paardenbloem|zoethout|artisjok|meidoorn|detox|rustgevende|relax thee|slaap thee|tijm|rozemarijn|linde thee|brandnetel|lavendel|melisse|mariadistel|goudsbloem|passiebloem|vrouwenmantel|lapacho|tulsi|jeneverbes|dennen|korenbloem|damiana|sopropo|looizuur|vochtafdrijvende|pau d.arco|cactus|moringa"),
    ("Smaakthee en seizoensthee", "transactioneel", "/collections/thee",
     r"speculaas|slagroom|brulee|brûlée|kerst|herfst|winter|chocolade thee|karamel|caramel|vanille|kaneel|appel thee|champagne|speculoos|pompoen|chai|koek"),
    ("Engelstalig: 'tea'", "oriënterend (Engels, ambigu)", "/collections/thee",
     r"^tea$|^tea |\btea$|\btea\b|^tee$"),
    ("Thee kopen en losse thee (hoofdzoekwoorden)", "transactioneel", "/collections/thee",
     r"losse thee|thee kopen|kopen thee|thee online|thee bestellen|thee assortiment|assortiment thee|thee collectie|thee special|special thee|speciale theesoorten|exclusieve thee|thee luxe|luxe thee|bijzondere thee|thee aanbieding|thee merk|thee surprise|surprise thee|brievenbus|thee essentials|essentials thee|verse thee|thee blend|thee smaken|biologische thee|biologisch thee|thee zonder|natuurlijke thee|^thee$|beste thee|thee melange|thee soorten|^thee "),
    ("Thee longtail: gezondheid, soorten en overig (informatief)", "informatief", "/collections/thee",
     r"thee|theïne|theine|cafeine|cafeïne"),
]
CLUSTER_RES = [(n, i, p, re.compile(rx)) for n, i, p, rx in CLUSTERS]

LOKAAL_RE = re.compile(r"borne|twente|enschede|hengelo|almelo|oldenzaal|hof van twente|delden|goor|rijssen|nijverdal|deventer|zenderen|hertme|overijssel")


def norm_page(url):
    u = urlparse(url)
    path = u.path.rstrip("/") or "/"
    return path


def classify(q, top_page=None):
    ql = q.lower().strip()
    if SPAM_RE.search(ql):
        return "Spam en irrelevant (volwassen inhoud)", "negeren"
    if BRAND_RE.search(ql):
        return "Merk: Tante Rie", "merk"
    if BRAND_AMBIG_RE.search(ql):
        return "Merk (vermoedelijk): tante-varianten", "merk"
    if RIE_RE.search(ql):
        return "Irrelevant: RI&E (risico-inventarisatie)", "negeren"
    if re.search(r"\btante\b", ql) and not re.search(r"thee|servies", ql):
        return "Irrelevant: andere 'tante' (personen, restaurants)", "negeren"
    for n, i, p, rx in CLUSTER_RES:
        if rx.search(ql):
            return n, "non-brand"
    if top_page and top_page.startswith("/products/"):
        return "Productnamen en cadeau-mokken (long tail op productpagina's)", "non-brand"
    return "Overig non-brand (niet ingedeeld)", "non-brand"


def load(name):
    return json.load(open(BASE + f"{DATUM}-{name}.json"))["rows"]


def main(out):
    queries = load("queries-90d")
    qp = load("query-page-90d")

    toppage = {}
    _best = {}
    for r in qp:
        q = r["keys"][0]
        if r["impressions"] > _best.get(q, -1):
            _best[q] = r["impressions"]
            toppage[q] = norm_page(r["keys"][1])
    # query-niveau
    cl = collections.defaultdict(lambda: {"clicks": 0, "impr": 0, "pos_w": 0.0, "queries": []})
    per_query_cluster = {}
    for r in queries:
        q = r["keys"][0]
        n, kind = classify(q, toppage.get(q))
        per_query_cluster[q] = (n, kind)
        c = cl[n]
        c["kind"] = kind
        c["clicks"] += r["clicks"]
        c["impr"] += r["impressions"]
        c["pos_w"] += r["position"] * r["impressions"]
        c["queries"].append({"q": q, "clicks": r["clicks"], "impr": r["impressions"], "pos": r["position"], "ctr": r["ctr"]})

    # query-page niveau (genormaliseerd)
    pages_per_query = collections.defaultdict(lambda: collections.defaultdict(lambda: [0, 0, 0.0]))
    variant_rows = []
    host_stats = collections.Counter()
    for r in qp:
        q, pg = r["keys"][0], r["keys"][1]
        u = urlparse(pg)
        host_stats[u.netloc + "|" + u.scheme] += r["impressions"]
        if u.query:
            variant_rows.append(r)
        path = norm_page(pg)
        a = pages_per_query[q][path]
        a[0] += r["clicks"]
        a[1] += r["impressions"]
        a[2] += r["position"] * r["impressions"]

    # pagina per cluster
    page_cluster = collections.defaultdict(lambda: collections.defaultdict(lambda: [0, 0, 0.0]))
    for q, pgs in pages_per_query.items():
        n, kind = per_query_cluster.get(q) or classify(q, toppage.get(q))
        for pth, a in pgs.items():
            b = page_cluster[n][pth]
            b[0] += a[0]; b[1] += a[1]; b[2] += a[2]

    res = {
        "clusters": {n: {**{k: v for k, v in c.items() if k != "queries"},
                         "pos": c["pos_w"] / c["impr"] if c["impr"] else 0,
                         "queries": sorted(c["queries"], key=lambda x: -x["impr"])}
                     for n, c in cl.items()},
        "page_cluster": {n: {p: {"clicks": a[0], "impr": a[1], "pos": a[2] / a[1] if a[1] else 0} for p, a in d.items()}
                         for n, d in page_cluster.items()},
        "pages_per_query": {q: {p: {"clicks": a[0], "impr": a[1], "pos": a[2] / a[1] if a[1] else 0} for p, a in d.items()}
                            for q, d in pages_per_query.items()},
        "variant_rows": variant_rows,
        "host_stats": host_stats,
    }
    json.dump(res, open(out, "w"), ensure_ascii=False)


if __name__ == "__main__":
    main(sys.argv[1])
