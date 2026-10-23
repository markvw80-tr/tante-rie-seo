# Review Actie 4 en Actie 5, 22 oktober 2026

Kwaliteitsredacteur. Beoordeeld: marketing/onpage/voorstel-titles-joeff-blikken-2026-10-22.md (Actie 4) en marketing/content/concept-theewinkel-borne-2026-10-22.md (Actie 5). De voorstellen zelf zijn niet gewijzigd, er is niets in Shopify, het thema of changelog.md aangepast en er is niets gepubliceerd. De skill marketing:brand-review is in deze omgeving niet beschikbaar; ik heb de stijl- en spelregels uit CLAUDE.md en mijn rolbeschrijving toegepast.

## Samenvatting

| Stuk | Oordeel | Kern |
|---|---|---|
| Actie 4, Joeff en bewaarblikken | Goedgekeurd met aanpassingen | Stijl, lengtes en cijfers kloppen; geen afhalen of voorraadbelofte. Wel: "voor tegels" mogelijk een POS-only product, Joeff-meta bijna gelijk aan de Muuss-meta, en de bewaarblik-meta warmer en met "of" in plaats van "en". |
| Actie 5, theewinkelpagina | Goedgekeurd met aanpassingen, met een tweede review na de antwoorden van Mark | Geen jaartal en geen eigenaar in de klanttekst, NAP en tijden kloppen, voorraadregel goed. Wel: een Bunzlau-H2 die de eigen kannibalisatieregel breekt, enkele ongemarkeerde beweringen, "thee uit Twente" als misleidende herkomst, en de terugvalmeta is 156 tekens. |

## Wat ik zelf heb gecontroleerd en wat niet

Zelf geverifieerd:

1. Alle tekenaantallen hieronder, met de hand nageteld.
2. Paginacijfers in data/gsc/2026-10-21-nulmeting-huidig-page.json: Joeff 783/14/1,79/7,2; bewaarblikken 327/4/1,22/19,4; Muuss 15/2/7,0; theewinkelpagina 446/4/0,90/5,7. Vorige maand theewinkelpagina 582/4/5,6 in -vorigemaand-page.json. Alles gelijk aan de voorstellen en aan plan-2026-10.md.
3. Alle zoekopdrachten per pagina in -huidig-querypage.json die in de tabellen staan (Joeff zes regels, bewaarblikken negen regels, theewinkelpagina alle regels inclusief homepage-vergelijking). Alles klopt. De optelling 280 zichtbare vertoningen en 216 merkvertoningen (48 procent) klopt ook. Niet in de Joeff-tabel maar wel in de data: "muuss joeff", 6 vertoningen, positie 5,3; geen probleem.
4. NAP en openingstijden tegen marketing/autoriteit/brief-2026-10-21.md: Bakkerssteeg 6, 7622 GX Borne; 06 38 29 11 89 (footer-schrijfwijze); webshop@tanterie.nl; di t/m za 10:00 tot 17:00, maandag en zondag dicht; rolstoeltoegankelijke ingang staat aan in het profiel; openingsdatum profiel 4 april 2014. Het concept volgt dit.
5. llms.txt: zowel /Users/markvanwijk/TanteRie-Theme-Editor/templates/llms.txt.liquid als llms.txt noemen "opende in 2024" en "Eigenaar is Nikkie". De bewering van de content-redacteur klopt dus.
6. Het concept noemt in de klanttekst geen jaartal, geen eigenaar en geen naam (gezocht op 2014, 2024, Nikkie, eigenaar, sinds). Het enige "sinds [jaar]" staat in de interne toelichting als voorbeeld en gaat niet live.
7. Geen em-dashes, geen uitroeptekens en geen opsommingstekens in de voorgestelde klantteksten van beide stukken. De em-dash in de huidige bewaarblik-meta verdwijnt.
8. In de GSC-export van 90 dagen bestaan de product-URL's /products/tegelhouder-joeff, /products/tegeltje-kunsthouderschakel, /products/blik-rood, /products/theeblik-100-gram-emma-bridgewater-poppies en de effen 100-gramblikken in zwart, wit en zilver. Dat zegt iets over het bestaan van die producten, niet over hun publicatiestatus nu.

Niet zelf geverifieerd (geen Shopify-koppeling in deze sessie):

1. Publicatiestatus per product (welke Joeff- en blikproducten online staan); ik volg hier de opgave van On-page.
2. Of Muuss echt boorvrij is. De huidige collectie-meta en de Muuss-pagina zeggen het al, dus het is consistent met de eigen site, maar niet getoetst aan de fabrikant.
3. Of de collecties /collections/groene-thee, /collections/rooibos, /collections/kruidenthee, /collections/vruchtenthee, /collections/theefilters-en-maatschepjes, /collections/bakmixen en de pagina's /pages/theebereiding-faq, /pages/thee-cadeau en /pages/veelgestelde-vragen bestaan en een 200 geven.
4. Of Bunzlau Castle handgemaakt is volgens de eigen productteksten, en of Blond Amsterdam "kleurrijk" is volgens Mark.
5. De live meta description van de collecties en de theewinkelpagina.
6. De clustercijfers (537 vertoningen, 12 klikken) uit clusters-2026-10-21.md; ik heb alleen gezien dat ze gelijk zijn aan het plan.

## Actie 4. Titles en meta's Joeff en thee-bewaarblikken

Oordeel: goedgekeurd met aanpassingen.

### Tekenaantallen (nageteld)

| Tekst | Opgegeven | Nageteld | Grens | Oordeel |
|---|---:|---:|---:|---|
| Joeff title nieuw: Muuss van Joeff kopen \| Boorvrij wandsysteem \| Tante Rie | 56 | 56 | 60 | Goed |
| Joeff title huidig | 52 | 52 | 60 | Klopt |
| Joeff meta nieuw (eindigt op "Bestel online.") | 141 | 141 | 155 | Goed |
| Joeff meta variant B (eindigt op "Bestel online of kom langs.") | 154 | 154 | 155 | Goed, maar krap |
| Joeff meta huidig | 149 | 149 | 155 | Klopt |
| Bewaarblik title nieuw: Thee bewaarblik kopen: blikken voor losse thee \| Tante Rie | 58 | 58 | 60 | Goed |
| Bewaarblik title huidig | 46 | 46 | 60 | Klopt |
| Bewaarblik meta nieuw | 141 | 141 | 155 | Goed |
| Bewaarblik meta huidig | 129 | 129 | 155 | Klopt |
| Muuss title huidig | 56 | 58 | 60 | Telfout in het voorstel, wel binnen de grens |
| Muuss meta huidig | 156 | 156 | 155 | Klopt: te lang |

### Bevindingen

| Nr | Regel of tekst | Probleem | Verbetering |
|---|---|---|---|
| 4.1 | Joeff-meta: "voor tegels, kaarten en kunstbloemen" | Tegelhouder Joeff staat volgens het voorstel zelf alleen op de kassa. Als er online geen ander Joeff-product voor tegels staat, noemt de meta een toepassing waarvoor je online niets kunt kopen. In de data bestaat /products/tegeltje-kunsthouderschakel; of die online staat en bij Joeff hoort, heb ik niet kunnen zien. | On-page controleert in Shopify of Tegeltje kunsthouderschakel (of een ander tegelproduct) in de Joeff-collectie online staat. Zo ja: tekst blijft. Zo nee: "voor kaarten, kunstbloemen en meer" of "voor kaarten en kunstbloemen". |
| 4.2 | Joeff-meta begint met "Muuss van Joeff bij Tante Rie in Borne: boorvrij wandsysteem", de Muuss-pagina met "Muuss van Joeff bij Tante Rie in Borne: een boorvrij wandsysteem" | Bijna dubbele meta tussen twee pagina's die op dezelfde merknaam worden gevonden. Het voorstel wil de zoekopdrachten juist op de collectie laten landen; gelijke snippets werken dat tegen. | Joeff-meta laten beginnen met de koopintentie: "Bestel Muuss van Joeff bij Tante Rie in Borne: het boorvrije wandsysteem met basishouder en schakels voor tegels, kaarten en kunstbloemen." (138 tekens; met de aanpassing uit 4.1 korter). |
| 4.3 | Muuss-pagina, "geen wijziging voorgesteld" | De huidige meta is 156 tekens (boven de grens) en bevat de vaste belofte "in de winkel of online" voor alle Joeff-producten, terwijl de voorraadregel uit CLAUDE.md zegt dat de winkel alleen heeft wat op voorraad is. Dat is een bestaande overtreding, en met 4.2 de reden om deze meta in hetzelfde voorstel mee te nemen. | Voorstel aan Mark toevoegen, alleen meta, title blijft: "Hoe werkt Muuss van Joeff? Lees hoe het boorvrije wandsysteem met basishouder en schakels meegroeit met je smaak, en bekijk de collectie." (138 tekens). On-page controleert eerst of de pagina die uitleg echt geeft. Vraag aan Mark of hij dit wil. |
| 4.4 | Joeff-meta: geen "afhalen", geen voorraad | Gecontroleerd: de voorgestelde meta bevat geen afhaal- of voorraadbelofte. "bij Tante Rie in Borne" noemt de winkel als verkoper, dat is feitelijk. Goed. | Geen. |
| 4.5 | Variant B: "Bestel online of kom langs." | "Kom langs" na "bij Tante Rie in Borne" leest als: je kunt Muuss in de winkel zien. Dat is pas waar als er winkelvoorraad is; Shopify toont negatieve voorraad bij Joeff-producten. | Alleen gebruiken onder de voorwaarde die On-page zelf noemt (principebesluit actie 10 en gecontroleerde winkelvoorraad). Tot dan variant A. |
| 4.6 | Bewaarblik-meta: "of met print van Sara Miller en Sanderson" | Een blik heeft één print; "en" leest alsof beide merken op één blik staan. Bovendien eindigt de meta op "Tante Rie, Borne.", wat kortaf is voor de merkstem en geen uitnodiging bevat. | "Theeblikken voor losse thee, de meeste van 100 gram: effen in zwart, wit of zilver of met een print van Sara Miller of Sanderson. Bij Tante Rie in Borne." (153 tekens). |
| 4.7 | Bewaarblik-meta: merken en kleuren | Sara Miller en Sanderson komen overeen met de producten die volgens On-page online staan; de venster-, 250 gram- en 50 gram-blikken zijn terecht weggelaten. Wel: in de data bestaan ook /products/theeblik-100-gram-emma-bridgewater-poppies en /products/blik-rood. Het voorstel noemt alleen Garden Flowers als concept. Staat Poppies online, dan is het weglaten van Emma Bridgewater geen fout (de meta is geen volledige lijst), maar "effen in zwart, wit of zilver" is dan onvolledig als er ook een effen rood blik online staat. | On-page bevestigt in Shopify de publicatiestatus van Emma Bridgewater Poppies en Blik rood. Als rood online staat: "effen of met een print van Sara Miller of Sanderson" zonder kleurenlijst, of rood toevoegen als het binnen 155 tekens past. |
| 4.8 | "vooral van 100 gram" | Klopt met de opgave (ook een zilver blik van 50 gram en mogelijk het rechthoekige Flowerbed-blik online). "De meeste" is natuurlijker Nederlands. | Zie 4.6. |
| 4.9 | Title "Thee bewaarblik kopen" | Correct Nederlands is "theebewaarblik", maar de zoekopdracht is los geschreven en de H1 ook. In een title is dat aanvaardbaar. | Geen wijziging; niet in klantlopende tekst overnemen. |
| 4.10 | Kannibalisatie | Collectie Joeff (koopintentie) en Muuss-pagina (uitleg) zijn verschillende intenties; met 4.2 en 4.3 is dat ook in de snippet zichtbaar. Bewaarblikken: de collectie is de enige doelpagina; productpagina's die meedoen op "losse thee bewaarblik" zijn geen probleem. | Zie 4.2 en 4.3. |
| 4.11 | Muuss-title "56 tekens" | Telfout, het zijn er 58. | Corrigeren in het voorstel; geen gevolgen. |

Eerlijkheid en vragen aan Mark: goed. Verzending, levertijd, voorraad en de afhaalzin zijn als beslissing bij Mark neergelegd en niet ingevuld.

## Actie 5. Theewinkelpagina

Oordeel: goedgekeurd met aanpassingen. De MARK-vragen zijn eerlijk gemarkeerd en het stuk mag in deze vorm naar Mark. Na zijn antwoorden komt de definitieve tekst nog een keer langs mij, omdat er dan zinnen bij komen of vervallen.

### Jaartal en eigenaar

Gecontroleerd: de klanttekst (title, meta, H1, introductie, alle H2-secties en FAQ) noemt geen openingsjaar, geen "sinds" en geen eigenaar. De nieuwe body vervangt de huidige tekst met "in 2024" en "Nikkie", zodat die tegenstrijdigheid van de pagina verdwijnt. Ze blijft wel bestaan in llms.txt (2024, Nikkie, en in de statische llms.txt nog webshop.tanterie.nl en "4,9/5 Judge.me" naast 4,8 in het profiel). Dat valt buiten dit concept; advies: Technisch SEO zet llms.txt op de lijst, maar pas na het antwoord van Mark over 2014 en 2024.

### Tekenaantallen (nageteld)

| Tekst | Opgegeven | Nageteld | Grens | Oordeel |
|---|---:|---:|---:|---|
| Title A: Theewinkel in Borne, Twente \| Tante Rie, Bakkerssteeg 6 | 55 | 55 | 60 | Goed |
| Title B: Theewinkel Borne: thee en servies in Twente \| Tante Rie | 55 | 55 | 60 | Goed |
| Meta met openingstijden | 154 | 153 | 155 | Goed |
| Meta met terugvalzin "Kom langs of bestel online." | niet opgegeven | 156 | 155 | Te lang |

### Bevindingen

| Nr | Regel of tekst | Probleem | Verbetering |
|---|---|---|---|
| 5.1 | Terugvalzin meta: "Kom langs of bestel online." | Dan wordt de meta 156 tekens, één te veel. | "Kom langs in de winkel." (152 tekens) of de versie met openingstijden houden. |
| 5.2 | H2 "Bunzlau Castle en Blond Amsterdam bekijken en afhalen" | Het concept schrijft zelf: "geen Bunzlau-titel of -H2 die de collectie beconcurreert". Deze H2 doet precies dat, voor de zoekterm met de op een na grootste profielvraag. | "Servies bekijken en afhalen in de winkel". Bunzlau Castle en Blond Amsterdam blijven in de alinea en de links. |
| 5.3 | "Borne ligt tussen Hengelo en Almelo, en onze klanten komen niet alleen uit Borne zelf." | Het tweede deel is een bewering over klanten die buiten de MARK-markering staat, terwijl de zin erna juist als vraag is gemarkeerd. | De markering om de hele bewering zetten. Zonder bevestiging blijft alleen: "Borne ligt tussen Hengelo en Almelo." |
| 5.4 | "Zoek je thee uit Twente, dan is Beste van Borne de thee die de naam van ons dorp draagt." | "Thee uit Twente" suggereert een Twentse herkomst van de thee, en thee wordt niet in Twente geteeld. Dat is een herkomstclaim die niet klopt. De zin is wel als vraag gemarkeerd, maar de formulering moet ook na een ja anders. | Na antwoord van Mark bijvoorbeeld: "Wil je thee met een Twents tintje, dan is Beste van Borne de melange die naar ons dorp is vernoemd." Alleen als Mark bevestigt wat het is en dat hij in de winkel ligt (Shopify-voorraad is negatief). |
| 5.5 | "Het grootste deel van de winkel is thee." | Bewering over de winkelinrichting die ik nergens kan controleren; de profielzoektermen laten juist veel servies zien. | "In de winkel vind je [losse thee] in veel soorten, van zwarte thee ..." en de eerste zin laten vallen. "In alle soorten" wordt "in veel soorten". |
| 5.6 | "van zwarte thee zoals Earl Grey en Assam" | Earl Grey bestaat online (/products/earl-grey in het plan); Assam heb ik niet kunnen controleren. | Content-redacteur bevestigt dat Assam online staat, anders alleen Earl Grey noemen. |
| 5.7 | Links naar groene thee, rooibos, kruidenthee, vruchtenthee en andere collecties | De linktabel zegt "bestaan al deels". Een link naar een collectie die niet bestaat geeft een 404 op de belangrijkste lokale pagina. | Voor publicatie elke link-URL controleren op status 200 en op producten; wat niet bestaat gaat eruit of krijgt een bestaand doel. "Witte thee" heeft nu geen link; dat is goed zolang er geen collectie is. |
| 5.8 | FAQ "Kan ik Bunzlau Castle of Blond Amsterdam laten bezorgen? Nee, die twee merken versturen we niet. Je kunt ze in de winkel kopen of online bestellen en afhalen in Borne." | Zelfde feit als in de servies-sectie, waar het wel als MARK-vraag staat; hier niet. Het plan noemt Bunzlau en Blond "alleen af te halen", dus het is waarschijnlijk juist, maar de bevestiging moet voor beide plekken gelden. | Een markering toevoegen of een notitie dat de FAQ meevalt met vraag 6. |
| 5.9 | "het kleurrijke servies van Blond Amsterdam" | De autoriteitsbrief (bericht 4) noemt hetzelfde servies "licht en eenvoudig". Twee teksten die het merk verschillend beschrijven. | Mark kiest één beschrijving, die in beide teksten komt. Tot dan "het servies van Blond Amsterdam" zonder bijvoeglijk naamwoord. |
| 5.10 | "Het blauwe, handgemaakte Poolse servies van Bunzlau Castle" | Algemeen bekend en waarschijnlijk juist, maar niet getoetst aan de eigen productteksten. | Content-redacteur controleert of de Bunzlau-productteksten "handgemaakt" en "Pools" noemen; anders "het blauwe Poolse servies". |
| 5.11 | "Soms vinden mensen ons als kookwinkel in Twente. We zijn in de eerste plaats een theewinkel, maar ..." | Stroeve zin die op een zoekwoord is geschreven. | "Naast thee vind je bij ons ook [bakmixen] en koffiebonen, dus ook wie in Twente een kleine kookwinkel zoekt, kan bij ons terecht. Voor een cadeau helpt onze [gids voor theecadeaus] je op weg." Het woord kookwinkel staat er dan één keer in, zoals het plan vraagt, zonder title of H1. |
| 5.12 | Meta: "Tante Rie is de theewinkel in Borne" en intro "de theewinkel in het centrum van Borne" | "De" suggereert de enige; ik kan niet nagaan of dat zo is. Het Bedrijfsprofiel-concept gebruikt dezelfde formulering. | Klein punt voor Mark: als er geen andere theewinkel in Borne is, blijft het staan; anders "een theewinkel". |
| 5.13 | "ons dorp" | Borne is een gemeente en kern van ruim 20.000 inwoners; "dorp" is in de volksmond normaal en warm. | Geen wijziging nodig; vervalt met 5.4 als de zin vervalt. |
| 5.14 | Voorraadregel | Goed. De FAQ zegt letterlijk dat alles online te bestellen is en dat de winkel alleen heeft wat op voorraad is. Geen vaste regel "ook verkrijgbaar in de winkel"; die blijft bij actie 10. Productkaarten alleen met online producten en geen POS-only producten zoals Luminlique: goed. | Bij de productkaarten ook letten op negatieve voorraad (1001 Nacht -7 volgens de brief); online bestelbaar is iets anders dan in de winkel. |
| 5.15 | Kannibalisatie | De intentietabel is goed: theewinkel en langskomen op deze pagina, merk op de homepage, losse thee op /collections/thee, Bunzlau op de collectie, servies op /pages/serviezen. Twee punten: de H2 uit 5.2, en "thee winkel borne" landt ook op /pages/thee-en-koffie en /pages/serviezen. De rol van /pages/thee-en-koffie (185 merkvertoningen) staat niet in de tabel. | 5.2 aanpassen; /pages/thee-en-koffie in de intentietabel opnemen en daar een link met ankertekst "theewinkel in Borne" naar deze pagina zetten. |
| 5.16 | H1 en SEO-basis | Eén H1, met theewinkel en Borne; Twente in een H2 en in de title. Hoofdzoekwoord staat in title, H1, eerste zin en een H2, natuurlijk geplaatst. | Geen. |
| 5.17 | Analyse, regel "NAP ... Gelijk aan footer, contactpagina en Bedrijfsprofiel" | Volgens de brief staat het telefoonnummer niet in de paginatekst van de contactpagina. Geen klanttekst, wel een onnauwkeurigheid. | Corrigeren in het concept. |

Stijl: vloeiend proza, je-vorm, warm en deskundig. Geen vulwoorden of clichés van betekenis; "gerust" en "even" zijn gewoon spreektaal en passen bij een persoonlijke winkel. Geen gezondheidsclaims, prijzen of acties. "Zodat je thee lang goed blijft" is een gewone bewaartip, geen claim.

Eerlijkheid en vragen aan Mark: goed. Openingsjaar, eigenaar, parkeren, station, rolstoeltoegang, proeven en ruiken, eigen mix, bestellen op maat, herkomst van klanten, Beste van Borne, koffie, verzending, feestdagen, foto's en kaart zijn allemaal als vraag gemarkeerd. Uitzonderingen staan in 5.3 en 5.8.

## Voor de maker

On-page (Actie 4): 4.1, 4.2, 4.3 en 4.6 verwerken, 4.7 controleren in Shopify, 4.11 corrigeren. Daarna kan het voorstel naar Mark; een nieuwe review is niet nodig als alleen deze teksten veranderen.

Content-redacteur (Actie 5): 5.1, 5.2, 5.3, 5.5, 5.8, 5.11 en 5.17 verwerken; 5.6, 5.7 en 5.10 controleren; 5.4, 5.9 en 5.12 als vraag aan Mark toevoegen. Na de antwoorden van Mark de definitieve tekst opnieuw langs de Kwaliteitsredacteur.
