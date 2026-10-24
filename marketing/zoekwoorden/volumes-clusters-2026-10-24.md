# Zoekvolumes per cluster

Gegenereerd door scripts/volumes_in_clusters.py. Volumes: Google Keyword Planner via scripts/zoekvolumes.py (Nederlands, Nederland). Vertoningen, klikken en posities: Search Console, 90 dagen, uit de clustertabellen. Een zoekwoord zonder volume in de bestanden blijft leeg en telt niet mee.

Bronbestanden: data/keyword-planner/2026-10-24-ideeen-seeds.json, data/keyword-planner/2026-10-24-invoerlijst.json, data/keyword-planner/2026-10-24-zoekvolumes.json

Leeswijzer:

- Vert./maand is het 90-daagse aantal vertoningen gedeeld door 3.
- Aandeel zichtbaarheid is vert./maand gedeeld door het maandvolume van hetzelfde zoekwoord. Een hoog aandeel op een lage positie betekent dat de pagina al vaak getoond wordt; een laag aandeel op een goede positie wijst op weinig vertoningen ten opzichte van de vraag.
- De bijlage in het clusterrapport bevat alleen de top zoekwoorden per cluster, dus de som van de zoekwoorden is lager dan het clustertotaal in de tabel Clusters.
- Keyword Planner voegt dicht bij elkaar liggende varianten samen (bijvoorbeeld ricedk en rice dk). Dezelfde zoekers kunnen dan in meer dan een regel zitten, waardoor het clustertotaal te hoog kan uitvallen. Het totaal is dus een bovengrens, geen exacte som.

## Overzicht

| Cluster | Doelpagina | Zoekwoorden met volume | Volume/maand (som) | Vert./maand (zoekwoorden met volume) | Aandeel zichtbaarheid | Vert. 90d (heel cluster) | Pos. cluster |
|---|---|---:|---:|---:|---:|---:|---:|
| Bunzlau Castle en Bunzlau servies | /collections/bunzlau | 8 van 8 | 9.450 | 654 | 7% | 4.030 | 19,8 |
| Pools aardewerk en pools servies (generiek) | /collections/bunzlau | 8 van 8 | 1.980 | 90 | 5% | 276 | 35,1 |
| Muuss en Joeff (wanddecoratie) | /collections/joeff | 8 van 8 | 1.550 | 438 | 28% | 1.343 | 7,8 |
| Rice DK en Rice by Rice | /collections/rice | 6 van 8 | 990 | 343 | 35% | 1.893 | 15,9 |
| Blond Amsterdam servies | /pages/blond-amsterdam-servies | 8 van 8 | 6.530 | 132 | 2% | 777 | 10,2 |
| Natural Flower Cards | /collections/nfc-natural-flower-cards | 3 van 4 | 370 | 65 | 18% | 217 | 6,9 |
| Pineut Water Twist en Delfts blauw waterfles | /products/waterfles-delfts-blauw | 8 van 8 | 480 | 100 | 21% | 347 | 9,9 |
| Sterrenmunt | /products/sterrenmunt | 8 van 8 | 1.690 | 66 | 4% | 220 | 21,0 |
| Thee voor bedrijven, kantoor en horeca (zakelijk) | /pages/zakelijk | 0 van 8 | - | - | - | 2.156 | 37,2 |
| Theewinkel (generiek en lokaal) | /pages/theewinkel-borne-twente | 8 van 8 | 6.000 | 352 | 6% | 1.598 | 13,3 |
| Thee bewaarblik en theeblikken | /collections/thee-bewaarblikken | 6 van 8 | 1.610 | 204 | 13% | 1.073 | 21,5 |
| Proefpakket en kennismaken met thee | /collections/proefpakketten | 6 van 8 | 1.050 | 196 | 19% | 743 | 37,2 |
| Koude thee, cold brew en ijsthee | /pages/cold-brew-thee | 8 van 8 | 1.260 | 129 | 10% | 468 | 24,6 |
| Thee cadeau en theegeschenk | /pages/thee-cadeau | 8 van 8 | 2.530 | 59 | 2% | 532 | 40,9 |
| Thee accessoires (zeefje, schep, maatlepel, toren) | /collections/thee-accessoires | 8 van 8 | 440 | 218 | 50% | 1.266 | 34,3 |
| Thee kopen en losse thee (hoofdzoekwoorden) | /collections/thee | 8 van 8 | 21.330 | 252 | 1% | 2.087 | 41,7 |
| Servies, mokken en bekers (generiek) | /pages/serviezen | 7 van 8 | 30.620 | 95 | 0% | 658 | 11,5 |
| Taart, bakmixen en bakken | /collections/bakmixen | 8 van 8 | 7.400 | 66 | 1% | 239 | 11,8 |
| Groene, witte en oolong thee en matcha | /collections/groene-thee | 8 van 8 | 11.480 | 152 | 1% | 937 | 42,4 |
| Zwarte thee (assam, ceylon, earl grey) | /collections/zwarte-thee | 7 van 8 | 4.780 | 56 | 1% | 315 | 36,5 |
| Rooibos en honeybush | /collections/rooibos | 8 van 8 | 9.090 | 92 | 1% | 314 | 27,9 |
| Vruchtenthee en fruitige thee | /collections/vruchtenthee | 8 van 8 | 10.390 | 83 | 1% | 420 | 35,2 |
| Kruidenthee (kamille, munt, gember, salie) | /collections/kruidenthee | 8 van 8 | 15.640 | 144 | 1% | 1.442 | 41,5 |
| Smaakthee en seizoensthee | /collections/thee | 8 van 8 | 2.520 | 63 | 2% | 319 | 35,3 |
| Thee longtail: gezondheid, soorten en overig (informatief) | /collections/thee | 8 van 8 | 5.970 | 69 | 1% | 1.204 | 40,1 |
| Engelstalig: 'tea' | /collections/thee | 0 van 8 | - | - | - | 949 | 5,6 |
| Productnamen en cadeau-mokken (long tail op productpagina's) | - | 8 van 8 | 3.710 | 62 | 2% | 588 | 20,2 |
| Overig non-brand (niet ingedeeld) | - | 2 van 8 | 20 | 10 | 52% | 710 | 20,2 |
| Lokaal: Borne, Twente en omgeving | /pages/theewinkel-borne-twente | 13 van 15 | 1.150 | 127 | 11% | 423 | - |

## Per cluster

### Bunzlau Castle en Bunzlau servies

Doelpagina: /collections/bunzlau. Cluster in Search Console: 4.030 vertoningen, 29 klikken in 90 dagen, gemiddelde positie 19,8.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| bunzlau castle | 5.400 | HIGH | 600 | 200,0 | 20,1 | 2 | 4% | 5.200 |
| bunzlau servies | 1.900 | HIGH | 325 | 108,3 | 15,3 | 4 | 6% | 1.792 |
| bunzlau | 1.600 | HIGH | 411 | 137,0 | 15,3 | 3 | 9% | 1.463 |
| bunzlau castle servies | 320 | HIGH | 104 | 34,7 | 21,2 | 0 | 11% | 285 |
| bunzlau castle mokken | 110 | HIGH | 160 | 53,3 | 25,3 | 0 | 48% | 57 |
| bunzlau servies kopen in polen | 90 | HIGH | 118 | 39,3 | 10,6 | 2 | 44% | 51 |
| bunzlau castle borden | 20 | HIGH | 146 | 48,7 | 27,1 | 0 | 243% | 0 |
| bunzlau thee | 10 | HIGH | 97 | 32,3 | 13,2 | 0 | 323% | 0 |

Totaal zoekvolume: 9.450 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: 653,7 per maand, aandeel zichtbaarheid 7%.

Seizoen: piek in december 2025 (15.990, 160% van gemiddeld), november 2025 (13.470, 135% van gemiddeld); gemiddeld 9.990 per maand, op basis van 8 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 9.310 | 13.470 | 15.990 | 11.160 | 8.080 | 9.440 | 8.730 | 9.140 | 7.700 | 7.450 | 9.500 | 9.910 |

### Pools aardewerk en pools servies (generiek)

Doelpagina: /collections/bunzlau. Cluster in Search Console: 276 vertoningen, 1 klikken in 90 dagen, gemiddelde positie 35,1.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| pools servies | 720 | HIGH | 81 | 27,0 | 38,2 | 0 | 4% | 693 |
| pools serviesgoed | 720 | HIGH | 4 | 1,3 | 29,2 | 0 | 0% | 719 |
| pools aardewerk | 320 | HIGH | 74 | 24,7 | 45,8 | 0 | 8% | 295 |
| pools servies sale | 110 | HIGH | 6 | 2,0 | 18,7 | 0 | 2% | 108 |
| pools aardewerk verkooppunten | 50 | HIGH | 8 | 2,7 | 11,8 | 1 | 5% | 47 |
| pools aardewerk theepot | 30 | MEDIUM | 26 | 8,7 | 19,4 | 0 | 29% | 21 |
| pools aardewerk mokken | 20 | HIGH | 24 | 8,0 | 29,6 | 0 | 40% | 12 |
| pools aardewerk servies | 10 | LOW | 47 | 15,7 | 32,4 | 0 | 157% | 0 |

Totaal zoekvolume: 1.980 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: 90,0 per maand, aandeel zichtbaarheid 5%.

Seizoen: piek in november 2025 (2.700, 131% van gemiddeld), december 2025 (2.690, 131% van gemiddeld); gemiddeld 2.058 per maand, op basis van 8 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 2.290 | 2.700 | 2.690 | 2.380 | 1.930 | 1.970 | 1.650 | 2.180 | 1.530 | 1.640 | 2.010 | 1.720 |

### Muuss en Joeff (wanddecoratie)

Doelpagina: /collections/joeff. Cluster in Search Console: 1.343 vertoningen, 31 klikken in 90 dagen, gemiddelde positie 7,8.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| joeff | 880 | LOW | 354 | 118,0 | 8,5 | 1 | 13% | 762 |
| muuss | 390 | LOW | 632 | 210,7 | 7,2 | 21 | 54% | 179 |
| luminlique | 90 | MEDIUM | 45 | 15,0 | 7,0 | 3 | 17% | 75 |
| muuss galerijwand | 70 | LOW | 44 | 14,7 | 9,5 | 1 | 21% | 55 |
| joeff muuss | 50 | LOW | 155 | 51,7 | 8,2 | 3 | 103% | 0 |
| muuss joeff | 40 | LOW | 28 | 9,3 | 8,0 | 1 | 23% | 31 |
| muuss wanddecoratie | 20 | MEDIUM | 19 | 6,3 | 9,6 | 0 | 32% | 14 |
| muuss verkooppunten | 10 | LOW | 36 | 12,0 | 6,0 | 0 | 120% | 0 |

Totaal zoekvolume: 1.550 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: 437,7 per maand, aandeel zichtbaarheid 28%.

Seizoen: piek in november 2025 (2.240, 155% van gemiddeld), oktober 2025 (1.840, 127% van gemiddeld), december 2025 (1.810, 125% van gemiddeld); gemiddeld 1.448 per maand, op basis van 8 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 1.840 | 2.240 | 1.810 | 1.650 | 1.340 | 1.550 | 1.150 | 1.220 | 930 | 930 | 1.310 | 1.400 |

### Rice DK en Rice by Rice

Doelpagina: /collections/rice. Cluster in Search Console: 1.893 vertoningen, 3 klikken in 90 dagen, gemiddelde positie 15,9.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| ricebyrice | 480 | HIGH | 214 | 71,3 | 8,6 | 0 | 15% | 409 |
| rice dk | 390 | HIGH | 495 | 165,0 | 22,6 | 1 | 42% | 225 |
| rice denmark | 50 | HIGH | 91 | 30,3 | 18,9 | 0 | 61% | 20 |
| rice beker l | 30 | HIGH | 85 | 28,3 | 7,4 | 1 | 94% | 2 |
| rice beker m | 30 | HIGH | 59 | 19,7 | 7,7 | 0 | 66% | 10 |
| rice webshop | 10 | HIGH | 84 | 28,0 | 19,4 | 0 | 280% | 0 |
| ricedk | - | - | 129 | 43,0 | 9,4 | 0 | - | - |
| rice by rice | - | - | 60 | 20,0 | 24,3 | 0 | - | - |

Totaal zoekvolume: 990 per maand over 6 van 8 zoekwoorden (bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: 342,7 per maand, aandeel zichtbaarheid 35%.

Seizoen: piek in mei 2026 (1.340, 125% van gemiddeld); gemiddeld 1.070 per maand, op basis van 6 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 960 | 930 | 1.020 | 1.220 | 830 | 1.130 | 1.110 | 1.340 | 960 | 1.200 | 1.220 | 920 |

### Blond Amsterdam servies

Doelpagina: /pages/blond-amsterdam-servies. Cluster in Search Console: 777 vertoningen, 1 klikken in 90 dagen, gemiddelde positie 10,2.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| blond | 5.400 | LOW | 44 | 14,7 | 7,8 | 0 | 0% | 5.385 |
| blond amsterdam servies | 480 | HIGH | 53 | 17,7 | 8,9 | 0 | 4% | 462 |
| servies blond amsterdam | 390 | HIGH | 53 | 17,7 | 9,7 | 0 | 5% | 372 |
| kan blond amsterdam in de vaatwasser | 110 | LOW | 85 | 28,3 | 8,3 | 0 | 26% | 82 |
| servies blond | 70 | HIGH | 36 | 12,0 | 10,3 | 0 | 17% | 58 |
| kan blond amsterdam servies in de vaatwasser | 40 | LOW | 49 | 16,3 | 8,6 | 0 | 41% | 24 |
| kan blond amsterdam in de magnetron | 30 | LOW | 33 | 11,0 | 6,3 | 0 | 37% | 19 |
| mag blond amsterdam servies in de vaatwasser | 10 | LOW | 43 | 14,3 | 8,7 | 0 | 143% | 0 |

Totaal zoekvolume: 6.530 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: 132,0 per maand, aandeel zichtbaarheid 2%.

Seizoen: geen duidelijke piek (geen maand boven 125% van het gemiddelde); gemiddeld 6.652 per maand, op basis van 8 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 7.630 | 7.930 | 7.190 | 6.420 | 7.130 | 6.560 | 6.120 | 7.890 | 5.130 | 5.050 | 6.320 | 6.460 |

### Natural Flower Cards

Doelpagina: /collections/nfc-natural-flower-cards. Cluster in Search Console: 217 vertoningen, 1 klikken in 90 dagen, gemiddelde positie 6,9.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| natural flower cards | 170 | LOW | 157 | 52,3 | 6,7 | 1 | 31% | 118 |
| naturalflowercards | 110 | LOW | 37 | 12,3 | 8,5 | 0 | 11% | 98 |
| natural flowers | 90 | MEDIUM | 1 | 0,3 | 3,0 | 0 | 0% | 90 |
| natural flowercards | - | - | 22 | 7,3 | 5,9 | 0 | - | - |

Totaal zoekvolume: 370 per maand over 3 van 4 zoekwoorden (bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: 65,0 per maand, aandeel zichtbaarheid 18%.

Seizoen: piek in januari 2026 (520, 140% van gemiddeld), september 2026 (470, 126% van gemiddeld); gemiddeld 372 per maand, op basis van 3 van 4 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 440 | 340 | 420 | 520 | 370 | 390 | 340 | 320 | 250 | 290 | 320 | 470 |

### Pineut Water Twist en Delfts blauw waterfles

Doelpagina: /products/waterfles-delfts-blauw. Cluster in Search Console: 347 vertoningen, 1 klikken in 90 dagen, gemiddelde positie 9,9.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| watertwist | 140 | HIGH | 33 | 11,0 | 6,5 | 0 | 8% | 129 |
| water twist | 140 | HIGH | 17 | 5,7 | 12,6 | 0 | 4% | 134 |
| waterfles delfts blauw | 50 | HIGH | 56 | 18,7 | 12,1 | 0 | 37% | 31 |
| pineut water twist | 50 | HIGH | 45 | 15,0 | 8,1 | 0 | 30% | 35 |
| delfts blauw waterfles | 40 | HIGH | 44 | 14,7 | 11,7 | 0 | 37% | 25 |
| water scoop | 20 | HIGH | 49 | 16,3 | 8,7 | 0 | 82% | 4 |
| delfts blauw drinkfles | 20 | HIGH | 36 | 12,0 | 8,5 | 0 | 60% | 8 |
| drinkfles delfts blauw | 20 | HIGH | 21 | 7,0 | 12,2 | 0 | 35% | 13 |

Totaal zoekvolume: 480 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: 100,3 per maand, aandeel zichtbaarheid 21%.

Seizoen: piek in juni 2026 (1.220, 257% van gemiddeld), mei 2026 (920, 194% van gemiddeld), juli 2026 (830, 175% van gemiddeld); gemiddeld 474 per maand, op basis van 8 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 240 | 290 | 360 | 280 | 230 | 300 | 280 | 920 | 1.220 | 830 | 490 | 250 |

### Sterrenmunt

Doelpagina: /products/sterrenmunt. Cluster in Search Console: 220 vertoningen, 0 klikken in 90 dagen, gemiddelde positie 21,0.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| sterrenmunt | 880 | HIGH | 32 | 10,7 | 13,7 | 0 | 1% | 869 |
| sterrenmunt thee gezond | 260 | LOW | 35 | 11,7 | 39,2 | 0 | 4% | 248 |
| sterrenmix thee | 260 | HIGH | 27 | 9,0 | 50,4 | 0 | 3% | 251 |
| sterrenmunt thee bloeddruk | 110 | LOW | 10 | 3,3 | 16,3 | 0 | 3% | 107 |
| waar is sterrenmunt thee goed voor | 70 | LOW | 17 | 5,7 | 11,8 | 0 | 8% | 64 |
| wat is sterrenmunt | 40 | LOW | 46 | 15,3 | 6,2 | 0 | 38% | 25 |
| wat zit er in sterrenmunt thee | 40 | LOW | 7 | 2,3 | 7,3 | 0 | 6% | 38 |
| sterrenmunt bloeddruk | 30 | LOW | 25 | 8,3 | 8,6 | 0 | 28% | 22 |

Totaal zoekvolume: 1.690 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: 66,3 per maand, aandeel zichtbaarheid 4%.

Seizoen: piek in januari 2026 (2.510, 145% van gemiddeld), oktober 2025 (2.310, 134% van gemiddeld), november 2025 (2.290, 132% van gemiddeld); gemiddeld 1.729 per maand, op basis van 8 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 2.310 | 2.290 | 1.980 | 2.510 | 1.890 | 1.750 | 1.410 | 1.390 | 1.060 | 1.070 | 1.300 | 1.790 |

### Thee voor bedrijven, kantoor en horeca (zakelijk)

Doelpagina: /pages/zakelijk. Cluster in Search Console: 2.156 vertoningen, 0 klikken in 90 dagen, gemiddelde positie 37,2.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| thee op kantoor | - | - | 325 | 108,3 | 47,3 | 0 | - | - |
| thee kantoor | - | - | 196 | 65,3 | 38,7 | 0 | - | - |
| thee op het werk | - | - | 190 | 63,3 | 65,2 | 0 | - | - |
| thee inkopen voor wederverkoop | - | - | 109 | 36,3 | 39,9 | 0 | - | - |
| thee zakelijk | - | - | 98 | 32,7 | 27,2 | 0 | - | - |
| thee voor hotels | - | - | 88 | 29,3 | 21,8 | 0 | - | - |
| losse thee horeca | - | - | 77 | 25,7 | 23,8 | 0 | - | - |
| zakelijke thee | - | - | 75 | 25,0 | 30,5 | 0 | - | - |

Geen zoekwoord van dit cluster staat in de volumebestanden; het volume is onbekend.

Seizoen: geen maandcijfers in de bestanden.

### Theewinkel (generiek en lokaal)

Doelpagina: /pages/theewinkel-borne-twente. Cluster in Search Console: 1.598 vertoningen, 22 klikken in 90 dagen, gemiddelde positie 13,3.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| theewinkel | 2.900 | HIGH | 569 | 189,7 | 12,0 | 5 | 7% | 2.710 |
| thee winkel | 2.900 | HIGH | 128 | 42,7 | 17,1 | 1 | 1% | 2.857 |
| winkel borne | 70 | LOW | 49 | 16,3 | 10,3 | 0 | 23% | 54 |
| kookwinkel twente | 50 | LOW | 62 | 20,7 | 3,9 | 3 | 41% | 29 |
| theewinkel opende | 50 | LOW | 52 | 17,3 | 8,0 | 0 | 35% | 33 |
| kruidenwinkel borne | 30 | LOW | 58 | 19,3 | 6,2 | 1 | 64% | 11 |
| thee uit twente | 0 | UNSPECIFIED | 94 | 31,3 | 7,0 | 0 | - | 0 |
| telvrije winkel | 0 | UNSPECIFIED | 43 | 14,3 | 43,1 | 0 | - | 0 |

Totaal zoekvolume: 6.000 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: 351,7 per maand, aandeel zichtbaarheid 6%.

Seizoen: piek in december 2025 (9.060, 157% van gemiddeld), oktober 2025 (7.420, 128% van gemiddeld), november 2025 (7.420, 128% van gemiddeld); gemiddeld 5.785 per maand, op basis van 6 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 7.420 | 7.420 | 9.060 | 7.370 | 5.940 | 5.980 | 3.950 | 4.990 | 3.370 | 3.930 | 5.000 | 4.990 |

### Thee bewaarblik en theeblikken

Doelpagina: /collections/thee-bewaarblikken. Cluster in Search Console: 1.073 vertoningen, 4 klikken in 90 dagen, gemiddelde positie 21,5.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| thee blikjes | 590 | HIGH | 121 | 40,3 | 29,7 | 0 | 7% | 550 |
| theeblikjes voor losse thee | 480 | HIGH | 102 | 34,0 | 23,6 | 2 | 7% | 446 |
| thee bewaarblik | 210 | HIGH | 240 | 80,0 | 12,1 | 0 | 38% | 130 |
| thee koker | 210 | HIGH | 38 | 12,7 | 9,0 | 0 | 6% | 197 |
| losse thee blikjes | 90 | HIGH | 75 | 25,0 | 32,2 | 0 | 28% | 65 |
| bewaarblik rechthoekig | 30 | HIGH | 36 | 12,0 | 2,6 | 0 | 40% | 18 |
| thee blikken | - | - | 116 | 38,7 | 29,4 | 0 | - | - |
| theeblikken voor losse thee | - | - | 72 | 24,0 | 20,9 | 0 | - | - |

Totaal zoekvolume: 1.610 per maand over 6 van 8 zoekwoorden (bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: 204,0 per maand, aandeel zichtbaarheid 13%.

Seizoen: piek in december 2025 (2.240, 139% van gemiddeld), januari 2026 (2.190, 136% van gemiddeld); gemiddeld 1.612 per maand, op basis van 6 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 1.760 | 1.860 | 2.240 | 2.190 | 1.600 | 1.460 | 1.380 | 1.330 | 1.000 | 1.070 | 1.660 | 1.800 |

### Proefpakket en kennismaken met thee

Doelpagina: /collections/proefpakketten. Cluster in Search Console: 743 vertoningen, 0 klikken in 90 dagen, gemiddelde positie 37,2.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| thee pakketten | 720 | HIGH | 35 | 11,7 | 47,5 | 0 | 2% | 708 |
| proefpakket thee | 110 | HIGH | 232 | 77,3 | 36,2 | 0 | 70% | 33 |
| thee proefpakket | 110 | HIGH | 181 | 60,3 | 38,0 | 0 | 55% | 50 |
| losse thee proefpakket | 50 | HIGH | 108 | 36,0 | 27,5 | 0 | 72% | 14 |
| luxe thee pakket | 50 | HIGH | 20 | 6,7 | 60,6 | 0 | 13% | 43 |
| theepakketten | 10 | HIGH | 13 | 4,3 | 37,0 | 0 | 43% | 6 |
| proefpakket - verrassing | - | - | 71 | 23,7 | 37,6 | 0 | - | - |
| thee pakket | - | - | 23 | 7,7 | 44,7 | 0 | - | - |

Totaal zoekvolume: 1.050 per maand over 6 van 8 zoekwoorden (bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: 196,3 per maand, aandeel zichtbaarheid 19%.

Seizoen: piek in december 2025 (2.330, 223% van gemiddeld), november 2025 (2.020, 193% van gemiddeld), oktober 2025 (1.450, 139% van gemiddeld); gemiddeld 1.046 per maand, op basis van 6 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 1.450 | 2.020 | 2.330 | 1.130 | 820 | 860 | 690 | 740 | 600 | 560 | 600 | 750 |

### Koude thee, cold brew en ijsthee

Doelpagina: /pages/cold-brew-thee. Cluster in Search Console: 468 vertoningen, 0 klikken in 90 dagen, gemiddelde positie 24,6.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| ijs thee | 1.000 | HIGH | 15 | 5,0 | 48,2 | 0 | 0% | 995 |
| koude thee | 140 | HIGH | 121 | 40,3 | 29,0 | 0 | 29% | 100 |
| thee voor koud water | 40 | HIGH | 96 | 32,0 | 22,8 | 0 | 80% | 8 |
| thee koud water | 30 | HIGH | 40 | 13,3 | 17,2 | 0 | 44% | 17 |
| koud water thee | 20 | HIGH | 26 | 8,7 | 17,1 | 0 | 43% | 11 |
| handybrew ijsthee | 10 | HIGH | 37 | 12,3 | 50,9 | 0 | 123% | 0 |
| cold brew thee kopen | 10 | HIGH | 32 | 10,7 | 16,1 | 0 | 107% | 0 |
| kan je thee maken met koud water | 10 | LOW | 20 | 6,7 | 7,3 | 0 | 67% | 3 |

Totaal zoekvolume: 1.260 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: 129,0 per maand, aandeel zichtbaarheid 10%.

Seizoen: piek in juni 2026 (2.070, 149% van gemiddeld); gemiddeld 1.388 per maand, op basis van 8 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 1.170 | 1.170 | 1.460 | 1.210 | 1.060 | 1.300 | 1.280 | 1.700 | 2.070 | 1.620 | 1.550 | 1.070 |

### Thee cadeau en theegeschenk

Doelpagina: /pages/thee-cadeau. Cluster in Search Console: 532 vertoningen, 2 klikken in 90 dagen, gemiddelde positie 40,9.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| thee cadeau | 1.000 | HIGH | 32 | 10,7 | 41,3 | 0 | 1% | 989 |
| thee als cadeau | 1.000 | HIGH | 20 | 6,7 | 54,1 | 0 | 1% | 993 |
| luxe thee cadeau set | 210 | HIGH | 28 | 9,3 | 41,4 | 0 | 4% | 201 |
| thee geschenkset | 140 | HIGH | 18 | 6,0 | 43,8 | 0 | 4% | 134 |
| geschenk thee | 90 | HIGH | 21 | 7,0 | 51,9 | 0 | 8% | 83 |
| thee kadootjes | 50 | HIGH | 20 | 6,7 | 57,3 | 0 | 13% | 43 |
| relatiegeschenk thee | 30 | HIGH | 18 | 6,0 | 35,5 | 0 | 20% | 24 |
| thee cadeau bezorgen | 10 | HIGH | 21 | 7,0 | 51,2 | 0 | 70% | 3 |

Totaal zoekvolume: 2.530 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: 59,3 per maand, aandeel zichtbaarheid 2%.

Seizoen: piek in december 2025 (7.040, 243% van gemiddeld), november 2025 (5.800, 200% van gemiddeld), oktober 2025 (4.060, 140% van gemiddeld); gemiddeld 2.902 per maand, op basis van 8 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 4.060 | 5.800 | 7.040 | 2.490 | 2.170 | 2.340 | 1.720 | 2.140 | 2.120 | 1.440 | 1.420 | 2.090 |

### Thee accessoires (zeefje, schep, maatlepel, toren)

Doelpagina: /collections/thee-accessoires. Cluster in Search Console: 1.266 vertoningen, 1 klikken in 90 dagen, gemiddelde positie 34,3.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| thee accessoires | 260 | HIGH | 186 | 62,0 | 46,3 | 0 | 24% | 198 |
| losse thee presentatie | 50 | HIGH | 87 | 29,0 | 35,6 | 0 | 58% | 21 |
| thee toren | 40 | HIGH | 35 | 11,7 | 28,9 | 0 | 29% | 28 |
| losse thee accessoires | 20 | HIGH | 121 | 40,3 | 44,5 | 0 | 202% | 0 |
| theezeefje rvs | 20 | HIGH | 39 | 13,0 | 11,1 | 0 | 65% | 7 |
| maatschepje 3 gram | 20 | HIGH | 36 | 12,0 | 6,6 | 0 | 60% | 8 |
| thee accessoires kopen | 20 | HIGH | 34 | 11,3 | 29,8 | 0 | 57% | 9 |
| leuke thee accessoires | 10 | HIGH | 116 | 38,7 | 53,5 | 0 | 387% | 0 |

Totaal zoekvolume: 440 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: 218,0 per maand, aandeel zichtbaarheid 50%.

Seizoen: piek in november 2025 (740, 175% van gemiddeld), december 2025 (660, 156% van gemiddeld), oktober 2025 (610, 144% van gemiddeld); gemiddeld 423 per maand, op basis van 8 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 610 | 740 | 660 | 500 | 420 | 360 | 360 | 370 | 290 | 160 | 270 | 340 |

### Thee kopen en losse thee (hoofdzoekwoorden)

Doelpagina: /collections/thee. Cluster in Search Console: 2.087 vertoningen, 6 klikken in 90 dagen, gemiddelde positie 41,7.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| thee | 14.800 | HIGH | 184 | 61,3 | 36,5 | 0 | 0% | 14.739 |
| losse thee | 2.900 | HIGH | 221 | 73,7 | 36,8 | 0 | 3% | 2.826 |
| losse thee kopen | 1.600 | HIGH | 45 | 15,0 | 27,6 | 1 | 1% | 1.585 |
| thee kopen | 880 | HIGH | 49 | 16,3 | 34,1 | 0 | 2% | 864 |
| biologische thee | 590 | HIGH | 95 | 31,7 | 46,9 | 0 | 5% | 558 |
| verse thee kopen | 480 | HIGH | 54 | 18,0 | 26,5 | 1 | 4% | 462 |
| thee blend | 50 | HIGH | 41 | 13,7 | 52,7 | 0 | 27% | 36 |
| thee zonder aroma | 30 | HIGH | 67 | 22,3 | 45,0 | 0 | 74% | 8 |

Totaal zoekvolume: 21.330 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: 252,0 per maand, aandeel zichtbaarheid 1%.

Seizoen: piek in oktober 2025 (56.820, 267% van gemiddeld); gemiddeld 21.279 per maand, op basis van 8 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 56.820 | 23.670 | 23.680 | 24.440 | 18.850 | 19.020 | 15.620 | 15.710 | 12.150 | 11.630 | 13.170 | 20.590 |

### Servies, mokken en bekers (generiek)

Doelpagina: /pages/serviezen. Cluster in Search Console: 658 vertoningen, 7 klikken in 90 dagen, gemiddelde positie 11,5.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| servies | 14.800 | HIGH | 85 | 28,3 | 6,4 | 2 | 0% | 14.772 |
| serviezen | 14.800 | HIGH | 38 | 12,7 | 9,5 | 0 | 0% | 14.787 |
| servies kopen | 880 | HIGH | 17 | 5,7 | 4,2 | 1 | 1% | 874 |
| melk mok | 70 | HIGH | 53 | 17,7 | 6,9 | 0 | 25% | 52 |
| beker melamine | 50 | HIGH | 18 | 6,0 | 28,8 | 0 | 12% | 44 |
| boeren mok | 20 | HIGH | 24 | 8,0 | 9,9 | 0 | 40% | 12 |
| tumbler mok | 0 | UNSPECIFIED | 49 | 16,3 | 8,5 | 0 | - | 0 |
| melk mokken | - | - | 17 | 5,7 | 7,8 | 0 | - | - |

Totaal zoekvolume: 30.620 per maand over 7 van 8 zoekwoorden (bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: 94,7 per maand, aandeel zichtbaarheid 0%.

Seizoen: piek in december 2025 (55.660, 168% van gemiddeld), november 2025 (45.890, 138% van gemiddeld); gemiddeld 33.229 per maand, op basis van 6 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 37.330 | 45.890 | 55.660 | 37.330 | 30.590 | 30.720 | 25.050 | 25.070 | 25.040 | 24.910 | 30.670 | 30.490 |

### Taart, bakmixen en bakken

Doelpagina: /collections/bakmixen. Cluster in Search Console: 239 vertoningen, 2 klikken in 90 dagen, gemiddelde positie 11,8.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| baking | 3.600 | LOW | 64 | 21,3 | 4,8 | 0 | 1% | 3.579 |
| bakwinkel | 1.900 | MEDIUM | 8 | 2,7 | 3,1 | 1 | 0% | 1.897 |
| bakzolder | 1.600 | LOW | 25 | 8,3 | 13,5 | 0 | 1% | 1.592 |
| dubai cake | 140 | LOW | 63 | 21,0 | 6,8 | 0 | 15% | 119 |
| paardenstaart thee | 110 | HIGH | 6 | 2,0 | 40,8 | 0 | 2% | 108 |
| aardbeien cake mix | 30 | HIGH | 4 | 1,3 | 20,2 | 0 | 4% | 29 |
| de bakzolder cakemix | 10 | LOW | 23 | 7,7 | 9,5 | 0 | 77% | 2 |
| dubi cakes | 10 | LOW | 6 | 2,0 | 11,0 | 0 | 20% | 8 |

Totaal zoekvolume: 7.400 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: 66,3 per maand, aandeel zichtbaarheid 1%.

Seizoen: piek in augustus 2026 (21.210, 279% van gemiddeld); gemiddeld 7.590 per maand, op basis van 8 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 6.330 | 7.030 | 7.710 | 6.180 | 5.700 | 7.040 | 5.640 | 5.400 | 4.720 | 6.010 | 21.210 | 8.110 |

### Groene, witte en oolong thee en matcha

Doelpagina: /collections/groene-thee. Cluster in Search Console: 937 vertoningen, 2 klikken in 90 dagen, gemiddelde positie 42,4.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| groene thee | 4.400 | HIGH | 72 | 24,0 | 51,5 | 0 | 1% | 4.376 |
| oolong thee | 1.900 | HIGH | 94 | 31,3 | 49,4 | 0 | 2% | 1.869 |
| witte thee | 1.600 | HIGH | 67 | 22,3 | 53,3 | 0 | 1% | 1.578 |
| jasmijn thee | 1.600 | HIGH | 36 | 12,0 | 55,4 | 0 | 1% | 1.588 |
| chinese thee | 880 | HIGH | 31 | 10,3 | 46,8 | 0 | 1% | 870 |
| matcha thee kopen | 720 | HIGH | 71 | 23,7 | 44,5 | 0 | 3% | 696 |
| losse groene thee | 210 | HIGH | 42 | 14,0 | 36,7 | 0 | 7% | 196 |
| groene thee citroen | 170 | HIGH | 44 | 14,7 | 32,4 | 0 | 9% | 155 |

Totaal zoekvolume: 11.480 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: 152,3 per maand, aandeel zichtbaarheid 1%.

Seizoen: piek in januari 2026 (15.300, 137% van gemiddeld), december 2025 (14.600, 131% van gemiddeld); gemiddeld 11.128 per maand, op basis van 8 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 12.860 | 12.490 | 14.600 | 15.300 | 12.820 | 12.300 | 10.980 | 10.480 | 8.090 | 6.930 | 8.030 | 8.650 |

### Zwarte thee (assam, ceylon, earl grey)

Doelpagina: /collections/zwarte-thee. Cluster in Search Console: 315 vertoningen, 3 klikken in 90 dagen, gemiddelde positie 36,5.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| zwarte thee | 1.600 | HIGH | 52 | 17,3 | 49,8 | 0 | 1% | 1.583 |
| pu erh thee | 1.300 | HIGH | 14 | 4,7 | 37,6 | 0 | 0% | 1.295 |
| darjeeling thee | 720 | HIGH | 24 | 8,0 | 44,0 | 0 | 1% | 712 |
| earl grey thee | 720 | HIGH | 19 | 6,3 | 46,6 | 0 | 1% | 714 |
| assam thee | 320 | HIGH | 31 | 10,3 | 42,0 | 0 | 3% | 310 |
| darjeeling thee kopen | 70 | HIGH | 13 | 4,3 | 32,3 | 1 | 6% | 66 |
| losse zwarte thee | 50 | HIGH | 15 | 5,0 | 23,3 | 0 | 10% | 45 |
| zwarte theesoorten | - | - | 16 | 5,3 | 39,4 | 0 | - | - |

Totaal zoekvolume: 4.780 per maand over 7 van 8 zoekwoorden (bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: 56,0 per maand, aandeel zichtbaarheid 1%.

Seizoen: piek in januari 2026 (6.310, 128% van gemiddeld); gemiddeld 4.928 per maand, op basis van 7 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 5.760 | 6.020 | 5.250 | 6.310 | 5.400 | 5.170 | 5.090 | 4.970 | 3.950 | 3.240 | 4.080 | 3.890 |

### Rooibos en honeybush

Doelpagina: /collections/rooibos. Cluster in Search Console: 314 vertoningen, 0 klikken in 90 dagen, gemiddelde positie 27,9.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| rooibos | 5.400 | MEDIUM | 48 | 16,0 | 12,7 | 0 | 0% | 5.384 |
| rooibos thee | 1.900 | HIGH | 49 | 16,3 | 43,1 | 0 | 1% | 1.884 |
| rooibos tea | 1.000 | HIGH | 12 | 4,0 | 9,2 | 0 | 0% | 996 |
| rooibos vanille thee | 480 | HIGH | 19 | 6,3 | 39,9 | 0 | 1% | 474 |
| honeybush thee | 170 | HIGH | 13 | 4,3 | 47,9 | 0 | 3% | 166 |
| losse rooibos thee | 70 | HIGH | 93 | 31,0 | 28,5 | 0 | 44% | 39 |
| losse rooibosthee | 70 | HIGH | 11 | 3,7 | 25,8 | 0 | 5% | 66 |
| rooibosthee cafeïnevrij | 0 | UNSPECIFIED | 30 | 10,0 | 22,7 | 0 | - | 0 |

Totaal zoekvolume: 9.090 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: 91,7 per maand, aandeel zichtbaarheid 1%.

Seizoen: piek in januari 2026 (13.670, 133% van gemiddeld), november 2025 (13.410, 131% van gemiddeld), oktober 2025 (12.870, 126% van gemiddeld); gemiddeld 10.248 per maand, op basis van 7 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 12.870 | 13.410 | 12.770 | 13.670 | 11.070 | 11.170 | 10.170 | 8.410 | 5.960 | 6.400 | 7.780 | 9.300 |

### Vruchtenthee en fruitige thee

Doelpagina: /collections/vruchtenthee. Cluster in Search Console: 420 vertoningen, 0 klikken in 90 dagen, gemiddelde positie 35,2.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| hibiscus thee | 8.100 | HIGH | 53 | 17,7 | 45,3 | 0 | 0% | 8.082 |
| citroenmelisse thee | 1.600 | HIGH | 16 | 5,3 | 32,2 | 0 | 0% | 1.595 |
| citroengras thee | 320 | HIGH | 20 | 6,7 | 44,9 | 0 | 2% | 313 |
| vruchten thee | 140 | HIGH | 27 | 9,0 | 33,1 | 0 | 6% | 131 |
| aardbeien slagroom thee | 90 | HIGH | 63 | 21,0 | 22,4 | 0 | 23% | 69 |
| vlierbessen thee | 90 | HIGH | 25 | 8,3 | 12,6 | 0 | 9% | 82 |
| aardbeienthee | 50 | HIGH | 29 | 9,7 | 49,5 | 0 | 19% | 40 |
| fruitige thee | 0 | UNSPECIFIED | 15 | 5,0 | 41,7 | 0 | - | 0 |

Totaal zoekvolume: 10.390 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: 82,7 per maand, aandeel zichtbaarheid 1%.

Seizoen: geen duidelijke piek (geen maand boven 125% van het gemiddelde); gemiddeld 9.890 per maand, op basis van 7 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 9.180 | 8.830 | 8.370 | 10.660 | 10.240 | 12.330 | 11.140 | 11.660 | 9.520 | 8.300 | 9.920 | 8.530 |

### Kruidenthee (kamille, munt, gember, salie)

Doelpagina: /collections/kruidenthee. Cluster in Search Console: 1.442 vertoningen, 2 klikken in 90 dagen, gemiddelde positie 41,5.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| kamille thee | 6.600 | HIGH | 55 | 18,3 | 46,6 | 0 | 0% | 6.582 |
| salie thee | 2.400 | HIGH | 52 | 17,3 | 44,4 | 0 | 1% | 2.383 |
| paardenbloem thee | 2.400 | HIGH | 38 | 12,7 | 48,7 | 0 | 1% | 2.387 |
| kurkuma thee | 1.900 | HIGH | 38 | 12,7 | 47,7 | 0 | 1% | 1.887 |
| pepermunt thee | 1.600 | HIGH | 44 | 14,7 | 44,8 | 0 | 1% | 1.585 |
| fenegriek thee | 590 | HIGH | 40 | 13,3 | 45,9 | 0 | 2% | 577 |
| cactus thee | 110 | HIGH | 114 | 38,0 | 20,1 | 0 | 35% | 72 |
| cactusvijg thee | 40 | HIGH | 52 | 17,3 | 22,5 | 0 | 43% | 23 |

Totaal zoekvolume: 15.640 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: 144,3 per maand, aandeel zichtbaarheid 1%.

Seizoen: piek in januari 2026 (19.130, 129% van gemiddeld); gemiddeld 14.879 per maand, op basis van 8 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 16.660 | 15.670 | 15.550 | 19.130 | 15.940 | 16.280 | 18.320 | 14.800 | 10.700 | 10.380 | 12.020 | 13.100 |

### Smaakthee en seizoensthee

Doelpagina: /collections/thee. Cluster in Search Console: 319 vertoningen, 4 klikken in 90 dagen, gemiddelde positie 35,3.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| chai thee | 1.300 | HIGH | 16 | 5,3 | 45,8 | 0 | 0% | 1.295 |
| kaneel thee | 480 | HIGH | 23 | 7,7 | 54,1 | 0 | 2% | 472 |
| winter thee | 260 | HIGH | 16 | 5,3 | 47,0 | 0 | 2% | 255 |
| chocolade thee | 170 | HIGH | 13 | 4,3 | 46,2 | 0 | 3% | 166 |
| speculaas thee | 110 | HIGH | 63 | 21,0 | 20,5 | 0 | 19% | 89 |
| speculaasmix | 110 | HIGH | 14 | 4,7 | 21,1 | 0 | 4% | 105 |
| thee kerstpakket | 70 | HIGH | 18 | 6,0 | 43,9 | 0 | 9% | 64 |
| yogi tea curcuma chai losse thee | 20 | UNSPECIFIED | 26 | 8,7 | 50,2 | 0 | 43% | 11 |

Totaal zoekvolume: 2.520 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: 63,0 per maand, aandeel zichtbaarheid 2%.

Seizoen: piek in november 2025 (5.060, 189% van gemiddeld), oktober 2025 (4.640, 173% van gemiddeld), december 2025 (4.430, 165% van gemiddeld); gemiddeld 2.678 per maand, op basis van 8 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 4.640 | 5.060 | 4.430 | 3.480 | 2.270 | 2.190 | 1.630 | 1.760 | 1.170 | 1.170 | 1.630 | 2.700 |

### Thee longtail: gezondheid, soorten en overig (informatief)

Doelpagina: /collections/thee. Cluster in Search Console: 1.204 vertoningen, 1 klikken in 90 dagen, gemiddelde positie 40,1.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| mate thee | 2.400 | HIGH | 32 | 10,7 | 44,5 | 0 | 0% | 2.389 |
| marokkaanse thee | 1.900 | HIGH | 18 | 6,0 | 44,0 | 0 | 0% | 1.894 |
| cafeïnevrije thee | 1.000 | HIGH | 66 | 22,0 | 45,2 | 0 | 2% | 978 |
| cafeïne thee | 590 | LOW | 20 | 6,7 | 41,9 | 0 | 1% | 583 |
| tastea thee | 50 | HIGH | 15 | 5,0 | 51,3 | 0 | 10% | 45 |
| gezonde theesoorten | 10 | HIGH | 23 | 7,7 | 49,0 | 0 | 77% | 2 |
| peper thee | 10 | HIGH | 17 | 5,7 | 24,9 | 0 | 57% | 4 |
| theemix | 10 | HIGH | 17 | 5,7 | 7,6 | 0 | 57% | 4 |

Totaal zoekvolume: 5.970 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: 69,3 per maand, aandeel zichtbaarheid 1%.

Seizoen: piek in januari 2026 (7.900, 130% van gemiddeld); gemiddeld 6.072 per maand, op basis van 8 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 7.400 | 7.440 | 7.080 | 7.900 | 6.910 | 6.600 | 5.350 | 5.140 | 4.680 | 4.620 | 4.260 | 5.490 |

### Engelstalig: 'tea'

Doelpagina: /collections/thee. Cluster in Search Console: 949 vertoningen, 1 klikken in 90 dagen, gemiddelde positie 5,6.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| tea | - | - | 890 | 296,7 | 5,2 | 0 | - | - |
| herbal tea | - | - | 4 | 1,3 | 5,5 | 0 | - | - |
| high tea borne | - | - | 4 | 1,3 | 54,2 | 0 | - | - |
| ice tea maken met losse thee | - | - | 3 | 1,0 | 9,0 | 0 | - | - |
| tea eggs near me | - | - | 3 | 1,0 | 1,0 | 0 | - | - |
| white tea | - | - | 3 | 1,0 | 7,0 | 0 | - | - |
| chinese tea | - | - | 2 | 0,7 | 1,0 | 0 | - | - |
| dutch tea | - | - | 2 | 0,7 | 3,5 | 0 | - | - |

Geen zoekwoord van dit cluster staat in de volumebestanden; het volume is onbekend.

Seizoen: geen maandcijfers in de bestanden.

### Productnamen en cadeau-mokken (long tail op productpagina's)

Doelpagina: -. Cluster in Search Console: 588 vertoningen, 7 klikken in 90 dagen, gemiddelde positie 20,2.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| kir | 1.900 | LOW | 14 | 4,7 | 8,8 | 0 | 0% | 1.895 |
| you did it | 880 | HIGH | 38 | 12,7 | 9,9 | 0 | 1% | 867 |
| kitchen queen | 390 | LOW | 21 | 7,0 | 8,1 | 0 | 2% | 383 |
| spice up your life | 210 | LOW | 30 | 10,0 | 10,8 | 0 | 5% | 200 |
| superbedankt | 140 | LOW | 24 | 8,0 | 10,0 | 0 | 6% | 132 |
| super juf | 110 | HIGH | 15 | 5,0 | 7,2 | 0 | 5% | 105 |
| christa mulder | 50 | LOW | 19 | 6,3 | 6,6 | 2 | 13% | 44 |
| jij bent top | 30 | MEDIUM | 25 | 8,3 | 6,8 | 0 | 28% | 22 |

Totaal zoekvolume: 3.710 per maand over 8 van 8 zoekwoorden (bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: 62,0 per maand, aandeel zichtbaarheid 2%.

Seizoen: piek in juni 2026 (4.920, 135% van gemiddeld); gemiddeld 3.634 per maand, op basis van 8 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 3.910 | 3.350 | 4.260 | 3.780 | 3.230 | 3.420 | 3.390 | 3.760 | 4.920 | 3.790 | 2.900 | 2.900 |

### Overig non-brand (niet ingedeeld)

Doelpagina: -. Cluster in Search Console: 710 vertoningen, 10 klikken in 90 dagen, gemiddelde positie 20,2.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| arie borne | 10 | LOW | 21 | 7,0 | 7,1 | 0 | 70% | 3 |
| schutting borne | 10 | MEDIUM | 10 | 3,3 | 43,7 | 0 | 33% | 7 |
| engelse serre | - | - | 15 | 5,0 | 36,0 | 0 | - | - |
| koffiezetapparaat | - | - | 14 | 4,7 | 5,5 | 0 | - | - |
| waarde | - | - | 12 | 4,0 | 11,0 | 0 | - | - |
| ja | - | - | 11 | 3,7 | 8,1 | 0 | - | - |
| r i e | - | - | 11 | 3,7 | 23,9 | 0 | - | - |
| chocolade | - | - | 9 | 3,0 | 3,6 | 0 | - | - |

Totaal zoekvolume: 20 per maand over 2 van 8 zoekwoorden (bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: 10,3 per maand, aandeel zichtbaarheid 52%.

Seizoen: piek in september 2026 (80, 457% van gemiddeld); gemiddeld 18 per maand, op basis van 2 van 8 zoekwoorden.

| Maand | oktober 2025 | november 2025 | december 2025 | januari 2026 | februari 2026 | maart 2026 | april 2026 | mei 2026 | juni 2026 | juli 2026 | augustus 2026 | september 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Volume (som) | 10 | 10 | 10 | 10 | 10 | 10 | 20 | 20 | 10 | 10 | 10 | 80 |

### Lokaal: Borne, Twente en omgeving

Doelpagina: /pages/theewinkel-borne-twente. Cluster in Search Console: 423 vertoningen, 6 klikken in 90 dagen.

| Zoekwoord | Volume/maand | Concurrentie | Vert. 90d | Vert./maand | Pos. | Klikken | Aandeel zichtbaarheid | Onbenut volume/maand |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| winkels in borne | 720 | LOW | 8 | 2,7 | 10,6 | 0 | 0% | 717 |
| winkel borne | 70 | LOW | 49 | 16,3 | 10,3 | 0 | 23% | 54 |
| kookwinkel twente | 50 | LOW | 62 | 20,7 | 3,9 | 3 | 41% | 29 |
| beste van borne | 50 | LOW | 16 | 5,3 | 7,9 | 0 | 11% | 45 |
| theewinkel enschede | 50 | MEDIUM | 12 | 4,0 | 20,2 | 0 | 8% | 46 |
| kookwinkel almelo | 50 | LOW | 8 | 2,7 | 2,9 | 0 | 5% | 47 |
| koffie borne | 40 | LOW | 6 | 2,0 | 5,7 | 0 | 5% | 38 |
| kruidenwinkel borne | 30 | LOW | 58 | 19,3 | 6,2 | 1 | 64% | 11 |
| toko borne | 30 | LOW | 12 | 4,0 | 8,1 | 0 | 13% | 26 |
| natuurwinkel borne | 20 | LOW | 24 | 8,0 | 10,2 | 0 | 40% | 12 |
| borne winkel | 20 | LOW | 21 | 7,0 | 8,3 | 1 | 35% | 13 |
| kookwinkel borne | 20 | LOW | 11 | 3,7 | 1,5 | 1 | 18% | 16 |
| thee uit twente | 0 | UNSPECIFIED | 94 | 31,3 | 7,0 | 0 | - | 0 |
| winkels borne | - | - | 29 | 9,7 | 23,7 | 0 | - | - |
| borne winkels | - | - | 13 | 4,3 | 27,7 | 0 | - | - |

Totaal zoekvolume: 1.150 per maand over 13 van 15 zoekwoorden (bovengrens, zie leeswijzer). Vertoningen van die zoekwoorden: 127,0 per maand, aandeel zichtbaarheid 11%.

Seizoen: piek in december 2025 (1.420, 130% van gemiddeld), april 2026 (1.410, 129% van gemiddeld); gemiddeld 1.091 per maand, op basis van 12 van 15 zoekwoorden.

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

