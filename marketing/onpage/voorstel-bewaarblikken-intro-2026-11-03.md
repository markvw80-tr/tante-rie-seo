# Voorstel intro /collections/thee-bewaarblikken (vroege start, onderdeel 2)

Opgesteld door On-page op 24 oktober 2026 (opdracht uit marketing/plan-2026-11-vroege-start.md, afspraak oplevering 3 november). Status: alleen voorstel. Er is niets gewijzigd in Shopify, het thema of changelog.md. Review door de Kwaliteitsredacteur op 4 november (samen met het cadeaupakket), voor en na bij Mark op 5 november, doorvoeren uiterlijk 13 november na akkoord.

Bronnen: Shopify Admin API (alleen lezen, 24 oktober 2026, ook de live code van thema 203153015048), Search Console-export data/gsc/2026-10-21-query-page-90d.json (23 juli tot en met 18 oktober), marketing/zoekwoorden/clusters-2026-10-24.md, marketing/onpage/voorstel-titles-joeff-blikken-2026-10-22.md en changelog (regel van 22 oktober). De data is van 21 oktober; ik werk deze cijfers bij vlak voor 3 november als de Search Console-scripts dan beschikbaar zijn (V81).

## Nulwaarden en doel

Collectie /collections/thee-bewaarblikken (562351145224), 28 dagen: 327 vertoningen, 4 klikken, CTR 1,22 procent, positie 19,4. Doel zes weken na publicatie: 'thee blikjes' op positie 20 of beter, CTR minstens 2 procent. 'thee blikjes' heeft 590 zoekopdrachten per maand (november 880, december 1.000), 'theeblikjes voor losse thee' 480, 'thee bewaarblik' 210.

Zoekopdrachten die nu op de collectie landen (90 dagen):

| Zoekopdracht | Vertoningen | Klikken | Positie |
|---|---:|---:|---:|
| thee bewaarblik | 163 | 0 | 16,2 |
| thee blikken | 116 | 0 | 29,4 |
| thee blikjes | 115 | 0 | 31,0 |
| theeblikjes voor losse thee | 98 | 2 | 23,2 |
| theeblikken voor losse thee | 69 | 0 | 20,2 |
| losse thee blikjes | 66 | 0 | 30,7 |

Het plan noemt voor 'thee bewaarblik' positie 12,1; in deze 90-dagenexport is dat 16,2. Het verschil komt uit het andere venster; het verandert het doel niet.

## Welke blikken online staan (24 oktober)

De collectie telt nu 25 producten (22 oktober: 24). Online op Webshop: 14. Alleen kassa (niet online): 10. Concept: 1 (Emma Bridgewater Garden Flowers). Dit wijkt af van het voorstel van 22 oktober (toen 19 online); sindsdien zijn nieuwe producten toegevoegd die alleen op de kassa staan, zoals de series "Blikje ..." en het gouden blik.

| Online product | Merk | Inhoud | Prijs | Voorraad | Bestelbaar |
|---|---|---|---:|---:|---|
| Zwart thee bewaarblik | Havelaar | 100 gram | 4,50 | 20 | ja |
| Wit thee bewaarblik | Havelaar | 100 gram | 4,50 | 52 | ja |
| Zilver thee bewaarblik | Havelaar | 100 gram | 4,50 | 69 | ja |
| Zilver thee bewaarblik | Tante Rie | 50 gram | 2,50 | 79 | ja |
| Arts & Craft groen | Tante Rie | 100 gram | 6,25 | 8 | ja |
| Arts & Craft blauw | Tante Rie | 100 gram | 6,25 | 9 | ja |
| Flowers | Tante Rie | 100 gram | 6,25 | -4 (doorverkopen aan) | ja |
| Sara Miller Chelsea Roze | Sara Miller London | 100 gram | 6,25 | 2 | ja |
| Sara Miller Filigree | Sara Miller London | 100 gram | 6,25 | 2 | ja |
| Sara Miller Green Birds | Sara Miller London | 100 gram | 6,25 | 0 | nee |
| Sara Miller Haveli Paars | Sara Miller London | 100 gram | 6,25 | 0 | nee |
| Sanderson Foraging | Sanderson | 100 gram | 6,25 | 2 | ja |
| Sanderson Chinoiserie Hall | Sanderson | 100 gram | 6,25 | -3 | nee |
| Emma Bridgewater Poppies | Emma Bridgewater | 100 gram | 6,25 | 8 | ja |

Alleen kassa, dus niet te noemen: Blikje herfst, Blikje bij, Blikje vogels, Blikje paarse bloemen (rond en gewoon), Sara Miller Palm Garden Roze, Sara Miller India Blue, het gouden blik van 50 gram en beide zwarte blikken met venster (50 en 250 gram).

Gevolgen voor de tekst:
1. Ik noem merken, geen losse dessins: drie dessins zijn nu uitverkocht (Green Birds, Haveli, Chinoiserie Hall) en zouden snel achterhaald zijn. Elk genoemd merk heeft minstens één bestelbaar blik: Sara Miller London (Chelsea, Filigree), Sanderson (Foraging), Emma Bridgewater (Poppies) en Arts & Craft.
2. Alleen "de meeste blikken" zijn 100 gram. Er is online één blik van 50 gram (zilver). Dat noem ik.
3. Geen "ook in de winkel", geen "op voorraad", geen "snel leverbaar" (besluit Mark 21-10).
4. Prijzen staan niet in de intro, zodat die niet verouderen.

## Hoe de collectiepagina de tekst toont

In sections/tr-collection-redesign.liquid staat de eerste alinea van de collectiebeschrijving boven het productraster en alles na de eerste alinea in een blok onder het raster. De huidige beschrijving bestaat uit één alinea en staat dus boven het raster. Mijn voorstel zet de nieuwe intro vóór de huidige alinea. Daardoor wordt de nieuwe intro de zichtbare tekst boven het raster en schuift de huidige alinea naar het blok onder het raster. Die alinea laat ik inhoudelijk ongewijzigd.

## Voor en na

| Onderdeel | Huidig | Voorgesteld |
|---|---|---|
| Beschrijving (descriptionHtml) | `<p>In een goed afgesloten blik blijft losse thee langer vers en behoudt het zijn aroma. Al onze theeblikken zijn gemaakt van stevig metaal met een goed sluitende deksel, die licht, lucht en vocht buiten houdt. Kies uit eenvoudige zwarte of witte blikken, of ga voor een van de mooie geïllustreerde varianten van Arts &amp; Craft, Sara Miller of Flowers. Ook leuk als cadeau naast een losse theesoort.</p>` | `<p>Thee blikjes zijn er bij Tante Rie in effen zwart, wit en zilver en met een print van onder meer Sara Miller London, Sanderson, Emma Bridgewater en Arts &amp; Craft. De meeste theeblikjes voor losse thee bewaren zo'n 100 gram; het zilveren blik is er ook in 50 gram. Combineer je blik met een van onze ruim 130 <a href="/collections/thee">losse theesoorten</a>.</p>` gevolgd door de huidige alinea, ongewijzigd |
| SEO-title | Thee bewaarblik kopen: blikken voor losse thee \| Tante Rie (58 tekens) | Ongewijzigd |
| Metabeschrijving | Theeblikken voor losse thee, de meeste van 100 gram: effen in zwart, wit of zilver of met een print van Sara Miller of Sanderson. Bij Tante Rie in Borne. (153 tekens) | Ongewijzigd |
| H1 | Thee Bewaarblikken | Ongewijzigd |

De nieuwe intro: 60 woorden, 325 tekens, drie zinnen. Hij bevat 'thee blikjes' (zin 1) en 'theeblikjes voor losse thee' (zin 2). De zoekopdracht 'thee bewaarblik' (op 16,2) is via de H1 en de title gedekt.

## Reden

1. De twee zoektermen waar de collectie nog ver af staat ('thee blikjes' op 29,7 tot 31 en 'theeblikjes voor losse thee' op 23 tot 24) komen in de huidige tekst niet voor. 'blik' en 'theeblikken' wel, 'blikjes' niet. Google leest dat als verwant, maar de zoeker die 'thee blikjes' typt ziet nu geen woord terug.
2. De intro geeft in één blik wat de zoeker wil weten: welke kleuren en prints, welke merken en hoeveel erin past (100 gram, een kleiner blik van 50 gram). Dat is specifieke informatie in plaats van een algemene belofte, en het scheelt klikken naar productpagina's om dat uit te zoeken.
3. De link naar /collections/thee verbindt het blik met de losse thee en geeft de collectie een interne link naar de belangrijkste thee-pagina. 'Ruim 130' staat ook op de theewinkelpagina.
4. De intro bevat geen voorraadbelofte, geen winkelvermelding, geen uitroepteken, geen gedachtestreepje, geen opsomming en geen vulwoorden. Het gebruik van "je" past bij de rest van de site.
5. De huidige alinea blijft staan omdat ze al klopt voor de online blikken (metaal, goed sluitend, zwart, wit en geïllustreerd). Eén opmerking: de alinea noemt het blik "Flowers", dat online staat met voorraad -4 en beleid doorverkopen. Dat is een bestaand risico, geen onderdeel van dit voorstel.

## Later voorstel: title na de meting van 19 november

De title en meta van 22 oktober blijven staan tot de 28-dagenmeting op 19 november (plan-2026-11-vroege-start). Dan beslis ik op basis van Search Console:

| Uitkomst van de meting | Actie |
|---|---|
| CTR collectie minstens 2 procent en 'thee bewaarblik' op 16 of beter | Title niet wijzigen |
| CTR onder 2 procent, of 'thee blikjes' nog slechter dan positie 25 | Title wijzigen volgens optie 1 of 2 hieronder, als apart voorstel voor Kwaliteitsredacteur en Mark |

| Optie | SEO-title | Tekens |
|---|---|---:|
| Huidig | Thee bewaarblik kopen: blikken voor losse thee \| Tante Rie | 58 |
| 1 (aanbevolen) | Thee blikjes en bewaarblikken voor losse thee \| Tante Rie | 57 |
| 2 | Thee blikjes kopen: bewaarblikken voor losse thee \| Tante Rie | 61 (lang, kan afkappen) |

Bij een nieuwe title past een kleine aanpassing van de meta: "Thee blikjes voor losse thee, de meeste van 100 gram: effen in zwart, wit of zilver of met een print van Sara Miller of Sanderson. Bij Tante Rie in Borne." (154 tekens). Dit is ook alleen een voorstel voor later.

Let op de timing: de intro gaat volgens plan uiterlijk 13 november live, dus op 19 november heeft ze maar een paar dagen gewerkt. De meting van 19 november zegt dus vooral iets over de title van 22 oktober. Het effect van de intro meet ik 28 dagen na livegang (uiterlijk 11 december) en na zes weken (uiterlijk 25 december). Dat valt midden in de decemberpiek (thee blikjes 1.000 per maand); houd er rekening mee dat seizoen en wijziging door elkaar lopen. De Analist moet daarom vergelijken met dezelfde periode in de rest van het thee-assortiment, niet alleen met de nulwaarden.

## Doorvoeren na akkoord (plan, niet uitgevoerd)

| Stap | Wat | Hoe | Backup |
|---|---|---|---|
| 1 | Beschrijving van collectie 562351145224 (descriptionHtml) | Shopify Admin API, collectionUpdate | oude descriptionHtml en SEO-velden in marketing/onpage/backup-bewaarblikken-intro-<datum>.json |
| 2 | Changelogregel | marketing/changelog.md | n.v.t. |

Eén object, ruim onder de grens van 20. Na het doorvoeren controleer ik de live pagina: zichtbare intro boven het raster, huidige alinea onder het raster, link naar /collections/thee werkt, geen dubbele alinea's. Daarna geef ik de Analist de livedatum voor de nulmeting.

## Open vragen (voor Mark, nog niet in vragen-voor-mark.md; de hoofdsessie verwerkt ze)

V103 (laag): "Flowers thee bewaarblik" staat online met voorraad -4 en beleid doorverkopen, en de huidige alinea noemt het blik. Klopt het dat dit blik wordt nabesteld? Zo niet, haal ik "of Flowers" uit de huidige alinea bij het doorvoeren (kleine wijziging, alleen met jouw akkoord).
V104 (laag): de series "Blikje ..." en het gouden blik van 50 gram staan alleen op de kassa. Wil je (een deel) online zetten? Dat zou de collectie voor 'thee blikjes' sterker maken. Ik publiceer niets zonder antwoord.
