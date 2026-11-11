# Meetkalender november en december 2026

Bron: marketing/plan-2026-11.md (sectie "Metingen die Mark lokaal moet draaien" en de weekplanning) en team/status.md in tante-rie-hq. Opgesteld op 7 november 2026. Wijzigt het plan, dan geldt het plan.

## Komende dagen

| Datum | Wat | Hoe |
|---|---|---|
| Maandag 9 nov (gedaan, rapport migratiemonitor-2026-11-09.md), daarna 16, 23 en 30 nov en 7 dec | Migratiemonitor en profielcijfers (wekelijks, elke maandag) | `python3 gsc_query.py --days 7 --dimensions query,page --limit 1000 --json` en `scripts/gbp_prestaties.py` |
| 11 nov | Eerste meting effect designrondes (beter 25 nov) | GSC en GA4 per apparaat |
| 11 nov (gedaan) | Merchant-check eenheidsprijs kamille en gemberwortel: nog leeg, zie V127; herhalen zodra Mark de regel heeft gemaakt | Merchant API, alleen lezen |
| Uiterlijk 13 nov | Bewaarblikken live, direct nulwaarden per pagina | `python3 gsc_query.py --days 28 --dimensions query,page --limit 1000 --json` |
| Uiterlijk 14 nov | Bunzlau live, nulwaarden op de livedag | idem |

## Daarna

| Datum | Wat |
|---|---|
| 18 nov | Schemacontrole in Search Console (rapporten Producten en Merchant listings) |
| 18 tot 21 nov | Maandrapport: GSC 28 dagen (ook per apparaat), GA4 (`python3 ga4_report.py --property properties/521523059 --json`), Shopify-sessies en -bestellingen |
| Rond 19 nov | 28-dagenmeting bewaarblikken (title van 22 okt) |
| Uiterlijk 20 nov | Cadeaupagina live, nulwaarden |
| 21 nov | Maandrapport met oordeel per actie uit maand 1 |
| 24 nov, 1, 8 en 15 dec | Vier weekmonitors: niet-merkmaat, Google-sessies en online bestellingen uit Shopify, profielklikken via UTM, Zoeken mobiel in het profiel |
| 25 nov | Beter moment voor het effect van de designrondes |
| 1 dec | Eenheidsprijs en gratis vermeldingen in Merchant Center (Producten, diagnose) |
| 5 tot 11 dec | Eerste meting Bunzlau en bewaarblikken |
| 12 en 26 dec | Latere metingen Bunzlau |
| 19 tot 21 dec | Maandrapport december en plan-2026-12 |

## Vervallen of afgerond

| Wat | Stand |
|---|---|
| Indexeringsrapport 5xx (was uiterlijk 24 nov) | Afgerond 25 okt: het ging om een kassa-artikel dat niet online hoort |
| Eenheidsprijs en gratis vermeldingen, eerste meting rond 25 okt | Voorbij; niet vastgesteld of die is gedaan |

## Bij Mark (lokaal, met eigen inlog)

- De commando's uit de tabellen, vanwege credentials.
- Rich Results Test.
- Chrome UX Report API inschakelen in Google Cloud (project tante-rie), vanwege de 403 op CrUX.

Ruwe uitvoer gaat naar `data/gsc/` als JJJJ-MM-DD-onderwerp.json.
