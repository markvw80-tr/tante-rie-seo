# Nulmeting SEO Tante Rie, oktober 2026

Opgesteld door de Analist op 21 oktober 2026. Alleen gelezen en gerapporteerd: er is niets gewijzigd in Shopify, het thema of changelog.md.

## Samenvatting in drie zinnen

Wat ging goed: het merkverkeer is stabiel (172 klikken op 337 vertoningen, vorige periode 151 klikken) en het aandeel van https://tanterie.nl/ in de homepagevertoningen steeg van 39,4 naar 77,7 procent. Wat niet: de klikken uit zoekopdrachten zonder merknaam daalden van 48 naar 40, terwijl de vertoningen daarvan bijna verdubbelden (5.950 naar 11.570) en de gemiddelde positie van 21,7 naar 34,2 zakte; ook staat het homepage-klikaandeel op https://tanterie.nl/ pas op 36,1 procent en kregen /pages/zakelijk en /pages/blond-amsterdam-servies in deze periode bijna geen vertoningen meer. Wat stellen we voor: de homepage ongemoeid laten tot de migratiemonitor twee weken op minstens 90 procent staat, de vertoningsval op twee doelpagina's laten controleren door Technisch SEO, en de nulwaarden in het plan vervangen door de 28-dagenwaarden uit dit rapport.

## Wat deze nulmeting is

Deze nulmeting beschrijft de situatie voor de schema-livegang van 21 oktober 2026 (changelog: productschema met shippingDetails en hasMerchantReturnPolicy, verzendtarief per gewichtsklasse, levertijd, en de srcset-wijziging voor snelheid). Het meetvenster eindigt op 19 oktober 2026 en ligt dus volledig voor die wijziging. Effecten van die wijziging kunnen pas vanaf de monitorrapporten en het maandrapport van 21 november worden beoordeeld, en pas na minimaal vier weken.

Venster en bronnen:

| Onderdeel | Waarde |
|---|---|
| Venster | 22 september tot en met 19 oktober 2026 (28 dagen) |
| Waarom niet tot 20 oktober | De date-dimensie geeft voor 20 en 21 oktober nog geen rijen; 19 oktober is de laatste dag met data (453 vertoningen, 16 klikken). Search Console loopt dus ruim twee dagen achter |
| Vorige maand | 25 augustus tot en met 21 september 2026 (de 28 dagen daarvoor) |
| Zelfde periode 2025 | Niet beschikbaar. De property sc-domain:tanterie.nl geeft voor 22 september tot en met 19 oktober 2025 nul rijen terug; de oudste dag met data in de property is 24 januari 2026. Er is dus ook geen optelling van webshop.tanterie.nl en tanterie.nl voor 2025 mogelijk. webshop.tanterie.nl staat niet als aparte property in de lijst van sites |
| Bron | Search Console, property sc-domain:tanterie.nl, via gsc_query.py. Ruwe exports: data/gsc/2026-10-21-nulmeting-<periode>-<dimensie>.json |
| Normalisatie | http, www en webshop samengevoegd tot het pad op tanterie.nl, queryparameters gestript (parameter-URL's apart geteld waar het ertoe doet) |

Beperkingen die bij alle cijfers horen. Het totaal komt uit de date-dimensie (387 klikken, 18.283 vertoningen). De som van de pagina-export is iets hoger (394 klikken), een bekend verschil in Search Console tussen aggregatieniveaus. De zoekopdrachtexport dekt 212 klikken (55 procent) en 13.023 vertoningen (71 procent) van het totaal; de rest zit in zoekopdrachten die Google niet toont. Alle verhoudingen tussen merk en niet-merk gelden dus voor de zichtbare zoekopdrachten. Posities zijn gemiddelden gewogen op vertoningen. Bij pagina's met tientallen vertoningen is een positie of CTR een momentopname en geen trend.

## Totaal

| Maat | 22 sep - 19 okt 2026 | 25 aug - 21 sep 2026 | Verschil |
|---|---:|---:|---:|
| Klikken | 387 | 402 | -4% |
| Vertoningen | 18.283 | 13.355 | +37% |
| CTR | 2,12% | 3,01% | - |
| Gemiddelde positie | 26,4 | 14,9 | - |

Klikken liggen vrijwel gelijk, vertoningen zijn met 37 procent gestegen en de gemiddelde positie is van 14,9 naar 26,4 gegaan. Het gemiddelde zakt omdat er vertoningen bij zijn gekomen op posities ver buiten de top 20, vooral op de homepage (zie hieronder); een verband met een oorzaak is hiermee niet vastgesteld.

Per week (klikken, vertoningen): 22 tot 28 september 96 en 4.687; 29 september tot 5 oktober 114 en 4.288; 6 tot 12 oktober 75 en 5.709; 13 tot 19 oktober 102 en 3.599. De vorige periode lag per week tussen 2.731 en 4.048 vertoningen en tussen 96 en 104 klikken.

## Merk tegenover niet-merk

Regels zoals in het clusterrapport (zoekwoord_clusters.py): merk is Tante Rie en schrijfwijzen, 'vermoedelijk merk' (tante, tantes servies) staat apart, 'rie' los is RI&E (risico-inventarisatie) en telt niet als merk, andere 'tante'-zoekopdrachten en spam staan apart. Parameter-URL's zijn in de zoekopdracht-export niet te scheiden; zij zijn apart geteld op paginaniveau (43 parameter-rijen, 5 klikken, 73 vertoningen; vorige periode 67 rijen, 14 klikken, 107 vertoningen).

| Groep | Klik | Vert | CTR | Pos | Klik vm | Vert vm | CTR vm | Pos vm |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Merk | 172 | 337 | 51,04% | 1,6 | 151 | 300 | 50,33% | 1,5 |
| Vermoedelijk merk | 0 | 51 | 0,00% | 16,6 | 0 | 70 | 0,00% | 17,2 |
| Non-brand | 40 | 11.570 | 0,35% | 34,2 | 48 | 5.950 | 0,81% | 21,7 |
| RI&E ('rie' los) | 0 | 831 | 0,00% | 44,7 | 0 | 594 | 0,00% | 32,5 |
| Andere 'tante' | 0 | 213 | 0,00% | 36,9 | 0 | 42 | 0,00% | 53,7 |
| Spam | 0 | 21 | 0,00% | 34,0 | 0 | 0 | - | 0,0 |
| Samen met zoekopdracht | 212 | 13.023 | 1,63% | 34,0 | 199 | 6.956 | 2,86% | 21,9 |

Kolommen met 'vm' zijn de vorige periode (25 augustus tot en met 21 september). Van de 212 klikken met bekende zoekopdracht komen er 172 (81 procent) uit merkzoekopdrachten. Niet-merk geeft 40 klikken op 11.570 vertoningen, een CTR van 0,35 procent. In de vorige periode was dat 48 klikken op 5.950 vertoningen, 0,81 procent. De RI&E-zoekopdrachten brengen 831 vertoningen en geen klik.

## Per apparaat

| Apparaat | Klik | Vert | CTR | Pos | Klik vm | Vert vm | CTR vm | Pos vm |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Mobile | 277 | 7.743 | 3,58% | 16,0 | 300 | 8.015 | 3,74% | 9,5 |
| Desktop | 100 | 10.286 | 0,97% | 34,3 | 88 | 5.139 | 1,71% | 23,6 |
| Tablet | 10 | 254 | 3,94% | 25,8 | 14 | 201 | 6,97% | 7,6 |

Mobiel levert 277 van de 387 klikken (71,6 procent), desktop 100 en tablet 10. Op desktop staan de meeste vertoningen (10.286) tegen een gemiddelde positie van 34,3.

Merk en niet-merk per apparaat (zichtbare zoekopdrachten):

| Groep | Apparaat | Klik | Vert | CTR |
|---|---:|---:|---:|---:|
| Merk | Mobile | 118 | 249 | 47,39% |
| Merk | Desktop | 51 | 83 | 61,45% |
| Merk | Tablet | 3 | 5 | 60,00% |
| Non-brand | Mobile | 30 | 3.275 | 0,92% |
| Non-brand | Desktop | 8 | 8.147 | 0,10% |
| Non-brand | Tablet | 2 | 148 | 1,35% |

## De homepage per URL-variant

| URL | Vert | Klik | Pos | Vert vm | Klik vm | Pos vm |
|---|---:|---:|---:|---:|---:|---:|
| http://www.tanterie.nl/ | 2.616 | 163 | 4,3 | 2.772 | 189 | 6,5 |
| https://www.tanterie.nl/ | 0 | 0 | - | 0 | 0 | - |
| http://tanterie.nl/ | 0 | 0 | - | 0 | 0 | - |
| https://tanterie.nl/ | 9.105 | 92 | 40,6 | 1.800 | 79 | 18,5 |
| http://webshop.tanterie.nl/ | 0 | 0 | - | 0 | 0 | - |
| https://webshop.tanterie.nl/ | 0 | 0 | - | 0 | 0 | - |

https://www.tanterie.nl/, http://tanterie.nl/ en webshop.tanterie.nl hadden in beide perioden geen homepagevertoningen. Homepage met parameters: geen rijen. Er staan in de pagina-export geen webshop-URL's meer.

Migratiemonitor-maatstaf, aandeel van https://tanterie.nl/ in de homepage:

| Periode | Vertoningen op https | Totaal homepage | Aandeel vertoningen | Klikken op https | Totaal homepage | Aandeel klikken |
|---|---:|---:|---:|---:|---:|---:|
| 22 sep tot en met 19 okt (nulmeting) | 9.105 | 11.721 | 77,7% | 92 | 255 | 36,1% |
| 25 aug tot en met 21 sep | 1.800 | 4.572 | 39,4% | 79 | 268 | 29,5% |
| Laatste 7 dagen (13 tot en met 19 okt, monitor) | 928 | 1.588 | 58,4% | 20 | 59 | 33,9% |
| 90 dagen, plan-2026-10 (23 juli tot 18 okt) | 12.635 | 20.770 | 60,8% | 247 | 790 | 31,3% |

De vier rijen lopen uiteen omdat de vensters verschillen; de weekmonitor gebruikt het venster van 7 dagen. De vertoningen op https://tanterie.nl/ zijn sterk gestegen (1.800 naar 9.105), maar op een gemiddelde positie van 40,6, terwijl http://www.tanterie.nl/ op positie 4,3 blijft staan en daar 163 van de 255 homepageklikken (64 procent) kreeg. De drempel van 90 procent voor vertoningen en klikken is voor beide maten nog niet gehaald.

## Per doelpagina (actie 2 tot en met 10)

Genormaliseerd naar tanterie.nl, parameters gestript. 'Param-vert' is het aantal vertoningen van parameter-URL's dat in de rij is opgeteld. Kolommen met 'vm' zijn de vorige periode. Posities onder de 50 vertoningen zijn indicatief.

| Actie | Pad | Klik | Vert | CTR | Pos | Klik vm | Vert vm | Pos vm | Param-vert |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | /collections/rice | 2 | 472 | 0,42% | 24,6 | 2 | 481 | 18,3 | 0 |
| 2 | /products/rice-j | 1 | 27 | 3,70% | 12,2 | 0 | 32 | 8,3 | 0 |
| 2 | /products/rice-a | 0 | 2 | 0,00% | 14,5 | 0 | 43 | 7,0 | 0 |
| 2 | /products/rice-r | 0 | 24 | 0,00% | 25,3 | 0 | 33 | 5,6 | 0 |
| 2 | /products/rice-l | 0 | 95 | 0,00% | 6,2 | 0 | 125 | 6,2 | 0 |
| 3 | /pages/theewinkel-borne-twente | 4 | 446 | 0,90% | 5,7 | 4 | 582 | 5,6 | 0 |
| 4 | /collections/joeff | 14 | 783 | 1,79% | 7,2 | 12 | 368 | 8,4 | 0 |
| 4 | /pages/muuss-van-joeff-de-wand-die-met-je-meebeweegt | 2 | 15 | 13,33% | 7,0 | 6 | 148 | 6,6 | 0 |
| 4 | /collections/nfc-natural-flower-cards | 2 | 60 | 3,33% | 6,6 | 1 | 101 | 7,1 | 0 |
| 4 | /collections/thee-bewaarblikken | 4 | 327 | 1,22% | 19,4 | 2 | 384 | 23,1 | 0 |
| 5 | /products/pineut-watertwist-carafe-strawberry-hibiscus | 0 | 12 | 0,00% | 13,9 | 0 | 21 | 8,3 | 0 |
| 5 | /products/pineut-watertwist-carafe-strawberry-hibiscus-kopie | 0 | 4 | 0,00% | 11,5 | 0 | 9 | 10,9 | 0 |
| 5 | /products/pineut-watertwist-carafe-citrus-mint-verbena-kopie | 0 | 0 | - | - | 0 | 7 | 9,4 | 0 |
| 5 | /products/pineut-watertwist-carafe-iced-tea-mango-green-tea-kopie | 0 | 1 | 0,00% | 13,0 | 0 | 7 | 14,9 | 0 |
| 5 | /products/pineut-watertwist-carafe-sangria-red-wine-bio-kopie | 0 | 0 | - | - | 0 | 2 | 28,5 | 0 |
| 5 | /products/pineut-cake-pouchbag-lemon-poppy-cake | 0 | 4 | 0,00% | 8,7 | 0 | 2 | 7,0 | 1 |
| 5 | /products/pineut-cake-pouchbag-lemon-poppy-cake-kopie | 0 | 18 | 0,00% | 3,0 | 0 | 6 | 4,8 | 14 |
| 6 | /collections/bunzlau | 17 | 1.329 | 1,28% | 21,2 | 15 | 1.522 | 21,4 | 0 |
| 6 | /blogs/nieuws/een-kijkje-bij-bunzlau-nieuwe-seizoensfavorieten-en-een-leuk-nieuwtje | 0 | 18 | 0,00% | 5,9 | 1 | 43 | 8,9 | 0 |
| 6 | /pages/serviezen | 7 | 431 | 1,62% | 2,4 | 12 | 478 | 2,8 | 0 |
| 7 | /pages/blond-amsterdam-servies | 0 | 48 | 0,00% | 7,5 | 3 | 829 | 8,0 | 0 |
| 7 | /collections/blond | 3 | 305 | 0,98% | 9,0 | 3 | 270 | 7,9 | 0 |
| 8 | /products/earl-grey | 0 | 3 | 0,00% | 25,3 | 0 | 5 | 7,2 | 0 |
| 8 | /products/beste-van-borne | 0 | 6 | 0,00% | 6,7 | 1 | 26 | 6,7 | 0 |
| 9 | /pages/zakelijk | 0 | 0 | - | - | 0 | 484 | 37,5 | 0 |
| 10 | / | 255 | 11.721 | 2,18% | 32,5 | 268 | 4.572 | 11,2 | 0 |
| 10 | /collections/bunzlau | 17 | 1.329 | 1,28% | 21,2 | 15 | 1.522 | 21,4 | 0 |
| 10 | /products/earl-grey | 0 | 3 | 0,00% | 25,3 | 0 | 5 | 7,2 | 0 |

Actie 7 en 9 met zoveel mogelijk context: /pages/zakelijk had in de vorige periode 484 vertoningen op positie 37,5 en in de nulmeting geen enkele vertoning; /pages/blond-amsterdam-servies ging van 829 naar 48 vertoningen. Dit rapport stelt de oorzaak niet vast; zie aanbeveling 2.

Actie 8 (product-schema), nulwaarden uit Search Console: alle productpagina's samen hadden 339 paden met 56 klikken en 2.920 vertoningen (vorige periode 346 paden, 59 klikken, 3.668 vertoningen). De items in de rapporten Producten en Merchant listings (fout 'Duplicate field brand', waarschuwingen shippingDetails en hasMerchantReturnPolicy) zijn niet via de Search Console API op te halen; die aantallen moet de Technisch SEO-specialist uit de interface noteren. De controle-URL's /products/rice-j, /products/earl-grey en /products/beste-van-borne staan in de tabel hierboven; voor een accessoire, een bakmix en een Bunzlau-product noemt het plan geen vaste URL, dus daar is geen nulwaarde vastgelegd.

Actie 10 (snelheid), nulwaarden: Lighthouse mobiel uit het plan, homepage 61 (LCP 6,9 s, 3.293 KiB), bunzlau 68 (LCP 5,1 s, 2.531 KiB), earl-grey 60 (LCP 11,3 s, 3.150 KiB); die cijfers zijn niet opnieuw gemeten. Uit Search Console: mobiel is 71,6 procent van de klikken (277 van 387) en 42,4 procent van de vertoningen (7.743 van 18.283). Een uitsplitsing van apparaat per pagina is niet betrouwbaar uit te lezen (de export pagina plus apparaat geeft maar 215 van de 387 klikken terug) en staat daarom niet in dit rapport. Echte veldgegevens (CrUX) zijn er niet, want de CrUX API staat nog niet aan (beslissing 10).

## Per cluster

Clusters, regels en doelpagina's volgen het clusterrapport van 21 oktober (scripts/zoekwoord_clusters.py). Cluster-CTR en -positie zijn gewogen op vertoningen. 'Hoofdzoekwoord' geeft de vertoningen en positie in dit venster; bij hoofdzoekwoorden met weinig vertoningen is de positie een momentopname. Het clusterrapport rekent over 90 dagen; deze tabel over 28 dagen, dus de cijfers verschillen met opzet.

| Cluster | Klik | Vert | CTR | Pos | Hoofdzoekwoord | Klik vm | Vert vm | Pos vm |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Thee kopen en losse thee (hoofdzoekwoorden) | 3 | 1.796 | 0,17% | 45,1 | losse thee (178 vert, pos 43,8) | 1 | 151 | 24,4 |
| Kruidenthee (kamille, munt, gember, salie) | 1 | 1.161 | 0,09% | 45,4 | cactus thee (1 vert, pos 32,0) | 0 | 103 | 29,0 |
| Thee longtail: gezondheid, soorten en overig (informatief) | 0 | 1.072 | 0,00% | 41,3 | cafeïnevrije thee (66 vert, pos 45,2) | 0 | 69 | 41,4 |
| Bunzlau Castle en Bunzlau servies | 5 | 854 | 0,59% | 24,3 | bunzlau castle (74 vert, pos 41,4) | 10 | 942 | 25,4 |
| Groene, witte en oolong thee en matcha | 1 | 761 | 0,13% | 46,8 | oolong thee (94 vert, pos 49,4) | 0 | 65 | 33,2 |
| Thee accessoires (zeefje, schep, maatlepel, toren) | 0 | 664 | 0,00% | 37,2 | thee accessoires (124 vert, pos 42,6) | 0 | 270 | 41,0 |
| Muuss en Joeff (wanddecoratie) | 10 | 571 | 1,75% | 7,4 | muuss (260 vert, pos 6,6) | 11 | 335 | 7,4 |
| Theewinkel (generiek en lokaal) | 12 | 537 | 2,23% | 15,3 | theewinkel (153 vert, pos 11,6) | 5 | 457 | 10,9 |
| Thee cadeau en theegeschenk | 0 | 446 | 0,00% | 44,7 | thee cadeau (28 vert, pos 42,2) | 1 | 39 | 18,7 |
| Rice DK en Rice by Rice | 0 | 442 | 0,00% | 25,8 | rice dk (126 vert, pos 46,0) | 0 | 484 | 17,6 |
| Engelstalig: 'tea' | 1 | 407 | 0,25% | 4,3 | tea (378 vert, pos 3,8) | 0 | 351 | 6,0 |
| Overig non-brand (niet ingedeeld) | 1 | 308 | 0,32% | 19,9 | - (geen vertoningen) | 4 | 189 | 22,9 |
| Thee bewaarblik en theeblikken | 1 | 303 | 0,33% | 26,4 | thee bewaarblik (45 vert, pos 16,8) | 1 | 351 | 23,4 |
| Vruchtenthee en fruitige thee | 0 | 280 | 0,00% | 40,2 | aardbeien slagroom thee (2 vert, pos 25,0) | 0 | 65 | 30,8 |
| Proefpakket en kennismaken met thee | 0 | 260 | 0,00% | 43,4 | proefpakket thee (53 vert, pos 46,0) | 0 | 282 | 35,3 |
| Zwarte thee (assam, ceylon, earl grey) | 0 | 245 | 0,00% | 42,2 | zwarte thee (50 vert, pos 51,5) | 2 | 11 | 9,2 |
| Servies, mokken en bekers (generiek) | 3 | 240 | 1,25% | 11,8 | servies (39 vert, pos 4,5) | 2 | 201 | 11,3 |
| Smaakthee en seizoensthee | 1 | 234 | 0,43% | 42,3 | speculaas thee (15 vert, pos 42,7) | 3 | 13 | 16,1 |
| Thee voor bedrijven, kantoor en horeca (zakelijk) | 0 | 224 | 0,00% | 40,9 | thee op kantoor (geen vertoningen) | 0 | 451 | 38,9 |
| Rooibos en honeybush | 0 | 142 | 0,00% | 34,2 | losse rooibos thee (7 vert, pos 41,9) | 0 | 79 | 27,0 |
| Productnamen en cadeau-mokken (long tail op productpagina's) | 0 | 132 | 0,00% | 41,5 | - (geen vertoningen) | 4 | 123 | 20,9 |
| Koude thee, cold brew en ijsthee | 0 | 125 | 0,00% | 32,0 | koude thee (28 vert, pos 28,1) | 0 | 112 | 28,7 |
| Blond Amsterdam servies | 0 | 84 | 0,00% | 16,7 | kan blond amsterdam in de vaatwasser (2 vert, pos 7,5) | 1 | 440 | 9,5 |
| Pools aardewerk en pools servies (generiek) | 0 | 82 | 0,00% | 36,7 | pools servies (18 vert, pos 41,1) | 1 | 115 | 35,0 |
| Taart, bakmixen en bakken | 0 | 79 | 0,00% | 12,9 | baking (51 vert, pos 4,5) | 2 | 60 | 13,3 |
| Natural Flower Cards | 1 | 47 | 2,13% | 6,5 | natural flower cards (44 vert, pos 6,3) | 0 | 81 | 7,2 |
| Sterrenmunt | 0 | 46 | 0,00% | 37,8 | wat is sterrenmunt (geen vertoningen) | 0 | 38 | 14,1 |
| Pineut Water Twist en Delfts blauw waterfles | 0 | 28 | 0,00% | 13,7 | waterfles delfts blauw (1 vert, pos 14,0) | 0 | 73 | 10,6 |

## Vaste trackingzoekwoorden

Positie per URL, gewogen op vertoningen, zonder parameters.

| Zoekwoord | URL | Vert | Klik | Pos | Vert vm | Pos vm |
|---|---:|---:|---:|---:|---:|---:|
| bunzlau servies | http://www.tanterie.nl/ | 55 | 0 | 4,2 | 35 | 4,7 |
| bunzlau servies | https://tanterie.nl/collections/bunzlau | 38 | 0 | 32,5 | 49 | 28,6 |
| bunzlau servies | https://tanterie.nl/products/ontbijtbord-o-20-cm | 2 | 0 | 3,0 | 0 | - |
| bunzlau servies | https://tanterie.nl/ | 0 | 0 | - | 1 | 3,0 |
| theewinkel | https://tanterie.nl/ | 152 | 5 | 11,2 | 184 | 11,0 |
| theewinkel | http://www.tanterie.nl/ | 5 | 0 | 1,8 | 7 | 2,6 |
| theewinkel | https://tanterie.nl/pages/theewinkel-borne-twente | 3 | 0 | 91,3 | 0 | - |
| thee uit twente | https://tanterie.nl/ | 24 | 0 | 12,6 | 21 | 2,0 |
| thee uit twente | https://tanterie.nl/pages/theewinkel-borne-twente | 14 | 0 | 29,4 | 22 | 41,6 |
| thee uit twente | https://tanterie.nl/collections/kruidenthee | 1 | 0 | 73,0 | 10 | 77,7 |
| thee uit twente | http://www.tanterie.nl/ | 0 | 0 | - | 1 | 31,0 |
| tea | http://www.tanterie.nl/ | 378 | 0 | 3,8 | 338 | 5,9 |

'bunzlau servies' staat op http://www.tanterie.nl/ op positie 4,2 en op de collectie op 32,5. 'theewinkel' wordt bediend door de homepage (positie 11,2) en de eigen pagina staat op 91,3 met 3 vertoningen. 'thee uit twente' staat op de homepage op 12,6 en op de eigen pagina op 29,4. 'tea' staat alleen op http://www.tanterie.nl/ op positie 3,8 zonder klik.

## Shopify-analytics

Gemeten op 21 oktober 2026, alleen lezen, via `shopify store execute --store 0qkm31-r6.myshopify.com` zonder --allow-mutations (auth met read_reports en read_orders). Ruwe uitvoer: data/2026-10-21-nulmeting-shopify-*.json. De vensters zijn gelijk aan die van Search Console: 22 september t/m 19 oktober en 25 augustus t/m 21 september 2026. Bedragen zijn in de winkelvaluta (euro), Shopify total_sales.

Bronnen en definities:

| Maat | Bron | Definitie |
|---|---|---|
| Sessies | ShopifyQL `FROM sessions`, gegroepeerd op referrer_source en referrer_name | Sessies op de online winkel. Organisch zoeken is referrer_source 'search' (Google, Bing, Ecosia, DuckDuckGo, Yahoo); Shopify deelt in op de verwijzer, dus betaald verkeer zonder utm-tags kan hier meetellen |
| Bestellingen en omzet online | ShopifyQL `FROM sales` gegroepeerd op sales_channel, kanaal Online Store; gecontroleerd met Admin GraphQL orders (source_name niet pos) | total_sales, alle online bestellingen in het venster |
| POS | Zelfde query, kanaal Point of Sale | Kassa in de winkel in Borne; geen online omzet en niet bij organisch geteld |
| Bestellingen en omzet uit organisch zoeken | Admin GraphQL orders met customerJourneySummary (lastVisit en firstVisit) | ShopifyQL kan sales niet op referrer groeperen (fout: "Column 'referrer_source' not found"), dus is dit de enige route. Organisch is Google met sourceType SEO |

Sessies:

| Maat | 22 sep t/m 19 okt | 25 aug t/m 21 sep |
|---|---:|---:|
| Sessies totaal | 725 | 747 |
| Direct | 443 | 450 |
| Zoeken totaal (search) | 242 (33,4%) | 253 (33,9%) |
| waarvan Google | 229 (31,6%) | 237 (31,7%) |
| waarvan Bing | 10 | 10 |
| Social (Instagram en Facebook) | 34 | 31 |

Search Console telt klikken (387) en Shopify telt sessies (229 vanuit Google); die twee horen niet gelijk te zijn.

Bestellingen en omzet:

| Maat | 22 sep t/m 19 okt | 25 aug t/m 21 sep |
|---|---:|---:|
| Online bestellingen totaal | 2 | 5 |
| Online omzet totaal | 27,25 euro | 139,30 euro |
| POS-bestellingen (apart, geen online omzet) | 698 | 559 |
| POS-omzet (apart) | 14.895,61 euro | 9.668,27 euro |
| Online bestellingen met laatste bezoek Google organisch | 0 | 1 (30,60 euro) |
| Online bestellingen met eerste bezoek Google organisch | 0 | 2 (77,45 euro) |
| Online bestellingen zonder herkomstgegevens in Shopify | 2 | 2 |
| Online bestellingen met laatste bezoek direct | 0 | 2 |

In het huidige venster hebben beide online bestellingen (#3879 en #4026) geen bezoekgegevens, dus de herkomst is onbekend; organische omzet is dan 0 euro gemeten, niet bewezen 0. In het vorige venster zijn de organische cijfers één en twee bestellingen: te weinig om een conversiegraad of trend uit af te leiden. De online omzet is verwaarloosbaar naast de kassa (2 bestellingen tegenover 698 in het huidige venster); het zoekverkeer weerspiegelt zich dus vooral in winkelbezoek en niet in webshopomzet, wat dit rapport niet kan meten.

## Google Bedrijfsprofiel

Bron: Business Profile Performance API, locatie Tante Rie (locations/6267696427702073490), alleen lezen. Ruwe data: data/gbp/2026-08-01_2026-10-19-gbp-dagelijks.json en -zoektermen.json. Dezelfde twee vensters als hierboven. Het profiel loopt een paar dagen achter: op 18 en 19 oktober staan bijna overal geen waarden meer (nul en nog niet verwerkt zijn in de data niet te onderscheiden), dus de cijfers van het nulvenster zijn voor die twee dagen mogelijk te laag. De weektabel gebruikt daarom volledige ISO-weken (maandag tot en met zondag) tot week 42.

| Maat | 22 sep t/m 19 okt | 25 aug t/m 21 sep | Verschil |
|---|---:|---:|---:|
| Routeverzoeken | 80 | 80 | +0% |
| Websiteklikken | 135 | 180 | -25% |
| Bellen | 4 | 10 | -60% |
| Zoeken mobiel | 218 | 1.232 | -82% |
| Zoeken desktop | 69 | 146 | -53% |
| Maps mobiel | 176 | 160 | +10% |
| Maps desktop | 22 | 23 | -4% |
| Vertoningen samen (Zoeken en Maps, mobiel en desktop) | 485 | 1.561 | -69% |

Weektabel (vertoningen per kanaal, acties per week):

| ISO-week | Maandag | Routes | Website | Bellen | Zoeken mobiel | Zoeken desktop | Maps mobiel | Maps desktop |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 32 | 2026-08-03 | 29 | 42 | 0 | 307 | 30 | 53 | 9 |
| 33 | 2026-08-10 | 20 | 36 | 1 | 375 | 31 | 44 | 5 |
| 34 | 2026-08-17 | 27 | 45 | 2 | 416 | 45 | 38 | 5 |
| 35 | 2026-08-24 | 14 | 50 | 6 | 282 | 33 | 44 | 0 |
| 36 | 2026-08-31 | 29 | 32 | 2 | 269 | 34 | 45 | 9 |
| 37 | 2026-09-07 | 22 | 46 | 2 | 282 | 31 | 34 | 7 |
| 38 | 2026-09-14 | 15 | 53 | 0 | 387 | 39 | 42 | 4 |
| 39 | 2026-09-21 | 13 | 45 | 0 | 141 | 36 | 45 | 7 |
| 40 | 2026-09-28 | 28 | 45 | 0 | 53 | 21 | 51 | 7 |
| 41 | 2026-10-05 | 27 | 24 | 0 | 27 | 15 | 39 | 8 |
| 42 | 2026-10-12 | 12 | 25 | 4 | 45 | 10 | 42 | 3 |

Vertoningen in Zoeken op mobiel lagen van week 32 tot en met 38 tussen 269 en 416 per week, zakten in week 39 naar 141 en daarna naar 53, 27 en 45. Per dag begint de daling rond 22 september (30 vertoningen), met 18 op 23 september en 14 op 24 september; in de week daarvoor (14 tot 21 september) lagen de dagen tussen 31 en 114. Zoeken op desktop volgt dezelfde richting (30 tot 45 per week, daarna 36, 21, 15 en 10). Vertoningen in Maps (mobiel 34 tot 53 per week) en routeverzoeken (12 tot 29 per week, over de vensters gelijk op 80) bleven op niveau. Websiteklikken gingen van 32 tot 53 per week naar 24 en 25 in week 41 en 42, en bellen van 0 tot 6 per week naar 0 tot 4; bij deze kleine aantallen is dat een indicatie.

Zoektermen waarop het profiel werd getoond (maandcijfers augustus tot en met oktober samen, Google toont alleen termen boven een drempel):

| Zoekterm | Vertoningen |
|---|---:|
| servies | 209 |
| bunzlau servies | 150 |
| tante rie, bakkerssteeg, borne | 66 |
| rie | 53 |
| bunzlau | 51 |
| serviesset | 47 |
| losse thee | 39 |
| porselein servies | 32 |
| theepot | 25 |
| arie borne | 16 |

Daarna volgen termen waarvan Google alleen meldt dat ze onder de 15 liggen, onder andere beige servies, blond, bunzlau servies aanbieding, bunzlau winkels nederland, cadeauwinkel borne, kookwinkel borne en kadowinkel borne. De zoektermen zijn niet per week beschikbaar, dus ze laten niet zien welke termen zijn weggevallen. 'rie' staat hier ook als zoekterm (53) en kan, net als in Search Console, RI&E zijn.

Wat samenvalt, zonder oorzaak: de daling in Zoeken begint op 22 tot 24 september. Op 24 september zakken ook de vertoningen van /pages/blond-amsterdam-servies in Search Console van 24 (23 september) naar 1 en blijven daarna op 0 tot 3 per dag (/collections/blond blijft op ongeveer 10 per dag). In Search Console stegen de niet-merkvertoningen in dezelfde dagen juist, van ongeveer 200 per dag voor 22 september naar meestal 390 tot 680 per dag erna (met een dal van 190 tot 330 van 2 tot 7 oktober en van 14 tot 19 oktober), terwijl de niet-merkpositie van 21,7 naar 34,2 zakte en de niet-merkklikken van 48 naar 40 gingen. Dit zijn vier waarnemingen die in dezelfde weken liggen; het is niet vastgesteld dat ze met elkaar te maken hebben.

Mogelijke oorzaken die naast elkaar liggen en die dit rapport niet kan onderscheiden:

| Mogelijkheid | Wat ervoor of ertegen spreekt in de data | Hoe te controleren |
|---|---|---|
| Een Google-update | De dalingen in Zoeken (GBP) en bij de Blond-pagina (GSC) vallen op dezelfde dagen; Maps blijft stabiel | Datums van updates in het Google Search Status Dashboard naast 22 tot 24 september leggen |
| AI-overzichten of andere veranderingen in de zoekresultaten | Bij servies en bunzlau servies kan een andere resultaatopmaak het profiel verdringen; in de data niet te zien | Handmatig de zoekresultaten voor 'servies', 'bunzlau servies' en 'blond amsterdam servies' bekijken op mobiel vanuit Borne |
| Iets aan het profiel zelf | Niet na te gaan met de API; categorieën, producten, openingstijden of de websitelink kunnen rond die dagen zijn aangepast | Wijzigingshistorie van het Bedrijfsprofiel (Mark) en de lijst van recente bewerkingen |
| Een verandering in hoe vertoningen worden geteld of gerapporteerd | Kan niet worden uitgesloten; Maps en routeverzoeken wijzigen niet | Vergelijken met het rapport in de Bedrijfsprofiel-interface voor dezelfde dagen |

Websitelink in het profiel: Mark heeft de link in het Bedrijfsprofiel op 21 oktober veranderd van http://www.tanterie.nl/ naar https://tanterie.nl/. Alle cijfers in dit rapport liggen vóór die wijziging. Websiteklikken uit het profiel (135 in het nulvenster) zijn van dezelfde orde als de 163 klikken op http://www.tanterie.nl/ in Search Console; of klikken uit het profiel in Search Console op die homepage-URL terechtkomen, is niet vastgesteld. Als dat zo is, kan het https-aandeel van de homepage in de migratiemonitor vanaf 21 oktober snel stijgen doordat de link wijst naar de https-URL, en niet doordat Google de migratie heeft afgerond.

Aangepaste interpretatie van het 90-procentsignaal:

1. De monitor rekent sinds vandaag twee maten: het totale https-aandeel van de homepage en het https-aandeel voor alleen zoekopdrachten zonder merknaam. Die tweede maat komt niet via het profiel (op het nulpunt: 60,3 procent van de vertoningen, 516 van 856; klikken 2 van 4, te weinig om te beoordelen).
2. Het signaal 'migratie grotendeels rond' geldt alleen als beide maten twee weken achter elkaar minstens 90 procent halen. Het klikaandeel van de niet-merkmaat wordt pas beoordeeld bij minstens 10 klikken op de homepage per week.
3. Beschouw de monitor van 27 oktober als de eerste meting na de linkwijziging. Een sprong van het totale aandeel in die week is geen bewijs voor de migratie. Het homepage-besluit (de-optimalisatie) wacht dus op de niet-merkmaat.
4. Wil de SEO Lead de klikken uit het profiel scheiden, dan kan Mark overwegen aan de profiellink een parameter toe te voegen (bijvoorbeeld ?utm_source=gbp); parameter-URL's worden in de monitor al apart geteld. Dat is een wijziging in het Bedrijfsprofiel en vraagt zijn akkoord; ik heb niets gewijzigd.
5. De GBP-cijfers staan voortaan in elke weekmonitor (eigen sectie), met vergelijking met de week ervoor.

## Wat dit rapport niet zegt

Het zegt niet waarom de vertoningen steeg of de positie zakte, en het zegt niets over het effect van de schema-livegang van 21 oktober, omdat die buiten het venster valt. Een dag of week met meer of minder klikken is bij deze aantallen (circa 14 klikken per dag) geen trend.

## Drie aanbevelingen voor de SEO Lead

1. Houd het besluit over de homepage vast aan de migratiemonitor. De nulmeting laat zien dat https://tanterie.nl/ 77,7 procent van de homepagevertoningen heeft maar 36,1 procent van de klikken, op positie 40,6 tegenover 4,3 voor http://www.tanterie.nl/. Zolang beide maten niet twee weken achter elkaar op 90 procent staan, blijft de homepage ongemoeid, zoals het plan zegt. De monitor van 27 oktober is de eerste vergelijking.
2. Laat Technisch SEO vóór de tekstacties de vertoningsval controleren op /pages/zakelijk (484 naar 0 vertoningen) en /pages/blond-amsterdam-servies (829 naar 48), met URL-inspectie op indexatie, canonical en Google-gekozen canonical. Zijn die pagina's niet meer geïndexeerd of heeft Google een andere canonical gekozen, dan is de uitgangssituatie voor actie 7 en 9 anders dan het plan aanneemt. Werk daarnaast de nulwaarden in plan-2026-10 bij van 90 dagen naar deze 28-dagenwaarden, want de succescriteria (bijvoorbeeld CTR Joeff minstens 3 procent) zijn nu met een andere basis geschreven.
3. Kies een omzetmaat die bij deze winkel past. Online zijn er 2 tot 5 bestellingen per vier weken tegenover ruim 500 kassabestellingen, dus organische webshopomzet is geen bruikbare succesmaat. Gebruik sessies uit Google (229 in het nulvenster) en Search Console-klikken als hoofdmaat en overleg met Mark of winkelbezoek of kassaomzet een aanvullende maat moet worden. Neem het besluit over de CrUX API (beslissing 10) mee, zodat de mobiele snelheid ook met veldgegevens gemeten wordt. Vergelijking met 2025 is niet mogelijk met de huidige property; de eerste echte jaarvergelijking kan pas vanaf eind januari 2027.
