# Concept Actie 6: Blond Amsterdam, antwoord bovenaan en interne links

Status: beoordeeld op 23-10, goedgekeurd met kleine aanpassingen, publicatie pas na de voorwaarde in marketing/review/review-blond-2026-10-23.md (de specificatietabel op de Blond-productpagina's zegt nog "Handwas aanbevolen").

Opgesteld door de content-redacteur op 22 oktober 2026 en op dezelfde dag definitief gemaakt na de antwoorden van Mark in marketing/vragen-voor-mark.md (V7, V8, V11, V36 en V41 ingevuld; V9 en V10 leeg, dus die zinnen vervallen). De klanttekst bevat geen MARK-markeringen meer en van elke zin is er één versie. Volgende stap: review door de Kwaliteitsredacteur. Er is niets gewijzigd in Shopify, het thema of op live pagina's, en er staat niets in changelog.md.

URL: https://tanterie.nl/pages/blond-amsterdam-servies (blijft de hoofdpagina voor de vaatwasser- en magnetronvragen, zoals het plan besluit)

## Bronnen

| Bron | Wat ik eruit gebruik |
|---|---|
| CLAUDE.md | 70/30-prioriteit, voorraadregel winkel, POS-only producten, stijlregels, werkwijze vragen aan Mark |
| marketing/plan-2026-10.md, actie 6 | Opdracht, nulmeting, succescriterium, termijn (concept 28-10, live uiterlijk 31-10, beoordeling 21-11) |
| marketing/vragen-voor-mark.md | Antwoorden van Mark, zie sectie 5 |
| marketing/technisch/inspectie-blond-zakelijk-2026-10-21.md | Technische status, verloop per dag, oorzaak val, oplossing in drie stappen |
| marketing/rapporten/onderzoek-zichtbaarheidsval-2026-09.md | Blond-deel: val op 24 september, gelijk met de spamupdate (24-09 tot 8-10), positie bleef 7 tot 9 |
| marketing/zoekwoorden/clusters-2026-10-21.md | Cluster Blond Amsterdam servies (90 dagen) |
| marketing/review/review-actie-4-en-5-2026-10-22.md en marketing/content/concept-theewinkel-borne-2026-10-22.md | Lijn houden: "kleurrijk", "de theewinkel in Borne", afhaalzin, voorraadregel, linkcontrole |
| data/gsc/2026-10-21-nulmeting-huidig-page.json, -huidig-querypage.json (28 dagen, 22-09 t/m 19-10), -pages-90d.json en -query-page-90d.json | Paginacijfers en zoekopdrachten |
| Live pagina's (WebFetch, 22 oktober) | /pages/blond-amsterdam-servies, /collections/blond, /pages/serviezen, /collections/servies, /pages/theewinkel-borne-twente, /collections/thee, /pages/theebereiding-faq en de Blond-productpagina's Liefste Juf, A Hug in a Mug, Teapot 1,5L Blah en Cozy Days Mug 0,35L Tea |

Beperking: geen shell in deze sessie, dus de Search Console-scripts heb ik niet opnieuw gedraaid en de Shopify-koppeling niet gebruikt. Alle cijfers komen uit de exports van 21 oktober (sc-domain:tanterie.nl). De ophaaltool geeft citaten van maximaal 125 tekens en vat soms samen; On-page moet voor de voor-en-navergelijking de huidige body uit Shopify kopiëren als backup. De skills draft-content en brand-voice zijn in deze omgeving niet als skill aangeroepen; ik heb de stijlregels uit CLAUDE.md en mijn rolbeschrijving toegepast.

## 1. Analyse van de huidige pagina

### Wat er nu staat

| Onderdeel | Huidig |
|---|---|
| Title | Blond Amsterdam servies \| Tante Rie (35 tekens, volgens de inspectie) |
| Meta description | Niet zichtbaar in de opgehaalde pagina; On-page haalt hem uit Shopify |
| H1 | Blond Amsterdam servies |
| H2's en H3's | Waarom dit servies zo fijn is; Een greep uit de collectie; Materiaal en afwerking (H3 Welke maten er zijn); Zo dek je er je tafel mee (H3 Mooi combineren met wat je al hebt); Onderhoud en vaatwasser (H3 Magnetron en oven); Een cadeau om te geven; daarna de vaste footerblokken |
| Antwoord op de vaatwasservraag | Pas in de zesde inhoudssectie, en inhoudelijk onjuist volgens Mark: "Hier moeten we eerlijk zijn: de vaatwasser wordt afgeraden." Magnetron: "In de magnetron kan het servies wel, maar het wordt snel warm." Oven: "Voor de oven is het niet geschikt." |
| Afhalen | Het woord afhalen komt niet voor. Wel staat er de vaste themaregel "Snelle verzending: 1-2 werkdagen!" en "Verzendkosten vanaf €4,50", terwijl Blond niet verstuurd wordt |
| Links in de inhoud | Zes productlinks (Liefste Juf, Graduated, Forever Young, Thank You, Cat Lover, Mug Hearts) en "Bekijk de volledige Blond Amsterdam collectie" naar /collections/blond. Geen link naar de theewinkelpagina of /pages/serviezen |
| Inkomende links | Alleen vanaf /collections/blond (ankertekst "inspiratie over het Blond Amsterdam servies"). Niet in het menu, de footer, /pages/serviezen, /collections/servies, de theewinkelpagina of de productpagina's |
| Afbeeldingen | Zes productfoto's met alt-tekst gelijk aan de productnaam ("Blond Amsterdam Mazagran Liefste Juf") |

### Feiten op de huidige pagina die niet kloppen

1. "Bij Tante Rie in Borne vind je veertig stuks uit de collectie: mokken, bekers, borden, kommen en theedoeken." De collectie toont 40 producten, maar daarin staan geen kommen en geen theedoeken (wel mokken, mazagran-bekers, drie borden, een theepot, een thermosfles en het Cozy Days-artikel "Light House Stepped Gable Cozy"). Theedoeken verkoopt Tante Rie niet. Bovendien staan vijf van de veertig op "Te bestellen", dus ze liggen niet allemaal in de winkel. Dat botst met de voorraadregel.
2. "Een aantal Mazagran-bekers kun je laten personaliseren." Er is geen personalisatie (Mark). Ook de live productpagina van Liefste Juf zegt "Ons atelier kan een persoonlijke tekst op het handvat zetten"; dat pakt On-page apart op.
3. De vaatwasserzin: Mark heeft bevestigd dat Blond in de vaatwasser kan (V7).
4. De verzendregel van het thema ("Snelle verzending: 1-2 werkdagen") staat op een pagina over een merk dat alleen af te halen is. Dat is een themablok en geen paginatekst. Mark heeft akkoord gegeven dat On-page en Technisch SEO een voorstel maken; hetzelfde geldt voor de productzin "Tante Rie verzendt niet. Je haalt alles op in de winkel.", die leest alsof Tante Rie ook geen thee verstuurt.
5. Op /pages/serviezen staat bij Blond "een uitgebreide collectie die altijd op voorraad is bij Tante Rie". Dat klopt niet (vijf stukken op bestelling) en mag eruit volgens Mark; dat gebeurt in actie 8.

### Vaatwasser: gidspagina en productpagina's

Volgens Mark kan Blond Amsterdam in de vaatwasser (V7). De productpagina's van Liefste Juf, A Hug in a Mug, Teapot 1,5L Blah en Cozy Days Mug 0,35L Tea zeggen nu nog "Handwas aanbevolen" en "Niet aanbevolen voor de vaatwasser". Volgens V36 en V41 krijgen ze "Geschikt voor de vaatwasser"; dat wordt apart doorgevoerd. Advies: de gidspagina pas live zetten als die correctie op de productpagina's ook live is, of tegelijk. Anders spreken de pagina's elkaar tegen.

De inspectie noemde als mogelijke oorzaak van de val dat het oude antwoord (vaatwasser afgeraden) niet aansloot op de vraag. Volgens zoekresultaten vermelden ook andere verkopers Blond Amsterdam-bekers als vaatwasserbestendig. Met het nieuwe antwoord sluit de pagina daarop aan. In de klanttekst verwijs ik niet naar andere verkopers.

### Search Console-cijfers

Nulmeting uit het plan, 28 dagen (22 september t/m 19 oktober 2026):

| URL | Vert. | Klikken | CTR | Pos. |
|---|---:|---:|---:|---:|
| /pages/blond-amsterdam-servies | 48 | 0 | 0 % | 7,5 |
| /collections/blond | 305 | 3 | 0,98 % | 9,0 |

90 dagen tot 21 oktober (inclusief de piek van 16 augustus tot 23 september):

| URL | Vert. | Klikken | CTR | Pos. |
|---|---:|---:|---:|---:|
| /pages/blond-amsterdam-servies | 1.142 | 3 | 0,26 % | 7,9 |
| /collections/blond | 852 | 9 | 1,06 % | 8,1 |
| /pages/serviezen | 1.384 | 26 | 1,88 % | 2,9 |
| /collections/servies | 70 | 0 | 0 % | 7,5 |

Zoekopdrachten op de gidspagina, 90 dagen (vrijwel allemaal uit de periode voor 24 september):

| Zoekopdracht | Vert. | Klikken | Pos. |
|---|---:|---:|---:|
| kan blond amsterdam in de vaatwasser | 85 | 0 | 8,3 |
| blond amsterdam servies | 53 | 0 | 8,9 |
| servies blond amsterdam | 53 | 0 | 9,7 |
| kan blond amsterdam servies in de vaatwasser | 49 | 0 | 8,6 |
| mag blond amsterdam servies in de vaatwasser | 43 | 0 | 8,7 |
| servies blond | 36 | 0 | 10,3 |
| kan blond amsterdam in de magnetron | 31 | 0 | 6,0 |
| blond amsterdam vaatwasser | 31 | 1 | 9,2 |
| mag blond amsterdam in de vaatwasser | 27 | 0 | 10,5 |
| kunnen blond amsterdam mokken in de vaatwasser | 17 | 0 | 7,9 |
| mag blond amsterdam in de magnetron | 13 | 0 | 9,5 |
| blond amsterdam tante | 11 | 0 | 3,7 |
| mag blond servies in de vaatwasser | 8 | 0 | 6,8 |
| blond amsterdam in vaatwasser | 6 | 0 | 9,8 |
| blonde servies | 4 | 0 | 7,0 |

Samen zijn de vaatwasser- en magnetronvragen op de pagina 310 vertoningen en 1 klik in 90 dagen, op positie 6 tot 10,5.

Zoekopdrachten op de gidspagina, laatste 28 dagen: kan blond amsterdam in de magnetron (4 vert., pos. 6,2), blond amsterdam servies (4, pos. 8,8), mag blond amsterdam in de vaatwasser (3, pos. 11), kan blond amsterdam in de vaatwasser (2, pos. 7,5), kan blond amsterdam servies in de vaatwasser (2, pos. 8,5). Vaatwasser en magnetron samen: 11 vertoningen in vier weken, dus ongeveer 3 per week. Het succescriterium van 5 per week ligt daar net boven.

Zoekopdrachten op /collections/blond, laatste 28 dagen: blond (8, pos. 9,4), etagere blond (3, pos. 45,7), blond amsterdam nouri (3, pos. 8,7), blond amsterdam mug (2), blonde amsterdam mug (2), blondelicious (2) en verder losse merk- en productcombinaties met 1 vertoning. Geen enkele vaatwasser- of magnetronvraag.

Duiding. De positie is niet het probleem: de pagina stond voor en na de val op 7 tot 9. Het zoekwoordenpakket is per 24 september grotendeels verdwenen, op de dag dat de spamupdate begon en na een testperiode van ruim vijf weken. Omdat de positie al rond 8 lag en er bijna geen klikken kwamen, is er bovendien een CTR-probleem: wie vraagt "kan het in de vaatwasser", ziet in de snippet nu "Blond Amsterdam servies | Tante Rie" en geen antwoord. Een title en meta die de vraag herhalen en een antwoord in de eerste zin moeten beide verbeteren. Herstel na de update kan het effect vertekenen; daarover meer bij de meting.

## 2. Kannibalisatie met /collections/blond

| Intentie | Voorbeelden | Doelpagina | Wat de andere pagina doet |
|---|---|---|---|
| Onderhoud en gebruik | kan blond amsterdam in de vaatwasser, mag blond amsterdam in de magnetron, blond amsterdam vaatwasser | /pages/blond-amsterdam-servies | Collectie noemt vaatwasser en magnetron niet in title, meta of H1, en linkt met een ankertekst over de vaatwasser naar de gidspagina |
| Kennismaken met het merk en het servies | blond amsterdam servies, servies blond amsterdam, servies blond | /pages/blond-amsterdam-servies (houdt 'servies' in title en H1) | Collectie houdt "Blond Amsterdam" als H1 en "kopen" in de title |
| Kopen, merk en producten | blond, blond amsterdam, blond amsterdam mug, productnamen, etagere blond | /collections/blond en de productpagina's | Gidspagina krijgt geen "kopen" in title of meta |
| Servies algemeen | servies, serviezen | /pages/serviezen | Beide Blond-pagina's linken ernaar |

Bewijs: volgens de inspectie stonden voor de val 295 van de 362 Blond-vertoningen op de gidspagina en 23 op de collectie; na de val 25 op de collectie. De collectie heeft niets overgenomen en krijgt ook nu geen vaatwasservraag. Er is dus geen kannibalisatie, en het voorstel houdt dat zo door de intenties in title en meta uit elkaar te houden. Wat ik bewust niet doe: geen FAQ over vaatwasser op de collectiepagina, en de collectie-title "Blond Amsterdam Kopen | Mokken & Woonaccessoires | Tante Rie" blijft zoals hij is.

## 3. Definitieve tekst

Hoofdzoekwoord: kan Blond Amsterdam in de vaatwasser. Tweede zoekwoord: Blond Amsterdam magnetron. Beide staan in de title, de eerste alinea en een tussenkop.

### Title

**Blond Amsterdam servies: vaatwasser en magnetron | Tante Rie**

60 tekens, opnieuw nageteld (grens 60). Gekozen door Mark (V11, advies volgen).

### Metabeschrijving

Kan Blond Amsterdam servies in de vaatwasser of magnetron? Het korte antwoord, onderhoudstips en hoe je het kleurrijke servies afhaalt in Borne.

144 tekens, opnieuw nageteld (grens 155).

### H1

Blond Amsterdam servies (ongewijzigd)

### Antwoordblok direct onder de H1 (nieuw, vóór de intro)

Kan Blond Amsterdam servies in de vaatwasser? Ja, de mokken, bekers en borden kunnen in de vaatwasser. Wil je dat de kleurrijke illustraties lang mooi blijven, kies dan een mild programma. De mokken en bekers kunnen ook in de magnetron, al worden ze snel heet, dus pak ze voorzichtig vast. De theepot en de thermosfles horen niet in de magnetron, en in de oven hoort geen enkel stuk. Blond Amsterdam versturen we niet: je bestelt online en haalt je bestelling af in onze [theewinkel in Borne](/pages/theewinkel-borne-twente), of je komt langs en neemt mee wat er op voorraad is.

### Intro (vervangt de zin met "veertig stuks")

Bij Tante Rie vind je een ruime keuze uit de collectie, van mokken en mazagran-bekers tot borden, een [theepot van 1,5 liter](/products/teapot-1-5l-blah) en een thermosfles. Wat op voorraad is, staat ook in onze winkel in Borne, en wat er niet ligt, kun je bestellen.

De overige zinnen van de huidige intro blijven staan: "Blond Amsterdam maakt servies waar je vrolijk van wordt.", "Het Nederlandse merk is te herkennen aan de illustraties, elk met een eigen tekst of tafereeltje." en "Geen servies dat netjes in de kast blijft staan, maar spullen die je elke dag pakt."

### H2: Blond Amsterdam in de vaatwasser, magnetron of oven

Deze sectie vervangt de huidige H2 "Onderhoud en vaatwasser" met de H3 "Magnetron en oven" en komt direct na de intro, vóór "Een greep uit de collectie".

**H3: Kan Blond Amsterdam in de vaatwasser?**

Ja, de mokken, bekers en borden van Blond Amsterdam kunnen in de vaatwasser. Het servies is van keramiek met opgedrukte illustraties. Met een mild programma blijft die print het langst mooi.

**H3: Kan Blond Amsterdam in de magnetron?**

Ja, alle mokken en bekers kunnen in de magnetron, bijvoorbeeld om een kop thee of melk op te warmen. Het keramiek wordt daarbij snel heet, dus pak je mok voorzichtig vast als hij eruit komt. De theepot en de thermosfles horen niet in de magnetron.

**H3: Kan Blond Amsterdam in de oven?**

Nee, het servies is niet geschikt voor de oven. Grote hitte en snelle wisselingen tussen warm en koud kunnen het keramiek laten barsten of de print beschadigen.

**H3: Kan ik Blond Amsterdam laten bezorgen?**

Nee, Blond Amsterdam versturen we niet. Je bestelt online en haalt je bestelling af in onze winkel aan de Bakkerssteeg 6 in Borne, open van dinsdag tot en met zaterdag van 10.00 tot 17.00 uur. Ligt je bestelling klaar, dan krijg je van ons bericht, telefonisch of per mail. Staat een stuk niet op voorraad, dan kun je het toch bestellen. De levertijd verschilt per merk, dus vraag ernaar in de winkel. Kom je liever eerst kijken, bel dan even naar 06 38 29 11 89 om te vragen of het stuk dat je zoekt in de winkel staat.

### Aanvulling aan het eind van "Zo dek je er je tafel mee"

Bij de theepot zoek je in onze winkel ook de thee uit: we hebben [losse thee](/collections/thee) in veel soorten, en wie wil weten hoe heet het water moet zijn en hoe lang een thee trekt, vindt dat bij [theebereiding](/pages/theebereiding-faq). Een overzicht van al ons servies, ook van Bunzlau Castle en Rice, staat op de pagina [serviezen](/pages/serviezen).

### Wat blijft en wat vervalt in de bestaande secties

Blijven inhoudelijk staan: "Waarom dit servies zo fijn is", "Een greep uit de collectie" (zes productlinks), "Materiaal en afwerking" met de maten, "Zo dek je er je tafel mee" en "Een cadeau om te geven". De zin "Kom gerust langs in de winkel in Borne om te kijken wat er is, of bekijk de volledige Blond Amsterdam collectie online." past bij de voorraadregel en blijft.

Vervallen: de hele huidige sectie "Onderhoud en vaatwasser" met "Magnetron en oven" (vervangen door de nieuwe H2), en in "Een cadeau om te geven" de zinnen "Een aantal Mazagran-bekers kun je laten personaliseren." en "Houd dan rekening met een iets langere levertijd." Die sectie eindigt dan op "Je zoekt gewoon de tekst die past bij degene die hem krijgt."

Aanpassing Kwaliteitsredacteur (23-10): in "Materiaal en afwerking" wordt "Alles is gemaakt van keramiek, met de illustraties opgedrukt." vervangen door "Het servies is gemaakt van keramiek, met de illustraties opgedrukt." In dezelfde sectie staat de thermosfles van 0,5 liter, en het materiaal daarvan is niet bevestigd. On-page controleert het materiaal op /products/eb-thermo-bottle-0-5l-hearts; is die ook van keramiek, dan mag de oude zin blijven.

Notitie voor On-page: de prijsrange in "Materiaal en afwerking" (9,99 tot 39,99 euro) klopt met de collectie van vandaag, maar moet mee veranderen als de prijzen veranderen. Overweeg hem te schrappen.

### Afbeeldingen en alt-teksten

| Foto | Alt-tekst |
|---|---|
| Mazagran Liefste Juf | Blond Amsterdam mazagran-beker Liefste Juf van 0,5 liter met kleurrijke illustraties |
| Mazagran Graduated 0,5l | Blond Amsterdam mazagran-beker voor geslaagden, 0,5 liter |
| Forever Young | Kleurrijke Blond Amsterdam beker met de tekst Forever Young |
| Thank You | Blond Amsterdam beker met de tekst Thank You als bedankcadeau |
| Mug Cat Lover | Blond Amsterdam mok Cat Lover voor kattenliefhebbers |
| Mug 0,35l Hearts | Blond Amsterdam mok Hearts van 0,35 liter |
| Foto van Mark: Blond in de winkel (nieuw, staat in assets/afbeeldingen/ zodra Mark hem aanlevert) | Kleurrijk Blond Amsterdam servies in de theewinkel van Tante Rie in Borne |

On-page controleert bij het plaatsen of elke alt-tekst past bij wat de foto echt toont. De winkelfoto komt bij het antwoordblok of bij de bezorgvraag, waar hij laat zien dat je het servies in Borne kunt bekijken.

## 4. Interne links

Linkcontrole op 22 oktober 2026 via WebFetch op de live site. Zonder shell heb ik geen letterlijke statuscode; WebFetch meldt een foutstatus (404, 429, 403) apart. Alle pagina's hieronder gaven geen foutstatus en toonden echte inhoud.

### Uitgaande links vanaf de gidspagina

| Ankertekst | Doel | Controle 22-10 |
|---|---|---|
| theewinkel in Borne | /pages/theewinkel-borne-twente | Laadt. Link naar de lokale doelpagina uit actie 5 |
| theepot van 1,5 liter | /products/teapot-1-5l-blah | Laadt, op voorraad, "Alleen afhalen, geen verzending" |
| losse thee | /collections/thee | Laadt, H1 "Losse Thee", 137 producten |
| theebereiding | /pages/theebereiding-faq | Laadt, H1 "Theebereiding", met watertemperatuur en trektijd per soort |
| serviezen | /pages/serviezen | Laadt, H1 "Serviezen", sectie Blond Amsterdam |
| Bekijk de volledige Blond Amsterdam collectie (bestaat al) | /collections/blond | Laadt, 40 producten, "Alleen afhalen in Borne" |
| Zes productlinks (bestaan al) | /products/mazagran-liefste-juf en vijf andere | Liefste Juf laadt, op voorraad; de andere vijf staan in de collectie, waarvan Graduated, Forever Young en Mug Hearts als "Te bestellen" |

De thermosfles wordt in de tekst genoemd maar niet gelinkt. Doorverwijzingen zie ik met deze methode niet; On-page kan dat bij de voor-en-navergelijking met een crawler nagaan.

### Inkomende links naar de gidspagina

Succescriterium: minstens 4 interne links. Nu is er 1.

| Vanaf | Voorstel | Controle bronpagina 22-10 | Hoort bij |
|---|---|---|---|
| /collections/blond | Bestaande link houden, maar hoger in de intro en met een ankertekst die de vraag noemt: "Benieuwd of Blond Amsterdam in de vaatwasser of magnetron kan? Dat lees je op onze pagina over [Blond Amsterdam servies](/pages/blond-amsterdam-servies)." Geen vaatwasser in title, meta of H1 van de collectie | Laadt; link bestaat nu met ankertekst "inspiratie over het Blond Amsterdam servies" | Actie 6, On-page |
| /pages/serviezen | In de sectie Blond Amsterdam: "Kleurrijk en vrolijk servies van het Nederlandse merk Blond Amsterdam, alleen af te halen in onze winkel in Borne. Lees ook of [Blond Amsterdam in de vaatwasser en magnetron kan](/pages/blond-amsterdam-servies), of bekijk de [collectie](/collections/blond)." Vervangt de zin met "altijd op voorraad" | Laadt; nu geen link naar de gidspagina, wel naar de collectie | Actie 8 |
| /collections/servies | Achter de intro "Van handgemaakt Pools aardewerk tot kleurrijke melamine: kies het servies dat bij jou past." de zin: "Lees ook over [onderhoud van Blond Amsterdam servies](/pages/blond-amsterdam-servies)." | Laadt, H1 "Servies met karakter"; bewust een verzamelpagina (Mark), On-page doet een aanbeveling voor de inhoud | Actie 6, On-page |
| Blond-productpagina's | Eén zin bij de onderhoudsspecificatie, die volgens V36 en V41 "Geschikt voor de vaatwasser" wordt: "Meer over [Blond Amsterdam in de vaatwasser en magnetron](/pages/blond-amsterdam-servies)." Het snelst via één themablok dat alleen bij Blond-producten verschijnt, in plaats van veertig beschrijvingen apart. Dat is een themawijziging via een kopie, met voor en na en akkoord van Mark | Liefste Juf, A Hug in a Mug, Teapot en Cozy Days laden; geen ervan linkt naar de gidspagina, wel naar de collectie | Actie 6, On-page en Technisch SEO |
| /pages/theewinkel-borne-twente | Link "Blond Amsterdam servies" staat al in het concept van actie 5 | Laadt; nu alleen menu- en merklinks naar de collectie | Actie 5 |

Daarmee komt de pagina op vijf bronnen van inkomende links. Komen actie 5 en 8 later live dan 31 oktober, dan haalt de pagina met de collectie Blond, de collectie servies en de productpagina's toch het minimum, mits het productblok er is. Komt het productblok er niet, dan zijn er op 31 oktober maar twee en moet de beoordeling op 21 november daar rekening mee houden.

Niet doen: geen menu-item naar de gidspagina. Het menu "Servies" wijst naar de collectie, en dat is voor de koopintentie de goede bestemming.

## 5. Besluiten van Mark (22 oktober 2026)

| Onderwerp | Besluit | Verwerkt als |
|---|---|---|
| Vaatwasser (V7) | Kan in de vaatwasser | Antwoordblok en H3: mokken, bekers en borden kunnen in de vaatwasser, met de tip voor een mild programma. Theepot en thermosfles worden bij de vaatwasser niet genoemd |
| Vaatwasser op productpagina's (V36, V41) | Productpagina's krijgen "Geschikt voor de vaatwasser" | Wordt apart doorgevoerd; advies om tegelijk met de gidspagina live te gaan |
| Magnetron (V8) | Alle mokken en bekers wel, theepot en thermosfles niet | Antwoordblok en H3 |
| Bericht bij afhalen | Telefonisch, of per mail | Bezorgvraag |
| Levertijd bij "Te bestellen" | Verschilt per merk | Geen termijn; "vraag er gerust naar in de winkel" |
| Kommen, ovenhandschoenen, schort (V9) | Niet beantwoord | Niet genoemd; ze staan ook niet online |
| Zin over koelkast en warmhoudplaat (V10) | Niet beantwoord | Vervallen |
| Theedoeken | Verkoopt Tante Rie niet | Uit de intro |
| Personalisatie en atelier | Er is geen atelier | Personalisatiezinnen vervallen; productpagina Liefste Juf apart via On-page |
| Title en meta (V11) | Advies volgen | Title A (60 tekens), meta A (144 tekens) |
| Verzendregel en productzin | Voorstel mag | On-page en Technisch SEO |
| /collections/servies | Bewust verzamelpagina | On-page doet een aanbeveling |
| "Altijd op voorraad" op /pages/serviezen | Mag eruit | Actie 8 |
| Foto | Er is een foto | Mark levert aan in assets/afbeeldingen/ |
| Blond Amsterdam | Kleurrijk | "kleurrijke illustraties", "kleurrijke servies" |

## 6. Meting na drie weken

Publicatie uiterlijk 31 oktober, beoordeling 21 november, zoals in het plan. Direct na publicatie vraagt Technisch SEO opnieuw indexering aan via URL-inspectie en legt de datum vast.

Wat we meten, uit Search Console (sc-domain:tanterie.nl), filter pagina is /pages/blond-amsterdam-servies:

1. Vertoningen per week voor zoekopdrachten met vaatwasser, magnetron of oven. Succes: samen minstens 5 per week in de weken na publicatie. Nulmeting: ongeveer 3 per week (11 in 28 dagen).
2. Positie en klikken op diezelfde zoekopdrachten. Geen vast doel in het plan, maar een klik bij positie 6 tot 9 laat zien of de nieuwe title en meta werken.
3. Aantal interne links naar de pagina, geteld met een crawl of handmatig op de vijf bronpagina's. Succes: minstens 4.
4. Ter controle: vertoningen en klikken op /collections/blond. Die mogen niet dalen; zakken ze en stijgt de gidspagina op dezelfde zoekopdrachten, dan is er alsnog kannibalisatie.

Voorbeeld voor de export (de Analist of Technisch SEO draait hem):

```bash
cd ~/.claude/skills/seo/scripts && export PYTHONWARNINGS=ignore
python3 gsc_query.py --days 28 --dimensions date,query,page --limit 1000 --json > "/Users/markvanwijk/Tante Rie SEO/data/gsc/2026-11-21-blond-date-query-page.json"
python3 gsc_inspect.py https://tanterie.nl/pages/blond-amsterdam-servies --json
```

Filteren op de pagina en op de woorden vaatwasser, magnetron en oven gebeurt daarna op de export.

Kanttekening bij de uitkomst. De spamupdate liep van 24 september tot 8 oktober. Komen de vragen terug, dan kan dat ook herstel na de update zijn en niet alleen het effect van de tekst. Vergelijk daarom met Muuss (/pages/muuss-van-joeff-de-wand-die-met-je-meebeweegt), die hetzelfde patroon had en niet wordt aangepast: herstelt die ook, dan is de update waarschijnlijk de grote factor. Haalt de pagina het criterium niet, dan stoppen we volgens het plan het werk eraan en noemen we dat in plan-2026-11.

## Volgende stap

De Kwaliteitsredacteur beoordeelt dit stuk. Daarna maakt On-page de voor-en-navergelijking met een backup van de huidige body, title en meta, en het voorstel voor de links op collectie, servies en productpagina's. De correctie "Geschikt voor de vaatwasser" op de productpagina's gaat bij voorkeur tegelijk live. Publicatie en de regel in changelog.md volgen pas na akkoord van Mark.

## Verwerkt

| Datum | Wat |
|---|---|
| 22-10 | Eerste concept met twee antwoordversies voor de vaatwasser en vragen aan Mark |
| 22-10, eerste antwoorden | Magnetron beperkt tot mokken en bekers (theepot en thermosfles niet); afhalen telefonisch of per mail, geen levertijd; theedoeken uit de intro; kommen, ovenhandschoenen en schort nagekeken (staan niet online, dus niet genoemd); personalisatie en atelier weg; alternatieve title gecorrigeerd van 52 naar 53 tekens |
| 22-10, V7 | Vaatwasser: één versie, "kan in de vaatwasser" met de tip voor een mild programma; versie 1 en 2 en meta B vervallen; analyse vermeldt dat de productpagina's nog "handwas aanbevolen" zeggen |
| 22-10, definitief | V8: magnetron geldt voor alle mokken en bekers ("Ja, alle mokken en bekers"), theepot en thermosfles niet. V11: title A en meta A vastgezet, opnieuw nageteld (60 en 144 tekens). V9 leeg: kommen, ovenhandschoenen en schort niet genoemd. V10 leeg: de zin over koelkast en warmhoudplaat is vervallen. V36 en V41: productpagina's krijgen "Geschikt voor de vaatwasser", de markering over theepot en thermosfles is weg en die twee worden bij de vaatwasser niet genoemd. Alt-teksten zonder afgeleide kenmerken (geen "roze" en "getekende katten"). Alle MARK-markeringen verwijderd; vragenlijst vervangen door de tabel met besluiten. Status: klaar voor review |
