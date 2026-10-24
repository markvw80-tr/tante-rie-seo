#!/usr/bin/env python3
"""Koppelt zoekvolumes (Keyword Planner) aan de zoekwoordclusters en schrijft markdown.

Invoer:
  - uitvoer van scripts/zoekvolumes.py in data/keyword-planner/JJJJ-MM-DD-*.json
    (actie volumes met per_maand, of actie ideeen met alleen volume)
  - de clustertabellen in marketing/zoekwoorden/clusters-2026-10-21.md: de tabel per cluster
    (vertoningen, klikken, positie, doelpagina), de bijlage met top zoekwoorden per cluster
    en de tabel Lokale zoektermen.

Per cluster: totaal zoekvolume per maand, volume per zoekwoord naast vertoningen en positie,
aandeel zichtbaarheid (vertoningen per maand gedeeld door volume) en seizoenspatroon
(piekmaanden uit per_maand). Niets wordt geschat: een zoekwoord zonder volume in de
bestanden blijft leeg ("-") en telt niet mee in het clustertotaal.

Gebruik:
    python3 scripts/volumes_in_clusters.py                       # alle bestanden in data/keyword-planner/
    python3 scripts/volumes_in_clusters.py data/keyword-planner/2026-10-25-invoerlijst.json
    python3 scripts/volumes_in_clusters.py --uitvoer marketing/zoekwoorden/volumes-clusters-2026-10-25.md
    python3 scripts/volumes_in_clusters.py --clusters pad/naar/clusters.md --maanden 3

Bij meerdere bestanden wint per zoekwoord het nieuwste bestand, en een bestand met actie
volumes gaat voor een bestand met actie ideeen. Alleen lezen; schrijft alleen naar --uitvoer.
"""
import argparse
import collections
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KP = ROOT + "/data/keyword-planner/"
CLUSTERS_MD = ROOT + "/marketing/zoekwoorden/clusters-2026-10-21.md"
LOKAAL = "Lokaal: Borne, Twente en omgeving"
LOKAAL_DOELPAGINA = "/pages/theewinkel-borne-twente"
MAANDEN = {m: i + 1 for i, m in enumerate(
    "JANUARY FEBRUARY MARCH APRIL MAY JUNE JULY AUGUST SEPTEMBER OCTOBER NOVEMBER DECEMBER".split())}
MAAND_NL = ["", "januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus",
            "september", "oktober", "november", "december"]
PIEK_DREMPEL = 1.25  # een maand is piek bij minstens 125% van het gemiddelde


def nl(x, dec=0):
    s = f"{x:,.{dec}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def getal(tekst):
    """Nederlands getal ('1.934', '19,8', '0,72%') naar float; '-' of leeg naar None."""
    t = tekst.strip().replace("%", "").replace("(schatting)", "").strip()
    if not t or t == "-":
        return None
    try:
        return float(t.replace(".", "").replace(",", "."))
    except ValueError:
        return None


def rijen(regel):
    return [c.strip() for c in regel.strip().strip("|").split("|")]


def lees_clusters(pad):
    """Geeft (clusters, lokaal). clusters: naam -> {vert, klikken, pos, pagina, zoekwoorden[]}."""
    clusters = collections.OrderedDict()
    lokaal = []
    sectie = bijlage = None
    for regel in open(pad, encoding="utf-8"):
        regel = regel.rstrip("\n")
        if regel.startswith("## "):
            sectie, bijlage = regel[3:].strip(), None
            continue
        if regel.startswith("### "):
            bijlage = regel[4:].strip()
            continue
        if not regel.startswith("|") or set(regel) <= set("|-: "):
            continue
        c = rijen(regel)
        if sectie == "Clusters" and len(c) >= 10 and c[0] != "Cluster":
            clusters[c[0]] = {"vert": getal(c[4]) or 0, "klikken": getal(c[5]) or 0, "pos": getal(c[6]),
                              "pagina": c[8], "zoekwoorden": []}
        elif sectie and sectie.startswith("Bijlage") and bijlage and len(c) == 5 and c[0] != "Zoekwoord":
            if bijlage in clusters:
                clusters[bijlage]["zoekwoorden"].append(
                    {"zoekwoord": c[0], "vert": getal(c[1]) or 0, "klikken": getal(c[2]) or 0, "pos": getal(c[3])})
        elif sectie and sectie.startswith("Lokale zoektermen") and len(c) >= 6 and c[0] != "Zoekwoord":
            if c[6:7] and c[6].startswith("Irrelevant"):
                continue
            lokaal.append({"zoekwoord": c[0], "vert": getal(c[2]) or 0, "klikken": getal(c[3]) or 0, "pos": getal(c[4])})
    if lokaal:
        clusters[LOKAAL] = {"vert": sum(z["vert"] for z in lokaal), "klikken": sum(z["klikken"] for z in lokaal),
                            "pos": None, "pagina": LOKAAL_DOELPAGINA, "zoekwoorden": lokaal}
    return clusters


def lees_volumes(paden):
    """Geeft (volumes, bronnen). volumes: zoekwoord (kleine letters) -> {volume, per_maand, concurrentie}."""
    bestanden = []
    for p in paden:
        d = json.load(open(p, encoding="utf-8"))
        bestanden.append((d.get("actie") == "volumes", d.get("gemaakt", ""), os.path.basename(p), p, d))
    bestanden.sort(key=lambda x: x[:3])  # latere items overschrijven eerdere
    vol = {}
    for _, _, _, p, d in bestanden:
        for r in d.get("resultaten", []):
            sleutel = r["zoekwoord"].strip().lower()
            pm = {}
            for m in r.get("per_maand") or []:
                if m.get("maand") in MAANDEN and m.get("volume") is not None:
                    pm[(m["jaar"], MAANDEN[m["maand"]])] = m["volume"]
            nieuw = {"volume": r.get("volume"), "per_maand": pm, "concurrentie": r.get("concurrentie", "")}
            if sleutel in vol and not pm and vol[sleutel]["per_maand"]:
                nieuw["per_maand"] = vol[sleutel]["per_maand"]  # ideeen-bestand wist geen maandcijfers
            vol[sleutel] = nieuw
    return vol, [b[3] for b in bestanden]


def seizoen(zoekwoorden, vol):
    """Som per kalendermaand over zoekwoorden met per_maand. Geeft (reeks, gemiddelde, pieken, n)."""
    som = collections.defaultdict(int)
    n = 0
    for z in zoekwoorden:
        v = vol.get(z["zoekwoord"].lower())
        if v and v["per_maand"]:
            n += 1
            for k, x in v["per_maand"].items():
                som[k] += x
    if not som:
        return [], 0, [], 0
    reeks = sorted(som.items())
    gem = sum(x for _, x in reeks) / len(reeks)
    pieken = [(k, x) for k, x in sorted(reeks, key=lambda t: -t[1]) if gem and x >= PIEK_DREMPEL * gem]
    return reeks, gem, pieken, n


def maandnaam(k):
    return f"{MAAND_NL[k[1]]} {k[0]}"


def seizoentekst(reeks, gem, pieken, n, totaal):
    if not reeks:
        return "geen maandcijfers in de bestanden"
    if len(reeks) < 12:
        deel = f"let op: maar {len(reeks)} maanden beschikbaar. "
    else:
        deel = ""
    if not pieken:
        t = f"geen duidelijke piek (geen maand boven {nl(PIEK_DREMPEL * 100)}% van het gemiddelde)"
    else:
        t = "piek in " + ", ".join(f"{maandnaam(k)} ({nl(x)}, {nl(100 * x / gem)}% van gemiddeld)" for k, x in pieken[:3])
    return f"{deel}{t}; gemiddeld {nl(gem)} per maand, op basis van {n} van {totaal} zoekwoorden"


def rapport(clusters, vol, bronnen, maanden):
    uit = []
    p = uit.append
    p("# Zoekvolumes per cluster\n")
    p("Gegenereerd door scripts/volumes_in_clusters.py. Volumes: Google Keyword Planner via scripts/zoekvolumes.py "
      "(Nederlands, Nederland). Vertoningen, klikken en posities: Search Console, 90 dagen, uit de clustertabellen. "
      "Een zoekwoord zonder volume in de bestanden blijft leeg en telt niet mee.\n")
    p("Bronbestanden: " + ", ".join(os.path.relpath(b, ROOT) for b in bronnen) + "\n")
    p("Leeswijzer:\n")
    p(f"- Vert./maand is het 90-daagse aantal vertoningen gedeeld door {nl(maanden)}.")
    p("- Aandeel zichtbaarheid is vert./maand gedeeld door het maandvolume van hetzelfde zoekwoord. "
      "Een hoog aandeel op een lage positie betekent dat de pagina al vaak getoond wordt; een laag aandeel "
      "op een goede positie wijst op weinig vertoningen ten opzichte van de vraag.")
    p("- De bijlage in het clusterrapport bevat alleen de top zoekwoorden per cluster, dus de som van de "
      "zoekwoorden is lager dan het clustertotaal in de tabel Clusters.")
    p("- Keyword Planner voegt dicht bij elkaar liggende varianten samen (bijvoorbeeld ricedk en rice dk). "
      "Dezelfde zoekers kunnen dan in meer dan een regel zitten, waardoor het clustertotaal te hoog kan uitvallen. "
      "Het totaal is dus een bovengrens, geen exacte som.\n")

    p("## Overzicht\n")
    p("| Cluster | Doelpagina | Zoekwoorden met volume | Volume/maand (som) | Vert./maand (zoekwoorden met volume) | Aandeel zichtbaarheid | Vert. 90d (heel cluster) | Pos. cluster |")
    p("|---|---|---:|---:|---:|---:|---:|---:|")
    details = []
    for naam, c in clusters.items():
        met = [(z, vol.get(z["zoekwoord"].lower())) for z in c["zoekwoorden"]]
        met = [(z, v) for z, v in met if v and v["volume"] is not None]
        som = sum(v["volume"] for _, v in met)
        vm = sum(z["vert"] for z, _ in met) / maanden
        aandeel = f"{nl(100 * vm / som)}%" if som else "-"
        p(f"| {naam} | {c['pagina']} | {len(met)} van {len(c['zoekwoorden'])} | {nl(som) if met else '-'} | "
          f"{nl(vm) if met else '-'} | {aandeel} | {nl(c['vert'])} | {nl(c['pos'], 1) if c['pos'] else '-'} |")
        details.append((naam, c, met, som, vm))

    p("\n## Per cluster\n")
    for naam, c, met, som, vm in details:
        p(f"### {naam}\n")
        p(f"Doelpagina: {c['pagina']}. Cluster in Search Console: {nl(c['vert'])} vertoningen, "
          f"{nl(c['klikken'])} klikken in 90 dagen" + (f", gemiddelde positie {nl(c['pos'], 1)}" if c["pos"] else "") + ".\n")
        p("| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |")
        p("|---|---:|---|---:|---:|---:|---:|---:|---:|")
        for z in sorted(c["zoekwoorden"], key=lambda z: -((vol.get(z["zoekwoord"].lower()) or {}).get("volume") or 0)):
            v = vol.get(z["zoekwoord"].lower())
            vm_z = z["vert"] / maanden
            if v and v["volume"] is not None:
                aand = f"{nl(100 * vm_z / v['volume'])}%" if v["volume"] else "-"
                onbenut = nl(max(0, v["volume"] - vm_z))
                p(f"| {z['zoekwoord']} | {nl(v['volume'])} | {v['concurrentie'] or '-'} | {nl(z['vert'])} | {nl(vm_z, 1)} | "
                  f"{nl(z['pos'], 1) if z['pos'] else '-'} | {nl(z['klikken'])} | {aand} | {onbenut} |")
            else:
                p(f"| {z['zoekwoord']} | - | - | {nl(z['vert'])} | {nl(vm_z, 1)} | "
                  f"{nl(z['pos'], 1) if z['pos'] else '-'} | {nl(z['klikken'])} | - | - |")
        p("")
        if met:
            p(f"Totaal zoekvolume: {nl(som)} per maand over {len(met)} van {len(c['zoekwoorden'])} zoekwoorden "
              f"(bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: {nl(vm, 1)} per maand, "
              f"aandeel zichtbaarheid {nl(100 * vm / som) if som else '-'}%.\n")
        else:
            p("Geen zoekwoord van dit cluster staat in de volumebestanden; het volume is onbekend.\n")
        reeks, gem, pieken, n = seizoen(c["zoekwoorden"], vol)
        p(f"Seizoen: {seizoentekst(reeks, gem, pieken, n, len(c['zoekwoorden']))}.\n")
        if reeks:
            p("| Maand | " + " | ".join(maandnaam(k) for k, _ in reeks) + " |")
            p("|---|" + "---:|" * len(reeks))
            p("| Volume (som) | " + " | ".join(nl(x) for _, x in reeks) + " |\n")

    bekend = {z["zoekwoord"].lower() for c in clusters.values() for z in c["zoekwoorden"]}
    rest = sorted(((k, v) for k, v in vol.items() if k not in bekend and v["volume"] is not None),
                  key=lambda t: -t[1]["volume"])
    if rest:
        p("## Zoekwoorden met volume die in geen cluster staan\n")
        p("Bijvoorbeeld uit de actie ideeen of uit zoekwoorden buiten de bijlage. Mogelijke nieuwe clusters of ondersteunende zoekwoorden; "
          "indelen vraagt een beslissing van de zoekwoordonderzoeker.\n")
        p("| Zoekwoord | Volume/maand | Concurrentie |")
        p("|---|---:|---|")
        for k, v in rest[:40]:
            p(f"| {k} | {nl(v['volume'])} | {v['concurrentie'] or '-'} |")
        if len(rest) > 40:
            p(f"\nEn {len(rest) - 40} zoekwoorden met een lager volume; zie het JSON-bestand.")
        p("")
    return "\n".join(uit)


def main():
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    a.add_argument("bestanden", nargs="*", help="uitvoer van zoekvolumes.py (standaard alle json in data/keyword-planner/)")
    a.add_argument("--clusters", default=CLUSTERS_MD, help="clusterrapport in markdown")
    a.add_argument("--uitvoer", help="schrijf naar dit bestand in plaats van stdout")
    a.add_argument("--maanden", type=float, default=3.0, help="aantal maanden in de Search Console-periode (standaard 3 voor 90 dagen)")
    a = a.parse_args()
    paden = a.bestanden or sorted(glob.glob(KP + "*.json"))
    if not paden:
        sys.exit("Geen bestanden in data/keyword-planner/. Draai eerst scripts/zoekvolumes.py volumes --bestand ...")
    clusters = lees_clusters(a.clusters)
    if not clusters:
        sys.exit("Geen clustertabellen gevonden in " + a.clusters)
    vol, bronnen = lees_volumes(paden)
    tekst = rapport(clusters, vol, bronnen, a.maanden)
    if a.uitvoer:
        with open(a.uitvoer, "w", encoding="utf-8") as f:
            f.write(tekst + "\n")
        print("opgeslagen:", a.uitvoer, file=sys.stderr)
    else:
        print(tekst)
    niet = [z["zoekwoord"] for c in clusters.values() for z in c["zoekwoorden"] if z["zoekwoord"].lower() not in vol]
    if niet:
        print(f"{len(niet)} zoekwoorden uit de clusters hebben geen volume in de bestanden.", file=sys.stderr)


if __name__ == "__main__":
    main()
