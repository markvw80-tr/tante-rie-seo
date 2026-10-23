# Inspectie Blond-servicepagina en /pages/zakelijk, 21 oktober 2026

Technisch SEO. Alleen gelezen en geanalyseerd: er is niets gewijzigd in Shopify, het thema of changelog.md. Ruwe data staat in data/gsc/2026-10-21-blond-*.json.

## Samenvatting

Blond: de pagina is technisch gezond (geindexeerd, eigen canonical, in de sitemap, crawl op 21-10) en de tekst is sinds 17 augustus niet gewijzigd. De val van 23 naar 1 vertoning per dag viel op 24 september, een dag voor de thema- en paginawijzigingen van 25 september, dus die zijn de oorzaak niet. De zoekopdrachten over de vaatwasser en magnetron zijn nergens anders heen verschoven; ze zijn volledig verdwenen. Meest waarschijnlijke oorzaak: de pagina was een nieuwe pagina die een tijdelijke testpositie kreeg en daarna door Google is teruggezet, mogelijk omdat het antwoord (vaatwasser afgeraden) niet aansluit op de vraag. Zekerheid: middel (circa 60 procent).

Zakelijk: de pagina is al offline. Hij geeft sinds minstens 21 september een 404, staat niet meer in Shopify Pagina's en niet in de sitemap, en er is geen interne link meer. De vertoningen stopten op 2 september. De stappen die Mark moest doen, zijn dus al gedaan; er rest alleen een keuze over een redirect.

## Taak A: /pages/blond-amsterdam-servies

### 1. URL-inspectie (Search Console)

| URL | Status | Google-canonical | Laatste crawl | Opmerking |
|---|---|---|---|---|
| /pages/blond-amsterdam-servies | Submitted and indexed, PASS | gelijk aan eigen canonical | 21-10-2026 13:40 | Verwijzer: alleen de pagina-sitemap |
| /collections/blond | Submitted and indexed, PASS | gelijk aan eigen canonical | 15-10-2026 | Verwijzers: producten en privacy-pagina |
| /products/mazagran-liefste-juf | Submitted and indexed, PASS | gelijk | 12-10-2026 | Alleen waarschuwingen in schema (review, aggregateRating, shippingDetails; deels opgelost door de schema-livegang van 21-10) |
| /products/mazagran-a-hug-in-a-mug | Submitted and indexed, PASS | gelijk | 07-10-2026 | Idem |

Er is geen indexatie-, canonical-, robots- of dekkingsprobleem. Google heeft de pagina op 21 oktober nog gecrawld en houdt hem in de index.

### 2. Live HTML

| Controle | Resultaat |
|---|---|
| Statuscode | 200 |
| Canonical | https://tanterie.nl/pages/blond-amsterdam-servies (zelfverwijzend) |
| Meta robots | geen tag (dus index, follow) |
| Title | Blond Amsterdam servies \| Tante Rie |
| H1 | Blond Amsterdam servies (een H1) |
| Sitemap | ja, in sitemap_pages_1.xml; /collections/blond staat in sitemap_collections_1.xml |
| Interne links naar de pagina | alleen vanaf /collections/blond; niet in het hoofdmenu (dat wijst naar de collectie), de footer, de homepage of /pages/serviezen |
| Inhoud | circa 4.600 tekens, 40 stuks uit de collectie, sectie "Onderhoud en vaatwasser" met de mededeling dat de vaatwasser wordt afgeraden |

### 3. Verloop per dag (Search Console)

De pagina kreeg vertoningen vanaf 16 augustus, twee dagen na publicatie (14-08), en bleef daarna 15 tot 49 per dag. Op 23 september waren het er nog 24 en op 24 september 1. Daarna 8 vertoningen in totaal tot en met 19 oktober. Het laatste weekgemiddelde voor de val was circa 27 per dag. De val is dus abrupt en niet geleidelijk.

Zoekopdrachten voor de val (1 t/m 23 september, 362 vertoningen met blond in de query): kan blond amsterdam servies in de vaatwasser (42), kan blond amsterdam in de vaatwasser (38), mag blond amsterdam servies in de vaatwasser (38), blond amsterdam servies (33), servies blond (29), servies blond amsterdam (29), blond amsterdam vaatwasser (21), kan blond amsterdam in de magnetron (15). Na de val (24-09 t/m 21-10, 72 vertoningen) bestaat de top uit onbelangrijke staartzoekopdrachten (blond, blond amsterdam tante, etagere blond). De vaatwasser- en magnetronvragen komen nergens meer voor, niet op een andere URL.

Verschuiving of kannibalisatie: van de 362 vertoningen voor de val stonden er 295 op de pagina, 23 op /collections/blond en de rest op producten en de homepage. Na de val staan er 25 op /collections/blond (gelijk aan voorheen), de rest verspreid over producten. De collectie nam dus niets over; het totaal voor het Blond-cluster is van 362 naar 72 gedaald. Van kannibalisatie met collectie, product of homepage is geen bewijs. Het zoekverkeer is weg, niet verplaatst.

### 4. Changelog en themageschiedenis

In changelog.md staat voor 24 september niets over Blond of de pagina; de vermelding over Blond (21-10) valt na de val. Shopify toont als laatste wijziging van de pagina 17-08-2026, dus de inhoud is niet aangepast. Wel zijn op 25-09-2026 09:14 meerdere andere pagina's bijgewerkt (Contact, Privacy, Over ons, Veelgestelde vragen, Cold Brew, Theewinkel en andere), de Blond-pagina niet, en die bulkwijziging ligt een dag na de val. Thema's rond de datum: "Fix-bunzlau-voorraad-per-variant 2026-09-11" en "SEO-audit-fixes 2026-09-25", beide niet gepubliceerd (preview). De git-geschiedenis in ~/TanteRie-Theme-Editor loopt maar tot 27 mei 2026 en bevat dus niets voor deze periode. Er is geen aanwijsbare eigen wijziging op 23 of 24 september.

### 5. Conclusie, zekerheid en oplossing

Oorzaak: een Google-ranking-effect, geen technische fout. Nieuwe pagina's krijgen vaak enkele weken een testpositie; hier tussen 16 augustus en 23 september. Twee andere nieuwe pagina's tonen hetzelfde patroon: Muuss van Joeff (gepubliceerd 27-08) viel op 11 september van 11 naar 1 vertoning per dag, en /collections/proefpakketten zakte in september. Verder past het dat de zoekintentie "kan het in de vaatwasser" een ja of nee verwacht, terwijl de sectie hierover pas laag op de pagina staat en weinig zichtbaar is. Zekerheid: middel (60 procent) voor het testpositie-effect; hoog (95 procent) voor dat het niet aan indexatie, canonical, robots, sitemap of een eigen wijziging ligt. Niet uitgesloten: een algoritme-update rond 24 september of een SERP-wijziging (AI-overzicht voor deze vragen). Dat laat de data niet zien; Semrush en Ahrefs zijn hier niet bruikbaar.

Oplossing, in volgorde:

1. Geef de pagina meer interne autoriteit: link hem vanuit /collections/blond (nu al), /collections/servies, /pages/serviezen en de beschrijving van de Blond-producten. Nu is de pagina bijna een weespagina.
2. Zet een kort, direct antwoord bovenaan: "Kan Blond Amsterdam in de vaatwasser? Nee, handwas wordt aangeraden" en idem voor magnetron, met een FAQ-blok eronder (FAQPage-markup levert geen rijk resultaat meer op, maar de tekst wel passagevertoningen).
3. Vraag na de wijziging opnieuw indexering aan via URL-inspectie en meet drie weken.

### Actie 7 (FAQ en een hoofdpagina kiezen)

In de huidige vorm niet zinvol. De baseline in het plan (829 vertoningen, positie 8) bestaat niet meer: de pagina krijgt nu circa 1 vertoning per dag. Een FAQ toevoegen aan een pagina die geen vertoningen meer heeft, meet niets. En de beslissing om een hoofdpagina te kiezen is overbodig: /collections/blond heeft niets overgenomen en staat stabiel op 10 vertoningen per dag. Adviseer actie 7 om te zetten naar: eerst de vaatwasser- en magnetronvragen bovenaan de bestaande pagina beantwoorden en de interne links toevoegen (oplossing 1 en 2), de pagina als hoofdpagina voor deze vragen houden, en na drie weken beoordelen. De 829 vertoningen zijn een tijdelijke piek geweest en geen richtwaarde voor het succes.

## Taak B: /pages/zakelijk offline halen

### 1. Interne links

| Plek | Resultaat |
|---|---|
| Live HTML homepage, /pages/over-ons, /collections/bunzlau, /pages/contact | 0 treffers op "zakelijk" |
| Hoofdmenu (main-menu) en footermenu (footermenu), opgehaald met alleen-lezen query | geen menu-item naar /pages/zakelijk |
| Lokaal thema scripts/theme-live-2026-10-21/ | geen link naar /pages/zakelijk in templates, snippets, layout, config en locales; de enige regel met het woord "zakelijk" staat in sections/tr-page-cold-brew.liquid (FAQ-zin over een cold brew fles) en is geen link |
| Sitemap | niet aanwezig in sitemap_pages_1.xml |
| Shopify Pagina's | geen pagina met handle zakelijk (19 pagina's opgehaald) |
| Statuscode live | 404 |

Search Console: de laatste crawl 21-09-2026 gaf "Not found (404)", met als verwijzers twee productpagina's (fruitycakemix, tijd-voor-thee-bedankt) die toen nog naar de URL leken te linken; in de huidige HTML is dat niet meer terug te vinden.

### 2. Verkeer

Laatste 90 dagen: 2.110 vertoningen en 0 klikken op /pages/zakelijk. Vertoningen liepen tot 2 september (circa 50 per dag, positie rond 38) en stopten daarna. Er zijn dus geen klikken om te redirecten. Backlinks: Ahrefs en Semrush zijn niet via de API te gebruiken en er is geen export in data/ahrefs; backlinks zijn niet gecontroleerd. De 0 klikken maken dat risico klein.

### 3. Advies

Laat de 404 bestaan. De pagina had geen klikken, stond op positie 38 en hoort volgens het beleid niet verder ondersteund te worden. Een 301 naar de homepage of naar /pages/contact zou een soft-404-signaal kunnen geven omdat de inhoud niet overeenkomt. Een redirect heeft alleen zin als er backlinks blijken te zijn; dan 301 naar /pages/contact (de enige pagina waar zakelijke vragen terecht kunnen). Bestaat er al een redirect /pages/zakelijk-bestellen naar de homepage: die staat er en kan blijven of weg; niet nodig.

Wat Mark nog moet doen: niets verplicht. Controleer eventueel:

1. Online winkel, Pagina's: bevestig dat Zakelijk niet meer in de lijst staat (nu al zo). Was hij verborgen in plaats van verwijderd, dan is de status Verborgen goed.
2. Online winkel, Navigatie: Hoofdmenu en Footermenu bevatten geen Zakelijk-item (nu al zo).
3. Online winkel, Navigatie, URL-omleidingen: alleen een redirect aanmaken van /pages/zakelijk naar /pages/contact als er backlinks blijken (bijvoorbeeld uit een handmatige Ahrefs-export).
4. Themabestanden: geen enkel bestand in het live thema bevat een link naar /pages/zakelijk; er hoeft niets uit.
5. In Search Console hoeft niets te gebeuren; Google verwijdert de URL vanzelf. Eventueel "Verwijdering aanvragen" voor een snellere opruiming.

## Ruwe data

Bestanden in /Users/markvanwijk/Tante Rie SEO/data/gsc/: 2026-10-21-blond-inspect-*.json (vijf URL-inspecties), 2026-10-21-blond-date-page.json, 2026-10-21-blond-date-query-page.json en 2026-10-21-blond-site-date-page-alles.json (alle pagina's per dag, 1 augustus t/m 21 oktober).
