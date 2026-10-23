#!/usr/bin/env python3
"""Wekelijkse migratiemonitor Tante Rie (alleen lezen, Search Console).

Meet hoeveel van de homepage in Google nog op http://www.tanterie.nl/ staat en hoeveel
al op https://tanterie.nl/, over de laatste 7 volledige dagen, en volgt de posities van
'bunzlau servies', 'theewinkel', 'thee uit twente' en 'tea' per URL.

Gebruik (elke maandag):
    cd "/Users/markvanwijk/Tante Rie SEO/scripts"
    python3 migratiemonitor.py                    # datum = vandaag
    python3 migratiemonitor.py --datum 2026-10-27 # expliciete datum

Schrijft:
    marketing/rapporten/migratiemonitor-<datum>.md
    data/gsc/<datum>-migratiemonitor-{page,querypage,date}.json  (ruw)
    data/gsc/<datum>-migratiemonitor-samenvatting.json           (voor de volgende week)

Google Bedrijfsprofiel (GBP): het script haalt via gbp_prestaties.py dezelfde laatste 7 dagen met data
op (routeverzoeken, websiteklikken, bellen, vertoningen Zoeken en Maps) en vergelijkt ze met de 7 dagen
daarvoor. GBP loopt een paar dagen achter: de laatste dag met een waarde min 2 dagen is de einddatum.
Mislukt de GBP-ophaal (token, quota), dan loopt de GSC-monitor door met een melding in het rapport.
Ruwe GBP-data: data/gbp/<datum>-migratiemonitor-gbp.json.

Websitelink in het profiel: op 2026-10-21 is de link door Mark veranderd van http://www.tanterie.nl/ naar
https://tanterie.nl/. Het totale https-aandeel van de homepage kan daardoor stijgen zonder dat Google de
migratie heeft afgerond. Daarom rekent het script ook het https-aandeel voor de homepage bij alleen
niet-merkzoekopdrachten (die komen niet via het profiel); die maat is leidend voor het 90-procentsignaal.

Regels (plan-2026-10, actie 1):
- Signaal 'migratie grotendeels rond': https://tanterie.nl/ heeft minstens 90 procent van
  de homepagevertoningen EN van de homepageklikken, in deze week en in de vorige weekmonitor.
- Waarschuwing na 8 weken (16-12-2026): nog geen verschuiving, dan melden aan Technisch SEO.
  'Geen verschuiving' = het https-aandeel in vertoningen en in klikken ligt beide minder dan
  10 procentpunt boven het nulpunt (eerste monitor) en onder de 90 procent.
"""
import argparse
import glob
import json
import os
import sys
from datetime import date, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gsc_hulp as g
import zoekwoord_clusters as zc

ROOT = "/Users/markvanwijk/Tante Rie SEO/"
RAPPORT_DIR = ROOT + "marketing/rapporten/"
DREMPEL = 90.0
NULPUNT_DATUM = date(2026, 10, 21)
WAARSCHUWING_DATUM = NULPUNT_DATUM + timedelta(weeks=8)  # 2026-12-16
MIN_VERSCHUIVING_PP = 10.0
MIN_KLIKKEN_NM = 10  # onder dit aantal niet-merkklikken op de homepage wordt het klikaandeel niet beoordeeld
LINK_WIJZIGING = date(2026, 10, 21)  # websitelink GBP: http://www.tanterie.nl/ -> https://tanterie.nl/
GBP_LOCATIE = "locations/6267696427702073490"
GBP_BUFFER_DAGEN = 2
GBP_MAATEN = [
    ("BUSINESS_DIRECTION_REQUESTS", "Routeverzoeken"),
    ("WEBSITE_CLICKS", "Websiteklikken"),
    ("CALL_CLICKS", "Bellen"),
    ("BUSINESS_IMPRESSIONS_MOBILE_SEARCH", "Vertoningen Zoeken mobiel"),
    ("BUSINESS_IMPRESSIONS_DESKTOP_SEARCH", "Vertoningen Zoeken desktop"),
    ("BUSINESS_IMPRESSIONS_MOBILE_MAPS", "Vertoningen Maps mobiel"),
    ("BUSINESS_IMPRESSIONS_DESKTOP_MAPS", "Vertoningen Maps desktop"),
]


def nl(x, dec=0):
    s = f"{x:,.{dec}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def pp(x):
    return ("+" if x >= 0 else "-") + nl(abs(x), 1)


def homepage_niet_merk(qp_rows):
    """https-aandeel van de homepage voor alleen niet-merkzoekopdrachten (niet via het GBP-profiel)."""
    v = {}
    for r in qp_rows:
        q, url = r["keys"][0], r["keys"][1]
        naam, soort = zc.classify(q)
        if soort != "non-brand":
            continue
        variant, pad, par = g.split_url(url)
        if pad != "/" or par:
            continue
        o = v.setdefault(variant, {"clicks": 0, "impressions": 0})
        o["clicks"] += r["clicks"]
        o["impressions"] += r["impressions"]
    return g.https_aandeel(v)


def gbp_blok(d0):
    """Haal GBP-cijfers op voor het laatste 7-dagenvenster met data en de week daarvoor.
    Geeft een dict; bij een fout {'fout': tekst} zodat de GSC-monitor doorgaat."""
    try:
        import gbp_prestaties as gbp  # kan ImportError geven (requests, google-auth)
        sess = gbp.sessie()
        start = d0 - timedelta(days=35)
        eind = d0 - timedelta(days=1)
        params = [("dailyMetrics", m) for m, _ in GBP_MAATEN]
        for pre, dd in (("dailyRange.start_date", start), ("dailyRange.end_date", eind)):
            params += [(f"{pre}.year", dd.year), (f"{pre}.month", dd.month), (f"{pre}.day", dd.day)]
        data = gbp.get(sess, f"https://businessprofileperformance.googleapis.com/v1/{GBP_LOCATIE}:fetchMultiDailyMetricsTimeSeries", params)
    except (Exception, SystemExit) as e:  # gbp_prestaties gebruikt sys.exit bij HTTP-fouten
        return {"fout": f"{type(e).__name__}: {str(e)[:600]}"}
    dag = {}
    for reeks in data.get("multiDailyMetricTimeSeries", []):
        for ts in reeks.get("dailyMetricTimeSeries", []):
            for x in ts.get("timeSeries", {}).get("datedValues", []):
                dd = date(x["date"]["year"], x["date"]["month"], x["date"]["day"])
                dag.setdefault(ts["dailyMetric"], {})[dd.isoformat()] = int(x.get("value", 0) or 0)
    vertoningen = [m for m, _ in GBP_MAATEN if "IMPRESSIONS" in m]
    met_data = sorted(k for m in vertoningen for k, v in dag.get(m, {}).items() if v)
    if not met_data:
        return {"fout": "geen enkele dag met waarden in de GBP-respons", "ruw": data}
    laatste = date.fromisoformat(met_data[-1])
    e = laatste - timedelta(days=GBP_BUFFER_DAGEN)
    s_ = e - timedelta(days=6)
    ve = s_ - timedelta(days=1)
    vs = ve - timedelta(days=6)

    def som(m, a, b):
        return sum(v for k, v in dag.get(m, {}).items() if a <= date.fromisoformat(k) <= b)

    return {
        "venster": [s_.isoformat(), e.isoformat()], "vorig_venster": [vs.isoformat(), ve.isoformat()],
        "laatste_dag_met_data": laatste.isoformat(),
        "nu": {m: som(m, s_, e) for m, _ in GBP_MAATEN},
        "vorig": {m: som(m, vs, ve) for m, _ in GBP_MAATEN},
        "ruw": data,
    }


def vorige_samenvatting(datum):
    kandidaten = sorted(glob.glob(g.DATA + "*-migratiemonitor-samenvatting.json"))
    kandidaten = [k for k in kandidaten if os.path.basename(k)[:10] < datum]
    return json.load(open(kandidaten[-1])) if kandidaten else None


def eerste_samenvatting():
    kandidaten = sorted(glob.glob(g.DATA + "*-migratiemonitor-samenvatting.json"))
    return json.load(open(kandidaten[0])) if kandidaten else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--datum", default=date.today().isoformat())
    ap.add_argument("--dagen", type=int, default=7)
    a = ap.parse_args()
    datum = a.datum
    d0 = date.fromisoformat(datum)

    laatste = g.laatste_volledige_dag(datum)
    eind = date.fromisoformat(laatste)
    start = eind - timedelta(days=a.dagen - 1)
    s, e = start.isoformat(), eind.isoformat()
    pre = f"{g.DATA}{datum}-migratiemonitor-"
    dag = g.fetch(s, e, "date", pre + "date.json")
    pag = g.fetch(s, e, "page", pre + "page.json")
    qp = g.fetch(s, e, "query,page", pre + "querypage.json")
    dagen_met_data = sorted(r["keys"][0] for r in dag["rows"])

    varianten, param = g.homepage_per_variant(pag["rows"])
    aandeel = g.https_aandeel(varianten)
    track = g.posities_trackwoorden(qp["rows"])

    nm = homepage_niet_merk(qp["rows"])
    gbp_data = gbp_blok(d0)

    vorige = vorige_samenvatting(datum)
    eerste = eerste_samenvatting()
    nul = eerste["aandeel"] if (eerste and eerste["datum"] != datum) else aandeel

    def boven(a_):
        return (a_["aandeel_impressions"] or 0) >= DREMPEL and (a_["aandeel_clicks"] or 0) >= DREMPEL

    deze_boven = boven(aandeel)
    vorige_boven = bool(vorige and boven(vorige["aandeel"]))
    rond = deze_boven and vorige_boven
    weken_op_rij = (1 + (vorige.get("weken_op_rij", 0) if vorige else 0)) if deze_boven else 0

    verschuiving_i = (aandeel["aandeel_impressions"] or 0) - (nul["aandeel_impressions"] or 0)
    verschuiving_c = (aandeel["aandeel_clicks"] or 0) - (nul["aandeel_clicks"] or 0)
    geen_verschuiving = (verschuiving_i < MIN_VERSCHUIVING_PP and verschuiving_c < MIN_VERSCHUIVING_PP
                         and not deze_boven)
    # Niet-merkmaat: de websitelink van het profiel (gewijzigd op 21-10) telt hier niet mee.
    def boven_nm(a_):
        i_ok = (a_ or {}).get("aandeel_impressions") is not None and a_["aandeel_impressions"] >= DREMPEL
        klikken = (a_ or {}).get("clicks_totaal", 0)
        c_ok = klikken < MIN_KLIKKEN_NM or (a_["aandeel_clicks"] or 0) >= DREMPEL
        return bool(i_ok and c_ok)

    deze_boven_nm = boven_nm(nm)
    vorige_boven_nm = bool(vorige and boven_nm(vorige.get("aandeel_nietmerk")))
    rond_nm = deze_boven_nm and vorige_boven_nm
    weken_op_rij_nm = (1 + (vorige.get("weken_op_rij_nietmerk", 0) if vorige else 0)) if deze_boven_nm else 0
    rond_bevestigd = rond and rond_nm
    na_link = eind >= LINK_WIJZIGING
    waarschuwing = d0 >= WAARSCHUWING_DATUM and geen_verschuiving and not rond
    dagen_tot = (WAARSCHUWING_DATUM - d0).days

    samenvatting = {
        "datum": datum, "venster": [s, e], "aandeel": aandeel, "weken_op_rij": weken_op_rij,
        "rond": rond, "varianten": {k: v for k, v in varianten.items() if v["impressions"] or v["clicks"]},
        "track": track,
        "aandeel_nietmerk": nm, "weken_op_rij_nietmerk": weken_op_rij_nm,
        "rond_nietmerk": rond_nm, "rond_bevestigd": rond_bevestigd,
        "gbp": ({k: v for k, v in gbp_data.items() if k != "ruw"}),
    }
    if "ruw" in gbp_data:
        json.dump(gbp_data["ruw"], open(f"{ROOT}data/gbp/{datum}-migratiemonitor-gbp.json", "w"), indent=1)
    json.dump(samenvatting, open(pre + "samenvatting.json", "w"), indent=1)

    L = []
    L.append(f"# Migratiemonitor {datum}\n")
    L.append(f"Venster: {s} tot en met {e} ({a.dagen} dagen; laatste dag met data in Search Console: {laatste}). "
             f"Property sc-domain:tanterie.nl. Alleen lezen. "
             f"{'Dit is het nulpunt van de monitor.' if not vorige else 'Vergeleken met de monitor van ' + vorige['datum'] + ' (venster ' + vorige['venster'][0] + ' tot ' + vorige['venster'][1] + ').'}\n")
    if len(dagen_met_data) < a.dagen:
        L.append(f"Let op: er is data voor {len(dagen_met_data)} van de {a.dagen} dagen.\n")

    L.append("## Signalen\n")
    L.append(f"Signaal migratie grotendeels rond (totaal en niet-merk beide nodig): {'ja' if rond_bevestigd else 'nee'}.\n")
    L.append(f"Totaalmaat: {'ja' if rond else 'nee'}. "
             f"Deze week {'boven' if deze_boven else 'onder'} de {int(DREMPEL)} procent voor vertoningen en klikken samen"
             f"{', vorige monitor ' + ('boven' if vorige_boven else 'onder') if vorige else ', er is nog geen vorige monitor om mee te vergelijken'}. "
             f"Weken op rij boven de drempel: {weken_op_rij} (twee zijn nodig).\n")
    L.append(f"Niet-merkmaat (alleen zoekopdrachten zonder merknaam, dus niet beïnvloed door de websitelink in het Bedrijfsprofiel): "
             f"{nl(nm['aandeel_impressions'], 1) if nm['aandeel_impressions'] is not None else 'geen data'} procent van de homepagevertoningen "
             f"({nl(nm['impressions'])} van {nl(nm['impressions_totaal'])}) en {nl(nm['aandeel_clicks'], 1) if nm['aandeel_clicks'] is not None else 'geen data'} procent van de homepageklikken "
             f"({nl(nm['clicks'])} van {nl(nm['clicks_totaal'])}; onder {MIN_KLIKKEN_NM} klikken wordt het klikaandeel niet beoordeeld). "
             f"Deze week {'boven' if deze_boven_nm else 'onder'} de {int(DREMPEL)} procent"
             f"{', vorige monitor ' + ('boven' if vorige_boven_nm else 'onder of niet gemeten') if vorige else ''}. "
             f"Weken op rij: {weken_op_rij_nm} (twee zijn nodig).\n")
    if na_link or d0 >= LINK_WIJZIGING:
        L.append(f"Let op: op {LINK_WIJZIGING} is de websitelink in het Google Bedrijfsprofiel veranderd van http://www.tanterie.nl/ naar https://tanterie.nl/. "
                 f"Het totale https-aandeel kan door die link stijgen zonder dat de migratie zelf verder is. Beoordeel de migratie daarom vanaf de eerste monitor na die datum op de niet-merkmaat.\n")
    if waarschuwing:
        L.append(f"WAARSCHUWING: acht weken na het nulpunt ({WAARSCHUWING_DATUM}) is het https-aandeel niet verschoven "
                 f"(vertoningen {pp(verschuiving_i)} procentpunt, klikken {pp(verschuiving_c)} procentpunt ten opzichte van het nulpunt). "
                 f"Melden aan Technisch SEO voor controle van de adreswijziging in Search Console.\n".replace("WAARSCHUWING: ", "Waarschuwing: "))
    else:
        L.append(f"Waarschuwing acht weken: niet actief. Controledatum {WAARSCHUWING_DATUM} "
                 f"({'nog ' + str(dagen_tot) + ' dagen' if dagen_tot > 0 else 'verstreken'}). "
                 f"Verschuiving sinds het nulpunt: vertoningen {pp(verschuiving_i)} procentpunt, klikken {pp(verschuiving_c)} procentpunt.\n")

    L.append("## Homepage per URL-variant\n")
    L.append("| URL | Vertoningen | Klikken | Positie |\n|---|---:|---:|---:|")
    for v, o in sorted(varianten.items(), key=lambda kv: -kv[1]["impressions"]):
        if o["impressions"] or o["clicks"]:
            L.append(f"| {v}/ | {nl(o['impressions'])} | {nl(o['clicks'])} | {nl(o['position'], 1) if o['position'] else '-'} |")
    if param["impressions"]:
        L.append(f"| Homepage met parameters (apart, niet meegeteld) | {nl(param['impressions'])} | {nl(param['clicks'])} | - |")
    L.append("")
    L.append(f"Aandeel van https://tanterie.nl/ in de homepage: {nl(aandeel['aandeel_impressions'], 1)} procent van de vertoningen "
             f"({nl(aandeel['impressions'])} van {nl(aandeel['impressions_totaal'])}) en {nl(aandeel['aandeel_clicks'], 1)} procent van de klikken "
             f"({nl(aandeel['clicks'])} van {nl(aandeel['clicks_totaal'])}). Bij zo weinig klikken per week beweegt het klikaandeel snel door een paar klikken.\n")

    L.append("## Trackingzoekwoorden per URL\n")
    L.append("Positie is het gemiddelde gewogen op vertoningen, per URL zonder parameters.\n")
    L.append("| Zoekwoord | URL | Vertoningen | Klikken | Positie |\n|---|---|---:|---:|---:|")
    for q in g.TRACK:
        rijen = sorted(track[q].items(), key=lambda kv: -kv[1]["impressions"])
        if not rijen:
            L.append(f"| {q} | geen vertoningen in dit venster | 0 | 0 | - |")
        for url, o in rijen:
            L.append(f"| {q} | {url} | {nl(o['impressions'])} | {nl(o['clicks'])} | {nl(o['position'], 1)} |")
    L.append("")
    if vorige:
        L.append("### Verschil met de vorige monitor\n")
        L.append("| Zoekwoord | URL | Positie nu | Positie vorige | Verschil |\n|---|---|---:|---:|---:|")
        for q in g.TRACK:
            for url, o in sorted(track[q].items(), key=lambda kv: -kv[1]["impressions"]):
                p0 = vorige["track"].get(q, {}).get(url)
                if p0 and p0.get("position") is not None and o["position"] is not None:
                    L.append(f"| {q} | {url} | {nl(o['position'], 1)} | {nl(p0['position'], 1)} | {nl(o['position'] - p0['position'], 1)} |")
        L.append("")
    L.append("## Google Bedrijfsprofiel\n")
    if "fout" in gbp_data:
        L.append(f"GBP-cijfers niet opgehaald; de GSC-monitor is wel gedraaid. Melding: {gbp_data['fout']}\n")
    else:
        gs, ge = gbp_data["venster"]
        vs_, ve_ = gbp_data["vorig_venster"]
        L.append(f"Venster {gs} tot en met {ge}; vergeleken met {vs_} tot en met {ve_}. Het profiel loopt enkele dagen achter: de laatste dag met vertoningen is {gbp_data['laatste_dag_met_data']}, "
                 f"het venster eindigt {GBP_BUFFER_DAGEN} dagen eerder. Dagen zonder waarde tellen als nul.\n")
        L.append("| Maat | Deze week | Vorige week | Verschil |\n|---|---:|---:|---:|")
        for m, naam in GBP_MAATEN:
            a_, b_ = gbp_data["nu"][m], gbp_data["vorig"][m]
            L.append(f"| {naam} | {nl(a_)} | {nl(b_)} | {('+' if a_ >= b_ else '-') + nl(abs(a_ - b_))} |")
        L.append("")
    L.append("## Methode\n")
    L.append("Bron: Search Console via gsc_query.py en het Bedrijfsprofiel via gbp_prestaties.py. Venster: laatste 7 dagen met data. Homepage: alleen het pad / zonder parameters, "
             "per schema en host. Een vorige weekmonitor is het laatste bestand data/gsc/<datum>-migratiemonitor-samenvatting.json met een eerdere datum. "
             "De getallen zijn waarnemingen; ze zeggen niet waardoor een verschuiving komt.\n")
    path = f"{RAPPORT_DIR}migratiemonitor-{datum}.md"
    open(path, "w").write("\n".join(L))
    print(path)
    print(json.dumps({"venster": [s, e], "aandeel": aandeel, "rond": rond, "waarschuwing": waarschuwing}, indent=1))


if __name__ == "__main__":
    main()
