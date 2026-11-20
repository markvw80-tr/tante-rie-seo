# SEO-maandrapport november 2026

Opgesteld 20-11-2026 door de analist. Venster: 21-10 t/m 17-11 (28 dagen, laatste dag met data in Search Console) tegen 23-09 t/m 20-10 (28 dagen). Vergelijking met dezelfde periode vorig jaar is niet gemaakt: de shop draait pas sinds juli 2026 op tanterie.nl.

**Wat ging goed:** klikken zijn met 16 procent gestegen (389 naar 452) en de CTR is van 2,16 naar 3,08 procent gegaan. **Wat niet:** de vertoningen zijn 19 procent lager en het winkeldeel (theewinkelpagina en contact) levert met 3 klikken op 772 vertoningen vrijwel niets, terwijl dat 70 procent van de prioriteit is. **Wat stellen we voor:** de effectbeoordeling op 25-11 afwachten, het winkeldeel via titel en meta van de theewinkelpagina en het Bedrijfsprofiel aanpakken, en drie open besluiten van Mark (V133, V134, alt-regels) afhandelen.

## 1. Kerncijfers Search Console

Bron: gsc_query.py, sc-domain:tanterie.nl, web, date-dimensie; ruwe uitkomst data/gsc/2026-11-20-maandrapport.json.

| Maat | 21-10 t/m 17-11 | 23-09 t/m 20-10 | Verschil |
|---|---|---|---|
| Klikken | 452 | 389 | +63 (+16,2%) |
| Vertoningen | 14.670 | 18.036 | -3.366 (-18,7%) |
| CTR | 3,08% | 2,16% | +0,92 procentpunt |
| Gemiddelde positie | 10,1 | 26,1 | 16,0 beter |

Lees de positie voorzichtig. Het gemiddelde wordt gewogen op vertoningen, en de homepage had vorige periode 11.476 vertoningen en nu 4.810 (pagina-export). Een deel van de verbetering komt dus doordat vertoningen op ver weg gelegen posities verdwenen zijn, niet alleen doordat pagina's hoger staan. Een eerlijke oorzaak is uit deze cijfers niet te halen. Organisch verkeer in GA4 (data/ga4/2026-11-18-maandrapport-organic-28d.json en -56d.json): 357 sessies tegen 312 in de periode ervoor (56 dagen min 28 dagen), +14 procent.

Top 10 pagina's op klikken (pagina-export, zelfde venster; de som van de pagina's is 462 klikken, iets meer dan het datatotaal van 452, een bekend aggregatieverschil):

| Pagina | Klikken | Vertoningen | Positie | Klikken vorige periode |
|---|---|---|---|---|
| / | 288 | 4.810 | 5,9 | 256 |
| /collections/bunzlau | 26 | 2.200 | 14,3 | 19 |
| /pages/serviezen | 13 | 487 | 2,5 | 7 |
| /products/rice-q | 10 | 56 | 4,6 | 2 |
| /pages/thee-en-koffie | 9 | 455 | 3,0 | 7 |
| /collections/blond | 7 | 1.060 | 7,1 | 4 |
| /collections/joeff | 7 | 702 | 7,3 | 16 |
| /collections/rice | 7 | 494 | 14,3 | 2 |
| /collections/thee-bewaarblikken | 7 | 376 | 19,6 | 4 |
| /collections/rooibos | 4 | 38 | 13,9 | 0 |

## 2. Winkel Borne versus webshop

Indeling op pad, uit dezelfde pagina-export (klikken nu / vorige periode): winkel en lokaal (/pages/theewinkel-borne-twente en /pages/contact) 3 / 6 klikken op 772 / 784 vertoningen; webshop (/products en /collections) 134 / 103 klikken op 10.412 / 6.985 vertoningen; homepage 288 / 256; overige pagina's 37 / 31. De groei zit dus in de webshop. Het winkeldeel staat stil. Niet beoordeeld: merk tegenover niet-merk, kassaomzet, Shopify-omzet en Bedrijfsprofiel-acties. De Shopify-analytics zijn voor dit rapport niet opgehaald en de Bedrijfsprofielbestanden van 18-11 (data/gbp/) waren niet leesbaar; geen cijfer is daarom geschat.

## 3. Doorgevoerd en effect

Bron: marketing/changelog.md (bovenste 30 regels), effect-design-2026-11-15.md, migratiemonitor-2026-11-16.md.

- Designrondes 1 t/m 4 (live 28-10): tussenstand 15-11 liet 226 naar 240 klikken zien in 15 dagen, binnen de normale schommeling. Geen aantoonbaar effect; officiële beoordeling 25-11.
- Alt-teksten 52 losse theeën (28-10): nog geen vier weken, te vroeg om te oordelen.
- Bunzlau-collectie en 69 vaatwassertags (24-10): /collections/bunzlau steeg van 19 naar 26 klikken en van 1.343 naar 2.200 vertoningen. Dat past bij de wijziging, maar met deze aantallen is causaliteit niet aan te tonen; vier weken vol op 21-11.
- Bedrijfsprofiel (attributen, openingstijden 15-11, eerste bericht 18-11): te recent, geen oordeel.
- Migratie naar tanterie.nl: 99,8 procent van de homepagevertoningen op https://tanterie.nl/ in de monitor van 16-11; migratie grotendeels rond.
- 19-11: 15 alt-regels naar PIM gestuurd; er is nog niets live gewijzigd, dus niets te meten.

## 4. Open bij Mark

- V134 (marketing/vragen-voor-mark.md): eenheidsprijs losse thee, keuze A laten zoals het is of B vullen bij alle varianten. Advies SEO: B, lage prioriteit. V127 (Merchant Center-regel) vervalt bij A en is volgens SEO niet nodig.
- V133: handle van de Passionfruit Martini Cake aanpassen met 301-omleiding. Geen klikken, 5 vertoningen; lage urgentie.
- Alt-diff bij PIM (bericht seo-2026-11-19-1): PIM voert pas door na de diff en akkoord van Mark.

## 5. Drie aanbevelingen voor de SEO Lead

1. Beoordeel op 25-11 designrondes, alt-teksten en Bunzlau met minstens 28 dagen data, en schrijf per wijziging op of het effect aantoonbaar is.
2. Geef het winkeldeel voorrang: On-page herziet titel en meta van /pages/theewinkel-borne-twente (3 klikken op 772 vertoningen) en Lokaal bewaakt het berichtenschema van het Bedrijfsprofiel (24-11, 1-12, 8-12).
3. Leg V133, V134 en de alt-diff voor aan Mark, en voeg bij het volgende rapport Shopify-sessies en -omzet, merk tegenover niet-merk en leesbare Bedrijfsprofieldata toe.
