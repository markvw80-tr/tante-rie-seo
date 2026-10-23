# Voorstel Bedrijfsprofiel (actie 3), 23 oktober 2026

Opgesteld door de Autoriteit- en lokale SEO-specialist voor Mark. Profiel: locations/6267696427702073490. Alles is alleen lezend opgehaald; er is niets gewijzigd, geplaatst of verstuurd. Ruwe antwoorden staan in data/gbp/2026-10-23-voorstel-lezen.json en data/gbp/2026-10-23-categorieen-kandidaten.json. De klantteksten gaan na jouw akkoord eerst langs de Kwaliteitsredacteur, daarna voert het team ze door (V27: Team).

## 1. Huidige stand van het profiel (gelezen op 23 oktober)

| Onderdeel | Nu |
|---|---|
| Hoofdcategorie | Theewinkel (gcid:tea_store) |
| Extra categorieën | Cadeauwinkel (gcid:gift_shop), Koffiewinkel (gcid:coffee_store) |
| Beschrijving | 133 tekens: "Ruim 130 soorten losse thee, servies van Bunzlau Castle en Blond Amsterdam, leuke cadeau artikelen, diverse bakmixen en koffiebonen" |
| Website-link | https://tanterie.nl/?utm_source=gbp&utm_medium=organic&utm_campaign=bedrijfsprofiel (de UTM-tag staat er dus inmiddels op) |
| Reguliere tijden | dinsdag tot en met zaterdag 10:00 tot 17:00 |
| Speciale tijden | 11 stuks: 8 verlopen (5 april tot 25 mei 2026) en 3 nieuwe sinds 22 oktober: gesloten 25 december, 26 december en 1 januari |
| Producten en diensten (serviceItems) | Leeg |
| Lokale berichten | Geen |
| Foto's | 16 stuks. 8 nieuwe winkelfoto's van 23 oktober (1 omslagfoto: de gevel; 7 binnenfoto's), 4 foto's uit 2019 en 3 uit mei 2025 |

## 2. Categorieën

Alle namen zijn gecontroleerd in de Google-categorielijst voor regio NL, taal nl (categories.list, 4.051 categorieën, opgeslagen in data/gbp/2026-10-21-profiel-categorieen-nl.json; de kandidaten zijn op 23 oktober opnieuw opgehaald met categories:batchGet). Er bestaat geen categorie Servieswinkel of Theeserviesje. Voor servies zijn Porseleinwinkel en Winkel in aardewerk de dichtstbijzijnde. Google heeft per categorie geen structurele diensten (serviceTypes is leeg bij alle kandidaten).

Onderbouwing: de zoektermen waarop het profiel werd getoond (augustus tot en met 19 oktober) zijn servies 209, bunzlau servies 150, serviesset 47, porselein servies 32, losse thee 39 en theepot 25. Servies wordt dus vaker gezocht dan thee, maar de winkel is een theewinkel (besluit Mark 22-10), en de hoofdcategorie telt het zwaarst. Daarom blijft Theewinkel de hoofdcategorie.

| Positie | Nu | Voorstel | Reden |
|---|---|---|---|
| Hoofd | Theewinkel | Theewinkel | Blijft; "de theewinkel in Borne" |
| Extra 1 | Cadeauwinkel | Cadeauwinkel | Blijft |
| Extra 2 | niet aanwezig | Porseleinwinkel (gcid:chinaware_store) | servies, serviesset, porselein servies |
| Extra 3 | niet aanwezig | Winkel in aardewerk (gcid:pottery_store) | Bunzlau Castle is aardewerk; sluit aan op "bunzlau servies" |
| Extra 4 | niet aanwezig | Kookwinkel (gcid:kitchen_supply_store) | keukenartikelen, bakmixen, melamine en Rice |
| Extra 5 | niet aanwezig | Woonwinkel (gcid:home_goods_store) | lifestyle, Blond Amsterdam, woonaccessoires |
| Extra 6 | Koffiewinkel | Koffiewinkel, vraag aan Mark | Koffiebonen staan in het assortiment; zie vraag 3 |

Wat ik bewust niet voorstel: Winkel voor bakkerijbenodigdheden (bakmixen zijn geen bakbenodigdheden, risico op een verkeerde match), Glaswerkwinkel (glazen zijn geen kernassortiment), Souvenirwinkel en Bubbeltheewinkel. Volgens de Google-richtlijnen zijn maximaal negen extra categorieën toegestaan; dat heb ik niet via de API getest. Meer categorieën is niet beter: Kookwinkel en Woonwinkel zijn de zwakste van de vijf en kunnen weg als je het profiel scherper wilt houden. Zet alles in een keer door, noteer de datum, en pas daarna in dezelfde maand niets meer aan de categorieën aan, want een wijziging kan de vertoningen tijdelijk laten schommelen.

## 3. Beschrijving

Besluiten van Mark verwerkt: "de theewinkel in Borne", ruiken en eventueel proeven, parkeren met parkeerschijf of in de gratis parkeergarage, rolstoeltoegankelijk, Blond en Bunzlau-aardewerk alleen afhalen, melamine en Rice wel verzenden. Geen jaartal, geen eigenaar. Openingstijden staan er bewust niet in: die staan al in het profiel en in de beschrijving moeten ze anders bij elke wijziging mee.

Nu (133 tekens): "Ruim 130 soorten losse thee, servies van Bunzlau Castle en Blond Amsterdam, leuke cadeau artikelen, diverse bakmixen en koffiebonen"

Voorstel (549 tekens, maximum 750):

Tante Rie is de theewinkel in Borne, aan de Bakkerssteeg 6. Aan de theewand vind je ruim 130 soorten losse thee, en je kunt de thee ruiken en eventueel proeven voordat je kiest. Daarnaast hebben we servies van Bunzlau Castle en Blond Amsterdam, melamine en servies van Rice, cadeaus, bakmixen en koffiebonen. Het aardewerk van Bunzlau Castle en het servies van Blond Amsterdam haal je af in de winkel, melamine en Rice sturen we ook op. Parkeren kan in de buurt met een parkeerschijf of in de gratis parkeergarage. De winkel is rolstoeltoegankelijk.

Controlepunten: "ruim 130 soorten" staat al in het profiel en de site (de collectie Losse Thee telt 138 producten in Shopify). "Melamine en Rice sturen we ook op" volgt uit V3, V43 en V46 (melamine en Rice-kommen zijn verzendbaar gemaakt). Bunzlau-textiel is sinds V59 en V62 ook verzendbaar; de zin noemt daarom alleen het aardewerk.

## 4. Producten of diensten in het profiel

Wat de API laat zien: serviceItems is leeg, en geen van de kandidaatcategorieën heeft vooraf gedefinieerde diensten. De Business Information API kent alleen diensten (vrije tekstitems of gestructureerde items), geen producten met foto, prijs en link. Productcategorieën in het profiel kunnen daarom alleen via de profielomgeving zelf. Ik raad af om winkelartikelen als "dienst" in serviceItems te zetten: de vermelding verschijnt dan op een plek die bedoeld is voor diensten en niet in het productenblok.

Wat het team kan doen, handmatig in het profiel (Bewerken, Producten): vier productcategorieën, elk met drie tot vijf producten die op voorraad liggen en zonder prijzen. Alle links zijn gecontroleerd en geven 200 terug.

| Categorie | Link |
|---|---|
| Losse thee | https://tanterie.nl/collections/thee |
| Bunzlau Castle (alleen afhalen) | https://tanterie.nl/collections/bunzlau |
| Blond Amsterdam (alleen afhalen) | https://tanterie.nl/pages/blond-amsterdam-servies |
| Servies | https://tanterie.nl/pages/serviezen (de collectie /collections/servies is bewust een verzamelpagina, V12) |

Voeg bij elke link de UTM toe: ?utm_source=gbp&utm_medium=organic&utm_campaign=producten. Voor Rice en melamine kan later een vijfde categorie komen als de winkel die op voorraad heeft. Kies producten die op voorraad zijn in Borne; de Shopify-voorraad heeft telfouten (negatieve aantallen bij enkele theeproducten), dus controleer in de winkel.

## 5. Berichten: eerste vier

Aanpak: een bericht per week, op dinsdag. Elk bericht is een Update (geen aanbieding, geen evenement), maximaal 1.500 tekens, zonder prijzen, acties of voorraadbeloften. Foto's staan al in het profiel; voor de berichten gebruik je dezelfde bestanden uit marketing/technisch/winkelfotos-shopify-2026-10-23.json (portret 1536 bij 2048; Google snijdt berichtfoto's bij, controleer in de voorvertoning dat de kern in beeld blijft). De berichtenfunctie: het veld canOperateLocalPost ontbreekt in de API-uitkomst (zie 7); controleer in het profiel of Update toevoegen beschikbaar is voordat je plant.

**Bericht 1, dinsdag 27 oktober, de theewand.** Foto: theewand-losse-thee.jpg. Knop: Meer informatie, https://tanterie.nl/pages/theewinkel-borne-twente?utm_source=gbp&utm_medium=organic&utm_campaign=bericht-theewand

Aan de theewand in onze winkel in Borne staan ruim 130 soorten losse thee. Je kunt de thee ruiken en eventueel proeven voordat je een keuze maakt. Dat helpt vooral bij thee die je nog niet kent, want de geur vertelt vaak al veel over wat je in je kopje krijgt. Weet je niet waar je moet beginnen, vertel dan wat je normaal drinkt en wat je minder lekker vindt, dan zoeken we samen een thee die bij je past. Je vindt ons aan de Bakkerssteeg 6 in Borne, van dinsdag tot en met zaterdag van 10.00 tot 17.00 uur. Parkeren kan in de buurt met een parkeerschijf of in de gratis parkeergarage.

**Bericht 2, dinsdag 3 november, Bunzlau Castle.** Foto: bunzlau-wand.jpg (alternatief: bunzlau-kast.jpg). Knop: Meer informatie, https://tanterie.nl/collections/bunzlau?utm_source=gbp&utm_medium=organic&utm_campaign=bericht-bunzlau

In onze winkel in Borne staat het aardewerk van Bunzlau Castle op een wand en in een kast, zodat je het kunt bekijken en vasthouden. Kleur en glazuur zie je pas goed als je een stuk zelf in je handen hebt. Het aardewerk van Bunzlau Castle versturen we niet. Je bestelt het online en haalt het af in de winkel, of je komt langs en neemt mee wat er op voorraad is. Zoek je een bepaald stuk, bel dan vooraf even naar 06 38 29 11 89, dan kijken we of het er ligt. We zijn open van dinsdag tot en met zaterdag van 10.00 tot 17.00 uur aan de Bakkerssteeg 6.

**Bericht 3, dinsdag 10 november, Blond Amsterdam en de vaatwasser.** Foto: blond-amsterdam-wand.jpg. Knop: Meer informatie, https://tanterie.nl/pages/blond-amsterdam-servies?utm_source=gbp&utm_medium=organic&utm_campaign=bericht-blond-amsterdam

Blond Amsterdam maakt mokken en bekers met kleurrijke illustraties, en in onze winkel in Borne zie je ze zoals ze echt zijn. Een praktische vraag bij dit servies is of het in de vaatwasser kan. Dat kan: de mokken, bekers en borden kunnen erin, het liefst op een mild programma zodat de print lang mooi blijft. Blond Amsterdam versturen we niet. Je bestelt online en haalt het af in de winkel, of je neemt mee wat er op voorraad is. Meer over het servies lees je op onze pagina over Blond Amsterdam.

**Bericht 4, dinsdag 17 november, feestdagen.** Foto: cadeautafel-winkel.jpg. Knop: Meer informatie, https://tanterie.nl/pages/theewinkel-borne-twente?utm_source=gbp&utm_medium=organic&utm_campaign=bericht-feestdagen

In de feestdagen is Tante Rie gesloten op Eerste en Tweede Kerstdag, 25 en 26 december, en op Nieuwjaarsdag, 1 januari. De gewone openingstijden zijn dinsdag tot en met zaterdag van 10.00 tot 17.00 uur. Zoek je een cadeau voor iemand die van thee houdt, kom dan langs in de winkel aan de Bakkerssteeg 6 in Borne, dan denken we graag met je mee.

Opmerkingen bij de berichten:

1. Bericht 4 noemt alleen de gesloten dagen. Antwoorden op V35 (koopavonden en extra openingen in december) ontbreken nog. Komen die er, dan pas ik dit bericht aan voordat het online gaat.
2. Voor bericht 4 is een latere datum ook verdedigbaar, bijvoorbeeld 1 december, zodat het dichter bij Kerst staat. Dan schuift het vijfde bericht een week op. Mijn voorstel is 17 november met een herhaling rond 15 december.
3. De gevelfoto (gevel-bakkerssteeg-6.jpg) is al de omslagfoto in het profiel en blijft daarom buiten de berichten.
4. De Blond-zin over de magnetron is bewust weggelaten, omdat de antwoorden op V8 elkaar in het Beantwoord-overzicht tegenspreken ("Nee" op alle stukken, daarna "Alle").

## 6. Reviewbeleid (kort)

1. Vraag aan klanten tijdens of na het gesprek aan de kassa, mondeling. Vraag niet alleen aan klanten die tevreden lijken: selectief vragen valt volgens de Google-richtlijnen onder het filteren van reviews.
2. Geef geen korting, cadeautje, actie of kans op een prijs in ruil voor een review, ook niet voor een bepaald aantal sterren.
3. Gebruik de reviewlink van het profiel: https://search.google.com/local/writereview?placeid=ChIJSV7D_q0PuEcRcNdTRtisMbw. Laat die zien als QR-code bij de kassa.
4. Houd het tempo laag en regelmatig, een of twee per week. Het profiel heeft 33 reviews, drie in 2026.
5. Laat medewerkers en familie geen review plaatsen.
6. Reageer binnen een week op elke nieuwe review, in een of twee zinnen met iets concreets uit de review. Bij drie sterren of lager: bedank, bied een gesprek aan, geef geen persoonlijke gegevens en verdedig je niet in het openbaar.
7. De 33 onbeantwoorde reviews wachten op jouw akkoord op de conceptantwoorden in brief-2026-10-21.md, paragraaf 3.7.

## 7. Hulp bij V26: is er rond 21 tot 24 september iets in het profiel veranderd?

Alleen gelezen via de API op 23 oktober.

**Wat de API laat zien**

| Controle | Uitkomst |
|---|---|
| getGoogleUpdated | Eén verschil met jouw versie: Google heeft coördinaten (52,3012814 en 6,756405) die jouw versie niet bevat. Dat is Google's eigen kaartpositie, geen voorgestelde wijziging aan naam, categorie, adres, tijden, telefoon of beschrijving. De website-link staat nu gelijk aan die van Google (op 21 oktober was dat nog het enige verschil) |
| hasPendingEdits | Niet meer aanwezig in het antwoord, dus onwaar; op 21 oktober stond het op waar door de website-link. Er wacht nu niets bij Google op verwerking |
| hasVoiceOfMerchant | Waar: je hebt zeggenschap over het profiel |
| canOperateLocalPost | Ontbreekt in het antwoord. De API laat onwaar weg, dus dit betekent waarschijnlijk onwaar. Ik weet niet zeker of dat betekent dat berichten niet mogelijk zijn, of dat het veld niet meer gevuld wordt; controleer in het profiel of Update toevoegen werkt |
| openInfo | OPEN, canReopen waar, openingsdatum 4 april 2014. Geen opschorting of sluiting te zien |
| Verificatiestatus | Niet op te halen: de My Business Verifications API staat uit in Cloud-project 28634605562 (403). hasVoiceOfMerchant waar wijst op een geverifieerd profiel, maar dat is een indirecte aanwijzing |
| Meldingen | Niet op te halen: de My Business Notifications API staat uit in hetzelfde project (403) |
| Beheerders | Drie: Nikkie (eigenaar, PRIMARY_OWNER), Anke Kamp (MANAGER) en Mark van Wijk (MANAGER). Dit is nieuw ten opzichte van de brief van 21 oktober |
| Foto's | Geen foto toegevoegd in september. De jongste oude foto's zijn van mei 2025; de acht nieuwe zijn van 23 oktober |
| Reviews | Geen review in september (volgens de inventaris van 21 oktober; de laatste voor 19 oktober was van 17 juni) |
| Berichten | Geen lokale berichten, nooit geplaatst |

**Wat de prestatiecijfers laten zien** (data/gbp/2026-08-01_2026-10-19-gbp-dagelijks.json): Zoeken mobiel zat in de weken ervoor rond de 30 tot 55 vertoningen per dag, met een uitschieter van 114 op 19 september. Op 21 september 48, 22 september 30, 23 september 18, 24 september 14, 26 september 6, en sindsdien 5 tot 8 per dag. De val begint dus op 22 en 23 september en is op 26 september voltooid. Maps mobiel liep niet mee terug; die bleef rond 5 tot 14.

**Wat de API niet kan tonen**

1. Geschiedenis van wijzigingen: geen datum van laatste bewerking, geen log wie wat wanneer wijzigde. getGoogleUpdated toont alleen de huidige stand.
2. Meldingen en e-mails van Google over het profiel, en de verificatiegeschiedenis, zolang de twee API's hierboven uit staan.
3. Of Google het profiel kort heeft opgeschort of beoordeeld, en of een andere beheerder iets heeft aangepast.
4. Wijzigingen die Google zelf heeft doorgevoerd en die daarna op jouw versie zijn overgenomen.

**Wat dit betekent voor je vraag over de mailbox**

Het team kan je mailbox niet doorzoeken vanuit deze rol en doet dat ook niet zonder jouw instructie in de chat; de keuze en de uitvoering liggen bij jou. Je kunt het zelf in een minuut doen. Zoek in je mail tussen 15 en 30 september op: "Google Bedrijfsprofiel", "Business Profile", "Tante Rie" en "business-profile-noreply@google.com". Let op de onderwerpen over bewerkingen, voorgestelde wijzigingen, verificatie of een melding over kwaliteit. Nikkie en Anke Kamp staan als beheerders in het profiel en ontvangen dezelfde mails; mogelijk is iets bij een van hen binnengekomen. Vraag hen of ze rond 21 tot 24 september iets in het profiel hebben aangepast. Twee API's aanzetten (Verifications en Notifications, via de links in de foutmelding in data/gbp/2026-10-23-voorstel-lezen.json) geeft de verificatiestatus en de meldinginstelling, maar niet de oude meldingen zelf.

Voorlopige conclusie: er is niets in het profiel te zien dat de val verklaart. Er staan geen openstaande Google-wijzigingen en geen opschorting. De mogelijkheid dat een van de drie beheerders iets heeft aangepast, of dat Google een melding stuurde, blijft open en alleen jullie mailboxen en de profielgeschiedenis in het scherm kunnen dat tonen.

## Samenvatting en vragen voor Mark

**Samenvatting.** Het profiel heeft nu Theewinkel als hoofdcategorie, Cadeauwinkel en Koffiewinkel als extra, een beschrijving van 133 tekens, 16 foto's en geen berichten. Voorgesteld wordt: vier extra categorieën erbij (Porseleinwinkel, Winkel in aardewerk, Kookwinkel, Woonwinkel), een nieuwe beschrijving van 549 tekens met jouw besluiten, vier handmatige productcategorieën, vier wekelijkse berichten vanaf 27 oktober en een reviewbeleid zonder beloning. De API kan categorieën en beschrijving wijzigen, maar geen producten en geen berichtenplanning met foto's in dit voorstel; het team plaatst die handmatig. Voor V26 is in het profiel niets gevonden dat de val van 22 en 23 september verklaart.

**Vragen (ja of nee)**

| Nr | Vraag | Antwoord |
|---|---|---|
| 1 | Akkoord met de categorieën: hoofd Theewinkel, extra Cadeauwinkel, Porseleinwinkel, Winkel in aardewerk, Kookwinkel en Woonwinkel? | |
| 2 | Akkoord met de nieuwe beschrijving van 549 tekens, zonder openingstijden? | |
| 3 | Moet Koffiewinkel blijven staan als extra categorie? Nee betekent dat hij vervalt | |
| 4 | Akkoord met de vier productcategorieën (Losse thee, Bunzlau Castle, Blond Amsterdam, Servies) die het team handmatig invult? | |
| 5 | Akkoord met de vier berichten op 27 oktober, 3, 10 en 17 november, met de genoemde foto's en knoppen? | |
| 6 | Mag bericht 4 (feestdagen) op 17 november, met herhaling rond 15 december? Nee betekent 1 december | |
| 7 | Akkoord met het reviewbeleid, inclusief een QR-code bij de kassa? | |
| 8 | Wil je Nikkie en Anke Kamp vragen of zij rond 21 tot 24 september iets in het profiel hebben gewijzigd? | |
| 9 | Wil je zelf je mailbox doorzoeken met de zoekwoorden uit paragraaf 7 en de uitkomst hier noteren? | |
| 10 | Mogen de Verifications API en de Notifications API in Cloud-project 28634605562 worden aangezet, zodat de verificatiestatus leesbaar wordt? | |
