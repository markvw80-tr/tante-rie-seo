#!/usr/bin/env python3
"""Bouwt marketing/zoekwoorden/clusters-2026-10-21.md uit de GSC-exports.

Gebruik: python3 zoekwoord_rapport.py <tussenbestand.json> <uitvoer.md>
Het tussenbestand komt van zoekwoord_clusters.py. Alleen lezen uit data/gsc/.
"""
import json
import re
import sys
import collections

from zoekwoord_score import score, pos_factor, ctr_factor

BASE = "/Users/markvanwijk/Tante Rie SEO/data/gsc/"
D = "2026-10-21"


def nl(x, dec=0):
    s = f"{x:,.{dec}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def pct(clicks, impr):
    return nl(100 * clicks / impr, 2) + "%" if impr else "0%"


# --------------------------------------------------------------- advies per cluster
# (advies, basis-tekst, volumes nodig?) - getallen komen uit de data in de basis-tekst via {tags}
ADVIES = {
    "Bunzlau Castle en Bunzlau servies": (
        "Bestaande pagina aanpassen",
        "Collectie /collections/bunzlau staat gemiddeld op positie {pos} met CTR {ctr} op {impr} vertoningen. Verbeter intro, titel en meta, voeg interne links toe vanuit de homepage en blog, en beantwoord winkelvragen ('kopen in Polen', 'winkels Nederland', 'aanbieding'). Subtermen als mokken, borden, kannen en melkkan staan op positie 17 tot 27 en landen op dezelfde collectie; subcollecties pas na volumecheck.",
        "Nee voor merkterm, ja voor subcollecties"),
    "Pools aardewerk en pools servies (generiek)": (
        "Bestaande pagina aanpassen, later eventueel nieuwe gids",
        "{impr} vertoningen op positie {pos}: alleen een alinea op de Bunzlau-collectie toevoegen. Een aparte informatieve gids (Pools aardewerk: onderhoud, vaatwasser, herkomst) pas bouwen als het volume dat rechtvaardigt.",
        "Ja"),
    "Muuss en Joeff (wanddecoratie)": (
        "Bestaande pagina aanpassen",
        "'joeff' heeft 354 vertoningen op positie 8,5 met 1 klik; 'muuss' 632 vertoningen en 21 klikken op positie 7,2. Er zijn twee pagina's (collectie en pagina 'muuss-van-joeff'). Maak de collectie de doelpagina, pas titel en meta aan op beide merknamen en laat de pagina doorlinken.",
        "Nee"),
    "Rice DK en Rice by Rice": (
        "Bestaande pagina aanpassen",
        "Collectie /collections/rice: {impr} vertoningen op positie {pos}, CTR {ctr}. 'rice dk' (495) staat op 22,6, 'ricebyrice' (214) en 'ricedk' (129) op positie 8,6 en 9,4 zonder klik. Voeg de schrijfwijzen Rice DK, Rice by Rice en ricedk toe aan titel, intro en beschrijving.",
        "Nee"),
    "Blond Amsterdam servies": (
        "Bestaande pagina aanpassen",
        "{impr} vertoningen op positie {pos}, {clicks} klik. De pagina /pages/blond-amsterdam-servies staat op 7,9 met lage CTR. Veel zoekopdrachten zijn praktische vragen (vaatwasser, magnetron): voeg een FAQ-blok toe. Beslis welke van pagina en /collections/blond de hoofdrol krijgt.",
        "Nee"),
    "Natural Flower Cards": (
        "Bestaande pagina aanpassen",
        "'natural flower cards' 157 vertoningen op positie 6,7, 1 klik; schrijfwijze zonder spaties staat ook in de data. Titel en meta van /collections/nfc-natural-flower-cards aanpassen.",
        "Nee"),
    "Pineut Water Twist en Delfts blauw waterfles": (
        "Bestaande pagina aanpassen",
        "{impr} vertoningen op positie {pos}. Er bestaan twee productpagina's voor de Pineut Water Twist (een met 'kopie' in de slug) die elkaars vertoningen delen. Voeg samen of canonicaliseer.",
        "Nee"),
    "Sterrenmunt": (
        "Bestaande pagina aanpassen, daarna blog",
        "'wat is sterrenmunt' (46) en 'sterrenmunt thee gezond' (35) zijn informatieve vragen op een productpagina. Kort FAQ-blok op /products/sterrenmunt; blog alleen na volumecheck.",
        "Ja"),
    "Thee voor bedrijven, kantoor en horeca (zakelijk)": (
        "Bestaande pagina uitbreiden",
        "/pages/zakelijk krijgt {impr} vertoningen in dit cluster op positie {pos} en 0 klikken. 'horeca theeleverancier' (63, positie 8,6) en 'theeleverancier horeca' (48, positie 7,2) zijn de snelle winst. Splits eventueel later in kantoor en horeca, na volumecheck.",
        "Ja"),
    "Theewinkel (generiek en lokaal)": (
        "Bestaande pagina aanpassen",
        "'theewinkel' (569 vertoningen, positie 12,0) wordt bediend door de homepage; de eigen pagina /pages/theewinkel-borne-twente krijgt daar 3 vertoningen op positie 91. Maak de pagina de duidelijke doelpagina voor theewinkel, kruidenwinkel Borne en thee uit Twente.",
        "Ja (landelijk 'theewinkel')"),
    "Thee bewaarblik en theeblikken": (
        "Bestaande pagina aanpassen",
        "'thee bewaarblik' 240 vertoningen op positie 12,1 zonder klik. Collectie staat op 16,2, twee productpagina's op positie 2 maar zonder klik. Verbeter collectieteksten en titel; test of de productsnippets de klik wegnemen.",
        "Ja"),
    "Proefpakket en kennismaken met thee": (
        "Bestaande pagina aanpassen",
        "{impr} vertoningen op positie {pos}, 0 klikken. Doelpagina /collections/proefpakketten; de homepage concurreert mee. Eerst on-page verbeteren, dan meten.",
        "Ja"),
    "Koude thee, cold brew en ijsthee": (
        "Bestaande pagina aanpassen",
        "{impr} vertoningen op positie {pos}, 0 klikken. /pages/cold-brew-thee en /collections/ijsthee delen de vertoningen; kies de pagina als hoofdpagina en link de collectie ernaar.",
        "Ja"),
    "Thee cadeau en theegeschenk": (
        "Bestaande pagina aanpassen",
        "{impr} vertoningen op positie {pos}. Doelpagina /pages/thee-cadeau; de homepage krijgt nu de vertoningen voor 'thee cadeau' (27 vertoningen, positie 43). Er bestaan ook /pages/cadeaus-en-lekkers en /collections/cadeaus: kies een hoofdpagina.",
        "Ja"),
    "Thee accessoires (zeefje, schep, maatlepel, toren)": (
        "Bestaande pagina aanpassen",
        "{impr} vertoningen op positie {pos}. Collectie /collections/thee-accessoires staat op 45 voor 'thee accessoires' en de homepage wordt er soms bij gekozen. Subcollecties (theezeefjes, maatschepjes) bestaan al deels; geef /collections/thee-accessoires intro en interne links.",
        "Ja"),
    "Servies, mokken en bekers (generiek)": (
        "Bestaande pagina aanpassen",
        "'servies' 85 vertoningen op positie 6,4 (homepage, 2 klikken). Doelpagina /pages/serviezen: deze krijgt nu bijna alleen merkvertoningen. Maak er een echte servies-hub van met links naar Bunzlau, Blond Amsterdam en Rice.",
        "Ja"),
    "Taart, bakmixen en bakken": (
        "Bestaande pagina aanpassen",
        "{impr} vertoningen op positie {pos}. 'baking' (64) en 'dubai cake' (63) staan op positie 4,8 en 6,8 zonder klik; 'bakzolder' (25) landt op /collections/bakmixen.",
        "Ja"),
    "Groene, witte en oolong thee en matcha": (
        "Bestaande pagina aanpassen",
        "{impr} vertoningen op gemiddelde positie {pos}. Collectie /collections/groene-thee krijgt weinig; eerst indexering en onpage controleren voor je extra content bouwt.",
        "Ja"),
    "Zwarte thee (assam, ceylon, earl grey)": (
        "Bestaande pagina aanpassen",
        "{impr} vertoningen op positie {pos}. Laag volume; meenemen in collectieteksten.",
        "Ja"),
    "Rooibos en honeybush": (
        "Bestaande pagina aanpassen",
        "{impr} vertoningen op positie {pos}, 0 klikken. Doelpagina /collections/rooibos (positie 18,9 voor de collectie in de pagina-export).",
        "Ja"),
    "Vruchtenthee en fruitige thee": (
        "Bestaande pagina aanpassen",
        "{impr} vertoningen op positie {pos}. Doelpagina /collections/vruchtenthee (positie 14,9 in de pagina-export).",
        "Ja"),
    "Kruidenthee (kamille, munt, gember, salie)": (
        "Nieuwe pagina overwegen na volumecheck",
        "{impr} vertoningen over 138 verschillende kruiden, positie {pos}. Doelpagina /collections/kruidenthee; een gids 'welke kruidenthee bij welke klacht' is een mogelijke nieuwe pagina. Let op gezondheidsclaims.",
        "Ja"),
    "Smaakthee en seizoensthee": (
        "Bestaande pagina aanpassen",
        "{impr} vertoningen op positie {pos}. 'speculaas thee' (63) staat op 20,5 en heeft een eigen productpagina (positie 13,7).",
        "Ja"),
    "Engelstalig: 'tea'": (
        "Negeren (monitoren)",
        "'tea' heeft 890 vertoningen op positie 5,2 en 0 klikken. Geen Engelstalige content aanmaken: er zijn geen klikken die op vraag wijzen.",
        "Nee"),
    "Thee kopen en losse thee (hoofdzoekwoorden)": (
        "Bestaande pagina aanpassen",
        "'losse thee' 221 vertoningen op positie 36,8 en 'thee' 184 op 36,5, beide met de homepage als rankende pagina. Doelpagina /collections/thee; de homepage mag niet voor deze termen concurreren.",
        "Ja"),
    "Thee longtail: gezondheid, soorten en overig (informatief)": (
        "Nieuwe pagina overwegen na volumecheck",
        "{impr} vertoningen verdeeld over {n} unieke zoekopdrachten (gemiddeld {avg} per zoekwoord). Een enkele gids (cafeine, theesoorten) kan veel samen oppakken; nu geen aparte pagina's per soort.",
        "Ja"),
    "Productnamen en cadeau-mokken (long tail op productpagina's)": (
        "Negeren (komt vanzelf via productpagina's)",
        "Zoekopdrachten zijn exacte productnamen (bijvoorbeeld 'you did it', 'jij bent top') op positie rond 10 op de eigen productpagina. Geen actie behalve titelcontrole.",
        "Nee"),
    "Overig non-brand (niet ingedeeld)": (
        "Negeren",
        "Versnipperde restgroep ({n} unieke zoekopdrachten). Geen eenduidige onderwerpen; lokale ruis van Borne en Engelstalige 'near me' queries.",
        "Nee"),
}

GROEPEN = [
    ("Leveranciersmerken en merkproducten", [
        "Bunzlau Castle en Bunzlau servies", "Pools aardewerk en pools servies (generiek)",
        "Muuss en Joeff (wanddecoratie)", "Rice DK en Rice by Rice", "Blond Amsterdam servies",
        "Natural Flower Cards", "Pineut Water Twist en Delfts blauw waterfles", "Sterrenmunt"]),
    ("Thee: transactioneel, winkel, zakelijk en cadeau", [
        "Thee voor bedrijven, kantoor en horeca (zakelijk)", "Theewinkel (generiek en lokaal)",
        "Thee bewaarblik en theeblikken", "Proefpakket en kennismaken met thee",
        "Koude thee, cold brew en ijsthee", "Thee cadeau en theegeschenk",
        "Thee accessoires (zeefje, schep, maatlepel, toren)", "Thee kopen en losse thee (hoofdzoekwoorden)",
        "Servies, mokken en bekers (generiek)", "Taart, bakmixen en bakken"]),
    ("Thee: soorten en informatief", [
        "Groene, witte en oolong thee en matcha", "Zwarte thee (assam, ceylon, earl grey)", "Rooibos en honeybush",
        "Vruchtenthee en fruitige thee", "Kruidenthee (kamille, munt, gember, salie)",
        "Smaakthee en seizoensthee",
        "Thee longtail: gezondheid, soorten en overig (informatief)"]),
    ("Negeren of monitoren", [
        "Engelstalig: 'tea'", "Productnamen en cadeau-mokken (long tail op productpagina's)",
        "Overig non-brand (niet ingedeeld)"]),
]

DOELPAGINA_OVERRIDE = {}


def main(tussen, out):
    d = json.load(open(tussen))
    cl = d["clusters"]
    pc = d["page_cluster"]
    ppq = d["pages_per_query"]
    qrows = json.load(open(BASE + f"{D}-queries-90d.json"))["rows"]
    pages_rows = json.load(open(BASE + f"{D}-pages-90d.json"))["rows"]
    qp_rows = json.load(open(BASE + f"{D}-query-page-90d.json"))["rows"]
    daily = json.load(open(BASE + f"{D}-daily-90d.json"))["rows"]

    tot_clicks_pages = sum(r["clicks"] for r in pages_rows)
    tot_impr_pages = sum(r["impressions"] for r in pages_rows)
    tot_clicks_q = sum(r["clicks"] for r in qrows)
    tot_impr_q = sum(r["impressions"] for r in qrows)
    tot_clicks_qp = sum(r["clicks"] for r in qp_rows)
    tot_impr_qp = sum(r["impressions"] for r in qp_rows)

    brand = cl["Merk: Tante Rie"]
    brand2 = cl["Merk (vermoedelijk): tante-varianten"]
    rie = cl["Irrelevant: RI&E (risico-inventarisatie)"]
    ander = cl["Irrelevant: andere 'tante' (personen, restaurants)"]
    spam = cl["Spam en irrelevant (volwassen inhoud)"]
    nonbrand_names = [n for n, c in cl.items() if c["kind"] == "non-brand"]
    nb_clicks = sum(cl[n]["clicks"] for n in nonbrand_names)
    nb_impr = sum(cl[n]["impr"] for n in nonbrand_names)

    # ---- bijhouden doelpagina-aandeel
    def page_info(n, target):
        pg = pc.get(n, {})
        tot = sum(a["impr"] for a in pg.values())
        tgt = pg.get(target, {"impr": 0, "pos": 0, "clicks": 0})
        top = sorted(pg.items(), key=lambda i: -i[1]["impr"])[:3]
        return tot, tgt, top

    import importlib
    cm = importlib.import_module("zoekwoord_clusters")
    meta = {n: (i, p) for n, i, p, _ in cm.CLUSTERS}

    L = []
    w = L.append

    # =========================================================== kop
    w("# Zoekwoordclusters Tante Rie, 21 oktober 2026")
    w("")
    w("Opgesteld door de zoekwoord- en zoekintentie-onderzoeker. Bron: Search Console, property sc-domain:tanterie.nl, 90 dagen (export van 21 oktober 2026). Alleen analyse; er is niets aangepast in Shopify of het thema en er staat niets in de changelog.")
    w("")
    w("## Samenvatting")
    w("")
    n_cl = len([n for n, c in cl.items() if c["kind"] == "non-brand"])
    w(f"In 90 dagen kreeg tanterie.nl {nl(tot_clicks_pages)} klikken en {nl(tot_impr_pages)} vertoningen (paginaexport, inclusief geanonimiseerde zoekopdrachten). De zoekopdrachtexport dekt maar {nl(tot_impr_q)} vertoningen en {nl(tot_clicks_q)} klikken; de rest zit in zoekopdrachten die Google niet toont. Alle clusterberekeningen hieronder gebruiken dus die {nl(tot_impr_q)} vertoningen.")
    w("")
    w(f"Merk (Tante Rie, Tante Rie Borne, typo's) levert {nl(brand['clicks'])} van {nl(tot_clicks_q)} klikken ({nl(100*brand['clicks']/tot_clicks_q)}%) op slechts {nl(brand['impr'])} vertoningen. Alle echte non-brand zoekopdrachten samen leveren {nl(nb_clicks)} klikken op {nl(nb_impr)} vertoningen, een CTR van {pct(nb_clicks, nb_impr)}. De shop wordt dus bijna alleen gevonden door mensen die de naam al kennen.")
    w("")
    w(f"Het losse woord 'rie' is geen merk. Het gaat om RI&E (risico-inventarisatie): {nl(rie['impr'])} vertoningen in {len(rie['queries'])} zoekopdrachten, nul klikken, vrijwel allemaal op de homepage. Een eenvoudige 'bevat rie'-filter telt dit ten onrechte als merk. Met zo'n filter komt non-brand uit op 142 klikken en 27.518 vertoningen; mijn indeling geeft {nl(nb_clicks)} klikken en {nl(nb_impr)} vertoningen, omdat RI&E, andere 'tante'-zoekopdrachten en spam eruit zijn en de vermoedelijke merkvarianten apart staan.")
    w("")
    w(f"Ik heb de non-brand zoekopdrachten in {n_cl} clusters ingedeeld (zie tabellen), plus 5 clusters die geen kans zijn (merk, vermoedelijk merk, RI&E, andere 'tante', volwassen spam). De grootste kansen zijn Bunzlau, Rice, Theewinkel, Blond Amsterdam en Thee bewaarblik. De belangrijkste structurele bevinding is dat de homepage voor tientallen non-brand zoekopdrachten concurreert met de eigen doelpagina's en daar in meerdere gevallen hoger staat dan de doelpagina, zonder dat dit klikken oplevert.")
    w("")

    # =========================================================== methode
    w("## Methode")
    w("")
    w("Bestanden uit data/gsc/ (alleen gelezen):")
    w("")
    w(f"- 2026-10-21-queries-90d.json: {len(qrows)} zoekopdrachten, {nl(tot_clicks_q)} klikken, {nl(tot_impr_q)} vertoningen. Basis voor alle clusterberekeningen, zodat een zoekopdracht niet dubbel telt.")
    w(f"- 2026-10-21-query-page-90d.json: {len(qp_rows)} rijen zoekopdracht plus pagina, {nl(tot_clicks_qp)} klikken, {nl(tot_impr_qp)} vertoningen. Basis voor kannibalisatie, rankende pagina per cluster en variant-URL's.")
    w(f"- 2026-10-21-pages-90d.json: {len(pages_rows)} pagina's, {nl(tot_clicks_pages)} klikken, {nl(tot_impr_pages)} vertoningen. Alleen gebruikt voor paginatotalen.")
    w("- 2026-10-21-daily-90d.json en 2026-10-21-devices-90d.json: niet gebruikt voor de clustering. Het bestand url-inspection en overige bestanden zijn niet aangeraakt.")
    w("")
    w("Filters en regels:")
    w("")
    w("1. Brand: zoekopdrachten met 'tante rie', 'tanterie', 'tante riet', 'tante rikie' en gelijkaardige schrijfwijzen. Een tweede, aparte groep 'vermoedelijk merk' bevat 'tante' alleen, 'tantes servies', 'tante thee' en 'tante servies'; die tel ik niet mee als echt non-brand.")
    w("2. Irrelevant: het losse woord 'rie' (RI&E), andere 'tante'-zoekopdrachten (personen, restaurants) en volwassen spam.")
    w("3. Pagina-URL's: http en www zijn genormaliseerd naar het pad op tanterie.nl, queryparameters (variant, country, currency, utm) zijn verwijderd. Alle 26 rijen op webshop.tanterie.nl zijn samengevoegd met hun pad op tanterie.nl.")
    w("4. Clustering: handmatig opgestelde regels op trefwoorden in scripts/zoekwoord_clusters.py; de eerste passende regel wint, dus elke zoekopdracht zit in precies één cluster. Cluster-CTR = klikken gedeeld door vertoningen; cluster-positie is het gemiddelde gewogen op vertoningen.")
    w("5. Elke tabel noemt per cluster precies één doelpagina. Waar twee clusters dezelfde pagina delen is dat expliciet bedoeld en vermeld.")
    w("")
    w("Beperkingen: geen zoekvolumes (Ahrefs en Semrush werken niet via de API). Vertoningen zijn een proxy. Bij een gemiddelde positie boven 20 liggen vertoningen ver onder het echte zoekvolume; bij positie 1 tot 10 liggen ze er dichter bij. Gemiddelde posities zijn gemiddelden over meerdere zoekopdrachten en pagina's en kunnen een enkele goede positie verbergen.")
    w("")

    # variant-URL's
    vr = d["variant_rows"]
    v_impr = sum(r["impressions"] for r in vr)
    v_clicks = sum(r["clicks"] for r in vr)
    hs = d["host_stats"]
    w("### Variant-, zoek- en migratie-URL's")
    w("")
    w(f"- URL's met queryparameters: {len(vr)} rijen, {nl(v_impr)} vertoningen en {nl(v_clicks)} klikken, allemaal productpagina's met ?variant=...&utm_source=google&utm_medium=product_sync (Google Merchant-feed, organische productvermeldingen). Het is een verwaarloosbaar deel (minder dan 0,5% van de vertoningen) en is bij het groeperen samengevoegd. Er zijn geen zoek-URL's (/search) of ?_pos=-URL's in deze export gevonden.")
    w(f"- webshop.tanterie.nl: 26 rijen met {nl(hs.get('webshop.tanterie.nl|https', 0))} vertoningen. Restanten van de migratie, geen apart probleem.")
    w(f"- http://www.tanterie.nl/: {nl(hs.get('www.tanterie.nl|http', 0))} vertoningen in de zoekopdracht-paginaexport. Dit is nog steeds de URL die Google toont voor merkzoekopdrachten en voor veel non-brand zoekopdrachten met goede posities ('tea' positie 5,2 en 'bunzlau servies' positie 4,2 staan op de http://www-homepage, terwijl de https://tanterie.nl/-homepage voor dezelfde termen veel slechter staat). Voor de homepage is dat in de paginaexport 8.135 vertoningen en 543 klikken op http://www.tanterie.nl/ naast 12.635 vertoningen en 247 klikken op https://tanterie.nl/. Dit is een signaal voor de Technisch SEO-specialist: Google heeft de oude homepage-URL nog niet volledig vervangen.")
    w("")

    # =========================================================== merk split
    w("## Merk en non-brand")
    w("")
    w("| Groep | Zoekopdrachten | Vertoningen | Klikken | CTR | Opmerking |")
    w("|---|---:|---:|---:|---:|---|")
    def row(label, c, op):
        w(f"| {label} | {len(c['queries'])} | {nl(c['impr'])} | {nl(c['clicks'])} | {pct(c['clicks'], c['impr'])} | {op} |")
    row("Merk: Tante Rie", brand, "Positie 1,6; dit is vrijwel alle klikken")
    row("Vermoedelijk merk (tante, tantes servies)", brand2, "Niet zeker; niet meegeteld als non-brand kans")
    row("RI&E ('rie' los)", rie, "Irrelevant verkeer, zie verkeerd-rankende pagina's")
    row("Andere 'tante'", ander, "Irrelevant")
    row("Volwassen spam", spam, "Irrelevant; geen actie")
    w(f"| Non-brand (alle clusters) | {sum(len(cl[n]['queries']) for n in nonbrand_names)} | {nl(nb_impr)} | {nl(nb_clicks)} | {pct(nb_clicks, nb_impr)} | Basis voor de clusters |")
    w("")
    w(f"De klikken in de paginaexport ({nl(tot_clicks_pages)}) zijn ruim het dubbele van de klikken in de zoekopdrachtexport ({nl(tot_clicks_q)}). Het verschil zit in zoekopdrachten die Google niet toont (anonieme, zeldzame zoekopdrachten). Dat deel is niet te classificeren; het is waarschijnlijk grotendeels merkverkeer, maar dat is niet vast te stellen.")
    w("")

    # =========================================================== clustertabellen
    w("## Clusters")
    w("")
    w("Intentie: informatief, vergelijkend, transactioneel, lokaal of leveranciersmerk (zoeken op een merk dat Tante Rie verkoopt). De kolom Getal noemt het cijfer waarop het advies rust. Posities zijn gemiddelden. Cluster-CTR is klikken gedeeld door vertoningen.")
    w("")
    cluster_rows = {}
    for gnaam, namen in GROEPEN:
        w(f"### {gnaam}")
        w("")
        w("| Cluster | Hoofdzoekwoord | Ondersteunend | Intentie | Vert. 90d | Klikken | Pos. | CTR | Doelpagina | Advies | Getal waarop het advies rust |")
        w("|---|---|---|---|---:|---:|---:|---:|---|---|---|")
        for n in namen:
            c = cl[n]
            intent, target = meta.get(n, ("overig", "-"))
            qs = c["queries"]
            hoofd = qs[0]["q"] if qs else "-"
            ond = ", ".join(x["q"] for x in qs[1:5])
            adv, basis, vol = ADVIES[n]
            basis = basis.format(impr=nl(c["impr"]), pos=nl(c["pos"], 1), ctr=pct(c["clicks"], c["impr"]),
                                 clicks=nl(c["clicks"]), n=nl(len(qs)),
                                 avg=nl(c["impr"] / max(len(qs), 1), 1))
            if n == "Overig non-brand (niet ingedeeld)":
                target = "-"
            tot, tgt, top = page_info(n, target)
            share = f"{nl(100*tgt['impr']/tot)}% van de query-page-vertoningen" if tot else "n.v.t."
            cluster_rows[n] = (c, target)
            hk = f"{hoofd} ({nl(qs[0]['impr'])} vert., pos. {nl(qs[0]['pos'],1)})" if qs else "-"
            w(f"| {n} | {hk} | {ond} | {intent} | {nl(c['impr'])} | {nl(c['clicks'])} | {nl(c['pos'],1)} | {pct(c['clicks'], c['impr'])} | {target} | {adv} | {basis} Aandeel op doelpagina: {share}. |")
        w("")
    tg = collections.defaultdict(list)
    for n_, (i_, p_) in meta.items():
        tg[p_].append(n_)
    gedeeld = {p_: v for p_, v in tg.items() if len(v) > 1}
    w("Sommige clusters delen een doelpagina, omdat de site nog geen aparte pagina's heeft voor die onderwerpen: " + "; ".join(f"{p_} ({', '.join(v)})" for p_, v in gedeeld.items()) + ". Dat wijkt af van het principe 'een cluster, een pagina' en is de reden voor de adviezen over nieuwe pagina's na volumecheck. Elk cluster heeft wel precies een doelpagina.")
    w("")

    # ----- bijlage top queries per cluster
    # (komt achteraan)

    # =========================================================== kannibalisatie
    w("## Kannibalisatie")
    w("")
    nonbrand_set = set()
    for n in nonbrand_names:
        for x in cl[n]["queries"]:
            nonbrand_set.add(x["q"])
    kann = []
    multi_all = 0
    for q, pg in ppq.items():
        if q not in nonbrand_set:
            continue
        if len(pg) < 2:
            continue
        tot = sum(a["impr"] for a in pg.values())
        if tot < 10:
            continue
        s = sorted(pg.items(), key=lambda i: -i[1]["impr"])
        multi_all += 1
        if tot >= 25 and s[1][1]["impr"] / tot >= 0.15:
            kann.append((tot, q, s))
    kann.sort(reverse=True)
    home_involved = sum(1 for t, q, s in kann if any(p == "/" for p, a in s[:3]))
    w(f"Een zoekwoord telt hier als kannibalisatie als meer dan een tanterie.nl-pagina (na normalisatie) vertoningen krijgt, het zoekwoord minstens 25 vertoningen heeft en de tweede pagina minstens 15% van de vertoningen heeft. Dat zijn {len(kann)} non-brand zoekwoorden; bij een lagere drempel (minstens 10 vertoningen, elke tweede pagina) zijn er {multi_all} zoekwoorden met meer dan een pagina. In {home_involved} van de {len(kann)} gevallen is de homepage een van de betrokken pagina's. Let op: de pagina's staan niet in elk geval slecht; het gaat om vertoningen die verdeeld worden zonder dat de beoogde doelpagina wint.")
    w("")
    w("### Kernpatroon: de homepage concurreert met doelpagina's")
    w("")
    hpt = [(q, s, t) for t, q, s in kann if s[0][0] == "/" or s[1][0] == "/"]
    w("De homepage krijgt vertoningen voor termen die een eigen collectie of pagina hebben. In meerdere gevallen staat de homepage zelfs hoger dan de doelpagina. De meest duidelijke gevallen:")
    w("")
    w("| Zoekwoord | Totaal vert. | Pagina 1 (vert., klikken, pos.) | Pagina 2 | Pagina 3 | Beoogde doelpagina |")
    w("|---|---:|---|---|---|---|")
    def fmt(p):
        return f"{p[0]} ({nl(p[1]['impr'])}, {nl(p[1]['clicks'])}, {nl(p[1]['pos'],1)})"
    for t, q, s in kann[:25]:
        cells = [fmt(p) for p in s[:3]]
        while len(cells) < 3:
            cells.append("")
        n = next((nn for nn in nonbrand_names if any(x['q'] == q for x in cl[nn]['queries'])), "")
        tg = meta.get(n, ("", ""))[1] if n else ""
        w(f"| {q} | {nl(t)} | {cells[0]} | {cells[1]} | {cells[2]} | {tg} |")
    w("")
    w("### Gevallen per type")
    w("")
    w("1. **Homepage tegenover collectie of pagina.** 'theewinkel' (569 vertoningen, 5 klikken) staat op de homepage; de eigen pagina /pages/theewinkel-borne-twente krijgt voor dat zoekwoord 3 vertoningen op positie 91. Bij 'thee uit twente' staat de homepage op positie 6,1 (85 vertoningen), de eigen pagina op 37,9 (69 vertoningen) en /collections/kruidenthee op 77,8. Bij 'bunzlau servies' staat de homepage op positie 4,2 (129 vertoningen, 4 klikken) en /collections/bunzlau op 22,6 (199 vertoningen, 0 klikken). Bij 'proefpakket thee', 'thee accessoires', 'thee cadeau' en alle zakelijke zoekopdrachten is hetzelfde patroon zichtbaar (zie tabel).")
    w("2. **Collectie tegenover productpagina.** 'thee bewaarblik': collectie op positie 16,2 (163 vertoningen) en twee productpagina's op positie 2,3 en 1,8 (76 en 17 vertoningen), alle zonder klik. 'cold brew thee kopen': /collections/ijsthee op 17,4 en /pages/cold-brew-thee op 43,2. 'thee maatschepje': drie pagina's (/collections/thee-accessoires, /collections/theefilters-en-maatschepjes, /products/maatschepje).")
    w("3. **Collectie tegenover merkpagina.** Muuss/Joeff: /collections/joeff krijgt de meeste vertoningen ('muuss': 513 tegen 95), maar de pagina /pages/muuss-van-joeff-de-wand-die-met-je-meebeweegt staat hoger (4,8 tegen 7,5). Bunzlau: bij 'bunzlau castle nieuwe collectie' deelt de collectie vertoningen met het blog 'een kijkje bij Bunzlau' (19 tegen 9).")
    w("4. **Dubbele productpagina's.** 'pineut water twist' en 'watertwist': /products/pineut-watertwist-carafe-strawberry-hibiscus en dezelfde met '-kopie' in de slug delen vertoningen (35 en 10, en 24 en 11). Dit lijkt een dubbel product en kan beter samengevoegd of gecanonicaliseerd worden.")
    w("5. **Producten van een reeks.** 'rice alfabet beker' en 'rice beker letter' verspreiden vertoningen over rice-a, rice-r, rice-l en andere letters. Dat is een natuurlijk gevolg van de reeks en kan opgelost worden met een duidelijke collectiepagina voor Rice-bekers als hoofdpagina.")
    w("6. **Migratie.** De homepage heeft een tweede URL (http://www.tanterie.nl/) die nog vertoningen krijgt en daarmee positie en klikken over twee URL's verdeelt. Dit is geen inhoudelijke kannibalisatie maar wel een oorzaak van de gesplitste signalen op de homepage.")
    w("")
    w("Brand-sitelinks (zoals /pages/serviezen, /pages/thee-en-koffie, /pages/over-ons, /pages/contact en /pages/cadeaus-en-lekkers met positie 2 tot 3) zijn geen kannibalisatie. Het zijn sitelinks die bij 'tante rie' en 'tante rie borne' worden getoond; bijna al hun vertoningen zijn merkvertoningen.")
    w("")

    # =========================================================== verkeerd-rankende pagina's
    w("## Pagina's die voor het verkeerde zoekwoord ranken")
    w("")
    eng = cl["Engelstalig: 'tea'"]
    tea = next(x for x in eng["queries"] if x["q"] == "tea")
    w("| Pagina | Zoekwoord of groep | Vert. | Klikken | Pos. | Waarom het niet klopt | Voorstel |")
    w("|---|---|---:|---:|---:|---|---|")
    w(f"| / (http://www homepage) | tea | {nl(tea['impr'])} | 0 | {nl(tea['pos'],1)} | Engelstalig, 0 klikken ondanks positie 5; de doelgroep is Nederlandstalig. Waarschijnlijk ambigue of internationale zoeker. | Niet bijsturen; niet als kans tellen. Eerst controleren of de homepage-titel 'tea' bevat |")
    w(f"| / (homepage) | RI&E: rie, rie verplicht, rie opstellen, rie maken en {len(rie['queries'])-4} andere | {nl(rie['impr'])} | {nl(rie['clicks'])} | {nl(rie['pos'],1)} | RI&E is risico-inventarisatie en niets met thee te maken; komt door de naam 'Tante Rie' | Negeren; uitsluiten uit rapportages zodat CTR en gemiddelde positie van de homepage niet vertekend worden |")
    w(f"| / (homepage) | Andere 'tante' (tante toos, tante betsie, restaurants, personen) | {nl(ander['impr'])} | {nl(ander['clicks'])} | {nl(ander['pos'],1)} | Andere merken en personen | Negeren |")
    w(f"| / (homepage) | Volwassen spam | {nl(spam['impr'])} | 0 | {nl(spam['pos'],1)} | Irrelevant, mogelijk door de woorden 'tante' en 'rie' | Negeren; niet actief proberen te verminderen, wel melden aan Technisch SEO als het toeneemt |")
    bor = [x for x in cl["Overig non-brand (niet ingedeeld)"]["queries"] if "borne" in x["q"] or "near me" in x["q"]]
    w(f"| / (homepage) | Borne-ruis: vlaai, opticien, makelaar, tuinonderhoud, 'near me' (Engels), honing | {nl(sum(x['impr'] for x in bor))} | {nl(sum(x['clicks'] for x in bor))} | - | Zoekopdrachten naar andere bedrijven in Borne of naar 'near me'-zaken | Negeren; wel een voorbeeld van waarom lokale pagina's duidelijk moeten maken wat Tante Rie wel is |")
    w("| /pages/zakelijk | thee op kantoor, thee op het werk, horeca, hotels | 2.110 (paginaexport) | 0 | 35,4 | Het onderwerp klopt, de pagina staat zo ver weg (positie 20 tot 70) dat niemand klikt | Pagina uitbreiden, zie cluster 'Thee voor bedrijven' |")
    w("| / (homepage) | losse thee, thee, thee kopen, thee accessoires, thee proefpakket | 1.872 (cluster 'Thee kopen') | 5 | 42,2 | Brede termen waar Google de homepage kiest in plaats van een collectie | Zorg dat /collections/thee, /collections/proefpakketten en /collections/thee-accessoires de enige pagina's met die intentie zijn en pas interne links aan |")
    w("| /pages/serviezen, /pages/thee-en-koffie, /pages/over-ons, /pages/contact, /pages/cadeaus-en-lekkers | Alleen merkzoekopdrachten (sitelinks) | 5.779 samen (paginaexport) | 66 | 2,3 tot 3,3 | Deze pagina's hebben geen non-brand vertoningen van betekenis | Niet nodig om te corrigeren; wel kans voor /pages/serviezen om een echte servies-hub te worden |")
    w("")

    # =========================================================== lokaal
    w("## Lokale zoektermen (Borne, Twente, Enschede, Hengelo, Almelo)")
    w("")
    lokrx = re.compile(r"borne|twente|enschede|hengelo|almelo")
    lok = []
    for n in nonbrand_names:
        for x in cl[n]["queries"]:
            if lokrx.search(x["q"]):
                lok.append((x, n))
    lok.sort(key=lambda t: -t[0]["impr"])
    tot_lok = sum(t[0]["impr"] for t in lok)
    w(f"Er zijn {len(lok)} non-brand zoekopdrachten met een van deze plaatsnamen, samen {nl(tot_lok)} vertoningen en {nl(sum(t[0]['clicks'] for t in lok))} klikken (inclusief ruis van andere bedrijven in Borne). Dit is klein vergeleken met de totale non-brand vertoningen, maar de posities zijn goed: 'kookwinkel twente' staat op 3,9 met 3 klikken. Dat zijn echte kansen voor de winkel in Borne (brandzoekopdrachten als 'tante rie borne' zijn hier niet meegeteld).")
    w("")
    w("| Zoekwoord | Plaats | Vert. | Klikken | Pos. | Pagina's die vertoningen krijgen | Opmerking |")
    w("|---|---|---:|---:|---:|---|---|")
    for x, n in lok[:20]:
        plaats = next((p for p in ["borne", "twente", "enschede", "hengelo", "almelo"] if p in x["q"]), "")
        pg = ppq.get(x["q"], {})
        pgs = ", ".join(f"{p} ({nl(a['impr'])})" for p, a in sorted(pg.items(), key=lambda i: -i[1]["impr"])[:3])
        opm = ""
        if any(k in x["q"] for k in ("arie", "schutting", "opticien", "boekenwinkel", "kinderwinkel", "makelaar", "vlaai", "tuin")):
            opm = "Irrelevant: ander bedrijf of onderwerp"
        elif x["q"] == "kookwinkel twente":
            opm = "Goed: positie 3,9; homepage; dit is een winkelzoekopdracht"
        elif x["q"] == "thee uit twente":
            opm = "Homepage en eigen pagina verdelen; eigen pagina staat op positie 38"
        elif "enschede" in x["q"] or "hengelo" in x["q"] or "almelo" in x["q"]:
            opm = "Klein volume; geen aparte pagina's per plaats aanmaken zonder volumecheck"
        w(f"| {x['q']} | {plaats} | {nl(x['impr'])} | {nl(x['clicks'])} | {nl(x['pos'],1)} | {pgs} | {opm} |")
    w("")
    ens = [t for t in lok if any(p in t[0]["q"] for p in ["enschede", "hengelo", "almelo"])]
    w(f"Enschede, Hengelo en Almelo komen nauwelijks voor: {len(ens)} zoekopdrachten met samen {nl(sum(t[0]['impr'] for t in ens))} vertoningen (bijvoorbeeld 'theewinkel enschede' 12 vertoningen op positie 20,2, 'kookwinkel almelo' 8 op positie 2,9, 'kookwinkel hengelo' 5 op positie 7,4). Dat is te weinig om per stad een pagina te maken. Advies: de pagina /pages/theewinkel-borne-twente tot doelpagina voor lokale zoektermen maken, daar Twente, Enschede en Hengelo in de tekst noemen (afstand, reistijd) en lokale signalen in Google Bedrijfsprofiel versterken. Dat laatste valt onder de Autoriteit- en lokale SEO-specialist. Niet-Twentse plaatsen komen ook voor ('theewinkel amstelveen', 'thee winkel haarlem'): negeren.")
    w("")

    # =========================================================== prioriteitsscore
    w("## Prioriteitsscore")
    w("")
    w("De score is bewust eenvoudig: **score = vertoningen x positiefactor x CTR-factor**.")
    w("")
    w("- Positiefactor: 0,2 bij positie onder 4 (staat al bovenaan, weinig te winnen), 1,0 bij positie 4 tot 10, 0,8 bij 10 tot 20, 0,4 bij 20 tot 30, 0,15 boven 30 (kan nog ver weg zijn).")
    w("- CTR-factor: 1,0 bij CTR onder 0,5%, 0,6 bij 0,5 tot 2%, 0,3 bij 2 tot 5%, 0,1 boven 5%.")
    w("")
    w("Een hoge score betekent veel vertoningen die nu bijna niets opleveren en die binnen bereik van de top 10 liggen. Het is geen voorspelling van klikken. De factoren zijn een afweging, geen gemeten waarden. Brand, RI&E en andere irrelevante groepen krijgen geen score. 'tea' wordt uitgesloten omdat 0 klikken op positie 5,2 wijst niet op vraag naar deze zoekopdracht.")
    w("")
    sc = []
    for n in nonbrand_names:
        c = cl[n]
        if n in ("Engelstalig: 'tea'", "Overig non-brand (niet ingedeeld)",
                 "Productnamen en cadeau-mokken (long tail op productpagina's)"):
            continue
        ctr = 100 * c["clicks"] / c["impr"]
        sc.append((score(c["impr"], c["pos"], ctr), n, c, ctr))
    sc.sort(reverse=True, key=lambda t: t[0])
    w("| Rang | Cluster | Vert. | Klikken | Pos. | CTR | Score |")
    w("|---:|---|---:|---:|---:|---:|---:|")
    for i, (s_, n, c, ctr) in enumerate(sc, 1):
        w(f"| {i} | {n} | {nl(c['impr'])} | {nl(c['clicks'])} | {nl(c['pos'],1)} | {nl(ctr,2)}% | {nl(s_)} |")
    w("")
    # losse zoekwoorden
    qs_all = []
    for n in nonbrand_names:
        if n in ("Engelstalig: 'tea'",):
            continue
        for x in cl[n]["queries"]:
            qs_all.append((score(x["impr"], x["pos"], x["ctr"]), x, n))
    qs_all.sort(key=lambda t: -t[0])
    w("Top 15 losse zoekwoorden volgens dezelfde score:")
    w("")
    w("| Zoekwoord | Cluster | Vert. | Klikken | Pos. | Score |")
    w("|---|---|---:|---:|---:|---:|")
    for s_, x, n in qs_all[:15]:
        w(f"| {x['q']} | {n} | {nl(x['impr'])} | {nl(x['clicks'])} | {nl(x['pos'],1)} | {nl(s_)} |")
    w("")

    # =========================================================== volumes
    w("## Volumes: wat is bekend en wat niet")
    w("")
    w("Er zijn geen zoekvolumes uit Ahrefs of Semrush, en ik verzin er geen. Alle volume-inschattingen hieronder zijn schattingen op basis van Search Console-vertoningen: vertoningen per maand is het 90-daagse totaal gedeeld door 3. Dat is een ondergrens, want zoekers die een pagina niet zien (te lage positie) tellen niet mee.")
    w("")
    w("| Cluster | Vert./maand (schatting) | Betrouwbaarheid van de proxy | Volume nodig uit Keyword Planner of Ahrefs |")
    w("|---|---:|---|---|")
    for gnaam, namen in GROEPEN:
        for n in namen:
            c = cl[n]
            pos = c["pos"]
            betr = "redelijk (top 10)" if pos <= 10 else ("matig (positie 10 tot 20)" if pos <= 20 else "laag (positie boven 20, vertoningen zijn een kleine fractie van het zoekvolume)")
            vol = ADVIES[n][2]
            w(f"| {n} | {nl(c['impr']/3)} (schatting) | {betr} | {vol} |")
    w("")
    w("Volumes zijn vooral nodig voor: het zakelijke cluster (kantoor, horeca, hotels), de brede thee-termen ('losse thee', 'thee kopen'), de theesoorten en het longtail-cluster (vóór besloten wordt om een gids te schrijven), 'theewinkel' (landelijk volume), proefpakket, cadeau, accessoires en koude thee. Voor de leveranciersmerken is het volume van het merk in Nederland nuttig, maar niet nodig om de on-page aanpassingen te doen.")
    w("")

    # =========================================================== top 10
    w("## Top 10 prioriteiten voor de SEO Lead")
    w("")
    w("Gerangschikt op prioriteitsscore, met actie, onderbouwend getal en verwachte inspanning. Eerste vijf zijn quick wins op bestaande pagina's.")
    w("")
    def sc_of(n):
        c = cl[n]
        return score(c["impr"], c["pos"], 100 * c["clicks"] / c["impr"])
    top = [t[1] for t in sc[:10]]
    ACTIES = {
        "Bunzlau Castle en Bunzlau servies": ("Collectiepagina /collections/bunzlau herschrijven: intro, titel, meta, FAQ over vaatwasser en herkomst; interne links vanuit homepage en blog; homepage laat Bunzlau-zoekopdrachten over aan de collectie", "Gemiddelde positie 19,8 op 4.030 vertoningen, 0,72% CTR; de pagina zelf heeft in de paginaexport 7.030 vertoningen op positie 16,3 met 78 klikken", "Middel"),
        "Rice DK en Rice by Rice": ("Collectie /collections/rice optimaliseren op Rice DK, Rice by Rice en ricedk; productpagina's van de letterbekers linken naar de collectie", "'rice dk' 495 vertoningen op positie 22,6; 'ricebyrice' 214 op positie 8,6 en 'ricedk' 129 op 9,4, alle met bijna 0 klikken (totaal 1.893 vertoningen, 3 klikken)", "Laag"),
        "Theewinkel (generiek en lokaal)": ("/pages/theewinkel-borne-twente de doelpagina maken: titel en H1 op 'theewinkel', Borne en Twente; homepage laat de term los; interne links op 'theewinkel'", "'theewinkel' 569 vertoningen op positie 12,0 met 5 klikken, wordt bediend door de homepage; de eigen pagina heeft er 3 vertoningen op positie 91", "Laag tot middel"),
        "Blond Amsterdam servies": ("FAQ-blok (vaatwasser, magnetron) op /pages/blond-amsterdam-servies; beslis hoofdpagina tussen deze pagina en /collections/blond", "777 vertoningen, positie 10,2, 1 klik; 'kan blond amsterdam in de vaatwasser' alleen al 85 vertoningen op positie 8,3 zonder klik", "Laag"),
        "Thee bewaarblik en theeblikken": ("Collectie /collections/thee-bewaarblikken verbeteren; onderzoek waarom twee productpagina's op positie 2 geen klikken krijgen (titel, meta, prijs)", "'thee bewaarblik' 240 vertoningen op positie 12,1; collectie 16,2; productpagina's positie 2,3 en 1,8 met 0 klikken (1.073 vertoningen in het cluster)", "Laag"),
        "Muuss en Joeff (wanddecoratie)": ("Collectie /collections/joeff tot hoofdpagina maken; titel en meta op Muuss en Joeff; pagina 'muuss-van-joeff' linkt naar de collectie", "'joeff' 354 vertoningen op positie 8,5 met 1 klik; cluster 1.343 vertoningen en 31 klikken", "Laag"),
        "Pineut Water Twist en Delfts blauw waterfles": ("Dubbele Pineut-productpagina ('-kopie') samenvoegen of canonicaliseren", "347 vertoningen op positie 9,9; twee URL's delen de vertoningen (35 en 10, 24 en 11)", "Laag"),
        "Thee voor bedrijven, kantoor en horeca (zakelijk)": ("/pages/zakelijk uitbreiden met secties voor kantoor, horeca en wederverkoop; en eerst 'horeca theeleverancier' (positie 8,6) en 'theeleverancier horeca' (7,2) in titel opnemen", "2.156 vertoningen, 0 klikken, positie 37,2; die twee zoekopdrachten zitten al in de top 10", "Middel"),
        "Servies, mokken en bekers (generiek)": ("/pages/serviezen veranderen van merk-sitelink in servies-hub met links naar Bunzlau, Blond Amsterdam en Rice", "'servies' 85 vertoningen op positie 6,4; cluster 658 vertoningen op positie 11,5; /pages/serviezen zelf heeft bijna alleen merkvertoningen (899 van 975)", "Middel"),
        "Thee kopen en losse thee (hoofdzoekwoorden)": ("/collections/thee de doelpagina maken voor 'losse thee' en 'thee kopen'; homepage-teksten zodanig aanpassen dat de homepage niet meer voor deze termen concurreert", "'losse thee' 221 vertoningen op positie 36,8 en 'thee' 184 op 36,5, beide op de homepage; cluster 2.087 vertoningen, 6 klikken", "Middel tot hoog"),
    }
    w("| # | Cluster | Actie | Onderbouwend getal | Inspanning |")
    w("|---:|---|---|---|---|")
    for i, n in enumerate(top, 1):
        a = ACTIES[n]
        w(f"| {i} | {n} | {a[0]} | {a[1]} | {a[2]} |")
    w("")
    w("Daarnaast, buiten de top 10: Natural Flower Cards ('natural flower cards' 157 vertoningen op positie 6,7), koude thee (468 vertoningen, 0 klikken, positie 24,6) en de dubbele homepage-URL (http://www.tanterie.nl/ naast https://tanterie.nl/, voor Technisch SEO).")
    w("")

    # =========================================================== bijlage
    w("## Bijlage: top zoekwoorden per cluster")
    w("")
    for gnaam, namen in GROEPEN:
        for n in namen:
            c = cl[n]
            w(f"### {n}")
            w("")
            w("| Zoekwoord | Vert. | Klikken | Pos. | CTR |")
            w("|---|---:|---:|---:|---:|")
            for x in c["queries"][:8]:
                w(f"| {x['q']} | {nl(x['impr'])} | {nl(x['clicks'])} | {nl(x['pos'],1)} | {nl(x['ctr'],1)}% |")
            w("")

    text = ("\n".join(L) + "\n").replace("\u2014", "-").replace("\u2013", "-")
    open(out, "w").write(text)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
