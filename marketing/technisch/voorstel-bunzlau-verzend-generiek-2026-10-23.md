# Voorstel: Bunzlau-verzendsjabloon generiek maken (V61, optie B)

Datum: 2026-10-23. Status: preview klaar, wacht op akkoord van Mark. Niets gepubliceerd, geen productdata gewijzigd.

## Thema
- Bron: live thema #203153015048 (Agent-ready koppen 2026-10-09), gepulld.
- Nieuw, ongepubliceerd thema: **bunzlau-verzend-generiek 2026-10-23**, id **#204013568264**.
- Gewijzigd bestand: `sections/tr-product-bunzlau-melamine.liquid` (de template `product.bunzlau-melamine` blijft ongewijzigd).
- Diff: `marketing/technisch/voorstel-bunzlau-verzend-generiek-2026-10-23.diff`

## Wat verandert
- Tagline: type Melamine blijft "Melamine servies van Bunzlau Castle"; ander type wordt "{type} van Bunzlau Castle"; leeg type wordt "Bunzlau Castle".
- Materiaal-pill en tabelrij "Materiaal": alleen bij type Melamine. Bij andere types verdwijnen ze; er wordt geen ander materiaal verzonnen.
- Fallback-omschrijving: "Bunzlau Castle bij Tante Rie in Borne." zonder het woord melamine als het type geen Melamine is.
- Verder gecontroleerd: de sectie en het snippet tr-product-schema bevatten geen andere melamine-specifieke tekst of schema. De type-tag en het type-label in de galerij gebruikten al het producttype.

## Preview-links
Werkt met cookie-opslag (de redirect zet het preview-cookie; `curl -L -c jar -b jar`):
- https://tanterie.nl/products/servetten-garden-delight?view=bunzlau-melamine&preview_theme_id=204013568264
- https://tanterie.nl/products/bewaarblik-rechthoekig-flowerbed-19x15-cm?view=bunzlau-melamine&preview_theme_id=204013568264
- https://tanterie.nl/products/theemuts-streep?view=bunzlau-melamine&preview_theme_id=204013568264
- https://tanterie.nl/products/theemuts-ruit?view=bunzlau-melamine&preview_theme_id=204013568264
- https://tanterie.nl/products/melamine-bord-wild-flowers-o-25-cm?view=bunzlau-melamine&preview_theme_id=204013568264

## Controle op de preview (curl)
| Product | Type nu | Tagline | "Melamine" in tekst | Materiaal | Alleen afhalen / versturen we niet | shippingRate | Liquid-fouten |
|---|---|---|---|---|---|---|---|
| servetten-garden-delight | Servetten | Servetten van Bunzlau Castle | nee | nee | nee | 6,95 | geen |
| bewaarblik-rechthoekig-flowerbed-19x15-cm | Koekblik | Koekblik van Bunzlau Castle | nee | nee | nee | 6,95 | geen |
| theemuts-streep | leeg | Bunzlau Castle | nee | nee | nee | 6,95 | geen |
| theemuts-ruit | Keramiek | Keramiek van Bunzlau Castle | nee | nee | nee | 6,95 | geen |
| melamine-bord-wild-flowers-o-25-cm | Melamine | Melamine servies van Bunzlau Castle | ja, als live | ja (pill en tabel) | nee | 6,95 | geen |

- "Melamine" komt bij de vier verzendproducten alleen nog voor in technische strings (URL-parameter `view=bunzlau-melamine`, templatenaam), niet in zichtbare tekst.
- Melamine-bord: zichtbare tekst identiek aan live (3315 tekens, gelijk) en de markup van de productsectie is na whitespace-normalisatie byte-gelijk aan live. De andere 6 melamineproducten gebruiken dezelfde code en hetzelfde type; niet apart gecurld.
- JSON-LD op alle vijf pagina's geldig (4 blokken: WebSite, LocalBusiness, BreadcrumbList, Product). Product heeft merk Bunzlau Castle, InStock en shippingRate 6,95 (tag pakket).
- Rich Results Test en nieuwe crawl: pas na publicatie zinvol; niet uitgevoerd op de preview.

## Voorgestelde producttypes (NIET gezet in Shopify)
| Product | Nu | Voorstel | Tagline daarna |
|---|---|---|---|
| theemuts-streep | leeg | Theemuts | Theemuts van Bunzlau Castle |
| theemuts-ruit | Keramiek (fout) | Theemuts | Theemuts van Bunzlau Castle |
| servetten-garden-delight | Servetten | Servetten (ongewijzigd) | Servetten van Bunzlau Castle |
| bewaarblik-rechthoekig-flowerbed-19x15-cm | Koekblik | Bewaarblik | Bewaarblik van Bunzlau Castle |

Opmerking bij het blik: de producttitel zegt "Bewaarblik"; "Koekblik" mag ook, maar "Bewaarblik" past bij de titel en bij wat zoekers typen. Let op: als het type in collectiefilters of vaste regels voor andere producten wordt gebruikt, eerst nagaan of "Koekblik" daar al in zit.

## Aandachtspunten
- Nu (zonder typewijziging) zou theemuts-ruit "Keramiek van Bunzlau Castle" tonen en theemuts-streep alleen "Bunzlau Castle". Zet de types dus in dezelfde stap als het sjabloon wisselt.
- De tags "handgemaakt" en "keramiek" (V59) tonen in dit sjabloon nog het label "Handgemaakt". Die tags verwijderen blijft een aparte stap uit V59.
- Het product bunzlau-textiel (zonder foto, fout op de pagina) valt buiten dit voorstel.

## Volgende stappen na akkoord
1. Producttypes zetten (4 producten) en sjabloon van de 4 producten wisselen naar `bunzlau-melamine` (V59).
2. Thema #204013568264 publiceren, of alleen het sectiebestand overnemen in het live thema (kleiner risico, eigen diff).
3. Rich Results Test en nieuwe crawl op de 4 URL's, daarna changelog.
