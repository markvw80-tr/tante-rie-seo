# Voorstel: cafeïnehoudende thee uit de cafeïnevrije collecties (23 oktober 2026)

Opgesteld door On-page op 23 oktober 2026. Status: doorgevoerd op 24-10 (V82 akkoord, review Kwaliteitsredacteur met aanpassingen in T1, T2 en V1). Zie changelog 24-10. Marks akkoord op V67 geldt voor het maken van dit voorstel. Er is niets gewijzigd in Shopify, changelog.md of vragen-voor-mark.md. Shopify is alleen gelezen. Backup van de huidige stand: marketing/onpage/backup-cafeine-thee-collecties-2026-10-23.json.

Werkwijze en beperkingen. Per product zijn collectielidmaatschap, status, ingrediënten, tags, het metaveld cafeïnegehalte en de alt-teksten gelezen. Of een product online staat is afgeleid uit de online-winkel-URL (niet leeg), want het veld publishedOnCurrentPublication vraagt een scope die de koppeling niet heeft. De drie collecties zijn handmatige collecties, dus verplaatsen gaat per product. De afbeelding van Sterrennacht kon ik niet bekijken (de omgeving blokkeert het ophalen van afbeeldingen), dus de nieuwe alt-tekst beschrijft het product en geen beeldelementen. De live paginatitel (SEO-title) is niet in Shopify te lezen: het veld is leeg en de titel komt dus uit het thema. De themecode staat niet in deze omgeving.

# Deel 1. Welke producten bevatten cafeïne en waar horen ze

Alle zes producten van de lijst staan online (status actief, online-winkel-URL aanwezig) en bevatten cafeïne omdat de ingrediëntenlijst zwarte of groene thee noemt. Daarnaast is er één product dat niet op de lijst stond: Marocco Mint. Samen zeven producten.

| Product | Staat nu in | Waarom cafeïne (ingrediënten) | Voorstel collectie | Uit de cafeïnevrije collectie? |
|---|---|---|---|---|
| Boswandeling | vruchtenthee, zwarte-thee | Zwarte thee, aardbeibladeren, aroma, stukjes aardbei, saffloerbloesem | blijft in zwarte-thee | Ja, uit vruchtenthee |
| Sterrennacht | rooibos, zwarte-thee | Zwarte thee, rooibos, dadel, kaneel, sinaasappelschil, sinaasappelbloesem, aroma, saffloerbloesem | blijft in zwarte-thee | Ja, uit rooibos |
| Twentse Land | kruidenthee | Zwarte thee, peterselie, wortelvlokken, aroma | zwarte-thee erbij | Ja, uit kruidenthee |
| Gember Chai | kruidenthee, zwarte-thee | Zwarte thee, gember | blijft in zwarte-thee | Ja, uit kruidenthee |
| Elfjesthee | kruidenthee, groene-thee | Stukjes appel, groene thee, amandel, cassiabast, citrusschil, aroma | blijft in groene-thee | Ja, uit kruidenthee |
| Pu-erh thee | kruidenthee | Pu-erh zwarte thee (100%), volgens de productbeschrijving | zwarte-thee erbij | Ja, uit kruidenthee |
| Marocco Mint (niet op de lijst) | kruidenthee, groene-thee | Groene thee, kruizemunt, aroma | blijft in groene-thee | Ja, uit kruidenthee |

Wat dit betekent voor de aantallen na doorvoeren: kruidenthee gaat van 30 naar 25 producten (24 online, want Goede Nacht is een concept), rooibos van 24 naar 23, vruchtenthee van 10 naar 9, zwarte-thee van 42 naar 44. Groene-thee blijft 42. De zwarte-theepagina zegt "meer dan 40 losse zwarte theesoorten", dat blijft kloppen.

Alle zeven producten behouden hun plek in "thee" en "losse-thee-btw-9". Alleen de collecties vruchtenthee, rooibos en kruidenthee veranderen.

## Bijzonderheid: Pu-erh thee heeft de gegevens van een muntthee

Het product Pu-erh thee is vermoedelijk gemaakt door een kopie van Kruizemunt Nana Mint en daarna maar half aangepast. De productbeschrijving en het zetadvies zijn die van pu-erh, de rest niet. Dat is een groter risico dan de collectie zelf, want het product meldt zichzelf op meer plekken als cafeïnevrij (ook richting Google Shopping en Merchant Center). Voorstel voor de gegevens van dit ene product:

| Veld | Huidige waarde | Voorgestelde waarde | Reden |
|---|---|---|---|
| SEO-title | Kruizemunt Nana Mint – Zachte Spearmint Kruidenthee \| Tante Rie | Pu-erh Thee \| Aardse, Nagefermenteerde Thee \| Tante Rie (55 tekens) | Titel hoort bij het product. Noemt nu een ander product. |
| SEO-description | Kruizemunt Nana Mint (spearmint) is een zachte, caffeïnevrije kruidenthee met een milde, frisse muntsmaak. Ideaal voor Marokkaanse muntthee. Bestel bij Tante Rie. | Pu-erh: nagefermenteerde zwarte thee, krachtig, kruidig en aards, met een donkerrode kop. Vers afgewogen in Borne, verstuurd binnen 1 tot 2 werkdagen. (150 tekens) | Beschrijft nu een muntthee en claimt "caffeïnevrij". Nieuwe tekst gebruikt de smaak uit de productbeschrijving en de afgesproken levertijd (V64). |
| Tags | cafeïnevrij, fris, kruidenthee, munt, spearmint | aards, pu-erh, zwarte-thee | De tags kloppen niet met het product. Tag "cafeïnevrij" verdwijnt. |
| Metaveld smaakprofiel (custom) | Pure spearmint, helder en koel verfrissend. | Krachtig, kruidig en aards, met een houtachtig aroma en een donkerrode kop. | Smaak volgens de productbeschrijving. |
| Metaveld ingrediënten (beschrijving) | Spearmint (kruizemunt, 100%). | Pu-erh zwarte thee (100%). | Gelijk aan de ingrediëntenregel in de productbeschrijving. |
| Metaveld ingrediënten (custom) | (ontbreekt) | Pu-erh zwarte thee (100%). | Andere producten hebben dit veld ook. |
| Metaveld cafeïnegehalte | Decaf | Normaal | Pu-erh komt van de theeplant en bevat cafeïne. Zelfde waarde als Twentse Land en Boswandeling. |

Niet voorgesteld, wel gezien: het zetadvies in de metavelden (95 °C, 5 tot 7 minuten) wijkt af van de productbeschrijving (100°C, 3 tot 5 minuten), en het product heeft geen afbeelding. Zie vragen onderaan.

# Deel 2. Wijzigingen in collecties

## 2a. Producten uit en in collecties verplaatsen

| Actie | Collectie | Product | Reden |
|---|---|---|---|
| Verwijderen | vruchtenthee | Boswandeling | Zwarte thee als basis. Staat al in zwarte-thee. |
| Verwijderen | rooibos | Sterrennacht | Bevat zwarte thee naast rooibos. Staat al in zwarte-thee. |
| Verwijderen | kruidenthee | Twentse Land | Zwarte thee als basis. |
| Verwijderen | kruidenthee | Gember Chai | Zwarte thee als basis. Staat al in zwarte-thee. |
| Verwijderen | kruidenthee | Elfjesthee | Groene thee als basis. Staat al in groene-thee. |
| Verwijderen | kruidenthee | Marocco Mint | Groene thee als basis. Staat al in groene-thee. |
| Verwijderen | kruidenthee | Pu-erh thee | Zwarte (nagefermenteerde) thee. |
| Toevoegen | zwarte-thee | Twentse Land | Stond in geen enkele theesoortcollectie. |
| Toevoegen | zwarte-thee | Pu-erh thee | Stond in geen enkele theesoortcollectie. |

Zeven producten uit drie collecties en twee toevoegingen: 9 collectiehandelingen, 7 producten, ruim onder de grens van 20 producten per batch.

## 2b. Paginatekst (descriptionHtml)

Alleen de zinnen die veranderen staan hieronder, de rest van de HTML blijft gelijk. De intro's ("Kruidenthee ... is volledig cafeïnevrij", "Vruchtenthee ... is volledig cafeïnevrij", "Rooibos bevat geen cafeïne") blijven staan, want ze beschrijven de productsoort en zijn na het verplaatsen weer waar voor alle producten op de pagina. Voorwaarde: de punten Lavendel en Herfstkruiden in deel 4.

| Nr. | Collectie | Huidige tekst | Voorgestelde tekst | Reden |
|---|---|---|---|---|
| T1 | kruidenthee | `Bekijk ook de rooibos en vruchtenthee collecties voor meer cafeïnevrije alternatieven.` | `Bekijk ook de rooibos en vruchtenthee collecties voor meer cafeïnevrije alternatieven. Een blend met zwarte of groene thee als basis, zoals Gember Chai of Marocco Mint, bevat wel cafeïne. Die vind je bij <a href="/collections/zwarte-thee">zwarte thee</a> en <a href="/collections/groene-thee">groene thee</a>.` | Wie Gember Chai of Marocco Mint zoekt op deze pagina, weet nu waar ze staan en waarom. Twee interne links naar de juiste collecties. |
| T2 | kruidenthee | Tante Rie verstuurt vanuit Borne, Twente, binnen 1 tot 2 werkdagen in huis. | Je bestelling wordt vanuit Borne verstuurd binnen 1 tot 2 werkdagen. | Levertijd volgens V64 ("verstuurd binnen 1 tot 2 werkdagen"). De oude zin noemt "in huis", dat is bezorging en niet verzending, en liep grammaticaal niet. |
| T3 | kruidenthee | 's Avonds een rustgevende Slaap Lekker of kalmerende Goede Nacht voor een goede nachtrust. | 's Avonds een rustgevende Slaap Lekker of kalmerende Mooie Dromen voor een goede nachtrust. | Extra, buiten V67: Goede Nacht is een concept en dus niet online te koop. Mooie Dromen is actief, cafeïnevrij en een avondthee. |
| R1 | rooibos | `Bekijk ook de kruidentheeën en vruchtenthee voor meer cafeïnevrije opties.` | `Bekijk ook de kruidentheeën en vruchtenthee voor meer cafeïnevrije opties. Rooibos gemengd met zwarte thee, zoals Sterrennacht, bevat wel cafeïne en staat bij <a href="/collections/zwarte-thee">zwarte thee</a>.` | Sterrennacht verdwijnt van deze pagina; deze zin vangt wie hem hier zoekt op. |
| V1 | vruchtenthee | `Van zomers friszure <strong>Wilde Kers</strong> en <strong>Fruitmand</strong> tot tropische <strong>Harverwarmer</strong> (appel, ananas, kaneel) en herfstachtige <strong>Herfstkruiden</strong>. En <strong>Geluksthee</strong> met hibiscus, framboos en papaya — een kopje vol kleur. Bekijk ook onze <a href="/collections/rooibos">rooibos</a> en <a href="/collections/kruidenthee">kruidentheeën</a> voor meer cafeïnevrije opties.` | `Van zomers friszure <strong>Wilde Kers</strong> en <strong>Fruitmand</strong> tot tropische <strong>Pina Colada</strong> (ananas en kokos) en winterse <strong>Wintersfeer</strong> (appel, sinaasappel en cassia). <strong>Geluksthee</strong> combineert hibiscus, framboos en papaya tot een kopje vol kleur. Bekijk ook onze <a href="/collections/rooibos">rooibos</a> en <a href="/collections/kruidenthee">kruidentheeën</a> voor meer cafeïnevrije opties. Een fruitige blend met zwarte thee als basis, zoals Boswandeling met aardbei, bevat wel cafeïne en staat bij <a href="/collections/zwarte-thee">zwarte thee</a>.` | Kern: de zin over Boswandeling, zelfde reden als T1 en R1. Extra, buiten V67: "Harverwarmer" bestaat niet als product en Herfstkruiden staat in kruidenthee, niet in deze collectie; beide vervangen door producten die hier echt staan (ingrediënten gecontroleerd). Het gedachtestreepje is eruit, zoals de stijlregels vragen. |
| V2 | vruchtenthee | `Gebruik water van <strong>95–100°C</strong> en laat de thee <strong>5 tot 8 minuten</strong> trekken. Vruchtenthee wordt niet bitter. Gebruik 1 theelepel per 250 ml. Geen suiker nodig — het fruit geeft van nature zoetheid.` | `Gebruik water van <strong>95 tot 100°C</strong> en laat de thee <strong>5 tot 8 minuten</strong> trekken. Vruchtenthee wordt niet bitter. Gebruik 1 theelepel per 250 ml. Geen suiker nodig, want het fruit geeft van nature zoetheid.` | Extra, buiten V67: gedachtestreepje weg en de bereiding gelijkgetrokken met de rooibos- en kruidenpagina ("95 tot 100"). Te laten vervallen als Mark alleen de cafeïnepunten wil. |

De tekst in de kolommen Huidig en Voorgesteld staat als code, inclusief de HTML-tags die in de collectietekst staan.

## 2c. Meta-descriptions: levertijd bijwerken (V64)

De drie collecties hebben sinds V66 een live description met "bezorgd in 2 tot 3 werkdagen". Dat is door V64 achterhaald. De teksten zijn verder gelijk gebleven. Het veld seo.description en het metaveld global.description_tag bevatten dezelfde tekst en blijven gelijk.

| Nr. | Collectie | Huidige tekst | Voorgestelde tekst | Tekens | Reden |
|---|---|---|---|---:|---|
| M1 | kruidenthee | Losse kruidenthee: pure kamille en gember, pepermunt of een blend voor de avond. Vers afgewogen in Borne, bezorgd in 2 tot 3 werkdagen. | Losse kruidenthee: pure kamille en gember, pepermunt of een blend voor de avond. Vers afgewogen in Borne, verstuurd binnen 1 tot 2 werkdagen. | 141 | V64 |
| M2 | rooibos | Losse rooibos uit Zuid-Afrika in meer dan 20 blends, van naturel tot Crème Brûlée. Vers afgewogen in Borne, bezorgd in 2 tot 3 werkdagen. | Losse rooibos uit Zuid-Afrika in meer dan 20 blends, van naturel tot Crème Brûlée. Vers afgewogen in Borne, verstuurd binnen 1 tot 2 werkdagen. | 143 | V64 |
| M3 | vruchtenthee | Losse vruchtenthee van Wilde Kers tot Pina Colada, ook lekker als ijsthee. Vers afgewogen in Borne, bezorgd in 2 tot 3 werkdagen. | Losse vruchtenthee van Wilde Kers tot Pina Colada, ook lekker als ijsthee. Vers afgewogen in Borne, verstuurd binnen 1 tot 2 werkdagen. | 135 | V64 |

Buiten de drie collecties van V67 hebben ook zwarte-thee en groene-thee dezelfde verouderde levertijd in de description. Optioneel in dezelfde batch:

| Nr. | Collectie | Huidige tekst | Voorgestelde tekst | Tekens |
|---|---|---|---|---:|
| M4 | zwarte-thee | Losse zwarte thee: Assam, Darjeeling, English Breakfast en Earl Grey, ruim 40 soorten. Vers afgewogen in Borne, bezorgd in 2 tot 3 werkdagen. | Losse zwarte thee: Assam, Darjeeling, English Breakfast en Earl Grey, ruim 40 soorten. Vers afgewogen in Borne, verstuurd binnen 1 tot 2 werkdagen. | 147 |
| M5 | groene-thee | Meer dan 30 soorten losse groene thee: Japanse Sencha, Chinese Jasmijn en Marocco Mint. Vers afgewogen in Borne, bezorgd in 2 tot 3 werkdagen. | Meer dan 30 soorten losse groene thee: Japanse Sencha, Chinese Jasmijn en Marocco Mint. Vers afgewogen in Borne, verstuurd binnen 1 tot 2 werkdagen. | 148 |

## 2d. Paginatitel (SEO-title) van vruchtenthee en kruidenthee

Volgens het voorstel van 23-10 (voorstel-metas-thee-blond-2026-10-23.md) is de live title van kruidenthee "Losse Kruidenthee Kopen | Cafeïnevrij | Tante Rie" en van vruchtenthee "Losse Vruchtenthee Kopen | Cafeïnevrij | Tante Rie". Shopify geeft voor beide een lege SEO-title terug, dus de bron zit in het thema en ik kan de huidige tekst hier niet bevestigen of aanpassen.

Voorstel: niet wijzigen. Na het verplaatsen van de zeven producten is "Cafeïnevrij" in beide titels weer juist, en het is een van de weinige onderscheidende klikredenen op deze pagina's (cafeïnevrije thee voor de avond, kinderen, zwangerschap). Voorwaarde is dat Lavendel (deel 4) bevestigd cafeïnevrij is. Als Mark zekerheid wil, of als de voorwaarde niet gehaald wordt, is dit de reserve zonder claim, die in het thema moet worden aangepast:

| Collectie | Reservetitel | Tekens |
|---|---|---|
| kruidenthee | Losse Kruidenthee Kopen \| Kamille, Munt en Meer \| Tante Rie | 59 |
| vruchtenthee | Losse Vruchtenthee Kopen \| Fruitig en IJsthee \| Tante Rie | 57 |

# Deel 3. Alt-teksten

## 3a. Sterrennacht (gevraagd)

Sterrennacht heeft één afbeelding (media-id 65100373524744, bestand sterrennacht.jpg).

| Huidige alt-tekst | Voorgestelde alt-tekst | Tekens | Reden |
|---|---|---|---|
| Sterrennacht losse kruidenthee van Tante Rie | Sterrennacht van Tante Rie: losse zwarte thee met rooibos, kaneel en dadel | 74 | De huidige tekst noemt het product kruidenthee, terwijl het zwarte thee met rooibos is. Dat is onjuist en past niet bij de zoekwoorden waarop de pagina moet scoren. De nieuwe tekst noemt soort en smaak uit de ingrediënten. Ik kon de afbeelding zelf niet bekijken; controleer of de foto het product of de verpakking toont, dan klopt "losse zwarte thee" ook visueel. |

## 3b. Dezelfde fout bij de andere producten uit deze lijst (extra, buiten V67)

De alt-teksten van vier andere producten noemen een zwarte of groene thee "losse kruidenthee". Gelijke oorzaak, gelijke oplossing. Alleen toe te passen als Mark dit wil meenemen.

| Product | Media-id | Huidige alt-tekst | Voorgestelde alt-tekst |
|---|---|---|---|
| Boswandeling | 62224038166792 | Boswandeling losse kruidenthee van Tante Rie | Boswandeling van Tante Rie: losse zwarte thee met aardbei |
| Boswandeling | 63917515112712 | Boswandeling losse kruidenthee in het zakje van Tante Rie | Boswandeling, losse zwarte thee met aardbei, in het zakje van Tante Rie |
| Gember Chai | 65131145822472 | Gember Chai losse kruidenthee van Tante Rie | Gember Chai van Tante Rie: losse zwarte thee met gember |
| Elfjesthee | 65045995356424 | Elfjesthee losse kruidenthee van Tante Rie | Elfjesthee van Tante Rie: losse groene thee met appel en amandel |
| Marocco Mint | 62224110027016 | Marocco Mint losse kruidenthee van Tante Rie | Marocco Mint van Tante Rie: losse groene thee met kruizemunt |
| Marocco Mint | 63917364871432 | Marocco Mint losse kruidenthee in het zakje van Tante Rie | Marocco Mint, losse groene thee met kruizemunt, in het zakje van Tante Rie |

Twentse Land heeft al een juiste alt-tekst ("losse zwarte thee"). Pu-erh thee heeft geen afbeelding.

# Deel 4. Andere producten in de drie collecties die cafeïne kunnen bevatten

Alle 64 producten in de drie collecties zijn nagelopen op ingrediënten, tags en het metaveld cafeïnegehalte. Naast de zeven hierboven zijn er geen producten met zwarte, groene of witte thee, maté of koffie in de ingrediëntenlijst. Wel zijn er vier producten met tegenstrijdige gegevens en twee met sporen. Voor niets hiervan stel ik een wijziging voor tot Mark de bron heeft bevestigd.

| Product | Collectie | Wat tegenstrijdig is | Wat ik vermoed | Voorstel |
|---|---|---|---|---|
| Festival | rooibos | Ingrediënten: Rooibos, mango, kardemom. Maar productbeschrijving, SEO-title, SEO-description en tag zeggen "zwarte thee", en het metaveld cafeïnegehalte staat op Normaal. | Onduidelijk. Als het een zwarte thee is, klopt de ingrediëntenlijst niet; als het rooibos is, kloppen beschrijving, SEO en tags niet. | Niet wijzigen. Mark controleert de verpakking in de winkel (vraag N1). |
| Sinaasappel Chai | rooibos | Ingrediënten en productbeschrijving: rooibos, "na het avondeten", cafeïnevrij. Maar SEO-title, SEO-description, alt-teksten en tag zeggen "zwarte chai", cafeïnegehalte Normaal. | Rooibos. Twee bronnen (ingrediënten en beschrijving) zeggen dat, en de beschrijving is recent herschreven. | Niet wijzigen. Na bevestiging door Mark SEO, tags, alt-teksten en cafeïnegehalte corrigeren (vraag N1). |
| Inspiratie | rooibos | Ingrediënten, beschrijving en SEO-description: rooibos, cafeïnevrij. Maar tags "groene-thee" en "cafeïnearm", en cafeïnegehalte Cafeïnearm. | Rooibos. | Niet wijzigen. Na bevestiging tags en cafeïnegehalte corrigeren (vraag N1). |
| Lavendel | kruidenthee | Lege productbeschrijving, geen ingrediënten, geen cafeïnegehalte. SEO-title, SEO-description en afbeelding zijn die van Mama & Baby Thee. | Een onafgemaakt of gedupliceerd product. De naam doet een kruidenthee vermoeden. | Niet wijzigen. Mark bevestigt wat dit product is (vraag N2). Zolang dat open staat is de claim "alle kruidentheeën zijn cafeïnevrij" niet gecontroleerd voor dit ene product. |
| Herfstkruiden | kruidenthee | Bevat cacaodoppen. | Cacaodoppen bevatten van nature sporen cacao-alkaloïden, waaronder een heel klein beetje cafeïne. In de winkel gebruikelijk als cafeïnevrij gepresenteerd. | Geen wijziging. Alleen genoemd voor volledigheid. |
| Romance | rooibos | Bevat cacaobonen. | Zelfde als hierboven, iets meer dan bij doppen. | Geen wijziging. Alleen genoemd voor volledigheid. |

Overig gezien, niet voorgesteld. Twentse Land heeft als SEO-title en -description "Milde Earl Grey met bergamot", terwijl de ingrediënten (peterselie, wortelvlokken) en de productbeschrijving een hartige streekmelange beschrijven. Sterrennacht noemt in het metaveld smaakprofiel kruidnagel, die niet in de ingrediënten staat. Alle drie de metavelden custom.seo_h1 (H1) hebben een gedachtestreepje: "Kruidenthee Kopen — Kamille, Munt & Meer", "Losse Rooibos Thee — Cafeïnevrij & Vol van Smaak" en "Vruchtenthee Kopen — Natuurlijke Vruchtenmengsels". Komt in een volgend voorstel.

# Deel 5. Volgorde van doorvoeren (na akkoord Kwaliteitsredacteur en Mark)

Totaal minder dan 20 producten, dus één batch. Eerst de backup uit marketing/onpage/backup-cafeine-thee-collecties-2026-10-23.json (is gemaakt).

1. Producten verplaatsen (deel 2a), controleren dat de aantallen kloppen met de aantallen hierboven.
2. Productgegevens Pu-erh thee (deel 1).
3. Alt-tekst Sterrennacht (3a), en 3b als Mark dat wil.
4. Paginateksten (2b) en meta-descriptions (2c).
5. Terugcontrole met dezelfde query: collectieleden, tekst en seo-velden. Daarna in changelog.md.

Effect meten na 4 tot 6 weken in Search Console per collectiepagina (vertoningen, klikken, positie). De aantallen zijn laag, dus de meting is vooral een controle dat er geen daling is. Bij de producten is het zinvoller om te kijken of Twentse Land, Gember Chai en Boswandeling meer vertoningen krijgen op "zwarte thee"-zoektermen.

# Deel 6. Stijltoets op de nieuwe klantteksten

Getoetst op de regels uit CLAUDE.md. Geen gedachtestreepjes, geen uitroeptekens, geen opsommingstekens in klantteksten en geen vulwoorden in T1, T2, T3, R1, V1, V2, M1 tot en met M5 en de alt-teksten. De zinnen zijn concreet (productnamen, grondstoffen, levertijd), de levertijd is letterlijk de afgesproken formulering uit V64, en er staat nergens een winkelbelofte ("ook in de winkel") of een verzendbelofte buiten V64. De gebruikte producten zijn actief en online. Tekenaantallen van de metas zijn nagerekend (135 tot 148, allemaal onder 155). Formele review volgt door de Kwaliteitsredacteur.

Eén aandachtspunt voor de review: in T1 en V1 noem ik Gember Chai, Marocco Mint en Boswandeling als voorbeeld in de collectietekst. Dat is bewust, omdat mensen die deze producten kennen ze daar zoeken, maar het kan ook korter ("een blend met zwarte of groene thee als basis").

# Vragen voor Mark (nog niet in vragen-voor-mark.md)

N1. Festival, Sinaasappel Chai en Inspiratie: is het rooibos of zwarte/groene thee? Een blik op de verpakking in de winkel is genoeg. Dit bepaalt of ze in de collectie rooibos blijven en welke gegevens (tags, SEO, alt-tekst, cafeïnegehalte) gecorrigeerd moeten worden. Prioriteit hoog, want een verkeerde cafeïneclaim is een klantprobleem. Hoort bij dit bestand.

N2. Lavendel: wat is dit product? De pagina is leeg en gebruikt de tekst en foto van Mama & Baby Thee. Is het een echt product (met ingrediënten en foto), dan graag de gegevens; is het een dubbel, dan kan het uit de kruidenthee-collectie. Prioriteit midden.

N3. Pu-erh thee: welk zetadvies geldt, 95 °C en 5 tot 7 minuten (metavelden) of 100°C en 3 tot 5 minuten (productbeschrijving)? En is er een foto beschikbaar? Prioriteit laag.

N4. Zwarte-thee en groene-thee: mag de levertijd in de description in dezelfde batch worden bijgewerkt (M4 en M5)? Prioriteit laag.

N5. De paginatitel van kruidenthee en vruchtenthee zit in het thema (Shopify geeft een lege SEO-title). Kan iemand met toegang tot ~/TanteRie-Theme-Editor de huidige titel bevestigen? Prioriteit laag, alleen nodig als de titel zonder "Cafeïnevrij" moet.
