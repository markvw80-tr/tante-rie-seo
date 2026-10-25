# Search Console-meldingen: logboek

Logboek van de e-mails van Google Search Console sinds 1 september 2026, bijgehouden door de Technisch SEO-specialist. Bron: de mailbox van Mark, alleen gelezen via de Gmail-koppeling, alleen Search Console-mails, met toestemming van Mark (24-10-2026). Er is niets verstuurd, gelabeld, gearchiveerd of verwijderd. Er staan geen e-mailadressen of tokenlinks in dit bestand.

Laatst bijgewerkt: 24 oktober 2026. Laatst gelezen mail: 24-10-2026 08:06 UTC (Verkopersvermeldingen, ontbrekend veld image). Bij de volgende ronde alleen mails na dat moment lezen en nieuwe regels bovenaan de tabel "Logboek" toevoegen.

## Samenvatting

Er zijn 13 Search Console-mails gevonden (1 september tot en met 24 oktober): 9 over tanterie.nl en 4 over dutchteamaestro.com. Van de 9 mails over tanterie.nl zijn er 2 maandoverzichten (augustus en september), 1 gaat over indexering (Serverfout 5xx, 16 september) en 6 over gestructureerde gegevens (2 september, 25 september, 29 september twee keer, 16 oktober, 24 oktober). De 4 mails over dutchteamaestro.com (de tweede webshop van Mark en Nikkie, V71) zijn 2 maandoverzichten en 2 indexeringsmeldingen; daar doet dit team niets aan.

Gevonden is geen mail over een handmatige actie, beveiliging, eigendom of gebruikers, sitemaps, Core Web Vitals of de oude property webshop.tanterie.nl. Dat betekent dat er in deze periode geen zulke mail is verstuurd naar dit adres, niet dat het rapport in Search Console leeg is. Er is ook geen mail gevonden over een gestarte of afgeronde validatie van een oplossing.

Opgelost: de dubbele reviewgegevens van 25 en 29 september (drie mails) zijn op 23 oktober opgelost met de Judge.me-wijziging (changelog 23-10, regels over Judge.me-vinkje en Productschema Pakket en reviews). Waarschijnlijk opgelost maar nog niet bevestigd: "Dubbel veld brand" (16-10, thema-fix van 21-10) en de melding over offers, review of aggregateRating (02-09, de homepage-ItemList kreeg al offers). Open en onverklaard: de Serverfout (5xx) van 16 september en het ontbrekende veld image van vandaag.

Wat de mails niet geven: geen enkele mail noemt een URL. Ze noemen alleen het soort probleem en het aantal problemen of "sommige pagina's". De getroffen URL's staan alleen in het rapport in Search Console, en dat rapport kan het team in de cloudsessies niet bereiken (V81).

## Open meldingen, op volgorde van belang

### 1. Serverfout (5xx), nieuwe indexeringsreden, 16 september

Property tanterie.nl. De mail zegt "sommige pagina's" en geeft geen aantal of URL. Dit is de enige melding die vóór de zichtbaarheidsval van 22 en 23 september valt (zie marketing/rapporten/onderzoek-zichtbaarheidsval-2026-09.md, aanvulling 23-10, en plan-2026-11 actie 2). Waarschijnlijke oorzaak: niet vastgesteld. Mogelijkheden die nagelopen moeten worden: restanten van de migratie op webshop.tanterie.nl, een korte storing of overbelasting op het moment van crawlen, of URL's van producten die offline zijn gehaald. Het is een hypothese; de URL-lijst beslist.

Status: open. Volgende stap: export van het Indexeringsrapport (Pagina's, reden Serverfout (5xx), Exporteren) in data/gsc/, daarna per URL status controleren met curl en URL-inspectie en vaststellen of het migratie-URL's waren. Voorstel: de bestaande aanpak van plan-2026-11 actie 2, uiterlijk 5 december klaar. Blokkade: de export is handwerk of vraagt een sessie met toegang (V81, en V95 hieronder).

### 2. Verkopersvermeldingen, ontbrekend veld image (kritiek), 24 oktober

Property tanterie.nl. 1 probleem, kritiek: Google toont de betrokken pagina's niet als verkopersvermelding. Het aantal pagina's en de URL's staan niet in de mail. Waarschijnlijke oorzaak: een online gepubliceerd product zonder foto. In Shopify zijn 27 online producten zonder foto (Merchant-analyse 23-10, lijst in data/merchant/2026-10-23-online-zonder-foto.json), onder meer bunzlau-textiel en pu-erh-thee. Die twee zijn op 23-10 en 24-10 offline gehaald (pagina geeft nu 404), maar Google rapporteert met vertraging, dus de melding kan daarop slaan. Eerder (audit 21-10, Hoog 2) gaf ook luminlique-3-opzetters dezelfde fout; dat is een kassaproduct dat niet online hoort (404 is correct) en wordt niet doorgestuurd of gepubliceerd zonder overleg met Mark.

Status: open. Volgende stap: in het rapport Verkopersvermeldingen de voorbeeld-URL's bekijken en vergelijken met de lijst van 27 online producten zonder foto. Voorstel: het is een contentprobleem en geen themaprobleem; de oplossing is een foto (B3 in de Merchant-analyse, plan-2026-11 actie 6, Mark levert foto's, team plaatst na akkoord) of het product offline halen. Geen themawijziging nodig; een nepafbeelding in het schema is af te raden omdat het Google misleidt.

### 3. Verkopersvermeldingen, dubbel veld brand (kritiek), 16 oktober

Property tanterie.nl. 1 probleem, kritiek. Oorzaak is bekend: producten met de templates rice, joeff en waterfles hadden twee Product-blokken met verschillende merken (audit 21-10, Hoog 1). De mail van 16-10 komt vóór de fix. Status: waarschijnlijk opgelost op 21-10 (changelog 21-10, regel "Een Product- en een BreadcrumbList-blok per product", commit 22d37d4, en de Rich Results Test op 13 pagina's zonder fouten). Niet bevestigd door Search Console. Volgende stap: in het rapport op "Oplossing valideren" klikken, handwerk voor Mark (V95). Daarna sluiten zodra Google de validatie afrondt.

### 4. Productfragmenten, offers, review of aggregateRating moet zijn gespecificeerd (kritiek), 2 september

Property tanterie.nl. 1 probleem, kritiek. Oorzaak volgens de audit van 21-10: Product-items zonder offers, review of aggregateRating, onder meer in de homepage-ItemList. Het live thema geeft de vier uitgelichte producten inmiddels offers (voorstel-fixes-hoog-2026-10-21.md); het Judge.me-blok zonder offers is op 23-10 uitgezet. Status: waarschijnlijk opgelost, niet bevestigd. Volgende stap: valideren (V95) en controleren of in het Product-rapport nog items met deze fout staan; de tweede ItemList op de homepage nalopen als die nog Product-items zonder offers bevat.

### 5. Reviewfragmenten en samengestelde beoordelingen, 25 en 29 september

Zie het logboek: drie mails, alle drie over het dubbele Judge.me-blok. Opgelost op 23-10 (changelog 23-10: Judge.me "Add JSON-LD snippets" uitgezet door Mark, en productschema met review[] uit het themablok, 48 producten in profiel Pakket). Rest: in Search Console valideren (V95), zodat het rapport sluit. Dit staat laag in volgorde omdat de oorzaak is weggenomen.

Update 25-10: Mark heeft in het rapport Reviewfragmenten op "Oplossing valideren" geklikt. Voorbeelden in Search Console: drie keer https://tanterie.nl/products/geluksthee (het enige product met een Judge.me-review, 1 review). Uitkomst van de validatie volgt per mail; dan hier bijwerken. Productfragmenten en Verkopersvermeldingen: validatie en voorbeelden nog niet doorgegeven (V95).

## Logboek

Nieuwste bovenaan. Alle tanterie.nl-mails gaan over de property die de mail noemt als "tanterie.nl" (waarschijnlijk sc-domain:tanterie.nl; de mail zegt het niet).

| Datum | Soort melding | Property | Pagina's of aantal (zoals in de mail) | Waarschijnlijke oorzaak | Status | Volgende stap |
|---|---|---|---|---|---|---|
| 24-10 | Rich results: Verkopersvermeldingen, nieuw probleem (kritiek) "Ontbrekend veld image" | tanterie.nl | 1 probleem, aantal pagina's en URL's niet genoemd | Online product zonder foto (27 online producten zonder foto; bunzlau-textiel en pu-erh-thee net offline) | Open | Voorbeeld-URL's in Search Console bekijken; foto of offline (zie open melding 2; V95) |
| 16-10 | Rich results: Verkopersvermeldingen, nieuw probleem (kritiek) "Dubbel veld brand" | tanterie.nl | 1 probleem, geen URL's genoemd | Twee Product-blokken met verschillend merk op rice-, joeff- en waterfles-producten | Waarschijnlijk opgelost: changelog 21-10 (Een Product- en BreadcrumbList-blok per product, commit 22d37d4); niet bevestigd door Google | Valideren in Search Console (V95) |
| 07-10 | Indexering: nieuwe reden "Geblokkeerd vanwege ander 4xx-probleem" | dutchteamaestro.com | "Sommige pagina's", geen aantal | Niet te zeggen vanuit de mail; andere site | Geen actie voor dit team (V71, V96) | Alleen vastleggen; vraag V96 |
| 06-10 | Maandoverzicht zoekprestaties september | dutchteamaestro.com | 423 klikken, 92K vertoningen, 9 pagina's met eerste vertoningen | Niet van toepassing | Geen actie nodig (andere site) | Geen |
| 06-10 | Maandoverzicht zoekprestaties september | tanterie.nl | 446 klikken, 16,6K vertoningen, 51 pagina's met eerste vertoningen; top-pagina's http://www.tanterie.nl/ 213 klikken, https://tanterie.nl/ 100, /collections/joeff 16; top-zoekopdrachten tante rie 94, tante rie borne 79, muuss 8; apparaten 320 mobiel, 108 desktop, 18 tablet | Zie toelichting onder de tabel | Geen actie nodig | Meenemen in de maandrapportage (Analist) |
| 29-09 | Rich results: Verkopersvermeldingen, nieuw probleem (niet-kritiek) "Review heeft meerdere samengestelde beoordelingen" (in aggregateRating en in review) | tanterie.nl | 2 problemen, geen URL's genoemd | Dubbel Judge.me-blok naast het themablok | Opgelost 23-10: changelog 23-10 (Judge.me-vinkje uit; Productschema Pakket en reviews, V47, V58, V60) | Valideren (V95) |
| 29-09 | Rich results: Productfragmenten, nieuw probleem (niet-kritiek) "Review heeft meerdere samengestelde beoordelingen" (in review en aggregateRating) | tanterie.nl | 2 problemen, geen URL's genoemd | Idem | Opgelost 23-10, zelfde regels | Valideren (V95) |
| 25-09 | Rich results: Reviewfragmenten, nieuw probleem (kritiek) "Review heeft meerdere samengestelde beoordelingen" | tanterie.nl | 1 probleem, geen URL's genoemd | Idem | Opgelost 23-10, zelfde regels | Valideren (V95) |
| 16-09 | Indexering: nieuwe reden "Serverfout (5xx)" | tanterie.nl | "Sommige pagina's", geen aantal of URL's | Niet vastgesteld; migratierestanten of tijdelijke storing zijn hypotheses | Open | Export Indexeringsrapport en URL-controle (plan-2026-11 actie 2; V81, V95) |
| 08-09 | Maandoverzicht zoekprestaties augustus | dutchteamaestro.com | 304 klikken, 74,3K vertoningen, 13 pagina's met eerste vertoningen | Niet van toepassing | Geen actie nodig (andere site) | Geen |
| 08-09 | Maandoverzicht zoekprestaties augustus | tanterie.nl | 498 klikken, 21K vertoningen, 198 pagina's met eerste vertoningen; top-pagina's http://www.tanterie.nl/ 202 klikken, https://tanterie.nl/ 62, /collections/bunzlau 40; top-zoekopdrachten tante rie 96, tante rie borne 65, muuss 8; apparaten 379 mobiel, 104 desktop, 15 tablet | Zie toelichting onder de tabel | Geen actie nodig | Meenemen in de maandrapportage (Analist) |
| 06-09 | Indexering (sitemap): nieuwe reden "Alternatieve pagina met correcte canonieke tag" | dutchteamaestro.com | "Sommige pagina's", geen aantal | Normaal gedrag (pagina verwijst correct naar een canonieke versie); andere site | Geen actie voor dit team (V71, V96) | Alleen vastleggen; vraag V96 |
| 02-09 | Rich results: Productfragmenten, nieuw probleem (kritiek) "offers, review of aggregateRating moet zijn gespecificeerd" | tanterie.nl | 1 probleem, geen URL's genoemd | Product-items zonder offers, onder meer in de homepage-ItemList (audit 21-10) | Waarschijnlijk opgelost: live thema geeft de uitgelichte producten offers (voorstel-fixes-hoog-2026-10-21.md); niet bevestigd | Valideren (V95); tweede ItemList op de homepage nalopen |

### Toelichting bij de maandoverzichten van tanterie.nl

Augustus naar september: klikken van 498 naar 446 (min 10 procent, per dag ongeveer 16,1 naar 14,9), vertoningen van 21K naar 16,6K (min 21 procent), nieuwe pagina's met eerste vertoningen van 198 naar 51. Mobiele klikken zakten van 379 naar 320 (min 16 procent), desktop bleef gelijk (104 naar 108). Dat sluit aan bij het zichtbaarheidsonderzoek: klikken vrijwel gelijk, mobiel zwakker. De top-zoekopdrachten zijn in beide maanden merkzoekopdrachten (tante rie, tante rie borne, muuss). Opvallend is dat de oude link http://www.tanterie.nl/ in augustus 202 en in september 213 klikken kreeg, tegen 62 en 100 voor https://tanterie.nl/. Het Bedrijfsprofiel verwees tot 21 oktober naar de oude link (changelog 21-10, website-link), dus dit is geen migratieprobleem van Google maar het effect van die profiellink. Dit past bij de migratiemonitor. De cijfers in de mail zijn afgerond en tellen alleen weblocaties; vergelijk ze niet exact met data/gsc/.

## Koppeling met bestaand werk

De 5xx-melding van 16 september is het open spoor in het zichtbaarheidsonderzoek (aanvulling 23-10) en plan-2026-11 actie 2. De meldingen van 25 en 29 september over dubbele reviewgegevens zijn de directe aanleiding geweest voor V47 en V58 en zijn op 23-10 opgelost. De migratie naar tanterie.nl is zichtbaar in de maandoverzichten (www-link met veel klikken) en niet in een aparte migratiemelding; in de meldingen komt geen URL op webshop.tanterie.nl voor, maar omdat de mails geen URL's noemen is dat geen bewijs dat die niet meespelen bij de 5xx-melding.

## Dekking en beperkingen

Gezocht op afzender sc-noreply@google.com, op de afzender search-console-noreply@google.com (leeg) en op "Search Console" van een google.com-afzender (zelfde 13 mails). Alle 13 zijn volledig gelezen. Alleen mails ontvangen op het adres van Mark zijn te zien; meldingen die naar andere beheerders gaan staan hier niet. Mails vóór 1 september zijn niet bekeken. Search Console mailt alleen bij nieuwe problemen en niet bij herstel, dus het ontbreken van een mail betekent niet dat een probleem weg is.

## Vaste werkwijze

Aan het begin van elke opdracht, en minimaal wekelijks, leest de Technisch SEO-specialist nieuwe Search Console-mails sinds de laatste regel in dit logboek en werkt dit bestand bij (alleen lezen, alleen Search Console-mails, toestemming Mark 24-10). Nieuwe keuzes voor Mark gaan als V-nummer naar marketing/vragen-voor-mark.md. De eerstvolgende mail die wordt verwacht is het maandoverzicht van oktober, rond 6 november.
