# Concept Actie 5: theewinkelpagina als winkelpagina en lokale doelpagina

Opgesteld door de content-redacteur op 22 oktober 2026. Bijgewerkt op 22 oktober 2026 na de review van de Kwaliteitsredacteur (marketing/review/review-actie-4-en-5-2026-10-22.md) en de antwoorden van Mark in marketing/vragen-voor-mark.md; zie onderaan "Verwerkt na review 22-10".

**Status: goedgekeurd met kleine aanpassingen (tweede review 23-10, marketing/review/review-theewinkel-tweede-2026-10-23.md). Vier kleine correcties zijn door de Kwaliteitsredacteur in de klanttekst verwerkt.** De klanttekst bevat geen MARK-markeringen meer. Alleen de foto's (V25) volgen nog. Na de tweede review door de Kwaliteitsredacteur levert On-page de voor-en-navergelijking; publicatie pas na akkoord van Mark. Er is niets gewijzigd in Shopify, het thema of op live pagina's, en er staat niets in changelog.md.

URL: https://tanterie.nl/pages/theewinkel-borne-twente

## Bronnen

| Bron | Wat ik eruit gebruik |
|---|---|
| CLAUDE.md | 70/30-prioriteit, voorraadregel winkel, POS-only producten, stijlregels |
| marketing/plan-2026-10.md, actie 5 en werkwijze tekstacties | Opdracht, nulmeting, succescriterium |
| marketing/zoekwoorden/clusters-2026-10-21.md | Cluster Theewinkel (90 dagen), kannibalisatie, lokale zoektermen |
| marketing/autoriteit/brief-2026-10-21.md | NAP, openingstijden, profielbeschrijving, attributen, openingsdatum profiel |
| marketing/rapporten/nulmeting-2026-10.md | Paginacijfers en trackingzoekwoorden |
| data/gsc/2026-10-21-nulmeting-huidig-querypage.json en -page.json | Zoekopdrachten per pagina, 28 dagen (22 september tot en met 19 oktober 2026) |
| Live pagina's /pages/theewinkel-borne-twente, /pages/contact, /pages/serviezen, /pages/over-ons (opgehaald 22 oktober) | Huidige tekst, links, wat al op de site staat |
| Thema: templates/llms.txt.liquid | Tekst over openingsjaar en eigenaar |

Beperking: ik had in deze sessie geen shell, dus ik heb de Search Console-scripts niet opnieuw gedraaid en geen Shopify-koppeling gebruikt. Alle cijfers komen uit de exports van 21 oktober (sc-domain:tanterie.nl). De paginatekst heb ik via de live site gelezen; de ophaaltool gaf een samenvatting per sectie en niet de volledige letterlijke tekst. Voor de voor-en-navergelijking moet On-page de huidige body uit Shopify kopiëren als backup.

De skills draft-content en brand-voice zijn in deze omgeving niet beschikbaar. Ik heb de stijlregels uit CLAUDE.md en mijn rolbeschrijving toegepast.

## 1. Analyse van de huidige pagina

### Wat er nu staat

| Onderdeel | Huidig |
|---|---|
| Title | Theewinkel in Borne, Twente \| Tante Rie, Bakkerssteeg 6 (55 tekens) |
| Meta description | Niet zichtbaar in de opgehaalde pagina; On-page moet in Shopify nagaan of er een staat |
| H1 | Losse thee kopen in Twente? Tante Rie zit in Borne |
| H2's | Bezoek de winkel, Online bestellen, Theespeciaalzaak in Twente, Wat vind je bij Tante Rie?, Bereikbaar vanuit heel Twente, Kom langs in Borne (daarna de vaste footerblokken) |
| Inhoud | Ruim 130 theesoorten, persoonlijk advies, opening "in 2024" in het centrum van Borne, eigenaar Nikkie, gratis parkeren in de buurt, station op vijf minuten lopen, verzending door heel Nederland in 1 tot 2 werkdagen vanaf 4,50 euro |
| NAP | Bakkerssteeg 6, 7622 GX Borne; di t/m za 10:00 tot 17:00; 06 38 29 11 89; webshop@tanterie.nl. Gelijk aan footer en Bedrijfsprofiel. Op de contactpagina staat het telefoonnummer volgens de autoriteitsbrief niet in de paginatekst |
| Kaart | Geen ingesloten kaart, wel een link Routebeschrijving naar Google Maps |
| Links | Vooral naar theecollecties; "Bunzlau Castle servies" linkt naar /collections/servies, die volgens de autoriteitsbrief nul producten toont. Geen link naar /collections/bunzlau, /collections/blond, /pages/blond-amsterdam-servies of /pages/serviezen |
| Afbeeldingen | Alleen productkaarten (1001 Nacht, Aardbeien, Bakzolder cakemix, 50 JAAR); geen foto van de winkel, gevel of het servies |

### Problemen

1. De H1 richt zich op 'losse thee kopen'. Dat is de intentie van /collections/thee. Het woord theewinkel staat niet in de H1, en de pagina krijgt voor 'theewinkel' maar 3 vertoningen op positie 91,3, terwijl de homepage er 152 heeft op positie 11,2.
2. Servies ontbreekt bijna, terwijl servies (209) en bunzlau servies (150) de grootste zoektermen in het Bedrijfsprofiel zijn. Dat Bunzlau en Blond alleen in de winkel af te halen zijn, staat er niet.
3. De Bunzlau-link wijst naar een collectie die leeg lijkt.
4. Feiten die elkaar tegenspreken: de pagina en llms.txt zeggen dat de winkel in 2024 opende, het Bedrijfsprofiel noemt 4 april 2014 als openingsdatum en er zijn reviews uit 2015 en 2016. De over-onspagina spreekt van een "nieuwe eigenaar". Mogelijk is 2014 de opening en 2024 de overname, maar dat weet ik niet. Het plan waarschuwt ook al voor een ongeziene wijziging van 2024 naar 2014 in een oud thema.
5. Parkeren, station en verzendkosten staan op de pagina maar zijn nergens anders te controleren.
6. Geen eigen beeld van de winkel. Voor een pagina die mensen naar de Bakkerssteeg moet krijgen is dat het grootste gemis.

### Zoekopdrachten waarop de pagina vertoont (28 dagen, 22 september tot en met 19 oktober)

Pagina totaal: 446 vertoningen, 4 klikken, CTR 0,90 procent, positie 5,7. De maand ervoor: 582 vertoningen, 4 klikken, positie 5,6.

| Zoekopdracht | Vert. | Klikken | Pos. | Duiding |
|---|---:|---:|---:|---|
| tante rie borne | 134 | 0 | 1,8 | Merk; de pagina staat als sitelink |
| tante rie | 82 | 0 | 1,9 | Merk; sitelink |
| kruidenwinkel borne | 21 | 0 | 6,7 | Lokaal; deels mensen die een andere winkel zoeken (zie hieronder) |
| thee uit twente | 14 | 0 | 29,4 | Lokaal; homepage staat op 12,6 met 24 vertoningen |
| toko borne | 12 | 0 | 8,1 | Ruis: een toko is een ander soort winkel |
| theewinkel | 3 | 0 | 91,3 | Hoofdzoekwoord; homepage 152 op 11,2 |
| de theewinkel | 3 | 0 | 83 | Hoofdzoekwoord |
| thee winkel borne | 3 | 0 | 2,0 | Lokaal; ook homepage (http://www op 1, 2 klikken; https op 1,8, 1 klik), /pages/thee-en-koffie en /pages/serviezen |
| natuurwinkel borne | 3 | 0 | 11,3 | Lokaal, randgeval |
| de kruiderij borne, kruiderij borne, gezondheidswinkel borne, gezondheidswinkel de kruiderij, ja | elk 1 | 0 | 13 tot 39 | Ruis: zoeken naar een andere zaak |

Van de 446 vertoningen zijn er 216 (48 procent) merkvertoningen als sitelink, zonder klik. Zichtbare zoekopdrachten zijn samen 280 vertoningen; de overige 166 en alle 4 klikken zitten in zoekopdrachten die Google niet toont. Gevolg: de CTR van 0,90 procent en de positie van 5,7 worden vooral door de sitelinks bepaald. Een nieuwe title zal die cijfers weinig veranderen. De winst zit in vertoningen voor 'theewinkel', 'thee winkel borne' en 'thee uit twente', en dus in H1, tekst en interne links.

Wat ik bewust niet als doel neem: 'kruidenwinkel borne', 'natuurwinkel borne' en de 'kruiderij'-zoekopdrachten lijken voor een deel op een andere zaak in Borne te wijzen. 'toko borne' is ruis. 'theewinkel opende' (in de 90-dagenexport 52 vertoningen) gaat vermoedelijk over een winkel in het dorp Opende en niet over de opening van Tante Rie. De tekst noemt kruidenthee wel, maar beweert niet dat Tante Rie een kruidenwinkel is.

### Eén doelpagina per zoekintentie

| Intentie | Voorbeelden | Doelpagina | Wat de theewinkelpagina doet |
|---|---|---|---|
| Een theewinkel zoeken, lokaal of algemeen | theewinkel, thee winkel borne, theewinkel borne, thee uit twente, theewinkel enschede, thee winkel in de buurt | /pages/theewinkel-borne-twente | Hoofdpagina: title, H1, eerste alinea en een H2 op theewinkel in Borne en Twente |
| Langskomen: adres, tijden, route | tante rie bakkerssteeg borne (66 keer in het profiel), openingstijden | /pages/theewinkel-borne-twente | Hoofdpagina; /pages/contact blijft voor het formulier en e-mail en linkt hierheen |
| Merk | tante rie, tante rie borne | Homepage | Niets; de sitelink is prima |
| Losse thee kopen | losse thee, thee kopen | /collections/thee | H1 'Losse thee kopen in Twente?' verdwijnt; alleen een link met ankertekst losse thee |
| Bunzlau servies | bunzlau servies, bunzlau winkels nederland | /collections/bunzlau | Korte alinea en link; geen Bunzlau-titel of -H2 die de collectie beconcurreert |
| Servies algemeen | servies, serviesset, porselein servies | /pages/serviezen | Korte vermelding en link |
| Blond Amsterdam | blond amsterdam servies, vaatwasser | /pages/blond-amsterdam-servies en /collections/blond | Link |
| Kookwinkel | kookwinkel twente, kookwinkel borne | Homepage voorlopig (positie 2,6 en 1,9, met klikken) | Eén keer genoemd in de tekst, niet in title of H1. De homepage blijft ongemoeid volgens het plan; pas na het startsein uit actie 1 bekijken we of deze termen naar de theewinkelpagina moeten |
| Thee cadeau | thee cadeau | /pages/thee-cadeau | Link |
| Geschiedenis van de winkel | over tante rie | /pages/over-ons | Link, geen eigen verhaal op deze pagina |

## 2. Voorgestelde tekst

De klanttekst hieronder is definitief voor de tweede review. Alle MARK-vragen zijn beantwoord of vervallen (zie hoofdstuk 4).

### Title

**Theewinkel in Borne, Twente | Tante Rie, Bakkerssteeg 6** (55 tekens, nageteld; grens 60). Dit is de huidige title, advies A, gekozen door Mark (V24). Hij blijft dus ongewijzigd.

### Metabeschrijving

Tante Rie is de theewinkel in Borne, aan de Bakkerssteeg 6. Ruim 130 soorten losse thee, servies van Bunzlau en Blond Amsterdam. Kom langs in de winkel.

(152 tekens, nageteld; grens 155. Gekozen door Mark (V24): slotzin zonder openingstijden, zodat de meta niet mee hoeft te veranderen met de tijden.)

### H1

Theewinkel in Borne: Tante Rie aan de Bakkerssteeg

### Introductie

Tante Rie is de theewinkel in het centrum van Borne, aan de Bakkerssteeg 6. Je vindt hier ruim 130 soorten losse thee, servies van Bunzlau Castle en Blond Amsterdam, theeaccessoires, cadeaus en bakmixen. De winkel is open van dinsdag tot en met zaterdag van 10.00 tot 17.00 uur. We nemen de tijd om met je mee te zoeken naar een thee die past bij wat je graag drinkt, of het nu voor jezelf is of voor iemand anders.

### H2: Losse thee kiezen in onze theewinkel in Borne

In de winkel vind je [losse thee](/collections/thee) in veel soorten, van zwarte thee zoals Earl Grey en Assam tot [groene thee](/collections/groene-thee), witte thee, [rooibos](/collections/rooibos), [kruidenthee](/collections/kruidenthee) en [vruchtenthee](/collections/vruchtenthee). Weet je nog niet wat je zoekt, vertel dan wat je lekker vindt en wat je liever laat staan. Dan stellen we een paar soorten voor en vertellen we hoe je ze het best zet. Je mag gerust aan de thee ruiken en soms ook proeven, zodat je weet wat je mee naar huis neemt.

Voor thuis hebben we [theefilters en maatschepjes](/collections/theefilters-en-maatschepjes) en [bewaarblikken voor losse thee](/collections/thee-bewaarblikken), zodat je thee lang goed blijft. Hoe lang je welke thee laat trekken en hoe heet het water moet zijn, lees je ook op onze pagina over [theebereiding](/pages/theebereiding-faq).

### H2: Servies bekijken en afhalen in de winkel

Veel mensen komen naar de winkel voor het servies. Het blauwe, handgemaakte Poolse aardewerk van [Bunzlau Castle](/collections/bunzlau) kun je bij ons in handen nemen, zodat je kleur en decor kunt vergelijken met wat je thuis al hebt. Neem gerust een kopje of schoteltje mee als je wilt aanvullen. Zoek je een decor dat niet in de winkel staat, dan kunnen we het voor je bestellen. Daarnaast verkopen we het kleurrijke servies van [Blond Amsterdam](/collections/blond). Op de pagina over [Blond Amsterdam servies](/pages/blond-amsterdam-servies) lees je meer over het merk en het servies.

Het aardewerk van Bunzlau Castle en het servies van Blond Amsterdam versturen we niet. Je koopt ze in de winkel, of je bestelt online en haalt je bestelling op aan de Bakkerssteeg. Het melamineservies van Bunzlau Castle versturen we wel. Een overzicht van al ons servies, ook van Rice, vind je op de pagina [serviezen](/pages/serviezen).

### H2: Een theewinkel voor heel Twente

Borne ligt tussen Hengelo en Almelo. Naast thee vind je bij ons ook [bakmixen](/collections/bakmixen) en [koffiebonen](/pages/thee-en-koffie), dus ook wie in Twente een kleine kookwinkel zoekt, kan bij ons terecht. Voor een cadeau helpt onze [gids voor theecadeaus](/pages/thee-cadeau) je op weg.

### H2: Adres, openingstijden en bereikbaarheid

Je vindt Tante Rie aan de Bakkerssteeg 6, 7622 GX Borne. De winkel is open van dinsdag tot en met zaterdag van 10.00 tot 17.00 uur. Op maandag en zondag zijn we gesloten, en ook op Eerste en Tweede Kerstdag (25 en 26 december) en op Nieuwjaarsdag (1 januari). Je kunt ons bellen op 06 38 29 11 89 of mailen naar webshop@tanterie.nl.

Parkeren kan gratis in de buurt, met een parkeerschijf of in de parkeergarage. De winkel is toegankelijk voor rolstoelen. Plan je route met [Google Maps](https://www.google.com/maps/search/?api=1&query=Tante+Rie+Bakkerssteeg+6+Borne).

### H2: Vragen over de winkel

**Ligt alles uit de webshop ook in de winkel?**
Alles wat in de webshop staat kun je bestellen, maar in de winkel ligt alleen wat op voorraad is. Kom je voor iets bijzonders, zoals een bepaald stuk Bunzlau, bel of mail dan even voordat je komt. Dan weet je zeker dat het er is.

**Kan ik Bunzlau Castle of Blond Amsterdam laten bezorgen?**
Het aardewerk van Bunzlau Castle en het servies van Blond Amsterdam versturen we niet. Je kunt ze in de winkel kopen of online bestellen en afhalen in Borne. Het melamineservies van Bunzlau Castle kunnen we wel versturen.

**Kan ik ook online bestellen?**
Thee, accessoires en cadeaus kun je bestellen in de webshop, en we versturen door heel Nederland. Meer over bestellen, verzenden en retourneren lees je bij de [veelgestelde vragen](/pages/veelgestelde-vragen).

### Wat ik bewust heb weggelaten

Het openingsjaar en de naam van de eigenaar staan niet in de tekst, omdat V13 onbeantwoord is en de bronnen elkaar tegenspreken (2014 in het profiel, 2024 op de site). Het verhaal achter de naam staat al op /pages/over-ons. Het station, klanten uit andere plaatsen, zelf een theemix samenstellen, verzendtermijn en verzendkosten en de naam van de parkeergarage zijn weggelaten omdat ze niet bevestigd zijn. De verzendinformatie is teruggebracht tot één vraag met een verwijzing naar de veelgestelde vragen, omdat deze pagina over de winkel gaat. Er staan geen gezondheidsclaims, prijzen of acties in.

### Afbeeldingen en alt-teksten

Notitie: de foto's komen nog (V25). Mark zet ze in assets/afbeeldingen/. Tot ze er zijn, gaat de pagina zonder eigen foto's door de review; de alt-teksten hieronder worden bij aanlevering gecontroleerd tegen wat de foto echt toont. Voorstel voor vier foto's:

| Plek | Foto | Alt-tekst |
|---|---|---|
| Bovenaan, naast de intro | Gevel en ingang | Gevel van theewinkel Tante Rie aan de Bakkerssteeg 6 in Borne |
| Bij de thee-sectie | Schappen of wand met losse thee | Schappen met losse thee in de theewinkel van Tante Rie in Borne |
| Bij de servies-sectie | Bunzlau Castle in de winkel | Blauw Bunzlau Castle servies in de winkel van Tante Rie in Borne |
| Bij de servies-sectie | Blond Amsterdam in de winkel | Servies van Blond Amsterdam in de winkel van Tante Rie in Borne |

De bestaande productkaarten op de pagina mogen blijven, maar alleen met producten die online gepubliceerd zijn. Geen POS-only producten, zoals Luminlique, als online te koop tonen.

### Kaart

Geen ingesloten kaart. Alleen de bestaande routelink naar Google Maps blijft (V23 onbeantwoord, dus geen themawerk).

## 3. Interne links

### Uitgaande links vanaf de theewinkelpagina

| Ankertekst | Doel | Opmerking |
|---|---|---|
| losse thee | /collections/thee | Vervangt de H1-focus op losse thee kopen |
| groene thee, rooibos, kruidenthee, vruchtenthee | /collections/groene-thee, /collections/rooibos, /collections/kruidenthee, /collections/vruchtenthee | Alle vier gecontroleerd op 22 oktober: bestaan, met 42, 24, 29 en 10 producten. Witte thee krijgt geen link |
| theefilters en maatschepjes | /collections/theefilters-en-maatschepjes | Bestaat, 10 producten |
| bewaarblikken voor losse thee | /collections/thee-bewaarblikken | Bestaat, 19 producten; steunt actie 4 |
| theebereiding | /pages/theebereiding-faq | Bestaat, met trektijd en watertemperatuur per soort |
| Bunzlau Castle | /collections/bunzlau | Vervangt de huidige link naar /collections/servies; bestaat, 79 producten |
| Blond Amsterdam | /collections/blond | Nieuw; bestaat, 40 producten, met de vermelding "Alleen afhalen in Borne" |
| Blond Amsterdam servies | /pages/blond-amsterdam-servies | Nieuw, telt mee voor de vier interne links uit actie 6; bestaat, behandelt vaatwasser en magnetron |
| serviezen | /pages/serviezen | Nieuw, de servies-hub uit actie 8; bestaat |
| Beste van Borne | /products/beste-van-borne | Vervallen in de tweede review (23-10): V20 vroeg of Mark een link naar dit uitverkochte product wil en bleef leeg, dus zin en link zijn uit de klanttekst gehaald |
| bakmixen | /collections/bakmixen | Bestaat, 10 producten |
| koffiebonen | /pages/thee-en-koffie | Nieuw (V21); bestaat, noemt koffiebonen van een lokale branderie |
| gids voor theecadeaus | /pages/thee-cadeau | Bestaat; doelpagina van het cadeaucluster |
| veelgestelde vragen | /pages/veelgestelde-vragen | Bestaat |
| over ons | /pages/over-ons | Bestaat; staat nu alleen in "Wat ik bewust heb weggelaten", niet in de klanttekst |
| Google Maps | Routelink naar Bakkerssteeg 6 | Bestaat al |

### Inkomende links naar de theewinkelpagina

Ankertekst steeds 'theewinkel in Borne' of een natuurlijke variant daarvan.

| Vanaf | Voorstel | Hoort bij |
|---|---|---|
| Homepage | Linkblok onder de collectieslider met "Theewinkel in Borne, Twente" staat klaar in preview-thema 203908153608, nog niet live (changelog 21 oktober) | Beslissing 7 in het plan |
| Footer, blok Informatie | Ankertekst "Winkel in Borne" wordt "Theewinkel in Borne" | On-page, themawijziging via voorstel |
| /collections/bunzlau | In de nieuwe intro: "Bekijk het servies in onze theewinkel in Borne", met adres en tijden | Actie 7 |
| /pages/serviezen | "Al het servies is te zien in onze theewinkel in Borne" | Actie 8 |
| /pages/blond-amsterdam-servies | Bij de zin dat Blond alleen af te halen is | Actie 6 |
| /pages/contact | Zin "Wil je langskomen? Op de pagina over onze theewinkel in Borne lees je hoe je ons vindt" | NAP-werk actie 9 |
| /pages/over-ons | Aan het eind van het verhaal een link naar de winkel | Nieuw |
| Blog /blogs/nieuws/een-kijkje-bij-bunzlau-nieuwe-seizoensfavorieten-en-een-leuk-nieuwtje | Link bij de eerste vermelding van de winkel | Actie 7 |
| Productpagina's | Alleen via actie 10, en alleen bij producten met voorraad in de winkel; geen vaste regel 'ook verkrijgbaar in de winkel' op alle producten | Actie 10, principebesluit Mark |

## 4. Wat Mark moet aanleveren of beslissen

### Antwoorden Mark, 22 oktober 2026

| Vraag | Antwoord | Gevolg voor de tekst |
|---|---|---|
| 8. Beste van Borne | Het is thee. | Zin mag blijven, maar niet als "thee uit Twente" (review 5.4): thee wordt niet in Twente geteeld. Bijvoorbeeld: "Wil je thee met een Twents tintje, dan is Beste van Borne de thee die naar ons dorp is vernoemd." Nog open: wie stelt hem samen en ligt hij in de winkel (Shopify-voorraad is negatief). Zonder voorraad geen winkelbelofte in deze zin. |
| Review 5.9, Blond Amsterdam | Kleurrijk. | "Het kleurrijke servies van Blond Amsterdam" blijft. De autoriteitsbrief (bericht 4, "licht en eenvoudig") moet hierop worden aangepast. |
| Review 5.12, "de" of "een" theewinkel | De theewinkel. | "De theewinkel in Borne" blijft in meta en intro, ook in het Bedrijfsprofiel-concept. |
| V14, feestdagen | Gesloten op Eerste en Tweede Kerstdag en op Nieuwjaarsdag. | Gewone zin in de sectie Adres: gesloten op 25 en 26 december en op 1 januari. Koopavonden en extra openingen staan er niet in, die wachten op V35. |

### Stand van de vragen

De vragen en antwoorden staan in marketing/vragen-voor-mark.md, sectie 5 (V13 tot en met V25), zodat er één bron is. Hieronder staat per vraag wat er met de tekst is gebeurd. Een lege vraag is volgens CLAUDE.md geen nee: de zin die op het antwoord wachtte, is weggelaten.

| V-nummer | Onderwerp | Uitkomst | Gevolg in de tekst |
|---|---|---|---|
| V13 | Openingsjaar en eigenaar | Leeg, vervallen | Geen openingsjaar en geen eigenaar |
| V14 | Feestdagen | Beantwoord | Gesloten op 25 en 26 december en op 1 januari |
| V35 | Koopavonden en extra openingen in december | Open | Niets toegevoegd |
| V15 | Parkeren en station | Beantwoord: in de buurt, met parkeerschijf of in de parkeergarage, gratis | "Parkeren kan gratis in de buurt, met een parkeerschijf of in de parkeergarage." Geen station, geen naam van de garage |
| V16 | Rolstoeltoegankelijk | Beantwoord: ja | "De winkel is toegankelijk voor rolstoelen." |
| V17 | Ruiken, proeven, eigen theemix | Beantwoord: ruiken en eventueel proeven | "Je mag gerust aan de thee ruiken, en soms kun je ook een kopje proeven." Eigen mix vervallen |
| V18 | Bunzlau en Blond niet verstuurd, afhalen, decors op bestelling | Beantwoord: ja | Servies-sectie en FAQ stellig. Op aanwijzing van Mark geldt "niet versturen" alleen voor het Bunzlau-aardewerk; Bunzlau-melamine wordt wel verstuurd |
| V19 | Klanten uit Hengelo, Enschede en Almelo | Leeg, vervallen | Alleen "Borne ligt tussen Hengelo en Almelo." |
| V20 | Beste van Borne | Leeg, vervallen | Zin met de beschrijving van de productpagina, zonder winkelbelofte |
| V21 | Koffie | Leeg, vervallen | Koffiebonen linken naar /pages/thee-en-koffie |
| V22 | Verzendtermijn en -kosten | Leeg, vervallen | Alleen een verwijzing naar de veelgestelde vragen |
| V23 | Kaart | Leeg, vervallen | Alleen de routelink |
| V24 | Title en meta | Beantwoord: advies volgen | Title A (55 tekens), meta met "Kom langs in de winkel." (152 tekens) |
| V25 | Foto's van de winkel | Open | Notitie in de afbeeldingensectie; foto's komen nog |

## Meting

Nulmeting en succescriterium volgen het plan: binnen zes weken na publicatie vertoningen voor 'theewinkel' op een positie beter dan 30 en voor 'thee uit twente' beter dan 15, minstens 8 klikken per 28 dagen op de pagina, en minstens 12 clusterklikken per 28 dagen. Advies aan de Analist: rapporteer de pagina ook zonder de merkzoekopdrachten 'tante rie' en 'tante rie borne', omdat die nu bijna de helft van de vertoningen uitmaken en de CTR drukken. Houd daarnaast routeverzoeken en bellen in het Bedrijfsprofiel bij als context.

## Volgende stap

De tekst is klaar voor de tweede review door de Kwaliteitsredacteur. Daarna levert On-page de voor-en-navergelijking met backup van de huidige body, title en meta. Publicatie en de regel in changelog.md volgen pas na akkoord van Mark.

## Verwerkt na review 22-10

Linkcontrole op 22 oktober 2026 via WebFetch op de live site. Ik had geen shell, dus geen curl met een letterlijke statuscode. WebFetch meldt een foutstatus zoals 404 of 429 apart; alle pagina's hieronder laadden zonder foutstatus en met echte inhoud, dus geen 404-pagina. Twee keer kreeg ik een 429 (te veel verzoeken). /collections/thee-bewaarblikken laadde bij de tweede poging wel. /products/assam gaf alleen een 429 en is niet opnieuw opgevraagd; Assam staat wel zichtbaar in /collections/thee. Doorverwijzingen zie ik met deze methode niet; On-page kan dat bij de voor-en-navergelijking nog met een crawler nagaan.

| Punt | Wat ik deed |
|---|---|
| 5.1 | Terugvalzin voor de meta is nu "Kom langs in de winkel." (meta dan 152 tekens). Meta met openingstijden nageteld: 153 tekens. |
| 5.2 | H2 is nu "Servies bekijken en afhalen in de winkel". Bunzlau Castle en Blond Amsterdam staan alleen nog in de alinea en de links. |
| 5.3 | De bewering over klanten van buiten Borne staat nu volledig binnen de MARK-markering. Zonder bevestiging blijft "Borne ligt tussen Hengelo en Almelo." |
| 5.4 | Antwoord Mark verwerkt: "thee uit Twente" is weg. Nieuwe zin: "Een thee met een knipoog naar ons dorp is Beste van Borne, een zachte blend van witte en groene thee met sinaasappelschil en amandel." De omschrijving komt letterlijk van de live productpagina. Geen winkelbelofte; de vraag of hij in de winkel ligt en wie hem samenstelt staat als MARK-markering en in V20. |
| 5.5 | "Het grootste deel van de winkel is thee." is weg. De zin begint nu met "In de winkel vind je losse thee in veel soorten". |
| 5.6 | Gecontroleerd: Assam en Earl Grey staan allebei online in /collections/thee. De zin blijft. |
| 5.7 | Alle interne link-URL's gecontroleerd, zie de tabel hieronder. Alles bestaat; niets hoefde eruit. Witte thee heeft geen link, zoals de review adviseerde. |
| 5.8 | MARK-markering toegevoegd aan de FAQ over bezorgen, gekoppeld aan V18, zodat de servies-alinea en de FAQ samen blijven of samen veranderen. |
| 5.9 | Antwoord Mark: kleurrijk. "Het kleurrijke servies van Blond Amsterdam" blijft. De autoriteitsbrief (bericht 4, "licht en eenvoudig") moet nog worden aangepast door Autoriteit en lokaal; dat heb ik niet gedaan. |
| 5.10 | Gecontroleerd op /collections/bunzlau: "Authentiek handgemaakt aardewerk" en "Handgeschilderd in Polen". "Handgemaakte Poolse servies" blijft staan. "Blauwe" heb ik niet apart aan productteksten getoetst; de review had daar geen bezwaar tegen. |
| 5.11 | Kookwinkelzin herschreven volgens de review: "Naast thee vind je bij ons ook bakmixen en koffiebonen, dus ook wie in Twente een kleine kookwinkel zoekt, kan bij ons terecht. Voor een cadeau helpt onze gids voor theecadeaus je op weg." Kookwinkel staat er één keer in, niet in title of H1. |
| 5.12 | Antwoord Mark: "de theewinkel in Borne" blijft in meta en intro. |
| 5.17 | NAP-regel in de analyse gecorrigeerd: gelijk aan footer en Bedrijfsprofiel, en op de contactpagina staat het telefoonnummer niet in de paginatekst. |
| V14 (antwoord Mark 22-10) | De MARK-markering over feestdagen in de sectie Adres is vervangen door een gewone zin: "Op maandag en zondag zijn we gesloten, en ook op Eerste en Tweede Kerstdag (25 en 26 december) en op Nieuwjaarsdag (1 januari)." Koopavonden en extra openingen heb ik niet toegevoegd, omdat V35 nog open staat. De meta blijft ongewijzigd (153 tekens), want die noemt alleen de vaste tijden. |
| Hoofdstuk 4 | De eigen genummerde vragenlijst is vervangen door een tabel die per V-nummer (V13 tot en met V25, plus V35) zegt bij welk deel van de tekst de vraag hoort en wat er gebeurt zonder antwoord. De vragen zelf staan alleen nog in marketing/vragen-voor-mark.md. De MARK-markeringen in de tekst en de linktabel verwijzen nu naar V18 en V20 in plaats van naar de oude nummers. |
| Overig | 5.15 (/pages/thee-en-koffie opnemen in de intentietabel) zat niet in de opdracht en is niet verwerkt. Over ons wordt in de klanttekst niet gelinkt, alleen in de notitie over wat is weggelaten. |

| URL | Uitkomst |
|---|---|
| /collections/thee | Laadt, H1 "Losse Thee", 137 producten |
| /collections/groene-thee | Laadt, 42 producten |
| /collections/rooibos | Laadt, 24 producten |
| /collections/kruidenthee | Laadt, 29 producten |
| /collections/vruchtenthee | Laadt, 10 producten |
| /collections/theefilters-en-maatschepjes | Laadt, 10 producten |
| /collections/thee-bewaarblikken | Laadt na een eerste 429, 19 producten |
| /pages/theebereiding-faq | Laadt |
| /collections/bunzlau | Laadt, 79 producten |
| /collections/blond | Laadt, 40 producten |
| /pages/blond-amsterdam-servies | Laadt |
| /pages/serviezen | Laadt |
| /products/beste-van-borne | Laadt, maar toont "Tijdelijk uitverkocht" |
| /collections/bakmixen | Laadt, 10 producten |
| /pages/thee-cadeau | Laadt |
| /pages/veelgestelde-vragen | Laadt |
| /pages/over-ons | Laadt |
| /pages/thee-en-koffie | Laadt; nu gelinkt vanaf "koffiebonen" (V21) |
| /products/assam | Niet gecontroleerd door 429; Assam staat wel in /collections/thee |
| Google Maps-routelink | Externe link, niet gecontroleerd; bestaat al op de huidige pagina |

Tekenaantallen opnieuw nageteld: title A 55, title B 55 (grens 60); meta met openingstijden 153, meta met "Kom langs in de winkel." 152 (grens 155).

### Definitief gemaakt na antwoorden Mark (V15 tot en met V24)

| Punt | Wat ik deed |
|---|---|
| Alle MARK-markeringen | Uit de klanttekst gehaald. Wat beantwoord is, staat er als gewone zin; wat leeg bleef, is weggelaten. De uitleg over MARK-markeringen boven de tekst is vervangen door een korte statusregel. |
| V15 | "Parkeren kan gratis in de buurt, met een parkeerschijf of in de parkeergarage." Station en naam van de parkeergarage niet genoemd. |
| V16 | "De winkel is toegankelijk voor rolstoelen." |
| V17 | "Je mag gerust aan de thee ruiken, en soms kun je ook een kopje proeven, zodat je weet wat je mee naar huis neemt." "Soms" geeft "eventueel" weer. Zelf een mix samenstellen is vervallen. |
| V18 en melamine | Bunzlau-decors op bestelling staat er nu stellig. Servies-sectie en FAQ: "Het aardewerk van Bunzlau Castle en het servies van Blond Amsterdam versturen we niet", gevolgd door de zin dat het melamine servies van Bunzlau Castle wel verstuurd wordt. In de servies-sectie heet Bunzlau nu "aardewerk", zoals op /collections/bunzlau. |
| V19 | Alleen "Borne ligt tussen Hengelo en Almelo." |
| V20 | Beste van Borne met de beschrijving van de productpagina, zonder winkelbelofte. |
| V21 | "koffiebonen" linkt naar /pages/thee-en-koffie. |
| V22 | Verzendtermijn en verzendkosten niet genoemd; alleen de verwijzing naar de veelgestelde vragen. |
| V23 | Sectie Kaart: alleen de routelink. |
| V24 | Title A, de huidige: "Theewinkel in Borne, Twente \| Tante Rie, Bakkerssteeg 6", 55 tekens. Meta: "Tante Rie is de theewinkel in Borne, aan de Bakkerssteeg 6. Ruim 130 soorten losse thee, servies van Bunzlau en Blond Amsterdam. Kom langs in de winkel.", opnieuw nageteld op 152 tekens. Alternatief B en de meta met openingstijden zijn uit de klanttekst gehaald. |
| V13 | Geen openingsjaar en geen eigenaar; de voorbeeldzin daarvoor is uit "Wat ik bewust heb weggelaten" gehaald. |
| V25 | Notitie in de afbeeldingensectie dat de foto's nog komen. |
| Status | Bovenaan "Status: klaar voor review". vragen-voor-mark.md niet aangepast, zoals gevraagd. |
