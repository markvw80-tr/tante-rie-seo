# Analyse: waarom de bewaarblik-productpagina's op positie 2 geen klik krijgen

Opgesteld door de Technisch SEO-specialist, opdracht uit marketing/plan-2026-11-vroege-start.md (Onderdeel 2, V94 akkoord 24-10-2026). Datum van de analyse: 24 oktober 2026 (gepland voor 30 oktober). Status: alleen onderzoek en voorstel. In Shopify en in het thema is niets gewijzigd. Er is niets gepubliceerd.

## Samenvatting

1. De twee pagina's zijn https://tanterie.nl/products/flowers-theeblik en https://tanterie.nl/products/arts-craft-thee-bewaarblik-100-gram-1 (Arts & Craft blauw). Beide staan voor 'thee bewaarblik' gemiddeld op positie 2,3 en 1,8 en kregen op die zoekopdracht in 90 dagen nul klikken uit 76 en 17 vertoningen.
2. Titel, metabeschrijving, afbeeldingen en productgegevens zijn in orde en passen bij de zoekopdracht. Op de pagina's zelf zit geen fout die deze nul verklaart. Dat nul klikken bij positie 2 statistisch ongewoon is (bij een gewoon organisch resultaat op positie 2 zouden ongeveer 8 tot 11 klikken uit 76 vertoningen verwacht zijn) wijst op het soort plek in de zoekresultaten, niet op de tekst.
3. Waarschijnlijkste oorzaak: de vertoning komt uit een productblok of een andere Google-weergave (gratis productvermelding via Google & YouTube/Merchant Center, of afbeeldingen) en niet uit een gewoon blauw organisch resultaat. In zulke blokken telt Search Console een hoge positie voor het hele blok, terwijl de klik minder vaak op het productresultaat valt. Dit is een hypothese. Ik kon het niet toetsen, omdat de dimensie "zoekweergave" (searchAppearance) niet in de bestaande exports zit en Search Console vanuit deze omgeving niet bereikbaar is.
4. Daarnaast heb ik in het thema vier echte, maar kleine, tekortkomingen gevonden die voor alle accessoires gelden (zie bevindingen 3 tot 6). Ze verklaren de nul niet, maar ze maken de pagina's minder overtuigend voor wie wel doorklikt.
5. Voorstel: eerst meten (stap 1, zonder wijziging), dan twee kleine themawijzigingen en twee tekstwijzigingen voorleggen aan Mark (stap 2 tot 5). Zie "Voorstel". Niets van het voorstel is doorgevoerd.

## Wat ik wel en niet kon controleren

Wel gecontroleerd:

- Search Console-cijfers uit de bestaande exports in data/gsc/ (2026-10-21-query-page-90d.json, 2026-10-21-pages-90d.json, nulmeting-huidig en nulmeting-vorigemaand querypage en pagedevice). Periode 90 dagen: 23 juli tot en met 18 oktober 2026.
- Productgegevens uit Shopify, alleen lezen (Admin GraphQL): titel, SEO-title, metabeschrijving, beschrijving, status, verkoopkanalen, voorraad per locatie, gewicht, afbeeldingen met alt-tekst en afmetingen, collecties, metafields met beoordelingen.
- Thema-code, alleen lezen, van het live thema 203153015048 ("Agent-ready koppen 2026-10-09", rol MAIN): snippets/tr-product-schema.liquid, snippets/tr-offer-policies.liquid, snippets/schema-structured-data.liquid, sections/tr-accessoires-redesign.liquid en templates/product.accessoires.json. Het productschema is dus beoordeeld op de code en niet op de uitvoer.

Niet gecontroleerd (de openbare site gaf geen verbinding, HTTP-code 000 via de proxy):

- De live HTML, de echte title en snippet in Google, en wat de pagina's daadwerkelijk renderen.
- De Rich Results Test. Het productschema is alleen uit de Liquid-code gelezen. Of Google het zonder waarschuwing accepteert, is niet bevestigd. Dit moet na elke themawijziging nog met de Rich Results Test en een nieuwe crawl (zie "Controle na doorvoeren").
- Of het Judge.me-blok als tweede Product-blok op de Arts & Craft-pagina's nog staat (op 23-10 stond het er, zie voorstel-judgeme-schema-2026-10-23.md; sindsdien is het themablok uitgebreid, maar de app-instelling is niet bevestigd).
- De afbeeldingen zelf (CDN niet bereikbaar). Alleen afmetingen en alt-tekst zijn bekeken.
- De zoekresultaatpagina zelf (welke blokken Google toont voor 'thee bewaarblik'), en de zoekweergave in Search Console.
- Merchant Center (geen credentials in deze omgeving).

## De twee URL's en hun cijfers

Bron: Search Console, property sc-domain:tanterie.nl, 23 juli tot en met 18 oktober 2026 (90 dagen). Pagina's zijn samengevoegd over varianten met parameters (?variant=...&utm_medium=product_sync).

| URL | Vertoningen | Klikken | Positie (gewogen) | Hoofdzoekopdracht |
|---|---:|---:|---:|---|
| /products/flowers-theeblik | 145 | 1 | 3,9 | thee bewaarblik: 76 vertoningen, 0 klikken, positie 2,3 |
| /products/arts-craft-thee-bewaarblik-100-gram-1 | 95 | 2 | 5,0 | thee bewaarblik: 17 vertoningen, 0 klikken, positie 1,8 |

Alle zoekopdrachten per pagina (90 dagen, vertoningen, klikken, positie):

Flowers: thee bewaarblik 76, 0, 2,3. thee blik 3, 0, 4,7. thee blikjes 3, 0, 2,7. theeblikjes voor losse thee 2, 0, 6,5 (plus 1 op een parameter-URL, positie 3). theeblikjes 1, 0, 2 (en 1 op parameter-URL, positie 2). theeblik, theeblik voor losse thee en theeblikken voor losse thee elk 1 tot 2 vertoningen op positie 3. hema theeblik 1, positie 13.

Arts & Craft blauw: thee bewaarblik 17, 0, 1,8. losse thee bewaarblik 13, 0, 5,0. bewaarblik thee 2, 0, 3,0.

De klikken die de pagina's wel kregen (1 en 2) kwamen dus niet via 'thee bewaarblik'. Welke zoekopdracht ze gaf, is uit de export niet af te leiden zonder de rijen te zien (die zoekopdrachten staan niet in de export; Search Console laat zeldzame zoekopdrachten weg).

Ontwikkeling: Flowers had in de 28 dagen tot 21 september 16 vertoningen op 'thee bewaarblik' (positie 1,2) en in de 28 dagen tot 19 oktober 8 (positie 1,0). A&C blauw had 7 (positie 1,0) en daarna 4 (positie 4,2). De posities zijn dus al maanden hoog en de aantallen blijven klein.

Het aantal is klein: samen 93 vertoningen op 'thee bewaarblik' in 90 dagen, terwijl Keyword Planner 210 zoekopdrachten per maand geeft (clusters-2026-10-24.md). De pagina's worden dus bij ongeveer één op de zeven zoekopdrachten getoond. Dat past bij een blok dat Google maar soms toont, en niet bij een vaste organische positie 2. De collectie /collections/thee-bewaarblikken heeft voor dezelfde zoekopdracht 163 vertoningen op positie 16,2.

Een derde pagina lijkt op het eerste gezicht ook zo'n geval, maar hoort er niet bij: /products/bewaarblik-rechthoekig-flowerbed-19x15-cm (36 vertoningen voor 'bewaarblik rechthoekig', positie 2,6, 0 klikken; 1 klik in totaal via 'bewaarblik'). Dat is een koekblik van Bunzlau Castle voor 15,95 euro, geen theeblik. Het hoort niet bij de opdracht, maar het patroon (hoge positie, geen klik, productvermelding) is hetzelfde.

## Bevindingen

### 1. Vermoedelijke hoofdoorzaak: vertoningen komen niet uit het gewone organische resultaat (hoog, hypothese)

Wat ik zie. De posities (1,0 tot 2,3) voor een zoekopdracht waarop de collectie zelf op 16 staat, zijn onwaarschijnlijk voor een gewone organische vermelding van een productpagina. Bij 76 vertoningen en een gebruikelijke CTR van ongeveer 10 tot 15 procent op positie 2 is de kans op nul klikken kleiner dan 0,1 procent als het een gewoon resultaat was. Dat past wel bij een productblok, een Shopping-weergave of een afbeeldingenresultaat. De pagina's doen ook mee in de feed van Google & YouTube (alle drie de producten zijn daarvoor gepubliceerd) en Search Console toont vertoningen op parameter-URL's met utm_source=google en utm_content=sag_organic, de gratis productvermeldingen.

Oorzaak. De positie in een blok geldt voor het hele blok; een klik gaat daar vaak naar een kaartje of een product, dat ook onder een andere URL of in Google zelf kan landen. Wat ik niet weet: of de klikken wel gemeten worden onder een andere weergave, en welk blok het precies is.

Oplossing. Meten, niet aanpassen: zie voorstel stap 1. Pas als blijkt dat het om gewone organische resultaten gaat, is een tekstwijziging aan title of meta de logische vervolgstap.

### 2. Titel en snippet zijn in orde, en passen bij de zoekopdracht (info)

SEO-titels en metabeschrijvingen (uit Shopify):

| Product | SEO-title | Tekens | Meta |
|---|---|---:|---|
| Flowers | Flowers Thee Bewaarblik (100g) – Voor Losse Thee \| Tante Rie | 60 | Theeblik Flowers is een stijlvol bewaarblik voor ca. 100g losse thee. Houdt je thee vers en is perfect als cadeau. Bestel nu bij Tante Rie. |
| A&C blauw | Arts & Craft Thee Bewaarblik (100g) – Voor Losse Thee \| Tante Rie | 65 | Arts & Craft theeblik (100g) bewaart losse thee stijlvol en vers. Beschermt tegen licht en lucht en is perfect als cadeau. Bestel nu bij Tante Rie. |

Beide titels bevatten 'thee bewaarblik' en 'losse thee'. De zoekopdrachten (thee bewaarblik, losse thee bewaarblik, theeblikjes voor losse thee) passen bij het product: het is een blik voor 100 gram losse thee, in metaal, met afsluitend deksel. De zoekintentie is dus voor deze pagina's goed bediend. De H1 is de producttitel ("Flowers thee bewaarblik (100 gram)" en "Arts & Craft thee bewaarblik blauw (100 gram)").

Kleine minpunten, geen oorzaak van de nul: de A&C-titel is 65 tekens en wordt in Google waarschijnlijk afgekapt (rond 60 tekens); de streepjes in de titel zijn lange streepjes; de A&C groen en A&C blauw hebben exact dezelfde SEO-title en bijna dezelfde meta, dus Google kan de twee niet onderscheiden (zie bevinding 7).

### 3. Productgegevens en afbeeldingen (info, geen fout)

Alle drie online gepubliceerd (Webshop, Shop, Google & YouTube). Flowers staat ook op Point of Sale. De Arts & Craft-blikken staan niet op de kassa, maar wel op de locatie Tante Rie Borne in voorraad (8 en 9 stuks). Prijs 6,25 euro voor alle drie. Gewicht ongeveer 78 tot 89 gram, dus verzendtarief 4,50 euro in het schema. Alt-teksten zijn aanwezig en beschrijvend ("Flowers thee bewaarblik 100 gram voor losse thee"). Er zijn twee afbeeldingen per product. Flowers en A&C blauw zijn 4284 bij 4284 pixels (ruim voldoende, ook voor Google). A&C groen is 780 bij 705 en niet vierkant (voldoende voor Google, maar kleiner dan de rest). Ik kon de afbeeldingen niet bekijken.

### 4. Productschema (code gelezen, Rich Results Test niet gedraaid) (middel)

Wat er staat (snippets/tr-product-schema.liquid, vanuit layout/theme.liquid aangeroepen via schema-structured-data.liquid voor de templates standaard, thee en accessoires): een BreadcrumbList en een Product met name, description, url, image (maximaal 5), sku, brand, een Offer met prijs, valuta, beschikbaarheid, itemCondition, verzending (4,50 euro, 1 tot 2 dagen verwerking, 1 dag transport) en retourbeleid (14 dagen), en een AggregateRating met losse reviews als er beoordelingen zijn. De code is consistent en er is precies één themablok per pagina.

Wat daaruit volgt:

- Flowers heeft 0 beoordelingen, dus geen sterren in Google. A&C heeft 1 beoordeling van 5 sterren. Eén beoordeling is te weinig voor een vertrouwenswekkend sterrensnippet, en Google toont sterren pas bij een redelijk aantal. Er is hier niets te herstellen, maar het verklaart dat de snippet zich niet onderscheidt.
- Op de Arts & Craft-pagina's stond op 23-10 ook het Judge.me-blok als tweede Product-blok (voorstel-judgeme-schema-2026-10-23.md). Het themablok is intussen uitgebreid met de losse reviews, maar of Judge.me zijn eigen JSON-LD heeft uitgezet, is niet bevestigd. Dit is een bestaand voorstel en hoort hier niet apart opgelost te worden; wel meenemen in de Rich Results Test. Flowers heeft geen reviews en dus geen tweede blok.
- Er ontbreken gtin en mpn (barcode is leeg). Dat is optioneel, maar voor producten in Google-productvermeldingen helpt een gtin bij herkenning. Dit vraagt gegevens die ik niet heb.
- Geen priceValidUntil. Dat is optioneel en geeft hooguit een waarschuwing, geen fout.

Conclusie: het schema is geen aannemelijke oorzaak voor het uitblijven van klikken, op voorwaarde dat de Rich Results Test geen fouten toont. Dat moet nog worden gecontroleerd.

### 5. Voorraad van Flowers staat op min 4 (middel)

Flowers thee bewaarblik heeft voorraad -4 op locatie Tante Rie Borne (on_hand -4) en voorraadbeleid "doorverkopen" (CONTINUE). Daardoor blijft de pagina "op voorraad" en meldt het schema InStock, terwijl de telling niet klopt. Dit staat ook al in voorstel-titles-joeff-blikken-2026-10-22.md. Het raakt de klikken niet direct, maar wel de betrouwbaarheid van de Google-productvermelding en de vermelding "op voorraad" die Google toont. Het is aan Mark om de telling te corrigeren (een telling in de winkel). Ik pas niets aan. Zie vraag 2.

### 6. Thema-tekortkomingen op de accessoirespagina (laag tot middel, gelden voor alle producten met template accessoires)

Gelezen in sections/tr-accessoires-redesign.liquid. Niet live bekeken, dus de weergave moet nog worden gecontroleerd.

a. Tagline kan kapot zijn. De regel is `{{ section.settings.tagline | default: cur.type | append: ' van Tante Rie' }}`. Als de productsoort leeg is (bij deze drie blikken is productType leeg) en er geen tagline is ingesteld, staat er alleen " van Tante Rie" onder de H1. Aannemelijk, maar niet gezien op de live pagina.

b. Belofte over verwerking klopt niet met de rest. De uitklap "Verzending & retour" zegt "Bestellingen worden dezelfde werkdag verwerkt". Het schema zegt 1 tot 2 werkdagen verwerking, en het besluit van Mark (V64) is "verstuurd binnen 1 tot 2 werkdagen". Zelfde afwijking is al gemeld voor Rice (voorstel-melamine-rice-2026-10-22.md).

c. Vaste trust-tekst "Uit eigen winkel Borne" staat op alle accessoires. De A&C-blikken staan niet op de kassa. Dat is geen voorraadbelofte zoals "ook verkrijgbaar in de winkel", maar het ligt dichtbij de regel dat zo'n vermelding alleen bij voorraad mag. Zie vraag 3.

d. Dunne inhoud. De uitklappen "Gebruiksinstructie" en "Over dit product" tonen dezelfde beschrijving (twee keer dezelfde 40 woorden), "Reiniging & onderhoud" zegt "Raadpleeg de verpakking voor specifieke reinigingsinstructies" en de productdetails (materiaal, afmetingen) ontbreken, omdat de metafields leeg zijn. Voor een blik is materiaal (metaal), afmeting en inhoud (circa 100 gram thee) juist wat de zoeker wil weten. Een tekstvoorstel hoort bij On-page.

### 7. Duplicate titels en bijna-dubbele producten (laag)

A&C groen (/products/arts-craft-thee-bewaarblik-100-gram) en A&C blauw (-1) hebben dezelfde SEO-title en bijna dezelfde meta. Er zijn ook Zilver-blikken met 'kopie' in de URL (zilver-thee-bewaarblik-100-gram-kopie, 3 vertoningen). Google kiest één van de twee. De URL-eindes "-1" en "-kopie" zijn niet beschrijvend, maar het wijzigen van URL's vraagt een redirect en is niet de moeite waard voor deze aantallen.

### 8. Interne link: de kruimelpad wijst naar de verkeerde collectie (middel)

Het kruimelpad op de pagina en in het schema gebruikt `product.collections | first`. Voor alle drie de blikken is dat Thee Accessoires (de eerste collectie in de lijst), niet Thee Bewaarblikken. De pagina's die op positie 2 staan, geven dus geen interne link met de ankertekst "Thee Bewaarblikken" door aan de collectie die op 'thee blikjes' moet gaan scoren (positie 29,7). Gecontroleerd voor de drie blikken uit dit onderzoek; andere bewaarblikken die in beide collecties staan, hebben waarschijnlijk hetzelfde probleem (niet nagelopen). Dit is een kleine, goedkope winst voor het doel van Onderdeel 2.

## Voorstel

Volgorde: eerst meten, dan de themawijziging, dan teksten. Niets hiervan is doorgevoerd. Elke wijziging gaat na akkoord van Mark eerst naar een kopie van het thema (theme duplicate), met diff, en pas daarna live.

### Stap 1. Meten (geen wijziging, door Mark of de lokale sessie, V81)

Draai in de lokale sessie dezelfde export met de dimensie zoekweergave, over 90 dagen, voor de twee URL's en de zoekopdracht 'thee bewaarblik':

`python3 gsc_query.py --days 90 --dimensions query,page,searchAppearance --limit 1000 --json`, daarna filteren op de twee pagina's. Als het script de dimensie niet kent, kan het via de Search Console-interface: Prestaties, Zoekweergave. Een tweede controle is handmatig: zoek 'thee bewaarblik' in een privévenster op een Nederlandse verbinding, en kijk welk blok de producten toont. Daarmee wordt hypothese 1 bevestigd of verworpen.

Beslisregel: als de vertoningen onder "Productvermeldingen" of "Afbeeldingen" vallen, is er geen tekstwijziging nodig en blijft het bij het voorstel hieronder; als ze onder gewone webresultaten vallen, is de snippet de volgende stap (title en meta herschrijven, zie stap 4).

### Stap 2. Kruimelpad naar de juiste collectie (thema, klein)

Bestand: snippets/tr-product-schema.liquid (schema) en sections/tr-accessoires-redesign.liquid (zichtbaar kruimelpad). Alleen producten die in Thee Bewaarblikken staan, veranderen.

Voor (schema):

```liquid
{%- assign breadcrumb_collection = product.collections | first -%}
```

Na (schema):

```liquid
{%- assign breadcrumb_collection = product.collections | first -%}
{%- for c in product.collections -%}
  {%- if c.handle == 'thee-bewaarblikken' -%}{%- assign breadcrumb_collection = c -%}{%- endif -%}
{%- endfor -%}
```

Voor (zichtbaar kruimelpad, in de sectie):

```liquid
{%- for c in cur.collections limit:1 -%}<a href="{{ c.url }}">{{ c.title }}</a><span>›</span>{%- endfor -%}
```

Na:

```liquid
{%- assign tr_crumb = cur.collections | first -%}
{%- for c in cur.collections -%}{%- if c.handle == 'thee-bewaarblikken' -%}{%- assign tr_crumb = c -%}{%- endif -%}{%- endfor -%}
{%- if tr_crumb -%}<a href="{{ tr_crumb.url }}">{{ tr_crumb.title }}</a><span>›</span>{%- endif -%}
```

Effect: de bewaarblik-producten linken vanuit hun kruimelpad naar /collections/thee-bewaarblikken. Het raakt alleen producten in die collectie. Controle na doorvoeren: een product in beide collecties, een product alleen in Thee Accessoires, de BreadcrumbList in de Rich Results Test.

### Stap 3. Tagline-fout herstellen (thema, klein)

Voor:

```liquid
<p class="tra-tagline">{{ section.settings.tagline | default: cur.type | append: ' van Tante Rie' }}</p>
```

Na:

```liquid
{%- assign tr_tagline_base = section.settings.tagline | default: cur.type -%}
{%- if tr_tagline_base != blank -%}
<p class="tra-tagline">{{ tr_tagline_base | append: ' van Tante Rie' }}</p>
{%- endif -%}
```

Eerst op een live pagina bevestigen dat " van Tante Rie" echt zichtbaar is. Zo niet, vervalt deze stap. De klantzichtbare vervangtekst (eventueel een vaste ondertitel voor blikken) is een tekst en hoort bij On-page, met review door de Kwaliteitsredacteur.

### Stap 4. Teksten (door On-page, niet door mij; alleen voorleggen)

- Verzendtekst in de uitklap "Verzending & retour" afstemmen op V64: "verstuurd binnen 1 tot 2 werkdagen" in plaats van "dezelfde werkdag verwerkt". Dit geldt voor alle accessoires.
- Productdetails (materiaal, afmeting, inhoud) invullen via de metafields specificaties voor de bewaarblikken. De feiten moeten van Mark komen (bijvoorbeeld de afmetingen). Zie vraag 4.
- Alleen als stap 1 uitwijst dat het om gewone organische resultaten gaat, dan SEO-titels voor de twee A&C-blikken uit elkaar halen. Voorstel voor de titel, met kleur:

| Product | Voor | Na | Tekens |
|---|---|---|---:|
| A&C groen | Arts & Craft Thee Bewaarblik (100g) – Voor Losse Thee \| Tante Rie | Arts & Craft theeblik groen voor losse thee, 100 g \| Tante Rie | 63 |
| A&C blauw | Arts & Craft Thee Bewaarblik (100g) – Voor Losse Thee \| Tante Rie | Arts & Craft theeblik blauw voor losse thee, 100 g \| Tante Rie | 63 |

De Flowers-titel blijft staan: hij is goed. De title en meta van de collectie blijven ongewijzigd tot de 28-dagenmeting rond 19 november (plan-2026-11-vroege-start.md).

### Stap 5. Voorraad Flowers (Mark)

De telling van Flowers (-4) laten corrigeren en het voorraadbeleid bekijken (zie vraag 2).

## Controle na doorvoeren

Na elke themawijziging in de kopie: Rich Results Test op /products/flowers-theeblik en /products/arts-craft-thee-bewaarblik-100-gram-1 (BreadcrumbList en Product, geen fouten, alleen de bekende optionele waarschuwingen), een nieuwe crawl van de accessoires-pagina's, en een controle van de kruimelpaden. Daarna 28 dagen later opnieuw de query- en paginacijfers van deze twee pagina's naast deze nulmeting leggen (90 dagen: 76 en 17 vertoningen, 0 klikken op 'thee bewaarblik').

Succescriterium voor deze analyse is geen klik-uitkomst op deze twee pagina's: de bewaarblik-productpagina's kunnen het doel (de collectie voor 'thee blikjes' naar positie 20 of beter) alleen ondersteunen via interne links. Het meetbare criterium is dus stap 2, 'thee blikjes' op de collectie, en dat staat in de opdracht voor On-page.

## Vragen voor Mark (nog niet in vragen-voor-mark.md gezet; de hoofdsessie zet ze erin met het volgende vrije nummer, nu V95)

1. Draait de lokale sessie (V81) de export met zoekweergave voor deze twee pagina's, en kijkt iemand een keer in een privévenster naar de zoekresultaten voor 'thee bewaarblik'?
2. Flowers thee bewaarblik staat op min 4 stuks in Tante Rie Borne. Hoeveel liggen er echt, en wil je dat het voorraadbeleid op "niet doorverkopen" gaat? (Tot dat is gecorrigeerd meldt Google "op voorraad".)
3. De tekst "Uit eigen winkel Borne" staat op alle accessoirespagina's, ook bij blikken die niet op de kassa staan. Mag die blijven, of wil je hem alleen bij producten met voorraad?
4. Wat zijn de afmetingen en het materiaal van Flowers en van de Arts & Craft-blikken (hoogte, breedte, metaal)? Dan kunnen de productdetails op de pagina gevuld worden.
