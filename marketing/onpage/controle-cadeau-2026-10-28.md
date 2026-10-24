# Controle cadeau: kan /collections/cadeaus de hoofdpagina voor 'thee cadeau' zijn? (vroege start, onderdeel 3, stap 1)

Opgesteld door On-page op 24 oktober 2026 (opdracht uit marketing/plan-2026-11-vroege-start.md, afspraak oplevering 28 oktober). Status: alleen controle en advies. Er is niets gewijzigd in Shopify, het thema of changelog.md. Het voorstel met voor en na (stap 2) volgt op 3 november, na dit advies en de keuze van Mark.

Bronnen: Shopify Admin API (alleen lezen, 24 oktober 2026, inclusief de live code van thema 203153015048), Search Console-exports data/gsc/2026-10-21-query-page-90d.json (23 juli tot en met 18 oktober) en data/gsc/2026-10-21-nulmeting-huidig-querypage.json (22 september tot en met 19 oktober), marketing/zoekwoorden/clusters-2026-10-24.md, marketing/plan-2026-11.md en marketing/plan-2026-10.md. Het verkoopkanaal Online winkel heet in deze Shopify "Webshop"; "online" betekent hieronder gepubliceerd op Webshop (de productpagina heeft dan een onlineStoreUrl).

## Het advies in het kort

Kies /collections/cadeaus als hoofdpagina voor 'thee cadeau', onder drie voorwaarden. De criteria uit het plan wijzen die kant op: 21 van de 32 producten staan online (66 procent) en alle 21 kunnen verstuurd worden, dus het merendeel is niet "niet online of niet verzendbaar". Daarbij hoort de volle waarheid over de collectie en over /pages/thee-cadeau:

1. De collectie is dun als cadeauplek: van de 21 online producten zijn er 11 nu bestelbaar. Van de 15 theegeschenken (4 proefpakketten, 9 Tijd voor thee-kokers, 2 Thee en een mooi gesprek-sets) zijn er 7 bestelbaar. Er is geen enkele cadeauset met thee en servies of accessoires online: beide Luxe Thee Cadeausets zijn gearchiveerd, terwijl de huidige tekst en meta van de collectie "cadeausets" beloven.
2. /pages/thee-cadeau is als alternatief ongeschikt zolang de links niet gerepareerd zijn: zes links (de hoofdknop, de kaarten Complete en Kleine cadeausets, de budgetlink en de afsluitende knoppen) gaan naar /collections/geven-is-leuker, die niet op de Webshop staat (404 voor bezoekers), en de kaart "Juf en meester cadeaus" gaat naar een collectie waarvan alle 9 producten concept zijn. Ook /collections/blond-amsterdam bestaat niet.
3. Bijna alle zoekverkeer voor dit cluster landt op de homepage (87 procent van de vertoningen in 90 dagen, 96 procent in 28 dagen, positie 44 tot 46). Geen van de twee kandidaten heeft nu echte posities. De homepage blijft ongemoeid, dus de hoofdpagina moet de homepage verslaan op een duidelijke title, H1 en intro.

Voorwaarden aan het advies: (a) Mark beslist over de voorraad en volgorde (zie vraag V98 en V99); (b) /pages/thee-cadeau wordt in stap 2 een korte verwijspagina met werkende links; (c) de tekst van de collectie belooft alleen wat er online staat. Zonder (a) blijft de collectie zichtbaar maar half uitverkocht, en dat drukt de conversie in december, niet de ranking.

## 1. Nulwaarden en zoekopdrachten

Cluster 'thee cadeau' (queries met cadeau, geschenk of kado, zonder relatiegeschenk, cadeaubon en zakelijk; mijn afbakening, vergelijkbaar met het plan):

| Venster | Queries | Vertoningen | Klikken | Positie |
|---|---:|---:|---:|---:|
| 90 dagen (23 juli tot en met 18 oktober) | 95 | 500 | 2 | 41,2 |
| 28 dagen (22 september tot en met 19 oktober) | 61 | 423 | 0 | 45,9 |

Het plan noemt 532 vertoningen, 2 klikken en positie 40,9 (90 dagen) en 446, 0 klikken, positie 44,7 (28 dagen). Het verschil komt uit een iets andere afbakening van het cluster; de conclusie verandert er niet door. Voor de meting gebruik ik straks de afbakening van de Analist.

Op welke URL de cadeauzoekopdrachten landen:

| URL | Vertoningen 90 dgn | Aandeel | Klikken | Positie | Vertoningen 28 dgn | Aandeel |
|---|---:|---:|---:|---:|---:|---:|
| https://tanterie.nl/ (homepage) | 434 | 87% | 0 | 44,3 | 407 | 96% |
| /pages/thee-cadeau | 27 | 5% | 1 | 25,8 | 10 | 2% |
| /products/mazagran-cheers-to-18-years (zoekopdrachten over 18 jaar) | 24 | 5% | 1 | 10,0 | 0 | 0% |
| /collections/cadeaus | 5 | 1% | 0 | 31,8 | 1 | 0% |
| /collections/thee-bewaarblikken | 3 | 1% | 0 | 27,3 | 3 | 1% |

De grootste zoekopdrachten en waar ze landen (90 dagen):

| Zoekopdracht | Landingspagina | Vertoningen | Positie |
|---|---|---:|---:|
| luxe thee cadeau set | homepage | 25 | 45,3 |
| thee cadeau | homepage / thee-cadeau | 23 / 5 | 48,6 / 31,0 |
| thee cadeau bezorgen | homepage | 21 | 51,2 |
| thee als cadeau | homepage | 20 | 54,1 |
| geschenk thee | homepage | 19 | 54,8 |
| thee geschenkset | homepage | 17 | 46,0 |
| thee cadeau verjaardag | /pages/thee-cadeau | 10 (1 klik) | 10,8 |
| relatiegeschenk thee | /collections/cadeaus | 18 | 35,5 (zakelijk, tel niet mee) |

Lezing: de vraag is er (volume 1.000 per maand voor 'thee cadeau', november 2.400, december 2.900), maar Tante Rie heeft nog geen pagina die Google voor deze zoekopdrachten kiest. De enige snippet met een echte positie is /pages/thee-cadeau voor 'thee cadeau verjaardag' (10,8), op 10 vertoningen. Dat is te weinig om er een keuze op te baseren. Let op: 'luxe thee cadeau set' (210 per maand) en 'thee geschenkset' (140) vragen om sets, en die zijn er online niet.

## 2. Producten in /collections/cadeaus (32)

Collectie 561282515208, sortering Best verkocht, gepubliceerd op Webshop, Point of Sale, Shop en Google & YouTube. Eén voorraadlocatie: Tante Rie Borne. Alle 21 online producten hebben verzendprofiel Algemeen profiel (verstuurd, geen "alleen afhalen"); de cadeaubon is een Shopify-cadeaubon. Het Google-label alleen-afhalen staat op geen enkel product. "Bestelbaar" betekent: voorraad hoger dan 0 (of cadeaubon), of voorraad 0 of lager met beleid doorverkopen.

| # | Product | Merk | Status | Online | Verzendbaar | Voorraad | Bestelbaar |
|---:|---|---|---|---|---|---:|---|
| 1 | Theelepel bolvorm | Natural Flower Cards | actief | ja | ja | 18 | ja |
| 2 | Thee en een mooi gesprek - hoera | Natural Flower Cards | actief | ja | ja | -6 | nee |
| 3 | Tijd voor thee koker - Gefelicithee | Natural Flower Cards | actief | ja | ja | -3 | nee |
| 4 | Proefpakket Groene Thee | Tante Rie | actief | ja | ja | 3 | ja |
| 5 | Thee en een mooi gesprek - liefs | Natural Flower Cards | actief | ja | ja | -3 | nee |
| 6 | Geurstokje - Een warme groet | Natural Flower Cards | actief | ja | ja | -3 | nee |
| 7 | Tijd voor thee - veel liefs | Natural Flower Cards | actief | ja | ja | 0 | nee |
| 8 | Geurstokje - Dankjewel | Natural Flower Cards | actief | ja | ja | -2 | nee |
| 9 | Tijd voor thee - hartje | Natural Flower Cards | actief | ja | ja | 1 | ja |
| 10 | Tijd voor thee - Dankjewel | Natural Flower Cards | actief | ja | ja | 0 | nee |
| 11 | Proefpakket Kruidenthee | Tante Rie | actief | ja | ja | 8 | ja |
| 12 | Autoparfum - superbedankt | Natural Flower Cards | actief | ja | ja | 2 | ja |
| 13 | Tijd voor thee - jij bent goud waard | Natural Flower Cards | actief | ja | ja | 1 | ja |
| 14 | Tijd voor thee - Bedankt | Natural Flower Cards | actief | ja | ja | -1 | nee |
| 15 | Tijd voor thee - nieuw huis | Natural Flower Cards | actief | ja | ja | -1 | nee |
| 16 | Tijd voor thee - Gefeliciteerd | Natural Flower Cards | actief | ja | ja | 0 | nee |
| 17 | Tante Rie Cadeaubon (10, 25, 50, 100 euro) | Tante Rie | actief | ja | n.v.t. (cadeaubon) | niet bijgehouden | ja |
| 18 | Autoparfum - koning van de snelweg | Natural Flower Cards | actief | ja | ja | 1 | ja |
| 19 | Tijd voor thee - lieve zus | Natural Flower Cards | actief | ja | ja | 1 | ja |
| 20 | Notitieblok To do's - De leukste meester | Tante Rie | concept | nee | n.v.t. | 3 | nee |
| 21 | Notitieblok To do's - De liefste juf | Tante Rie | concept | nee | n.v.t. | 6 | nee |
| 22 | Kaart Leuke meester bedankt | Tante Rie | concept | nee | n.v.t. | 5 | nee |
| 23 | Kaart Bedankt lieve juf | Tante Rie | concept | nee | n.v.t. | 5 | nee |
| 24 | Forex tegeltje De liefste juf | Tante Rie | concept | nee | n.v.t. | 5 | nee |
| 25 | Forex tegeltje De leukste meester | Tante Rie | concept | nee | n.v.t. | 2 | nee |
| 26 | Katoenen tas De tofste meester | Tante Rie | concept | nee | n.v.t. | 2 | nee |
| 27 | Kaart Bedankt voor het leuke schooljaar | Tante Rie | concept | nee | n.v.t. | 10 | nee |
| 28 | Katoenen tas De liefste juf | Tante Rie | concept | nee | n.v.t. | 5 | nee |
| 29 | Proefpakket Rooibos | Tante Rie | actief | ja | ja | 10 (doorverkopen aan) | ja |
| 30 | Proefpakket Zwarte Thee | Tante Rie | actief | ja | ja | 10 | ja |
| 31 | Luxe Thee Cadeauset - Kir Royal Champagne | Tante Rie | gearchiveerd | nee | n.v.t. | - | nee |
| 32 | Luxe Thee Cadeauset - Beste van Borne | Tante Rie | gearchiveerd | nee | n.v.t. | - | nee |

Totalen:

| Groep | Aantal |
|---|---:|
| In de collectie | 32 |
| Online gepubliceerd (Webshop) | 21 |
| Concept (negen, allemaal juf- en meester-artikelen) | 9 |
| Gearchiveerd (beide Luxe Thee Cadeausets) | 2 |
| Online én verzendbaar | 21 van 21 |
| Online en alleen af te halen | 0 |
| Online en bestelbaar nu | 11 |
| Online maar uitverkocht (voorraad 0 of lager, geen doorverkoop) | 10 |
| Theegeschenken online (4 proefpakketten, 9 Tijd voor thee-kokers met 50 gram thee, 2 Thee en een mooi gesprek-sets met thee) | 15 |
| Daarvan bestelbaar | 7 (4 proefpakketten, 3 kokers) |
| Overig online (theelepel, 2 geurstokjes, 2 autoparfums, cadeaubon) | 6 |

Opmerkingen bij de tabel:
1. Tien van de 21 online producten hebben een negatieve voorraad (-6 tot -1) of 0. Dat wijst op verkoop aan de kassa zonder bijgewerkte voorraad. Met beleid "weigeren" zijn ze voor bezoekers uitverkocht. De collectie toont ze dan met het label "Uitverkocht" (themacode tr-collection-redesign).
2. De sortering is "Best verkocht". Bovenaan staan daardoor nu juist de uitverkochte Natural Flower Cards-producten, en de proefpakketten, het enige echte theeaanbod, staan midden in het raster. Dit is het eerste wat een bezoeker en Google zien.
3. Er is geen "luxe cadeauset" online. De zoekopdrachten 'luxe thee cadeau set' en 'thee geschenkset' kunnen dus alleen met de proefpakketten en de kokers beantwoord worden.
4. Een vermelding als "ook verkrijgbaar in de winkel" mag alleen bij voorraad (besluit Mark 21-10). Voor de tekst betekent dat: wel zeggen dat je in de winkel kunt ruiken en kiezen, nooit dat een bepaald product er ligt.

Verwante pagina's en collecties (ook gecontroleerd):

| Pagina of collectie | Status |
|---|---|
| /collections/proefpakketten | online, 5 producten: 4 actief en bestelbaar, Proefpakket Mix is concept |
| /collections/geven-is-leuker | NIET op Webshop (alleen Point of Sale, Shop en Google & YouTube): geeft online een 404. 15 producten, allemaal alleen kassa, waaronder 13 theegeschenken zoals "Theetje voor een topper" en "Sterkte thee" zonder beschrijving |
| /collections/juffen-en-meesters-cadeaus | online, maar alle 9 producten zijn concept: lege collectie |
| /collections/blond-amsterdam | bestaat niet (de collectie heet blond), geen redirect |

## 3. Huidige tekst van de drie pagina's

### /collections/cadeaus (collectie 561282515208)

| Onderdeel | Huidig | Tekens |
|---|---|---:|
| SEO-title | Thee Cadeau Kopen \| Cadeausets & Verrassingen – Tante Rie | 57 |
| Metabeschrijving | Op zoek naar een origineel thee cadeau? Bij Tante Rie vind je thee cadeausets, proefpakketten en accessoires — kant-en-klaar of zelf samen te stellen. | 150 |
| H1 | Thee Cadeaus (collectietitel; de H1 komt uit `collection.title`) | |
| Beschrijving | Drie alinea's. 1: "Op deze pagina vind je **theeproefpakketten** en **theecadeaus** van Tante Rie. Elk proefpakket bevat meerdere smaken losse thee in proefhoeveelheden — ideaal om te ontdekken welke thee bij je past, of als cadeau voor een theeliefhebber." 2: links naar zwarte thee, groene thee, rooibos, kruidenthee en het thee-assortiment van 130+ soorten. 3: "Naast proefpakketten vind je hier ook complete theecadeaus met losse thee, een zeefje, een blikje en een maatschepje — alles wat nodig is voor het perfecte theemoment. Leuk om zelf te bestellen of cadeau te geven." | |

Weergave (themacode): alinea 1 staat boven het productraster, alinea 2 en 3 in een blok onder het raster. De USP-balk toont de standaardteksten "Vers verpakt uit eigen winkel", "Meer dan 130 theesoorten", "Snel verzonden" (instellingen van sectie tr-collection-redesign staan leeg).

Bevindingen:
1. Title en meta noemen 'cadeausets' en 'verrassingen'. Die zijn er niet online.
2. De title bevat een gedachtestreepje (–), de meta en de beschrijving twee em-dashes. Dat is tegen de stijlregels.
3. Alinea 3 belooft "complete theecadeaus met losse thee, een zeefje, een blikje en een maatschepje". Zulke sets staan niet online (de Luxe Thee Cadeausets zijn gearchiveerd).
4. De titel is al 'Thee Cadeau Kopen', dus de hoofdterm staat al in de title; de H1 is "Thee Cadeaus" (meervoud, hoofdletter C), wat voor de zoekterm niet erg uitmaakt.

### /pages/thee-cadeau (pagina 166707790088, template cadeau)

| Onderdeel | Huidig | Tekens |
|---|---|---:|
| SEO-title (titel-tag) | Thee Cadeau Ideeën \| Voor Elk Budget & Gelegenheid \| Tante Rie | 62 |
| Metabeschrijving | Op zoek naar een thee cadeau? Tante Rie in Borne heeft cadeau-ideeën voor verjaardag, juf, collega en moederdag. Losse thee, Bunzlau Castle en meer. Binnen 1-2 werkdagen in huis. | 178 |
| H1 | Thee cadeau: ideeën voor elke theeliefhebber | |
| Body in Shopify | leeg; alle tekst staat in sections/tr-page-cadeau.liquid | |
| Tekst | Eyebrow "Thee cadeau gids", intro "Losse thee is een cadeau dat altijd past ...", secties Verjaardag, Juf en meester, Collega en Moederdag met drie kaarten per sectie, Per budget (tot 10, 10 tot 25, boven 25 euro), Cadeau tips (afhalen, verzending naar heel Nederland, "Persoonlijk bericht"), afsluitende knop | |

Bevindingen:
1. De hoofdknoppen en vier kaarten ("Bekijk alle cadeaus", "Complete cadeausets", "Kleine cadeausets", "Alle cadeau-ideeën bekijken") gaan naar /collections/geven-is-leuker. Die collectie staat niet op Webshop, dus bezoekers krijgen een 404. Het gaat om zes zichtbare links, plus de gestructureerde data (ItemList) onderaan de pagina.
2. "Bekijk de selectie" gaat naar /collections/juffen-en-meesters-cadeaus: een lege collectie (alle 9 concept). "Blond Amsterdam" linkt naar /collections/blond-amsterdam, die niet bestaat.
3. De meta (178 tekens) is te lang en wordt afgekapt. Ze noemt Bunzlau Castle en "binnen 1-2 werkdagen in huis" in één adem, terwijl Bunzlau-aardewerk alleen af te halen is.
4. De kaarten "Complete cadeausets" en "Kleine cadeausets" beloven sets die niet online staan. De kaarten onder "Moederdag" en "Boven 25 euro" sturen naar Bunzlau-servies, dat alleen af te halen is. De tekst zegt "Persoonlijk bericht ... geef dat aan bij je bestelling"; of dat nog kan is niet bevestigd (personalisatie is op 22-10 verwijderd, V1), en de tip "Verzending naar heel Nederland ... vers verpakt" past niet bij alles wat op de pagina staat.
5. De pagina is geen echte gids: er staan geen producten op, alleen links. Alleen 'thee cadeau verjaardag' laat een positie zien (10,8, 10 vertoningen).

### /pages/cadeaus-en-lekkers (pagina 165005787400, template page)

| Onderdeel | Huidig | Tekens |
|---|---|---:|
| SEO-title (titel-tag) | Een cadeau vol thee en lekkers dat je zelf mag samenstellen bij Tante Rie | 73 |
| Metabeschrijving | Tante Rie stelt op verzoek een persoonlijk cadeaupakket samen met bakmixen van De Bakzolder en een verpakking die precies past bij de gelegenheid en de ontvanger. | 162 |
| H1 | Cadeaus en Lekkers | |
| Body | "Naast thee en koffie vindt u bij Tante Rie ook heerlijke bakmixen van het merk De Bakzolder. Ideaal als cadeau of als traktatie voor uzelf." "Wij verzorgen op verzoek ook cadeauverpakking en stellen graag een persoonlijk cadeaupakket voor u samen. Vraag gerust naar de mogelijkheden." en een winkelfoto (alt "Cadeaus winkel") | |

Bevindingen:
1. Title (73) en meta (162) zijn te lang en krijgen geen impact op de cadeau-zoektermen; de pagina heeft in de data geen cadeau-queries.
2. De pagina staat in het footermenu ("Cadeaus en Lekkers") en gebruikt "u", terwijl de rest van de site "je" gebruikt. Het hoofdmenu "Cadeaus & Lekkers" linkt naar /collections/cadeaus, dus de collectie is al de menu-hoofdpagina.
3. De tekst is vooral een winkelaanbod ("op verzoek een persoonlijk cadeaupakket"). Dat is een mooi winkelargument voor Borne, maar de pagina moet niet met de hoofdpagina concurreren: geen 'thee cadeau' in title of meta, en één link naar de hoofdpagina. Dit is wel een stap-2-punt; de pagina is niet in de opdracht genoemd voor aanpassing.

## 4. Afweging en advies

| Criterium | /collections/cadeaus | /pages/thee-cadeau |
|---|---|---|
| Zoekintentie ('thee cadeau' is transactioneel) | Past: producten met prijs en winkelwagen | Zwakker: geen producten, alleen doorverwijzing |
| Vertoningen cluster nu | 1% (90 dgn), 0% (28 dgn) | 5% (90 dgn), 2% (28 dgn); enige echte positie (10,8) op 10 vertoningen |
| Producten online en verzendbaar | 21 van 32 online, 21 van 21 verzendbaar, 11 bestelbaar | Niet van toepassing, maar de belangrijkste links zijn kapot |
| Aansluiting op profielbericht van 10 november | Linkt al naar de collectie | Geen |
| Hoofdmenu | Menu "Cadeaus & Lekkers" wijst al naar de collectie | Staat niet in het menu |
| Risico | Dun aanbod, veel uitverkocht, sortering werkt tegen | Geen echte inhoud, kapotte links, meta met onwaarheid |

Advies: /collections/cadeaus is de hoofdpagina. Redenen: de zoekopdrachten zijn transactioneel, de collectie heeft verzendbare theegeschenken met prijs, het menu en het profielbericht wijzen er al naar, en de alternatieve pagina is nu een doodlopende gids. Het plan zegt "toch /pages/thee-cadeau als het merendeel van de producten niet online of niet verzendbaar is": dat is niet zo (66 procent online, 100 procent van het online aanbod verzendbaar).

Wat stap 2 (voorstel op 3 november) daaruit moet halen:
1. Title, meta en H1 van /collections/cadeaus op 'thee cadeau', zonder 'cadeausets' en zonder gedachtestreepjes; alleen beloven wat er online is: proefpakketten, kokers met thee, de cadeaubon en cadeaukaartjes.
2. /pages/thee-cadeau wordt kort: title en meta niet meer op de hoofdterm, een duidelijke link naar /collections/cadeaus, links naar /collections/proefpakketten en /pages/theewinkel-borne-twente, en geen links meer naar /collections/geven-is-leuker, /collections/juffen-en-meesters-cadeaus en /collections/blond-amsterdam. Dat is een wijziging in sections/tr-page-cadeau.liquid van het live thema; die gaat via een themakopie met diff, na akkoord van Mark (dit moet in het voorstel van 3 november als aparte stap staan, en is in de huidige opdracht niet benoemd).
3. De tekst van de Content-redacteur (concept-cadeau-2026-11-03.md) over proefpakketten, kokers en bezoek aan de theewand in Borne, zonder voorraadbelofte en zonder sets die er niet zijn.

Risico's die ik zie voor de effectmeting:
1. De homepage staat voor deze zoekopdrachten op positie 44 tot 55 en blijft ongemoeid. Het kan zijn dat Google de homepage blijft kiezen. Dat is geen reden om de collectie niet te kiezen, wel om het succescriterium van het plan (positie beter dan 30 voor 'thee cadeau' na zes weken, minstens 3 klikken per 28 dagen in december) niet hoger te leggen.
2. Als het assortiment onveranderd blijft, ziet een bezoeker in november en december vooral uitverkochte kaartjes. Dat raakt CTR niet, wel de verkoop. Daarom de vragen hieronder.

## Open vragen (voor Mark, nog niet in vragen-voor-mark.md; de hoofdsessie verwerkt ze)

V98 (hoog, vóór 3 november): kloppen de voorraden van de Natural Flower Cards-producten? Tien online cadeauproducten staan op 0 of lager: zes van de negen Tijd voor thee-kokers, beide Thee en een mooi gesprek-sets en beide geurstokjes. Komt er nieuwe levering voor december, of moeten ze offline tot er voorraad is? Zonder antwoord noem ik in de tekst geen enkele koker of set bij naam.
V99 (middel): mag de volgorde van /collections/cadeaus op handmatig, met de proefpakketten en bestelbare kokers bovenaan en de uitverkochte onderaan? Nu staat de sortering op Best verkocht. Dit is een collectie-instelling in Shopify, geen code.
V100 (middel): de collectie "Geven is leuker" heeft 13 theegeschenken (zoals "Theetje voor een topper", "Sterkte thee", "Feliciteer thee", ook Bakflesjes en Bierbrood in fles) die alleen op de kassa staan, zonder beschrijving. Wil je (een deel van) die online zetten als cadeauset-aanbod? Dat zou de cadeaupagina voor 'luxe thee cadeau set' en 'thee geschenkset' een stuk sterker maken, maar het is jouw beslissing en ze hebben eerst een beschrijving en foto's nodig. Ik publiceer niets zonder jouw antwoord.
V101 (laag): de meta en tekst van /pages/thee-cadeau zeggen dat een persoonlijk kaartje bijvoegen kan "bij je bestelling". Kan dat nog? Zonder antwoord haal ik die zin uit het voorstel.
V102 (laag): de USP-balk op /collections/cadeaus en alle andere standaardcollecties zegt "Vers verpakt uit eigen winkel" en "Snel verzonden" (standaardwaarden van het thema). "Vers verpakt" is bij het theewinkelconcept van 22-10 geschrapt. Mag dat in stap 2 meegenomen worden, als themainstelling?
