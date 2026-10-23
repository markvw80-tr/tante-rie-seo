# Voorstel: theewinkelpagina en Blond-gidspagina, 23 oktober 2026

Rol: Technisch SEO. Status: alleen voorstel, wacht op akkoord van Mark. Niets gepusht naar live thema 203153015048, geen productdata of pagina's in Shopify gewijzigd, changelog.md en vragen-voor-mark.md niet aangeraakt.

## Kopie en preview

- Themakopie: "theewinkel-blond 2026-10-23", theme-id **203993612552**, ongepubliceerd, gemaakt met `shopify theme duplicate` van live 203153015048. Daarin gepusht met `--only`: `sections/tr-page-lokaal.liquid` en `blocks/_announcement.liquid`. De rest is gelijk aan live (live is vooraf gepulld en niet gewijzigd).
- Preview theewinkel: https://tanterie.nl/pages/theewinkel-borne-twente?preview_theme_id=203993612552
- Preview Blond (toont alleen de aangepaste aankondigingsbalk, de tekst staat in de paginabody): https://tanterie.nl/pages/blond-amsterdam-servies?preview_theme_id=203993612552
- De preview vraagt een cookie: open de link in de browser, of gebruik met curl een cookie-jar en `-L`.
- Diffs: `marketing/technisch/voorstel-theewinkel-2026-10-23.diff` (themasectie), `voorstel-announcement-blond-2026-10-23.diff` (aankondigingsbalk), `voorstel-blond-body-2026-10-23.diff` (oude tegenover nieuwe body-HTML).

## Pagina 1: /pages/theewinkel-borne-twente

Template page.lokaal, sectie `tr-page-lokaal.liquid`; de paginabody is leeg. De sectie wordt alleen door deze ene pagina gebruikt (alle 19 pagina's nagelopen via de Admin API). Pagina-SEO-velden staan in Shopify, niet in het thema.

### Waarden voor Shopify-pagina-SEO (Mark zet ze zelf)

- Title: `Theewinkel in Borne, Twente | Tante Rie, Bakkerssteeg 6` (55 tekens, ongewijzigd volgens het concept)
- Meta: `Tante Rie is de theewinkel in Borne, aan de Bakkerssteeg 6. Ruim 130 soorten losse thee, servies van Bunzlau en Blond Amsterdam. Kom langs in de winkel.` (152 tekens)

### Voor en na per sectie

**Hero, eyebrow**
- Oud: "Theewinkel in Borne, Twente"
- Nieuw: vervallen (niet in het concept; de H1 en title noemen het al)

**Hero, H1**
- Oud: "Losse thee kopen in Twente? Tante Rie zit in Borne"
- Nieuw: "Theewinkel in Borne: Tante Rie aan de Bakkerssteeg"

**Hero, intro**
- Oud: "Meer dan 130 theesoorten, vers verpakt. Je kunt ze online bestellen of langskomen in onze winkel aan de Bakkerssteeg in Borne. Persoonlijk advies inbegrepen."
- Nieuw: "Tante Rie is de theewinkel in het centrum van Borne, aan de Bakkerssteeg 6. Je vindt hier ruim 130 soorten losse thee, servies van Bunzlau Castle en Blond Amsterdam, theeaccessoires, cadeaus en bakmixen. De winkel is open van dinsdag tot en met zaterdag van 10.00 tot 17.00 uur. We nemen de tijd om met je mee te zoeken naar een thee die past bij wat je graag drinkt, of het nu voor jezelf is of voor iemand anders."

**Hero, knop**
- Oud: knop "Bekijk het assortiment" naar /collections/thee
- Nieuw: vervallen (niet in het concept; losse thee is gelinkt in de tekst)

**Twee kaarten "Bezoek de winkel" en "Online bestellen"**
- Oud: adres, tijden met en-dash ("10:00 – 17:00"), telefoon, e-mail; en "Woon je niet in Borne? We versturen naar heel Nederland. Snel verzonden, vers verpakt vanuit de winkel." met vier collectielinks
- Nieuw: kaarten vervallen. Adres, tijden, telefoon, e-mail staan nu in de sectie "Adres, openingstijden en bereikbaarheid" in de tekst, met "10.00 tot 17.00 uur", de feestdagen, parkeren en rolstoeltoegankelijkheid. De bestelzin staat in de FAQ ("we versturen door heel Nederland", zonder "snel" en "vers verpakt"). De CSS van de kaarten en knoppen is verwijderd.

**H2 "Theespeciaalzaak in Twente" (met 2024, Nikkie, biologische kruidenthee, "proeven")**
- Oud: "Tante Rie opende in 2024 haar deuren in het centrum van Borne. Eigenaar Nikkie selecteert elk product met de hand: van Japanse Sencha en Ceylon zwarte thee tot biologische kruidenthee en seizoensgebonden blends." en "In de winkel kun je thee ruiken, proeven en vragen stellen. Voor online bestellingen geldt hetzelfde advies via e-mail of telefoon. Twente heeft een echte theespeciaalzaak nodig. Tante Rie wil dat zijn."
- Nieuw: vervallen. Vervangen door H2 "Losse thee kiezen in onze theewinkel in Borne" met de concepttekst (soorten, advies, ruiken en soms proeven, theefilters, bewaarblikken, theebereiding) en zes collectielinks.

**H2 "Wat vind je bij Tante Rie?" (opsomming)**
- Oud: lijst met vijf punten, onder meer "vers verpakt per bestelling", "Bunzlau Castle servies en theepotten", "Persoonlijk advies bij elke aankoop"
- Nieuw: vervangen door H2 "Servies bekijken en afhalen in de winkel" (Bunzlau Castle, Blond Amsterdam, niet versturen, melamine wel, link naar /pages/serviezen) en H2 "Een theewinkel voor heel Twente" (bakmixen, koffiebonen, cadeaugids). Geen opsommingstekens meer.

**H2 "Bereikbaar vanuit heel Twente" (station)**
- Oud: "Borne ligt centraal in Twente, op vijf minuten rijden van Hengelo en twintig minuten van Enschede, Almelo en Oldenzaal. Gratis parkeren vlakbij de winkel aan de Bakkerssteeg." en "Liever niet rijden? Borne heeft een eigen treinstation, vijf minuten lopen van de winkel."
- Nieuw: "Borne ligt tussen Hengelo en Almelo." (in "Een theewinkel voor heel Twente") en "Parkeren kan gratis in de buurt, met een parkeerschijf of in de parkeergarage. De winkel is toegankelijk voor rolstoelen." (in de sectie Adres). Afstanden en station zijn vervallen.

**Kaartsectie "Kom langs in Borne" met knoppen**
- Oud: kop, adresregel, knop "Routebeschrijving" (maps.google.com/?q=...) en knop "Online bestellen"
- Nieuw: vervallen. De routelink staat in de tekst: "Plan je route met Google Maps" (https://www.google.com/maps/search/?api=1&query=Tante+Rie+Bakkerssteeg+6+Borne), conform het concept.

**Nieuw: H2 "Adres, openingstijden en bereikbaarheid"** met adres, tijden, gesloten op maandag, zondag, 25 en 26 december en 1 januari, telefoon en e-mail (tel- en mailto-links zoals voorheen).

**Nieuw: H2 "Vragen over de winkel"** met drie vragen (H3): alles uit de webshop in de winkel, bezorging van Bunzlau en Blond, online bestellen met link naar /pages/veelgestelde-vragen. Opmaak: H3 in dezelfde koppenstijl als de H2's, tekst in de bestaande `.trlok-content` stijl.

### LocalBusiness-schema in de sectie

| Veld | Oud | Nieuw |
|---|---|---|
| description | "Theespeciaalzaak in Borne, Twente. Meer dan 130 losse theesoorten, vers verpakt. Online bestellen of langskomen in de winkel." | "Theewinkel in Borne, Twente, aan de Bakkerssteeg 6. Ruim 130 soorten losse thee, servies van Bunzlau Castle en Blond Amsterdam, theeaccessoires, cadeaus en bakmixen." |
| hasMap | https://maps.google.com/?q=Bakkerssteeg+6,+7622+GX+Borne | https://www.google.com/maps/search/?api=1&query=Tante+Rie+Bakkerssteeg+6+Borne |
| openingHoursSpecification | dinsdag tot en met zaterdag 10:00 tot 17:00 | ongewijzigd |
| Overig (naam, adres, geo, telefoon, e-mail, priceRange, sameAs, @id) | | ongewijzigd |

Geen openingsjaar en geen eigenaar. Feestdagen niet in het schema (zoals nu). Let op: dit blok heeft dezelfde @id (https://tanterie.nl/#organization) als LocalBusiness-blokken elders; in de preview zie ik twee LocalBusiness-blokken op de pagina (één uit het thema-layout, één uit de sectie). Dat was al zo op live en is niet gewijzigd; apart te beoordelen.

## Pagina 2: /pages/blond-amsterdam-servies

**Waar staat de tekst: in de paginabody**, template `page` (templates/page.json, gedeeld met veel andere pagina's, blok page-content). De H1 komt uit de paginatitel. Daarom: nieuwe body-HTML in `marketing/content/blond-body-2026-10-23.html`, niets in Shopify gezet.

### Verzendregel

"Snelle verzending: 1-2 werkdagen!" staat niet in de body maar in de aankondigingsbalk van het thema (`sections/header-group.json`, gerenderd door `blocks/_announcement.liquid`). Op live staat ze op deze pagina nog, omdat de eerdere afhaalfix alleen de templates blond en bunzlau dekte. In de kopie is de voorwaarde in `blocks/_announcement.liquid` uitgebreid met `or page.handle == 'blond-amsterdam-servies'`. Preview: de balk toont nu "Alleen afhalen in Borne" en "Bakkerssteeg 6 in Borne, dinsdag tot en met zaterdag 10:00 tot 17:00", en "1-2 werkdagen" komt niet meer voor. Dit is een extra themawijziging naast de tekst; vervalt het akkoord hiervoor, dan hoeft alleen dat ene bestand niet mee.

### Voor en na per sectie

**Boven de eerste H2 (nieuw antwoordblok)**
- Oud: geen
- Nieuw: "Kan Blond Amsterdam servies in de vaatwasser? Ja, de mokken, bekers en borden kunnen in de vaatwasser. ..." (volledige tekst uit het concept, met link naar de theewinkel in Borne)

**H2 Waarom dit servies zo fijn is**
- Oud: "... Bij Tante Rie in Borne vind je veertig stuks uit de collectie: mokken, bekers, borden, kommen en theedoeken. ..."
- Nieuw: "... Bij Tante Rie vind je een ruime keuze uit de collectie, van mokken en mazagran-bekers tot borden, een theepot van 1,5 liter en een thermosfles. Wat op voorraad is, staat ook in onze winkel in Borne, en wat er niet ligt, kun je bestellen. ..." De overige zinnen blijven.

**Nieuwe H2 Blond Amsterdam in de vaatwasser, magnetron of oven** (direct na de intro) met vier H3's: vaatwasser, magnetron, oven, bezorgen. Tekst letterlijk uit het concept na de review.

**H2 Een greep uit de collectie**
- Oud en nieuw: zes productlinks ongewijzigd. Alt-teksten vervangen door die uit het concept (bijvoorbeeld "Blond Amsterdam Mazagran Liefste Juf" wordt "Blond Amsterdam mazagran-beker Liefste Juf van 0,5 liter met kleurrijke illustraties"). De winkelfoto uit het concept ontbreekt nog (Mark levert aan).

**H2 Materiaal en afwerking**
- Oud: "Alles is gemaakt van keramiek, ..."
- Nieuw: "Het servies is gemaakt van keramiek, ..." (reviewaanpassing; materiaal thermosfles niet bevestigd). Prijsrange (9,99 tot 39,99 euro) ongewijzigd; moet mee veranderen met de prijzen of vervallen.

**H2 Zo dek je er je tafel mee**
- Oud: twee alinea's, eindigend op "... gaan de kleuren daar verrassend goed mee samen."
- Nieuw: extra alinea over losse thee, theebereiding en /pages/serviezen.

**H2 Onderhoud en vaatwasser met H3 Magnetron en oven**
- Oud: "Hier moeten we eerlijk zijn: de vaatwasser wordt afgeraden. ..." en "In de magnetron kan het servies wel, maar het wordt snel warm. ... Voor de oven is het niet geschikt."
- Nieuw: vervallen, vervangen door de nieuwe H2 hierboven.

**H2 Een cadeau om te geven**
- Oud: "... Een aantal Mazagran-bekers kun je laten personaliseren. Houd dan rekening met een iets langere levertijd."
- Nieuw: die twee zinnen vervallen; de rest en de zin "Kom gerust langs..." plus de collectielink blijven.

Title en meta volgens concept (Shopify-pagina-SEO, niet in de body): title `Blond Amsterdam servies: vaatwasser en magnetron | Tante Rie` (60 tekens), meta `Kan Blond Amsterdam servies in de vaatwasser of magnetron? Het korte antwoord, onderhoudstips en hoe je het kleurrijke servies afhaalt in Borne.` (144 tekens).

**Voorwaarde uit de review:** de gidspagina mag pas live als de specificatietabel en onderhoudskaart op de Blond-productpagina's "Vaatwasser ok" tonen (nu "Handwas aanbevolen" via een ontbrekende tag "vaatwasser" op de producten). Dat is een productdatawijziging en ligt niet in deze opdracht.

## Controle op de preview

| Controle | Theewinkel (preview) | Blond |
|---|---|---|
| HTTP-status pagina | 200 | 200 |
| Links in de tekst | 17 van 17 geven 200 (16 interne links en Google Maps; tel en mailto overgeslagen) | Alle 12 links van de nieuwe body geven 200 (live, op tanterie.nl) |
| "2024", "Nikkie", "station", "atelier", "personali", "Handwas aanbevolen", "vers verpakt", "biologische" in paginatekst | 0 | 0 in de nieuwe body; de huidige live body bevat nog "personaliseren" en "Handwas" (verwacht, want niets in Shopify gewijzigd) |
| Gedachtestreepje, uitroepteken in de paginatekst | 0 | 0 |
| JSON-LD geldig | Alle blokken parsen (WebSite, 2x LocalBusiness, BreadcrumbList) | Parsen (WebSite, LocalBusiness) |
| Liquid-fouten | 0 | 0 |
| HTML nieuwe body in balans | n.v.t. | ja |

Kanttekeningen: de aankondigingsbalk bovenaan elke pagina bevat site-breed "Snelle verzending: 1-2 werkdagen!" (en dus "werkdagen" en een uitroepteken), ook op de theewinkelpagina. Dat klopt voor thee en staat los van deze opdracht (open punt V6). De Blond-body kon niet op de preview worden gerenderd zonder de pagina in Shopify te wijzigen; de body is daarom op tekst, links en HTML-structuur gecontroleerd als bestand. De Rich Results Test en een nieuwe crawl volgen na publicatie, omdat daarvoor een publieke URL nodig is.

## Voorstel voor uitvoering na akkoord

1. Theewinkel: `sections/tr-page-lokaal.liquid` uit kopie 203993612552 naar live pushen met `--only`, na controle dat live nog gelijk is aan de basis van de diff. Mark zet title en meta in Shopify.
2. Blond: `blocks/_announcement.liquid` mee pushen (optioneel), body uit `marketing/content/blond-body-2026-10-23.html` in Shopify zetten en title/meta aanpassen, pas nadat de tag-kwestie op de Blond-producten is geregeld.
3. Daarna Rich Results Test, nieuwe crawl en een regel in changelog.md.
