# Zoekvolumes per cluster

Gegenereerd door scripts/volumes_in_clusters.py. Volumes: Google Keyword Planner via scripts/zoekvolumes.py (Nederlands, Nederland). Vertoningen, klikken en posities: Search Console, 90 dagen, uit de clustertabellen. Een zoekwoord zonder volume in de bestanden blijft leeg en telt niet mee.

Bronbestanden: data/keyword-planner/2026-10-24-ideeen-seeds.json, data/keyword-planner/2026-10-24-invoerlijst.json, data/keyword-planner/2026-10-24-zoekvolumes.json

Leeswijzer:

- Vert./maand is het 90-daagse aantal vertoningen gedeeld door 3.
- Aandeel zichtbaarheid is vert./maand gedeeld door het maandvolume van hetzelfde zoekwoord. Een hoog aandeel op een lage positie betekent dat de pagina al vaak getoond wordt; een laag aandeel op een goede positie wijst op weinig vertoningen ten opzichte van de vraag.
- De bijlage in het clusterrapport bevat alleen de top zoekwoorden per cluster, dus de som van de zoekwoorden is lager dan het clustertotaal in de tabel Clusters.
- Keyword Planner voegt dicht bij elkaar liggende varianten samen (bijvoorbeeld ricedk en rice dk) en geeft ze dezelfde maandreeks. Binnen een cluster telt zo'n groep met identieke maandreeks eenmaal; de andere regels staan in de tabel als "samengevoegd met ...". Zonder maandcijfers (ideeen-data) kan niet worden ontdubbeld.
- Zoekwoorden uit volume-uitsluitingen.txt (breed of niet passend) staan in de tabel als "niet meegeteld" en tellen niet mee in het kerntotaal. De kolom Incl. brede termen toont het totaal met die termen erbij, dus het verschil is wat de brede termen toevoegen.
- Ook het kerntotaal is een bovengrens: niet-identieke zoekwoorden kunnen overlappen (bunzlau castle en bunzlau; rooibos en rooibos thee).

Uitgesloten zoekwoorden: blond (algemeen woord (onder meer haarkleur), niet te koppelen aan het servies; 5.400 per maand); thee (kopterm met oktober-uitschieter 49.500 en winterpiek; apart als breed, niet nagejaagd); servies (brede kopterm waar grote webwinkels op ranken; zelfde reeks als serviezen); serviezen (zelfde maandreeks als servies (14.800), breed); baking (Engels woord, vertekend door augustus 2026 (18.100); hoort niet bij een collectie bakmixen); bakwinkel (winkelzoekers voor bakartikelen, geen aanbod bij bakmixen); luminlique (product staat alleen in de kassa (Shopify POS), niet online; 404 is correct); theewinkel opende (ander dorp (Groningen), lokale ruis); relatiegeschenk thee (zakelijk, buiten scope (geen SEO-werk aan /pages/zakelijk)); paardenstaart thee (verkeerd ingedeeld (kruidenthee), hoort niet bij bakmixen); natural flowers (algemene term, niet te koppelen aan de collectie Natural Flower Cards).

## Overzicht

| Cluster | Doelpagina | Zoekwoorden met volume | Kernvolume/maand | Incl. brede termen | Vert./maand (kern) | Aandeel zichtbaarheid | Vert. 90d (heel cluster) | Pos. cluster |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Bunzlau Castle en Bunzlau servies | /collections/bunzlau | 8 van 8 | 9.450 | gelijk | 654 | 7% | 4.030 | 19,8 |
| Pools aardewerk en pools servies (generiek) | /collections/bunzlau | 8 van 8 | 1.260 | gelijk | 90 | 7% | 276 | 35,1 |
| Muuss en Joeff (wanddecoratie) | /collections/joeff | 8 van 8 | 1.460 | 1.550 | 423 | 29% | 1.343 | 7,8 |
| Rice DK en Rice by Rice | /collections/rice | 6 van 8 | 990 | gelijk | 343 | 35% | 1.893 | 15,9 |
| Blond Amsterdam servies | /pages/blond-amsterdam-servies | 8 van 8 | 1.130 | 6.530 | 117 | 10% | 777 | 10,2 |
| Natural Flower Cards | /collections/nfc-natural-flower-cards | 3 van 4 | 280 | 370 | 65 | 23% | 217 | 6,9 |
| Pineut Water Twist en Delfts blauw waterfles | /products/waterfles-delfts-blauw | 8 van 8 | 340 | gelijk | 100 | 30% | 347 | 9,9 |
| Sterrenmunt | /products/sterrenmunt | 8 van 8 | 1.690 | gelijk | 66 | 4% | 220 | 21,0 |
| Thee voor bedrijven, kantoor en horeca (zakelijk) | /pages/zakelijk | 0 van 8 | - | - | - | - | 2.156 | 37,2 |
| Theewinkel (generiek en lokaal) | /pages/theewinkel-borne-twente | 8 van 8 | 3.050 | 3.100 | 334 | 11% | 1.598 | 13,3 |
| Thee bewaarblik en theeblikken | /collections/thee-bewaarblikken | 6 van 8 | 1.610 | gelijk | 204 | 13% | 1.073 | 21,5 |
| Proefpakket en kennismaken met thee | /collections/proefpakketten | 6 van 8 | 940 | gelijk | 196 | 21% | 743 | 37,2 |
| Koude thee, cold brew en ijsthee | /pages/cold-brew-thee | 8 van 8 | 1.260 | gelijk | 129 | 10% | 468 | 24,6 |
| Thee cadeau en theegeschenk | /pages/thee-cadeau | 8 van 8 | 1.500 | 1.530 | 53 | 4% | 532 | 40,9 |
| Thee accessoires (zeefje, schep, maatlepel, toren) | /collections/thee-accessoires | 8 van 8 | 440 | gelijk | 218 | 50% | 1.266 | 34,3 |
| Thee kopen en losse thee (hoofdzoekwoorden) | /collections/thee | 8 van 8 | 6.530 | 21.330 | 191 | 3% | 2.087 | 41,7 |
| Servies, mokken en bekers (generiek) | /pages/serviezen | 7 van 8 | 1.020 | 15.820 | 54 | 5% | 658 | 11,5 |
| Taart, bakmixen en bakken | /collections/bakmixen | 8 van 8 | 1.790 | 7.400 | 40 | 2% | 239 | 11,8 |
| Groene, witte en oolong thee en matcha | /collections/groene-thee | 8 van 8 | 11.480 | gelijk | 152 | 1% | 937 | 42,4 |
| Zwarte thee (assam, ceylon, earl grey) | /collections/zwarte-thee | 7 van 8 | 4.780 | gelijk | 56 | 1% | 315 | 36,5 |
| Rooibos en honeybush | /collections/rooibos | 8 van 8 | 9.020 | gelijk | 92 | 1% | 314 | 27,9 |
| Vruchtenthee en fruitige thee | /collections/vruchtenthee | 8 van 8 | 10.390 | gelijk | 83 | 1% | 420 | 35,2 |
| Kruidenthee (kamille, munt, gember, salie) | /collections/kruidenthee | 8 van 8 | 15.640 | gelijk | 144 | 1% | 1.442 | 41,5 |
| Smaakthee en seizoensthee | /collections/thee | 8 van 8 | 2.520 | gelijk | 63 | 2% | 319 | 35,3 |
| Thee longtail: gezondheid, soorten en overig (informatief) | /collections/thee | 8 van 8 | 5.970 | gelijk | 69 | 1% | 1.204 | 40,1 |
| Engelstalig: 'tea' | /collections/thee | 0 van 8 | - | - | - | - | 949 | 5,6 |
| Productnamen en cadeau-mokken (long tail op productpagina's) | - | 8 van 8 | 3.710 | gelijk | 62 | 2% | 588 | 20,2 |
| Overig non-brand (niet ingedeeld) | - | 2 van 8 | 20 | gelijk | 10 | 52% | 710 | 20,2 |
| Lokaal: Borne, Twente en omgeving | /pages/theewinkel-borne-twente | 13 van 15 | 1.150 | gelijk | 127 | 11% | 423 | - |

## Per cluster

### Bunzlau Castle en Bunzlau servies

Doelpagina: /collections/bunzlau. Cluster in Search Console: 4.030 vertoningen, 29 klikken in 90 dagen, gemiddelde positie 19,8.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| bunzlau castle | 5.400 | HIGH | 600 | 200,0 | 20,1 | 2 | 4% | 5.200 | ja |
| bunzlau servies | 1.900 | HIGH | 325 | 108,3 | 15,3 | 4 | 6% | 1.792 | ja |
| bunzlau | 1.600 | HIGH | 411 | 137,0 | 15,3 | 3 | 9% | 1.463 | ja |
| bunzlau castle servies | 320 | HIGH | 104 | 34,7 | 21,2 | 0 | 11% | 285 | ja |
| bunzlau castle mokken | 110 | HIGH | 160 | 53,3 | 25,3 | 0 | 48% | 57 | ja |
| bunzlau servies kopen in polen | 90 | HIGH | 118 | 39,3 | 10,6 | 2 | 44% | 51 | ja |
| bunzlau castle borden | 20 | HIGH | 146 | 48,7 | 27,1 | 0 | 243% | 0 | ja |
| bunzlau thee | 10 | HIGH | 97 | 32,3 | 13,2 | 0 | 323% | 0 | ja |

Kerntotaal zoekvolume: 9.450 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer; 0 samengevoegd, 0 niet meegeteld). Vertoningen van de kernzoekwoorden: 653,7 per maand, aandeel zichtbaarheid 7%.

Seizoen (kernzoekwoorden): piek in december 2025 (15.990, 160% van gemiddeld), november 2025 (13.470, 135% van gemiddeld); gemiddeld 9.990 per maand, op basis van 8 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 9.310 | 13.470 | 15.990 | 11.160 | 8.080 | 9.440 | 8.730 | 9.140 | 7.700 | 7.450 | 9.500 | 9.910 |

### Pools aardewerk en pools servies (generiek)

Doelpagina: /collections/bunzlau. Cluster in Search Console: 276 vertoningen, 1 klikken in 90 dagen, gemiddelde positie 35,1.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| pools servies | 720 | HIGH | 81 | 27,0 | 38,2 | 0 | 4% | 693 | ja |
| pools serviesgoed | 720 | HIGH | 4 | 1,3 | 29,2 | 0 | 0% | 719 | samengevoegd met pools servies |
| pools aardewerk | 320 | HIGH | 74 | 24,7 | 45,8 | 0 | 8% | 295 | ja |
| pools servies sale | 110 | HIGH | 6 | 2,0 | 18,7 | 0 | 2% | 108 | ja |
| pools aardewerk verkooppunten | 50 | HIGH | 8 | 2,7 | 11,8 | 1 | 5% | 47 | ja |
| pools aardewerk theepot | 30 | MEDIUM | 26 | 8,7 | 19,4 | 0 | 29% | 21 | ja |
| pools aardewerk mokken | 20 | HIGH | 24 | 8,0 | 29,6 | 0 | 40% | 12 | ja |
| pools aardewerk servies | 10 | LOW | 47 | 15,7 | 32,4 | 0 | 157% | 0 | ja |

Kerntotaal zoekvolume: 1.260 per maand over 7 van 8 zoekwoorden (bovengrens, zie leeswijzer; 1 samengevoegd, 0 niet meegeteld). Vertoningen van de kernzoekwoorden: 90,0 per maand, aandeel zichtbaarheid 7%.

Seizoen (kernzoekwoorden): piek in november 2025 (1.700, 131% van gemiddeld), december 2025 (1.690, 131% van gemiddeld); gemiddeld 1.294 per maand, op basis van 7 van 7 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 1.410 | 1.700 | 1.690 | 1.500 | 1.210 | 1.250 | 1.060 | 1.300 | 940 | 1.050 | 1.290 | 1.130 |

### Muuss en Joeff (wanddecoratie)

Doelpagina: /collections/joeff. Cluster in Search Console: 1.343 vertoningen, 31 klikken in 90 dagen, gemiddelde positie 7,8.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| joeff | 880 | LOW | 354 | 118,0 | 8,5 | 1 | 13% | 762 | ja |
| muuss | 390 | LOW | 632 | 210,7 | 7,2 | 21 | 54% | 179 | ja |
| luminlique | 90 | MEDIUM | 45 | 15,0 | 7,0 | 3 | 17% | 75 | niet meegeteld: product staat alleen in de kassa (Shopify POS), niet online; 404 is correct |
| muuss galerijwand | 70 | LOW | 44 | 14,7 | 9,5 | 1 | 21% | 55 | ja |
| joeff muuss | 50 | LOW | 155 | 51,7 | 8,2 | 3 | 103% | 0 | ja |
| muuss joeff | 40 | LOW | 28 | 9,3 | 8,0 | 1 | 23% | 31 | ja |
| muuss wanddecoratie | 20 | MEDIUM | 19 | 6,3 | 9,6 | 0 | 32% | 14 | ja |
| muuss verkooppunten | 10 | LOW | 36 | 12,0 | 6,0 | 0 | 120% | 0 | ja |

Kerntotaal zoekvolume: 1.460 per maand over 7 van 8 zoekwoorden (bovengrens, zie leeswijzer; 0 samengevoegd, 1 niet meegeteld). Vertoningen van de kernzoekwoorden: 422,7 per maand, aandeel zichtbaarheid 29%.
Totaal inclusief brede termen: 1.550 per maand, dus 90 meer door de niet meegetelde termen.

Seizoen (kernzoekwoorden): piek in november 2025 (2.150, 158% van gemiddeld), oktober 2025 (1.730, 127% van gemiddeld); gemiddeld 1.363 per maand, op basis van 7 van 7 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 1.730 | 2.150 | 1.700 | 1.510 | 1.230 | 1.480 | 1.080 | 1.150 | 880 | 880 | 1.240 | 1.330 |

### Rice DK en Rice by Rice

Doelpagina: /collections/rice. Cluster in Search Console: 1.893 vertoningen, 3 klikken in 90 dagen, gemiddelde positie 15,9.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| ricebyrice | 480 | HIGH | 214 | 71,3 | 8,6 | 0 | 15% | 409 | ja |
| rice dk | 390 | HIGH | 495 | 165,0 | 22,6 | 1 | 42% | 225 | ja |
| rice denmark | 50 | HIGH | 91 | 30,3 | 18,9 | 0 | 61% | 20 | ja |
| rice beker l | 30 | HIGH | 85 | 28,3 | 7,4 | 1 | 94% | 2 | ja |
| rice beker m | 30 | HIGH | 59 | 19,7 | 7,7 | 0 | 66% | 10 | ja |
| rice webshop | 10 | HIGH | 84 | 28,0 | 19,4 | 0 | 280% | 0 | ja |
| ricedk | - | - | 129 | 43,0 | 9,4 | 0 | - | - | - |
| rice by rice | - | - | 60 | 20,0 | 24,3 | 0 | - | - | - |

Kerntotaal zoekvolume: 990 per maand over 6 van 8 zoekwoorden (bovengrens, zie leeswijzer; 0 samengevoegd, 0 niet meegeteld). Vertoningen van de kernzoekwoorden: 342,7 per maand, aandeel zichtbaarheid 35%.

Seizoen (kernzoekwoorden): piek in mei 2026 (1.340, 125% van gemiddeld); gemiddeld 1.070 per maand, op basis van 6 van 6 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 960 | 930 | 1.020 | 1.220 | 830 | 1.130 | 1.110 | 1.340 | 960 | 1.200 | 1.220 | 920 |

### Blond Amsterdam servies

Doelpagina: /pages/blond-amsterdam-servies. Cluster in Search Console: 777 vertoningen, 1 klikken in 90 dagen, gemiddelde positie 10,2.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| blond | 5.400 | LOW | 44 | 14,7 | 7,8 | 0 | 0% | 5.385 | niet meegeteld: algemeen woord (onder meer haarkleur), niet te koppelen aan het servies; 5.400 per maand |
| blond amsterdam servies | 480 | HIGH | 53 | 17,7 | 8,9 | 0 | 4% | 462 | ja |
| servies blond amsterdam | 390 | HIGH | 53 | 17,7 | 9,7 | 0 | 5% | 372 | ja |
| kan blond amsterdam in de vaatwasser | 110 | LOW | 85 | 28,3 | 8,3 | 0 | 26% | 82 | ja |
| servies blond | 70 | HIGH | 36 | 12,0 | 10,3 | 0 | 17% | 58 | ja |
| kan blond amsterdam servies in de vaatwasser | 40 | LOW | 49 | 16,3 | 8,6 | 0 | 41% | 24 | ja |
| kan blond amsterdam in de magnetron | 30 | LOW | 33 | 11,0 | 6,3 | 0 | 37% | 19 | ja |
| mag blond amsterdam servies in de vaatwasser | 10 | LOW | 43 | 14,3 | 8,7 | 0 | 143% | 0 | ja |

Kerntotaal zoekvolume: 1.130 per maand over 7 van 8 zoekwoorden (bovengrens, zie leeswijzer; 0 samengevoegd, 1 niet meegeteld). Vertoningen van de kernzoekwoorden: 117,3 per maand, aandeel zichtbaarheid 10%.
Totaal inclusief brede termen: 6.530 per maand, dus 5.400 meer door de niet meegetelde termen.

Seizoen (kernzoekwoorden): piek in december 2025 (1.790, 160% van gemiddeld), februari 2026 (1.730, 155% van gemiddeld); gemiddeld 1.119 per maand, op basis van 7 van 7 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 1.030 | 1.330 | 1.790 | 1.020 | 1.730 | 1.160 | 720 | 1.290 | 730 | 650 | 920 | 1.060 |

### Natural Flower Cards

Doelpagina: /collections/nfc-natural-flower-cards. Cluster in Search Console: 217 vertoningen, 1 klikken in 90 dagen, gemiddelde positie 6,9.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| natural flower cards | 170 | LOW | 157 | 52,3 | 6,7 | 1 | 31% | 118 | ja |
| naturalflowercards | 110 | LOW | 37 | 12,3 | 8,5 | 0 | 11% | 98 | ja |
| natural flowers | 90 | MEDIUM | 1 | 0,3 | 3,0 | 0 | 0% | 90 | niet meegeteld: algemene term, niet te koppelen aan de collectie Natural Flower Cards |
| natural flowercards | - | - | 22 | 7,3 | 5,9 | 0 | - | - | - |

Kerntotaal zoekvolume: 280 per maand over 2 van 4 zoekwoorden (bovengrens, zie leeswijzer; 0 samengevoegd, 1 niet meegeteld). Vertoningen van de kernzoekwoorden: 64,7 per maand, aandeel zichtbaarheid 23%.
Totaal inclusief brede termen: 370 per maand, dus 90 meer door de niet meegetelde termen.

Seizoen (kernzoekwoorden): piek in september 2026 (400, 143% van gemiddeld), januari 2026 (380, 136% van gemiddeld), oktober 2025 (350, 125% van gemiddeld); gemiddeld 279 per maand, op basis van 2 van 2 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 350 | 250 | 280 | 380 | 280 | 280 | 250 | 250 | 180 | 220 | 230 | 400 |

### Pineut Water Twist en Delfts blauw waterfles

Doelpagina: /products/waterfles-delfts-blauw. Cluster in Search Console: 347 vertoningen, 1 klikken in 90 dagen, gemiddelde positie 9,9.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| watertwist | 140 | HIGH | 33 | 11,0 | 6,5 | 0 | 8% | 129 | ja |
| water twist | 140 | HIGH | 17 | 5,7 | 12,6 | 0 | 4% | 134 | samengevoegd met watertwist |
| waterfles delfts blauw | 50 | HIGH | 56 | 18,7 | 12,1 | 0 | 37% | 31 | ja |
| pineut water twist | 50 | HIGH | 45 | 15,0 | 8,1 | 0 | 30% | 35 | ja |
| delfts blauw waterfles | 40 | HIGH | 44 | 14,7 | 11,7 | 0 | 37% | 25 | ja |
| water scoop | 20 | HIGH | 49 | 16,3 | 8,7 | 0 | 82% | 4 | ja |
| delfts blauw drinkfles | 20 | HIGH | 36 | 12,0 | 8,5 | 0 | 60% | 8 | ja |
| drinkfles delfts blauw | 20 | HIGH | 21 | 7,0 | 12,2 | 0 | 35% | 13 | ja |

Kerntotaal zoekvolume: 340 per maand over 7 van 8 zoekwoorden (bovengrens, zie leeswijzer; 1 samengevoegd, 0 niet meegeteld). Vertoningen van de kernzoekwoorden: 100,3 per maand, aandeel zichtbaarheid 30%.

Seizoen (kernzoekwoorden): piek in juni 2026 (740, 217% van gemiddeld), mei 2026 (600, 176% van gemiddeld), juli 2026 (570, 167% van gemiddeld); gemiddeld 341 per maand, op basis van 7 van 7 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 190 | 240 | 290 | 240 | 190 | 230 | 210 | 600 | 740 | 570 | 380 | 210 |

### Sterrenmunt

Doelpagina: /products/sterrenmunt. Cluster in Search Console: 220 vertoningen, 0 klikken in 90 dagen, gemiddelde positie 21,0.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| sterrenmunt | 880 | HIGH | 32 | 10,7 | 13,7 | 0 | 1% | 869 | ja |
| sterrenmunt thee gezond | 260 | LOW | 35 | 11,7 | 39,2 | 0 | 4% | 248 | ja |
| sterrenmix thee | 260 | HIGH | 27 | 9,0 | 50,4 | 0 | 3% | 251 | ja |
| sterrenmunt thee bloeddruk | 110 | LOW | 10 | 3,3 | 16,3 | 0 | 3% | 107 | ja |
| waar is sterrenmunt thee goed voor | 70 | LOW | 17 | 5,7 | 11,8 | 0 | 8% | 64 | ja |
| wat is sterrenmunt | 40 | LOW | 46 | 15,3 | 6,2 | 0 | 38% | 25 | ja |
| wat zit er in sterrenmunt thee | 40 | LOW | 7 | 2,3 | 7,3 | 0 | 6% | 38 | ja |
| sterrenmunt bloeddruk | 30 | LOW | 25 | 8,3 | 8,6 | 0 | 28% | 22 | ja |

Kerntotaal zoekvolume: 1.690 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer; 0 samengevoegd, 0 niet meegeteld). Vertoningen van de kernzoekwoorden: 66,3 per maand, aandeel zichtbaarheid 4%.

Seizoen (kernzoekwoorden): piek in januari 2026 (2.510, 145% van gemiddeld), oktober 2025 (2.310, 134% van gemiddeld), november 2025 (2.290, 132% van gemiddeld); gemiddeld 1.729 per maand, op basis van 8 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 2.310 | 2.290 | 1.980 | 2.510 | 1.890 | 1.750 | 1.410 | 1.390 | 1.060 | 1.070 | 1.300 | 1.790 |

### Thee voor bedrijven, kantoor en horeca (zakelijk)

Doelpagina: /pages/zakelijk. Cluster in Search Console: 2.156 vertoningen, 0 klikken in 90 dagen, gemiddelde positie 37,2.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| thee op kantoor | - | - | 325 | 108,3 | 47,3 | 0 | - | - | - |
| thee kantoor | - | - | 196 | 65,3 | 38,7 | 0 | - | - | - |
| thee op het werk | - | - | 190 | 63,3 | 65,2 | 0 | - | - | - |
| thee inkopen voor wederverkoop | - | - | 109 | 36,3 | 39,9 | 0 | - | - | - |
| thee zakelijk | - | - | 98 | 32,7 | 27,2 | 0 | - | - | - |
| thee voor hotels | - | - | 88 | 29,3 | 21,8 | 0 | - | - | - |
| losse thee horeca | - | - | 77 | 25,7 | 23,8 | 0 | - | - | - |
| zakelijke thee | - | - | 75 | 25,0 | 30,5 | 0 | - | - | - |

Geen zoekwoord van dit cluster staat in de volumebestanden; het volume is onbekend.

Seizoen (kernzoekwoorden): geen maandcijfers in de bestanden.

### Theewinkel (generiek en lokaal)

Doelpagina: /pages/theewinkel-borne-twente. Cluster in Search Console: 1.598 vertoningen, 22 klikken in 90 dagen, gemiddelde positie 13,3.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| theewinkel | 2.900 | HIGH | 569 | 189,7 | 12,0 | 5 | 7% | 2.710 | ja |
| thee winkel | 2.900 | HIGH | 128 | 42,7 | 17,1 | 1 | 1% | 2.857 | samengevoegd met theewinkel |
| winkel borne | 70 | LOW | 49 | 16,3 | 10,3 | 0 | 23% | 54 | ja |
| kookwinkel twente | 50 | LOW | 62 | 20,7 | 3,9 | 3 | 41% | 29 | ja |
| theewinkel opende | 50 | LOW | 52 | 17,3 | 8,0 | 0 | 35% | 33 | niet meegeteld: ander dorp (Groningen), lokale ruis |
| kruidenwinkel borne | 30 | LOW | 58 | 19,3 | 6,2 | 1 | 64% | 11 | ja |
| thee uit twente | 0 | UNSPECIFIED | 94 | 31,3 | 7,0 | 0 | - | 0 | ja |
| telvrije winkel | 0 | UNSPECIFIED | 43 | 14,3 | 43,1 | 0 | - | 0 | ja |

Kerntotaal zoekvolume: 3.050 per maand over 6 van 8 zoekwoorden (bovengrens, zie leeswijzer; 1 samengevoegd, 1 niet meegeteld). Vertoningen van de kernzoekwoorden: 334,3 per maand, aandeel zichtbaarheid 11%.
Totaal inclusief brede termen: 3.100 per maand, dus 50 meer door de niet meegetelde termen.

Seizoen (kernzoekwoorden): piek in december 2025 (4.590, 157% van gemiddeld), oktober 2025 (3.770, 129% van gemiddeld), november 2025 (3.750, 128% van gemiddeld); gemiddeld 2.932 per maand, op basis van 4 van 6 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 3.770 | 3.750 | 4.590 | 3.740 | 3.010 | 3.060 | 2.020 | 2.520 | 1.720 | 1.980 | 2.510 | 2.520 |

### Thee bewaarblik en theeblikken

Doelpagina: /collections/thee-bewaarblikken. Cluster in Search Console: 1.073 vertoningen, 4 klikken in 90 dagen, gemiddelde positie 21,5.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| thee blikjes | 590 | HIGH | 121 | 40,3 | 29,7 | 0 | 7% | 550 | ja |
| theeblikjes voor losse thee | 480 | HIGH | 102 | 34,0 | 23,6 | 2 | 7% | 446 | ja |
| thee bewaarblik | 210 | HIGH | 240 | 80,0 | 12,1 | 0 | 38% | 130 | ja |
| thee koker | 210 | HIGH | 38 | 12,7 | 9,0 | 0 | 6% | 197 | ja |
| losse thee blikjes | 90 | HIGH | 75 | 25,0 | 32,2 | 0 | 28% | 65 | ja |
| bewaarblik rechthoekig | 30 | HIGH | 36 | 12,0 | 2,6 | 0 | 40% | 18 | ja |
| thee blikken | - | - | 116 | 38,7 | 29,4 | 0 | - | - | - |
| theeblikken voor losse thee | - | - | 72 | 24,0 | 20,9 | 0 | - | - | - |

Kerntotaal zoekvolume: 1.610 per maand over 6 van 8 zoekwoorden (bovengrens, zie leeswijzer; 0 samengevoegd, 0 niet meegeteld). Vertoningen van de kernzoekwoorden: 204,0 per maand, aandeel zichtbaarheid 13%.

Seizoen (kernzoekwoorden): piek in december 2025 (2.240, 139% van gemiddeld), januari 2026 (2.190, 136% van gemiddeld); gemiddeld 1.612 per maand, op basis van 6 van 6 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 1.760 | 1.860 | 2.240 | 2.190 | 1.600 | 1.460 | 1.380 | 1.330 | 1.000 | 1.070 | 1.660 | 1.800 |

### Proefpakket en kennismaken met thee

Doelpagina: /collections/proefpakketten. Cluster in Search Console: 743 vertoningen, 0 klikken in 90 dagen, gemiddelde positie 37,2.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| thee pakketten | 720 | HIGH | 35 | 11,7 | 47,5 | 0 | 2% | 708 | ja |
| proefpakket thee | 110 | HIGH | 232 | 77,3 | 36,2 | 0 | 70% | 33 | ja |
| thee proefpakket | 110 | HIGH | 181 | 60,3 | 38,0 | 0 | 55% | 50 | samengevoegd met proefpakket thee |
| losse thee proefpakket | 50 | HIGH | 108 | 36,0 | 27,5 | 0 | 72% | 14 | ja |
| luxe thee pakket | 50 | HIGH | 20 | 6,7 | 60,6 | 0 | 13% | 43 | ja |
| theepakketten | 10 | HIGH | 13 | 4,3 | 37,0 | 0 | 43% | 6 | ja |
| proefpakket - verrassing | - | - | 71 | 23,7 | 37,6 | 0 | - | - | - |
| thee pakket | - | - | 23 | 7,7 | 44,7 | 0 | - | - | - |

Kerntotaal zoekvolume: 940 per maand over 5 van 8 zoekwoorden (bovengrens, zie leeswijzer; 1 samengevoegd, 0 niet meegeteld). Vertoningen van de kernzoekwoorden: 196,3 per maand, aandeel zichtbaarheid 21%.

Seizoen (kernzoekwoorden): piek in december 2025 (2.070, 223% van gemiddeld), november 2025 (1.760, 190% van gemiddeld), oktober 2025 (1.240, 134% van gemiddeld); gemiddeld 928 per maand, op basis van 5 van 5 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 1.240 | 1.760 | 2.070 | 960 | 750 | 770 | 620 | 670 | 550 | 520 | 550 | 680 |

### Koude thee, cold brew en ijsthee

Doelpagina: /pages/cold-brew-thee. Cluster in Search Console: 468 vertoningen, 0 klikken in 90 dagen, gemiddelde positie 24,6.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| ijs thee | 1.000 | HIGH | 15 | 5,0 | 48,2 | 0 | 0% | 995 | ja |
| koude thee | 140 | HIGH | 121 | 40,3 | 29,0 | 0 | 29% | 100 | ja |
| thee voor koud water | 40 | HIGH | 96 | 32,0 | 22,8 | 0 | 80% | 8 | ja |
| thee koud water | 30 | HIGH | 40 | 13,3 | 17,2 | 0 | 44% | 17 | ja |
| koud water thee | 20 | HIGH | 26 | 8,7 | 17,1 | 0 | 43% | 11 | ja |
| handybrew ijsthee | 10 | HIGH | 37 | 12,3 | 50,9 | 0 | 123% | 0 | ja |
| cold brew thee kopen | 10 | HIGH | 32 | 10,7 | 16,1 | 0 | 107% | 0 | ja |
| kan je thee maken met koud water | 10 | LOW | 20 | 6,7 | 7,3 | 0 | 67% | 3 | ja |

Kerntotaal zoekvolume: 1.260 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer; 0 samengevoegd, 0 niet meegeteld). Vertoningen van de kernzoekwoorden: 129,0 per maand, aandeel zichtbaarheid 10%.

Seizoen (kernzoekwoorden): piek in juni 2026 (2.070, 149% van gemiddeld); gemiddeld 1.388 per maand, op basis van 8 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 1.170 | 1.170 | 1.460 | 1.210 | 1.060 | 1.300 | 1.280 | 1.700 | 2.070 | 1.620 | 1.550 | 1.070 |

### Thee cadeau en theegeschenk

Doelpagina: /pages/thee-cadeau. Cluster in Search Console: 532 vertoningen, 2 klikken in 90 dagen, gemiddelde positie 40,9.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| thee cadeau | 1.000 | HIGH | 32 | 10,7 | 41,3 | 0 | 1% | 989 | ja |
| thee als cadeau | 1.000 | HIGH | 20 | 6,7 | 54,1 | 0 | 1% | 993 | samengevoegd met thee cadeau |
| luxe thee cadeau set | 210 | HIGH | 28 | 9,3 | 41,4 | 0 | 4% | 201 | ja |
| thee geschenkset | 140 | HIGH | 18 | 6,0 | 43,8 | 0 | 4% | 134 | ja |
| geschenk thee | 90 | HIGH | 21 | 7,0 | 51,9 | 0 | 8% | 83 | ja |
| thee kadootjes | 50 | HIGH | 20 | 6,7 | 57,3 | 0 | 13% | 43 | ja |
| relatiegeschenk thee | 30 | HIGH | 18 | 6,0 | 35,5 | 0 | 20% | 24 | niet meegeteld: zakelijk, buiten scope (geen SEO-werk aan /pages/zakelijk) |
| thee cadeau bezorgen | 10 | HIGH | 21 | 7,0 | 51,2 | 0 | 70% | 3 | ja |

Kerntotaal zoekvolume: 1.500 per maand over 6 van 8 zoekwoorden (bovengrens, zie leeswijzer; 1 samengevoegd, 1 niet meegeteld). Vertoningen van de kernzoekwoorden: 53,3 per maand, aandeel zichtbaarheid 4%.
Totaal inclusief brede termen: 1.530 per maand, dus 30 meer door de niet meegetelde termen.

Seizoen (kernzoekwoorden): piek in december 2025 (4.100, 244% van gemiddeld), november 2025 (3.350, 199% van gemiddeld), oktober 2025 (2.370, 141% van gemiddeld); gemiddeld 1.682 per maand, op basis van 6 van 6 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 2.370 | 3.350 | 4.100 | 1.460 | 1.270 | 1.330 | 980 | 1.240 | 1.230 | 840 | 820 | 1.190 |

### Thee accessoires (zeefje, schep, maatlepel, toren)

Doelpagina: /collections/thee-accessoires. Cluster in Search Console: 1.266 vertoningen, 1 klikken in 90 dagen, gemiddelde positie 34,3.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| thee accessoires | 260 | HIGH | 186 | 62,0 | 46,3 | 0 | 24% | 198 | ja |
| losse thee presentatie | 50 | HIGH | 87 | 29,0 | 35,6 | 0 | 58% | 21 | ja |
| thee toren | 40 | HIGH | 35 | 11,7 | 28,9 | 0 | 29% | 28 | ja |
| losse thee accessoires | 20 | HIGH | 121 | 40,3 | 44,5 | 0 | 202% | 0 | ja |
| theezeefje rvs | 20 | HIGH | 39 | 13,0 | 11,1 | 0 | 65% | 7 | ja |
| maatschepje 3 gram | 20 | HIGH | 36 | 12,0 | 6,6 | 0 | 60% | 8 | ja |
| thee accessoires kopen | 20 | HIGH | 34 | 11,3 | 29,8 | 0 | 57% | 9 | ja |
| leuke thee accessoires | 10 | HIGH | 116 | 38,7 | 53,5 | 0 | 387% | 0 | ja |

Kerntotaal zoekvolume: 440 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer; 0 samengevoegd, 0 niet meegeteld). Vertoningen van de kernzoekwoorden: 218,0 per maand, aandeel zichtbaarheid 50%.

Seizoen (kernzoekwoorden): piek in november 2025 (740, 175% van gemiddeld), december 2025 (660, 156% van gemiddeld), oktober 2025 (610, 144% van gemiddeld); gemiddeld 423 per maand, op basis van 8 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 610 | 740 | 660 | 500 | 420 | 360 | 360 | 370 | 290 | 160 | 270 | 340 |

### Thee kopen en losse thee (hoofdzoekwoorden)

Doelpagina: /collections/thee. Cluster in Search Console: 2.087 vertoningen, 6 klikken in 90 dagen, gemiddelde positie 41,7.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| thee | 14.800 | HIGH | 184 | 61,3 | 36,5 | 0 | 0% | 14.739 | niet meegeteld: kopterm met oktober-uitschieter 49.500 en winterpiek; apart als breed, niet nagejaagd |
| losse thee | 2.900 | HIGH | 221 | 73,7 | 36,8 | 0 | 3% | 2.826 | ja |
| losse thee kopen | 1.600 | HIGH | 45 | 15,0 | 27,6 | 1 | 1% | 1.585 | ja |
| thee kopen | 880 | HIGH | 49 | 16,3 | 34,1 | 0 | 2% | 864 | ja |
| biologische thee | 590 | HIGH | 95 | 31,7 | 46,9 | 0 | 5% | 558 | ja |
| verse thee kopen | 480 | HIGH | 54 | 18,0 | 26,5 | 1 | 4% | 462 | ja |
| thee blend | 50 | HIGH | 41 | 13,7 | 52,7 | 0 | 27% | 36 | ja |
| thee zonder aroma | 30 | HIGH | 67 | 22,3 | 45,0 | 0 | 74% | 8 | ja |

Kerntotaal zoekvolume: 6.530 per maand over 7 van 8 zoekwoorden (bovengrens, zie leeswijzer; 0 samengevoegd, 1 niet meegeteld). Vertoningen van de kernzoekwoorden: 190,7 per maand, aandeel zichtbaarheid 3%.
Totaal inclusief brede termen: 21.330 per maand, dus 14.800 meer door de niet meegetelde termen.

Seizoen (kernzoekwoorden): piek in januari 2026 (9.640, 148% van gemiddeld), december 2025 (8.880, 136% van gemiddeld), november 2025 (8.870, 136% van gemiddeld); gemiddeld 6.529 per maand, op basis van 7 van 7 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 7.320 | 8.870 | 8.880 | 9.640 | 6.750 | 6.920 | 5.720 | 5.810 | 4.050 | 3.530 | 5.070 | 5.790 |

### Servies, mokken en bekers (generiek)

Doelpagina: /pages/serviezen. Cluster in Search Console: 658 vertoningen, 7 klikken in 90 dagen, gemiddelde positie 11,5.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| servies | 14.800 | HIGH | 85 | 28,3 | 6,4 | 2 | 0% | 14.772 | niet meegeteld: brede kopterm waar grote webwinkels op ranken; zelfde reeks als serviezen |
| serviezen | 14.800 | HIGH | 38 | 12,7 | 9,5 | 0 | 0% | 14.787 | niet meegeteld: zelfde maandreeks als servies (14.800), breed |
| servies kopen | 880 | HIGH | 17 | 5,7 | 4,2 | 1 | 1% | 874 | ja |
| melk mok | 70 | HIGH | 53 | 17,7 | 6,9 | 0 | 25% | 52 | ja |
| beker melamine | 50 | HIGH | 18 | 6,0 | 28,8 | 0 | 12% | 44 | ja |
| boeren mok | 20 | HIGH | 24 | 8,0 | 9,9 | 0 | 40% | 12 | ja |
| tumbler mok | 0 | UNSPECIFIED | 49 | 16,3 | 8,5 | 0 | - | 0 | ja |
| melk mokken | - | - | 17 | 5,7 | 7,8 | 0 | - | - | - |

Kerntotaal zoekvolume: 1.020 per maand over 5 van 8 zoekwoorden (bovengrens, zie leeswijzer; 1 samengevoegd, 2 niet meegeteld). Vertoningen van de kernzoekwoorden: 53,7 per maand, aandeel zichtbaarheid 5%.
Totaal inclusief brede termen: 15.820 per maand, dus 14.800 meer door de niet meegetelde termen.

Seizoen (kernzoekwoorden): piek in november 2025 (1.490, 142% van gemiddeld), december 2025 (1.460, 140% van gemiddeld); gemiddeld 1.046 per maand, op basis van 4 van 5 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 1.130 | 1.490 | 1.460 | 1.130 | 990 | 1.120 | 850 | 870 | 840 | 710 | 1.070 | 890 |

### Taart, bakmixen en bakken

Doelpagina: /collections/bakmixen. Cluster in Search Console: 239 vertoningen, 2 klikken in 90 dagen, gemiddelde positie 11,8.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| baking | 3.600 | LOW | 64 | 21,3 | 4,8 | 0 | 1% | 3.579 | niet meegeteld: Engels woord, vertekend door augustus 2026 (18.100); hoort niet bij een collectie bakmixen |
| bakwinkel | 1.900 | MEDIUM | 8 | 2,7 | 3,1 | 1 | 0% | 1.897 | niet meegeteld: winkelzoekers voor bakartikelen, geen aanbod bij bakmixen |
| bakzolder | 1.600 | LOW | 25 | 8,3 | 13,5 | 0 | 1% | 1.592 | ja |
| dubai cake | 140 | LOW | 63 | 21,0 | 6,8 | 0 | 15% | 119 | ja |
| paardenstaart thee | 110 | HIGH | 6 | 2,0 | 40,8 | 0 | 2% | 108 | niet meegeteld: verkeerd ingedeeld (kruidenthee), hoort niet bij bakmixen |
| aardbeien cake mix | 30 | HIGH | 4 | 1,3 | 20,2 | 0 | 4% | 29 | ja |
| de bakzolder cakemix | 10 | LOW | 23 | 7,7 | 9,5 | 0 | 77% | 2 | ja |
| dubi cakes | 10 | LOW | 6 | 2,0 | 11,0 | 0 | 20% | 8 | ja |

Kerntotaal zoekvolume: 1.790 per maand over 5 van 8 zoekwoorden (bovengrens, zie leeswijzer; 0 samengevoegd, 3 niet meegeteld). Vertoningen van de kernzoekwoorden: 40,3 per maand, aandeel zichtbaarheid 2%.
Totaal inclusief brede termen: 7.400 per maand, dus 5.610 meer door de niet meegetelde termen.

Seizoen (kernzoekwoorden): geen duidelijke piek (geen maand boven 125% van het gemiddelde); gemiddeld 1.753 per maand, op basis van 5 van 5 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 1.860 | 2.090 | 2.100 | 1.770 | 1.810 | 2.150 | 1.750 | 1.460 | 1.430 | 1.420 | 1.440 | 1.760 |

### Groene, witte en oolong thee en matcha

Doelpagina: /collections/groene-thee. Cluster in Search Console: 937 vertoningen, 2 klikken in 90 dagen, gemiddelde positie 42,4.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| groene thee | 4.400 | HIGH | 72 | 24,0 | 51,5 | 0 | 1% | 4.376 | ja |
| oolong thee | 1.900 | HIGH | 94 | 31,3 | 49,4 | 0 | 2% | 1.869 | ja |
| witte thee | 1.600 | HIGH | 67 | 22,3 | 53,3 | 0 | 1% | 1.578 | ja |
| jasmijn thee | 1.600 | HIGH | 36 | 12,0 | 55,4 | 0 | 1% | 1.588 | ja |
| chinese thee | 880 | HIGH | 31 | 10,3 | 46,8 | 0 | 1% | 870 | ja |
| matcha thee kopen | 720 | HIGH | 71 | 23,7 | 44,5 | 0 | 3% | 696 | ja |
| losse groene thee | 210 | HIGH | 42 | 14,0 | 36,7 | 0 | 7% | 196 | ja |
| groene thee citroen | 170 | HIGH | 44 | 14,7 | 32,4 | 0 | 9% | 155 | ja |

Kerntotaal zoekvolume: 11.480 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer; 0 samengevoegd, 0 niet meegeteld). Vertoningen van de kernzoekwoorden: 152,3 per maand, aandeel zichtbaarheid 1%.

Seizoen (kernzoekwoorden): piek in januari 2026 (15.300, 137% van gemiddeld), december 2025 (14.600, 131% van gemiddeld); gemiddeld 11.128 per maand, op basis van 8 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 12.860 | 12.490 | 14.600 | 15.300 | 12.820 | 12.300 | 10.980 | 10.480 | 8.090 | 6.930 | 8.030 | 8.650 |

### Zwarte thee (assam, ceylon, earl grey)

Doelpagina: /collections/zwarte-thee. Cluster in Search Console: 315 vertoningen, 3 klikken in 90 dagen, gemiddelde positie 36,5.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| zwarte thee | 1.600 | HIGH | 52 | 17,3 | 49,8 | 0 | 1% | 1.583 | ja |
| pu erh thee | 1.300 | HIGH | 14 | 4,7 | 37,6 | 0 | 0% | 1.295 | ja |
| darjeeling thee | 720 | HIGH | 24 | 8,0 | 44,0 | 0 | 1% | 712 | ja |
| earl grey thee | 720 | HIGH | 19 | 6,3 | 46,6 | 0 | 1% | 714 | ja |
| assam thee | 320 | HIGH | 31 | 10,3 | 42,0 | 0 | 3% | 310 | ja |
| darjeeling thee kopen | 70 | HIGH | 13 | 4,3 | 32,3 | 1 | 6% | 66 | ja |
| losse zwarte thee | 50 | HIGH | 15 | 5,0 | 23,3 | 0 | 10% | 45 | ja |
| zwarte theesoorten | - | - | 16 | 5,3 | 39,4 | 0 | - | - | - |

Kerntotaal zoekvolume: 4.780 per maand over 7 van 8 zoekwoorden (bovengrens, zie leeswijzer; 0 samengevoegd, 0 niet meegeteld). Vertoningen van de kernzoekwoorden: 56,0 per maand, aandeel zichtbaarheid 1%.

Seizoen (kernzoekwoorden): piek in januari 2026 (6.310, 128% van gemiddeld); gemiddeld 4.928 per maand, op basis van 7 van 7 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 5.760 | 6.020 | 5.250 | 6.310 | 5.400 | 5.170 | 5.090 | 4.970 | 3.950 | 3.240 | 4.080 | 3.890 |

### Rooibos en honeybush

Doelpagina: /collections/rooibos. Cluster in Search Console: 314 vertoningen, 0 klikken in 90 dagen, gemiddelde positie 27,9.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| rooibos | 5.400 | MEDIUM | 48 | 16,0 | 12,7 | 0 | 0% | 5.384 | ja |
| rooibos thee | 1.900 | HIGH | 49 | 16,3 | 43,1 | 0 | 1% | 1.884 | ja |
| rooibos tea | 1.000 | HIGH | 12 | 4,0 | 9,2 | 0 | 0% | 996 | ja |
| rooibos vanille thee | 480 | HIGH | 19 | 6,3 | 39,9 | 0 | 1% | 474 | ja |
| honeybush thee | 170 | HIGH | 13 | 4,3 | 47,9 | 0 | 3% | 166 | ja |
| losse rooibos thee | 70 | HIGH | 93 | 31,0 | 28,5 | 0 | 44% | 39 | ja |
| losse rooibosthee | 70 | HIGH | 11 | 3,7 | 25,8 | 0 | 5% | 66 | samengevoegd met losse rooibos thee |
| rooibosthee cafeïnevrij | 0 | UNSPECIFIED | 30 | 10,0 | 22,7 | 0 | - | 0 | ja |

Kerntotaal zoekvolume: 9.020 per maand over 7 van 8 zoekwoorden (bovengrens, zie leeswijzer; 1 samengevoegd, 0 niet meegeteld). Vertoningen van de kernzoekwoorden: 91,7 per maand, aandeel zichtbaarheid 1%.

Seizoen (kernzoekwoorden): piek in januari 2026 (13.530, 133% van gemiddeld), november 2025 (13.300, 131% van gemiddeld), oktober 2025 (12.780, 126% van gemiddeld); gemiddeld 10.172 per maand, op basis van 6 van 7 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 12.780 | 13.300 | 12.680 | 13.530 | 10.980 | 11.080 | 10.100 | 8.360 | 5.920 | 6.370 | 7.710 | 9.250 |

### Vruchtenthee en fruitige thee

Doelpagina: /collections/vruchtenthee. Cluster in Search Console: 420 vertoningen, 0 klikken in 90 dagen, gemiddelde positie 35,2.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| hibiscus thee | 8.100 | HIGH | 53 | 17,7 | 45,3 | 0 | 0% | 8.082 | ja |
| citroenmelisse thee | 1.600 | HIGH | 16 | 5,3 | 32,2 | 0 | 0% | 1.595 | ja |
| citroengras thee | 320 | HIGH | 20 | 6,7 | 44,9 | 0 | 2% | 313 | ja |
| vruchten thee | 140 | HIGH | 27 | 9,0 | 33,1 | 0 | 6% | 131 | ja |
| aardbeien slagroom thee | 90 | HIGH | 63 | 21,0 | 22,4 | 0 | 23% | 69 | ja |
| vlierbessen thee | 90 | HIGH | 25 | 8,3 | 12,6 | 0 | 9% | 82 | ja |
| aardbeienthee | 50 | HIGH | 29 | 9,7 | 49,5 | 0 | 19% | 40 | ja |
| fruitige thee | 0 | UNSPECIFIED | 15 | 5,0 | 41,7 | 0 | - | 0 | ja |

Kerntotaal zoekvolume: 10.390 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer; 0 samengevoegd, 0 niet meegeteld). Vertoningen van de kernzoekwoorden: 82,7 per maand, aandeel zichtbaarheid 1%.

Seizoen (kernzoekwoorden): geen duidelijke piek (geen maand boven 125% van het gemiddelde); gemiddeld 9.890 per maand, op basis van 7 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 9.180 | 8.830 | 8.370 | 10.660 | 10.240 | 12.330 | 11.140 | 11.660 | 9.520 | 8.300 | 9.920 | 8.530 |

### Kruidenthee (kamille, munt, gember, salie)

Doelpagina: /collections/kruidenthee. Cluster in Search Console: 1.442 vertoningen, 2 klikken in 90 dagen, gemiddelde positie 41,5.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| kamille thee | 6.600 | HIGH | 55 | 18,3 | 46,6 | 0 | 0% | 6.582 | ja |
| salie thee | 2.400 | HIGH | 52 | 17,3 | 44,4 | 0 | 1% | 2.383 | ja |
| paardenbloem thee | 2.400 | HIGH | 38 | 12,7 | 48,7 | 0 | 1% | 2.387 | ja |
| kurkuma thee | 1.900 | HIGH | 38 | 12,7 | 47,7 | 0 | 1% | 1.887 | ja |
| pepermunt thee | 1.600 | HIGH | 44 | 14,7 | 44,8 | 0 | 1% | 1.585 | ja |
| fenegriek thee | 590 | HIGH | 40 | 13,3 | 45,9 | 0 | 2% | 577 | ja |
| cactus thee | 110 | HIGH | 114 | 38,0 | 20,1 | 0 | 35% | 72 | ja |
| cactusvijg thee | 40 | HIGH | 52 | 17,3 | 22,5 | 0 | 43% | 23 | ja |

Kerntotaal zoekvolume: 15.640 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer; 0 samengevoegd, 0 niet meegeteld). Vertoningen van de kernzoekwoorden: 144,3 per maand, aandeel zichtbaarheid 1%.

Seizoen (kernzoekwoorden): piek in januari 2026 (19.130, 129% van gemiddeld); gemiddeld 14.879 per maand, op basis van 8 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 16.660 | 15.670 | 15.550 | 19.130 | 15.940 | 16.280 | 18.320 | 14.800 | 10.700 | 10.380 | 12.020 | 13.100 |

### Smaakthee en seizoensthee

Doelpagina: /collections/thee. Cluster in Search Console: 319 vertoningen, 4 klikken in 90 dagen, gemiddelde positie 35,3.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| chai thee | 1.300 | HIGH | 16 | 5,3 | 45,8 | 0 | 0% | 1.295 | ja |
| kaneel thee | 480 | HIGH | 23 | 7,7 | 54,1 | 0 | 2% | 472 | ja |
| winter thee | 260 | HIGH | 16 | 5,3 | 47,0 | 0 | 2% | 255 | ja |
| chocolade thee | 170 | HIGH | 13 | 4,3 | 46,2 | 0 | 3% | 166 | ja |
| speculaas thee | 110 | HIGH | 63 | 21,0 | 20,5 | 0 | 19% | 89 | ja |
| speculaasmix | 110 | HIGH | 14 | 4,7 | 21,1 | 0 | 4% | 105 | ja |
| thee kerstpakket | 70 | HIGH | 18 | 6,0 | 43,9 | 0 | 9% | 64 | ja |
| yogi tea curcuma chai losse thee | 20 | UNSPECIFIED | 26 | 8,7 | 50,2 | 0 | 43% | 11 | ja |

Kerntotaal zoekvolume: 2.520 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer; 0 samengevoegd, 0 niet meegeteld). Vertoningen van de kernzoekwoorden: 63,0 per maand, aandeel zichtbaarheid 2%.

Seizoen (kernzoekwoorden): piek in november 2025 (5.060, 189% van gemiddeld), oktober 2025 (4.640, 173% van gemiddeld), december 2025 (4.430, 165% van gemiddeld); gemiddeld 2.678 per maand, op basis van 8 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 4.640 | 5.060 | 4.430 | 3.480 | 2.270 | 2.190 | 1.630 | 1.760 | 1.170 | 1.170 | 1.630 | 2.700 |

### Thee longtail: gezondheid, soorten en overig (informatief)

Doelpagina: /collections/thee. Cluster in Search Console: 1.204 vertoningen, 1 klikken in 90 dagen, gemiddelde positie 40,1.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| mate thee | 2.400 | HIGH | 32 | 10,7 | 44,5 | 0 | 0% | 2.389 | ja |
| marokkaanse thee | 1.900 | HIGH | 18 | 6,0 | 44,0 | 0 | 0% | 1.894 | ja |
| cafeïnevrije thee | 1.000 | HIGH | 66 | 22,0 | 45,2 | 0 | 2% | 978 | ja |
| cafeïne thee | 590 | LOW | 20 | 6,7 | 41,9 | 0 | 1% | 583 | ja |
| tastea thee | 50 | HIGH | 15 | 5,0 | 51,3 | 0 | 10% | 45 | ja |
| gezonde theesoorten | 10 | HIGH | 23 | 7,7 | 49,0 | 0 | 77% | 2 | ja |
| peper thee | 10 | HIGH | 17 | 5,7 | 24,9 | 0 | 57% | 4 | ja |
| theemix | 10 | HIGH | 17 | 5,7 | 7,6 | 0 | 57% | 4 | ja |

Kerntotaal zoekvolume: 5.970 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer; 0 samengevoegd, 0 niet meegeteld). Vertoningen van de kernzoekwoorden: 69,3 per maand, aandeel zichtbaarheid 1%.

Seizoen (kernzoekwoorden): piek in januari 2026 (7.900, 130% van gemiddeld); gemiddeld 6.072 per maand, op basis van 8 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 7.400 | 7.440 | 7.080 | 7.900 | 6.910 | 6.600 | 5.350 | 5.140 | 4.680 | 4.620 | 4.260 | 5.490 |

### Engelstalig: 'tea'

Doelpagina: /collections/thee. Cluster in Search Console: 949 vertoningen, 1 klikken in 90 dagen, gemiddelde positie 5,6.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| tea | - | - | 890 | 296,7 | 5,2 | 0 | - | - | - |
| herbal tea | - | - | 4 | 1,3 | 5,5 | 0 | - | - | - |
| high tea borne | - | - | 4 | 1,3 | 54,2 | 0 | - | - | - |
| ice tea maken met losse thee | - | - | 3 | 1,0 | 9,0 | 0 | - | - | - |
| tea eggs near me | - | - | 3 | 1,0 | 1,0 | 0 | - | - | - |
| white tea | - | - | 3 | 1,0 | 7,0 | 0 | - | - | - |
| chinese tea | - | - | 2 | 0,7 | 1,0 | 0 | - | - | - |
| dutch tea | - | - | 2 | 0,7 | 3,5 | 0 | - | - | - |

Geen zoekwoord van dit cluster staat in de volumebestanden; het volume is onbekend.

Seizoen (kernzoekwoorden): geen maandcijfers in de bestanden.

### Productnamen en cadeau-mokken (long tail op productpagina's)

Doelpagina: -. Cluster in Search Console: 588 vertoningen, 7 klikken in 90 dagen, gemiddelde positie 20,2.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| kir | 1.900 | LOW | 14 | 4,7 | 8,8 | 0 | 0% | 1.895 | ja |
| you did it | 880 | HIGH | 38 | 12,7 | 9,9 | 0 | 1% | 867 | ja |
| kitchen queen | 390 | LOW | 21 | 7,0 | 8,1 | 0 | 2% | 383 | ja |
| spice up your life | 210 | LOW | 30 | 10,0 | 10,8 | 0 | 5% | 200 | ja |
| superbedankt | 140 | LOW | 24 | 8,0 | 10,0 | 0 | 6% | 132 | ja |
| super juf | 110 | HIGH | 15 | 5,0 | 7,2 | 0 | 5% | 105 | ja |
| christa mulder | 50 | LOW | 19 | 6,3 | 6,6 | 2 | 13% | 44 | ja |
| jij bent top | 30 | MEDIUM | 25 | 8,3 | 6,8 | 0 | 28% | 22 | ja |

Kerntotaal zoekvolume: 3.710 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer; 0 samengevoegd, 0 niet meegeteld). Vertoningen van de kernzoekwoorden: 62,0 per maand, aandeel zichtbaarheid 2%.

Seizoen (kernzoekwoorden): piek in juni 2026 (4.920, 135% van gemiddeld); gemiddeld 3.634 per maand, op basis van 8 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 3.910 | 3.350 | 4.260 | 3.780 | 3.230 | 3.420 | 3.390 | 3.760 | 4.920 | 3.790 | 2.900 | 2.900 |

### Overig non-brand (niet ingedeeld)

Doelpagina: -. Cluster in Search Console: 710 vertoningen, 10 klikken in 90 dagen, gemiddelde positie 20,2.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| arie borne | 10 | LOW | 21 | 7,0 | 7,1 | 0 | 70% | 3 | ja |
| schutting borne | 10 | MEDIUM | 10 | 3,3 | 43,7 | 0 | 33% | 7 | ja |
| engelse serre | - | - | 15 | 5,0 | 36,0 | 0 | - | - | - |
| koffiezetapparaat | - | - | 14 | 4,7 | 5,5 | 0 | - | - | - |
| waarde | - | - | 12 | 4,0 | 11,0 | 0 | - | - | - |
| ja | - | - | 11 | 3,7 | 8,1 | 0 | - | - | - |
| r i e | - | - | 11 | 3,7 | 23,9 | 0 | - | - | - |
| chocolade | - | - | 9 | 3,0 | 3,6 | 0 | - | - | - |

Kerntotaal zoekvolume: 20 per maand over 2 van 8 zoekwoorden (bovengrens, zie leeswijzer; 0 samengevoegd, 0 niet meegeteld). Vertoningen van de kernzoekwoorden: 10,3 per maand, aandeel zichtbaarheid 52%.

Seizoen (kernzoekwoorden): piek in september 2026 (80, 457% van gemiddeld); gemiddeld 18 per maand, op basis van 2 van 2 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 10 | 10 | 10 | 10 | 10 | 10 | 20 | 20 | 10 | 10 | 10 | 80 |

### Lokaal: Borne, Twente en omgeving

Doelpagina: /pages/theewinkel-borne-twente. Cluster in Search Console: 423 vertoningen, 6 klikken in 90 dagen.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand | Telt mee |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| winkels in borne | 720 | LOW | 8 | 2,7 | 10,6 | 0 | 0% | 717 | ja |
| winkel borne | 70 | LOW | 49 | 16,3 | 10,3 | 0 | 23% | 54 | ja |
| kookwinkel twente | 50 | LOW | 62 | 20,7 | 3,9 | 3 | 41% | 29 | ja |
| beste van borne | 50 | LOW | 16 | 5,3 | 7,9 | 0 | 11% | 45 | ja |
| theewinkel enschede | 50 | MEDIUM | 12 | 4,0 | 20,2 | 0 | 8% | 46 | ja |
| kookwinkel almelo | 50 | LOW | 8 | 2,7 | 2,9 | 0 | 5% | 47 | ja |
| koffie borne | 40 | LOW | 6 | 2,0 | 5,7 | 0 | 5% | 38 | ja |
| kruidenwinkel borne | 30 | LOW | 58 | 19,3 | 6,2 | 1 | 64% | 11 | ja |
| toko borne | 30 | LOW | 12 | 4,0 | 8,1 | 0 | 13% | 26 | ja |
| natuurwinkel borne | 20 | LOW | 24 | 8,0 | 10,2 | 0 | 40% | 12 | ja |
| borne winkel | 20 | LOW | 21 | 7,0 | 8,3 | 1 | 35% | 13 | ja |
| kookwinkel borne | 20 | LOW | 11 | 3,7 | 1,5 | 1 | 18% | 16 | ja |
| thee uit twente | 0 | UNSPECIFIED | 94 | 31,3 | 7,0 | 0 | - | 0 | ja |
| winkels borne | - | - | 29 | 9,7 | 23,7 | 0 | - | - | - |
| borne winkels | - | - | 13 | 4,3 | 27,7 | 0 | - | - | - |

Kerntotaal zoekvolume: 1.150 per maand over 13 van 15 zoekwoorden (bovengrens, zie leeswijzer; 0 samengevoegd, 0 niet meegeteld). Vertoningen van de kernzoekwoorden: 127,0 per maand, aandeel zichtbaarheid 11%.

Seizoen (kernzoekwoorden): piek in december 2025 (1.420, 130% van gemiddeld), april 2026 (1.410, 129% van gemiddeld); gemiddeld 1.091 per maand, op basis van 12 van 13 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 1.360 | 1.130 | 1.420 | 1.110 | 960 | 1.020 | 1.410 | 1.050 | 760 | 730 | 1.070 | 1.070 |

## Zoekwoorden met volume die in geen cluster staan

Bijvoorbeeld uit de actie ideeen of uit zoekwoorden buiten de bijlage. Mogelijke nieuwe clusters of ondersteunende zoekwoorden; indelen vraagt een beslissing van de zoekwoordonderzoeker.

| Zoekwoord | Volume/maand | Concurrentie |
|---|---:|---|
| serviessets | 14.800 | HIGH |
| hk living koffiekopjes | 14.800 | HIGH |
| theepot | 9.900 | HIGH |
| hk living mok | 3.600 | HIGH |
| bredemeijer theepot | 2.400 | HIGH |
| servies ikea | 2.400 | HIGH |
| dubbelwandige theepot | 1.900 | HIGH |
| theepot met warmhouder | 1.900 | HIGH |
| theepot dubbelwandig | 1.900 | HIGH |
| theepot warmhouder | 1.900 | HIGH |
| melamine servies | 1.600 | HIGH |
| theepot met filter | 1.600 | HIGH |
| glazen theepot | 1.600 | HIGH |
| kop en schotel | 1.600 | HIGH |
| koffiekopjes xenos | 1.600 | HIGH |
| thee adventskalender | 1.300 | HIGH |
| marokkaanse theepot | 1.300 | HIGH |
| koffiekopjes zonder oor | 1.300 | HIGH |
| theepot action | 1.300 | HIGH |
| wijnglazen xenos | 1.300 | HIGH |
| theecadeau | 1.000 | HIGH |
| hkliving theepot | 1.000 | HIGH |
| hk living theepot | 1.000 | HIGH |
| theepot hema | 1.000 | HIGH |
| hema theepot | 1.000 | HIGH |
| bo camp servies | 880 | HIGH |
| melamine borden | 880 | HIGH |
| gietijzeren theepot | 880 | HIGH |
| theekan | 880 | HIGH |
| theepot gietijzer | 880 | HIGH |
| adventskalender thee | 720 | HIGH |
| servies zwart | 720 | HIGH |
| pickwick adventskalender | 720 | HIGH |
| servies winkel | 720 | HIGH |
| hkliving kopjes | 720 | HIGH |
| blond mok | 720 | HIGH |
| douwe egberts kopjes | 720 | HIGH |
| blond amsterdam theepot | 720 | HIGH |
| theepot blond amsterdam | 720 | HIGH |
| servies aanbieding | 590 | HIGH |

En 155 zoekwoorden met een lager volume; zie het JSON-bestand.

