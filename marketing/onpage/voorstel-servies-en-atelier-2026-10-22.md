# Voorstel /collections/servies en atelier-zinnen op Blond-producten (22 oktober 2026)

Opgesteld door On-page op 22 oktober 2026. Status: voorstel, wacht op de Kwaliteitsredacteur en Mark. Er is niets gewijzigd in Shopify, het thema of de live pagina's, en er is niets in changelog.md gezet. Shopify is alleen gelezen; het thema is alleen gelezen in ~/TanteRie-Theme-Editor.

Cijfers: Search Console, property sc-domain:tanterie.nl, 22 september tot en met 19 oktober 2026 (28 dagen), uit data/gsc/2026-10-21-nulmeting-huidig-page.json en 2026-10-21-nulmeting-huidig-querypage.json. URL-inspectie van /collections/servies via gsc_inspect (22 oktober 2026).

# Deel 1. /collections/servies

## Wat de pagina nu is

| Onderdeel | Bevinding |
|---|---|
| Collectie in Shopify | Collection 579349709064, handle servies, handmatige selectie zonder regels, 0 producten, lege beschrijving, gepubliceerd |
| Template | templates/collection.servies.json met de sectie tr-servies-hub: een H1 "Servies met karakter", een ondertitel en drie merkkaarten (Bunzlau Castle, Rice, Blond Amsterdam) |
| De "vier producten" | Dat zijn geen producten van deze collectie. Op de live pagina staan 1001 Nacht, 50 JAAR, Aardbeien en Aardbeien Cakemix in de footer-sectie met de zoekfunctie ("Zoekopdracht, Zoeken, Wissen, Producten"). Die footer staat op elke pagina. De collectie zelf toont dus geen producten, en de pagina is al een bewuste verzamelpagina. |
| Fout in de Blond-kaart | De kaart voor Blond Amsterdam heeft in het template geen collectie en geen URL. De live link is leeg (`href=""`), dus een klik doet niets. Bunzlau en Rice linken wel goed. |
| Indexatie | Geïndexeerd (Submitted and indexed), canonical klopt, laatst gecrawld 13 oktober. Gelinkt vanaf de homepage; Search Console noemt als verwijzers een blogpost en de privacypagina. |
| SEO-title huidig | Servies Kopen \| Bunzlau, Rice & Blond Amsterdam \| Tante Rie (59 tekens) |
| Metabeschrijving huidig | Mooi servies van Bunzlau Castle, Rice DK en Blond Amsterdam bij Tante Rie in Borne. Theepotten, mokken, borden en kommen. Online bestellen of afhalen in Twente. (160 tekens, 5 boven de grens van 155; "afhalen in Twente" is een vaste belofte, zie actie 10) |

## Cijfers (28 dagen)

| Pagina | Vertoningen | Klikken | CTR | Positie | Opmerking |
|---|---:|---:|---:|---:|---|
| /collections/servies | 11 | 0 | 0 | 6,0 | Eén zoekopdracht ("de prijs"), geen servieszoekterm |
| /pages/serviezen | 431 | 7 | 1,62 procent | 2,4 | Vrijwel alleen merk: "tante rie" 186 vertoningen, "tante rie borne" 135 vertoningen en 5 klikken. "tantes servies" 2 vertoningen. |
| /collections/bunzlau | 1.329 | 17 | 1,28 procent | 21,2 | 136 producten. "bunzlau" 87, "bunzlau castle" 74, "bunzlau servies" 38 vertoningen |
| /collections/blond | 305 | 3 | 0,98 procent | 9,0 | 40 producten |
| /collections/rice | 472 | 2 | 0,42 procent | 24,6 | 155 producten, ook lifestyle en geen servies |
| /pages/blond-amsterdam-servies | 48 | 0 | 0 | 7,5 | Vaatwasser- en magnetronvragen |

De algemene zoekterm "servies" (39 vertoningen, 2 klikken, positie 4,4) en "servies kopen" (6 vertoningen, 1 klik, positie 1,3) landen op de homepage http://www.tanterie.nl/, niet op de collectie of de hub. In het Bedrijfsprofiel staat "servies" 209 keer in de zoektermen (plan-2026-10.md). Het volume zit dus in de winkelvraag en bij de homepage, niet bij deze collectiepagina.

## Aanbeveling

Houd /collections/servies als merkenhub (geen productlijst) en voer vier kleine verbeteringen door. Maak er dus geen automatische verzamelcollectie van met al het servies, en voeg haar niet samen met /pages/serviezen.

Onderbouwing:

1. Een automatische collectie met al het online servies zou ongeveer 136 Bunzlau-producten, 40 Blond-producten en een deel van de 155 Rice-producten samenbrengen. Dat zijn ruim 200 producten in één lijst, zonder gemeenschappelijke tag of producttype dat ik heb kunnen controleren. De pagina zou voor dezelfde producten concurreren met de drie merkcollecties. Dat is het kannibalisatierisico dat we willen vermijden, en het verzwakt juist Bunzlau, de sterkste collectie (1.329 vertoningen, winkelzoektermen 201 in het profiel). Een brede collectie wint ook niet op "servies": de term gaat nu naar de homepage.
2. Samenvoegen met /pages/serviezen levert niets op. De collectiepagina heeft 11 vertoningen en 0 klikken, dus er is geen verkeer om te beschermen of te winnen. De hub-pagina heeft positie 2,4 als sitelink bij merkzoekopdrachten en haar inhoud moet volgens het plan (actie 8) blijven staan. Een redirect van de collectie naar de pagina haalt een geïndexeerde, gelinkte URL weg en laat de merkenkaarten verdwijnen die bezoekers snel naar de juiste collectie brengen.
3. De twee pagina's kunnen naast elkaar bestaan als ze een verschillende taak krijgen. /pages/serviezen is het informatieve en lokale overzicht (servies in de winkel in Borne, per merk een alinea). /collections/servies is de kooproute: een snelle keuze per merk, met zoekwoord "servies kopen" in de title. Het onderscheid is nu al deels zo, maar de Blond-kaart werkt niet en de meta noemt "afhalen in Twente" voor alles.
4. De kans op kannibalisatie is klein, omdat de collectie nu niet rankt. Ik meet het daarom na: als de collectie na 28 dagen ook op "tantes servies" en merkloze servieszoektermen verschijnt naast de hub, ga ik opnieuw kijken naar een van de twee als hoofdpagina.

### Voorgestelde wijzigingen

| Onderdeel | Huidig | Voorgesteld | Tekens | Reden |
|---|---|---|---|---|
| Blond-kaart (thema, template collection.servies.json) | Collectie leeg, URL leeg | Collectie blond, URL /collections/blond | n.v.t. | De kaart is nu een dode link. Bij 305 vertoningen op /collections/blond is dit de snelste winst. Het thema valt onder Technisch SEO. |
| SEO-title | Servies Kopen \| Bunzlau, Rice & Blond Amsterdam \| Tante Rie | Servies kopen \| Bunzlau, Blond Amsterdam en Rice \| Tante Rie | 60 (nu 59) | "Servies kopen" blijft voorop, de volgorde van de merken volgt de vraag (Bunzlau het meest, dan Blond, dan Rice) en het weglaten van "Rice DK" maakt de naam gelijk aan de collectie. |
| Metabeschrijving | Mooi servies van Bunzlau Castle, Rice DK en Blond Amsterdam bij Tante Rie in Borne. Theepotten, mokken, borden en kommen. Online bestellen of afhalen in Twente. | Servies per merk bij Tante Rie in Borne: handgemaakt Pools aardewerk van Bunzlau Castle, kleurrijke mokken van Blond Amsterdam en onbreekbaar Rice. | 147 (nu 160) | Past binnen 155 tekens, noemt per merk wat het onderscheidt en laat de vaste belofte "afhalen" weg tot actie 10 is besloten. Blond heet "kleurrijk" volgens het besluit van Mark. |
| Tekst onder de kaarten (nieuwe regel in de sectie, thema) | Geen tekst behalve de ondertitel | Bij Tante Rie, de theewinkel in Borne, kies je servies per merk. Bunzlau Castle is handgemaakt Pools aardewerk, Blond Amsterdam brengt kleurrijke mokken en borden met een tekst, en Rice is melamine dat bijna niet kapot gaat. Wil je eerst zien wat er in de winkel ligt, lees dan het overzicht van servies in de winkel in Borne. | 326 | Geeft Google tekst om de pagina te begrijpen en verbindt de twee pagina's met een duidelijke rolverdeling. "Servies in de winkel in Borne" is de ankertekst naar /pages/serviezen. |
| H1 | Servies met karakter | Geen wijziging | n.v.t. | Werkt, al staat het zoekwoord er niet in. De title draagt het zoekwoord. |

Opmerkingen voor de Kwaliteitsredacteur: de tekst onder de kaarten noemt geen voorraad, geen afhalen en geen openingsjaar. "Bijna niet kapot gaat" volgt de huidige merkregel van de pagina "Kleurrijke melamine, bijna onbreekbaar". Of Bunzlau en Blond alleen af te halen zijn, staat in het plan; ik heb dat bewust niet in de meta gezet.

### Beslissingen voor Mark (deel 1)

1. Akkoord met de aanbeveling (merkenhub houden, vier verbeteringen), of liever toch een automatische verzamelcollectie of een samenvoeging met /pages/serviezen.
2. Of de hub wordt opgenomen in de links van actie 8 zodat de ankertekst naar /pages/serviezen en terug klopt (de pagina-inhoud van actie 8 mag blijven staan).
3. Of de tekst onder de kaarten via het thema (Technisch SEO) mag worden toegevoegd. De collectie-beschrijving in Shopify wordt door dit template niet getoond; dus de tekst gaat in het template of in de sectie-instellingen.

# Deel 2. Atelier en personalisatie in productbeschrijvingen

## Wat is gezocht en gevonden

Mark zegt dat er geen atelier is en volgens zijn antwoord op vraag 5 van de Blond-review (concept-blond-2026-10-22.md) is er geen personalisatie. De productpagina's beloven dat wel. Ik heb in Shopify alle producten gezocht op "atelier", "personaliseren", "persoonlijke tekst" en "handvat", en de gevonden beschrijvingen volledig gelezen (descriptionHtml).

Uitkomst: 38 producten. 34 staan online (status actief, gepubliceerd in de webshop) en 4 zijn concept. Bij 34 producten staat het woord "atelier" in de tekst, bij 4 producten wordt personalisatie beloofd zonder dat woord (Matcha Princess, I Do, EB Cappuccino Mug 0,5L Hearts en Dier Mug Cat Lover). Er is geen invoerveld voor een tekst in het thema (geen blok product_custom_property in de templates), geen variant en geen meerprijs voor personalisatie. Een klant kan dus niets bestellen wat de tekst belooft. Dat bevestigt het besluit van Mark.

Niet meegenomen of niet gecontroleerd: de SEO-velden (title en meta) van deze producten, de productafbeeldingen met voorbeeldfoto's van een handschrift ("zie bijgaande foto"), de tags en de beschrijvingen van niet-Blond-producten die het woord niet bevatten. De pagina /pages/blond-amsterdam-servies bevat ook een personalisatiezin; die staat al in concept-blond-2026-10-22.md en hoort niet in deze lijst. Rice-producten E en J noemen "Schrijf een naam op tafel" en "Spel een naam op het aanrecht"; dat gaat over letterbekers en is geen belofte, dus geen wijziging.

## Voorstel

Standaardvoorstel (Optie A): de zinnen over personalisatie gaan eruit en er komt niets voor in de plaats. De rest van de tekst blijft staan, ook de vaatwasser- en materiaaltekst. Er is geen vervangende zin nodig, want de beschrijvingen eindigen daarna op een volledige zin.

Optie B (alleen als Mark bevestigt dat er toch een manier is om te personaliseren, met de voorwaarden): "atelier" vervangen door wat klopt, bijvoorbeeld "Personaliseren kan via Blond Amsterdam" met levertijd en prijs. Dat kan ik pas schrijven met de feiten van Mark; ik doe dat niet op aanname.

### Voor en na: Mazagran Liefste Juf (/products/mazagran-liefste-juf)

Voor:
> Heb jij gewoon de leukste en liefste juf van de wereld? Verras haar met deze nieuwe leuke kleurrijke Blond Amsterdam mazagran in XL formaat van 0,5l met vrolijke illustraties. Thanks for helping me grow! Heb jij geen juf maar een meester? Niet getreurd, ook daar hebben we een beker voor in ons assortiment. Ons atelier kan een persoonlijke tekst op het handvat zetten. Dit duurt iets langer, maar maakt de beker wel extra bijzonder natuurlijk. Personaliseren is handwerk, dus het handschrift kan afwijken van het voorbeeld.

Na:
> Heb jij gewoon de leukste en liefste juf van de wereld? Verras haar met deze nieuwe leuke kleurrijke Blond Amsterdam mazagran in XL formaat van 0,5l met vrolijke illustraties. Thanks for helping me grow! Heb jij geen juf maar een meester? Niet getreurd, ook daar hebben we een beker voor in ons assortiment.

Opmerking: "Thanks for helping me grow!" is de tekst op de beker en geen eigen tekst van Tante Rie; ik laat hem staan. De Kwaliteitsredacteur kan beslissen of het uitroepteken in een geciteerde beker-tekst mag.

### Patronen

| Patroon | Zinnen die eruit gaan (in de huidige tekst) |
|---|---|
| P1 | Ons atelier kan een persoonlijke tekst op het handvat zetten. Dit duurt iets langer [(7 werkdagen)], maar maakt de beker wel extra bijzonder natuurlijk. [Zie bijgaande foto voor voorbeeld.] [Personaliseren is handwerk, dus het handschrift kan afwijken van het voorbeeld.] De zinnen tussen rechte haken ontbreken bij sommige producten. |
| P2 | Je kunt deze [beker] ook laten personaliseren. Het Blond Amsterdam atelier personaliseert elk item met de hand, zodat je een uniek en persoonlijk cadeau hebt voor [...]. Houd er wel rekening mee dat het verzenden van gepersonaliseerde items iets langer kan duren, maar het resultaat is absoluut de moeite waard. |
| P3 | Laat dit product personaliseren met een naam of boodschap in ons atelier en maak er een echt persoonlijk cadeau van. Houd bij personalisatie rekening met een iets langere levertijd. (Per product net anders verwoord, zie kolom Opmerking.) |
| P4 | Eén tot drie losse zinnen over het atelier, de naam of het handschrift, zie kolom Opmerking |
| P5 | Personalisatie zonder het woord atelier, zie kolom Opmerking |
| D | Concept, zie kolom Opmerking |

### Alle 38 producten

| Nr | Product | Handle | Status | Patroon | Opmerking |
|---|---|---|---|---|---|
| 1 | Congratulations Party | `congratulations-party` | online | P1 | geen zin 'Zie bijgaande foto'; de zin 'Ontdek meer items en cadeaus uit van Blond Amsterdam.' blijft |
| 2 | Miss Creativity | `miss-creativity` | online | P1 |  |
| 3 | Best Friend | `best-friend` | online | P1 | dubbele spatie voor de zin gaat mee weg |
| 4 | Forever Young | `forever-young` | online | P1 | alleen de eerste twee zinnen komen voor; 'De XL beker (Mazagranvorm) hoort bij de collectie Specials...' blijft |
| 5 | Fashion Girl | `fashion-girl` | online | P1 | '(7 werkdagen)' staat in de zin |
| 6 | Mazagran Liefste Juf | `mazagran-liefste-juf` | online | P1 | zin 'Heb jij geen juf maar een meester? ...' blijft; geen zin 'Zie bijgaande foto'. Dit is de pagina uit de opdracht van Mark |
| 7 | Mazagran A Hug in a Mug | `mazagran-a-hug-in-a-mug` | online | P1 | de tekst staat in een p-tag; de p-tag blijft, de laatste vier zinnen gaan eruit |
| 8 | Mazagran Sister | `mazagran-sister` | online | P1 | '(7 werkdagen)'; de slotzinnen over de collectie Specials blijven |
| 9 | Mama | `mama` | online | P1 |  |
| 10 | Kitchen Queen | `kitchen-queen` | online | P1 | '(7 werkdagen)' |
| 11 | Meester | `meester` | online | P1 | de slotzin 'Ontdek meer items van Blond Amsterdam.' blijft |
| 12 | The Man | `the-man` | online | P1 | slotzinnen over de collectie Specials blijven |
| 13 | 50 Jaar | `50-jaar` | online | P1 |  |
| 14 | Groom | `groom` | online | P1 | '(7 werkdagen)' |
| 15 | Miss Brains | `miss-brains` | online | P1 | slotzinnen over de collectie Specials blijven |
| 16 | Love to Travel | `love-to-travel` | online | P2 | De slotzin 'Ontdek meer inspirerende items ...' blijft |
| 17 | Mazagran Graduated 0,5L | `mazagran-graduated-0-5l` | online | P2 | In plaats van 'ook laten personaliseren' staat hier 'Geslaagd Beker' |
| 18 | Teapot 1,5L Blah | `teapot-1-5l-blah` | online | P2 | Het gaat om een theepot, geen beker |
| 19 | Thank You | `thank-you` | online | P2 |  |
| 20 | Papa | `papa` | online | P2 |  |
| 21 | Game On | `game-on` | online | P3 | De zin eindigt zonder punt ('...als je dat doet'); 'Ontdek meer items van Blond Amsterdam.' blijft |
| 22 | Cup of Sunshine | `cup-of-sunshine` | online | P3 | Daarna volgen de wasadviezen, die blijven |
| 23 | ED Bord 18 cm Tompouce | `ed-bord-18-cm-tompouce` | online | P3 | Het is een bord; de zin 'Zo stel je eenvoudig een kleurrijke en persoonlijke tafel samen.' blijft, want die gaat over de tafel |
| 24 | Dad | `dad-1` | online | P3 | Ook de zin 'De tekst komt op het oor van de beker.' gaat eruit |
| 25 | Mazagran Orange 0,5L | `mazagran-orange-0-5l` | online | P3 | De zin ervoor ('En ja, deze beker is niet alleen leuk voor jezelf, maar ook perfect als cadeau ...') blijft; 'Ontdek meer items van Blond Amsterdam.' blijft |
| 26 | Cozy Days Mug 0,35L Tea | `cozy-days-mug-0-35l-tea` | online | P4 | Alleen de zin 'Personaliseer hem in ons atelier.' gaat eruit |
| 27 | EB Pink Mug 0,35L Hearts | `eb-pink-mug-0-35l-hearts` | online | P4 | Twee zinnen: 'Je kunt de beker laten personaliseren in ons atelier met een naam of korte tekst.' en 'Perfect om cadeau te doen of om jouw eigen blond momentje nét even persoonlijker te maken.' |
| 28 | Opa | `opa` | online | P4 | Twee zinnen: 'In ons atelier kun je de beker laten personaliseren met een tekst op het handvat.' en 'Personaliseren is handwerk en duurt daardoor iets langer, maar maakt de beker wel extra bijzonder.' De beschrijving eindigt dan op de zin over de mazagran |
| 29 | Hart voor de Zorg | `hart-voor-de-zorg` | online | P4 | Twee zinnen: 'Je kan de XL beker persoonlijker maken door er een naam op te laten schrijven door ons atelier (de tekst wordt op het handvat geschreven).' en 'Personaliseren is handwerk, hierdoor kan het handschrift afwijken van het voorbeeld.' De zin over de inhoudsmaat blijft |
| 30 | Mazagran Cheers to 18 Years | `mazagran-cheers-to-18-years` | online | P4 | Drie zinnen: 'Je kan een naam of persoonlijke tekst door ons atelier op de beker laten zetten.', 'De tekst wordt op het handvat gezet, zie ook bijgaand voorbeeld.' en 'Personaliseren is handwerk, hierdoor kan het handschrift afwijken van het voorbeeld.' |
| 31 | Matcha Princess | `matcha-princess` | online | P5 | Geen woord 'atelier', wel personalisatie: 'Extra leuk: deze mazagran is te personaliseren met een naam of korte boodschap.', 'Zo maak je er een uniek en persoonlijk cadeau van voor een matcha-lover, vriendin of jezelf.' en 'Houd bij personalisatie rekening met een iets langere levertijd.' |
| 32 | I Do | `i-do` | online | P5 | Geen woord 'atelier': 'Extra bijzonder: deze mazagran is te personaliseren met een naam of korte boodschap.', 'Zo maak je er een uniek en persoonlijk huwelijkscadeau van dat nog lang gebruikt én gekoesterd wordt.' en 'Houd bij personalisatie rekening met een iets langere levertijd.' Het cadeau-argument staat al eerder in de tekst |
| 33 | EB Cappuccino Mug 0,5L Hearts | `eb-cappuccino-mug-0-5l-hearts` | online | P5 | Geen woord 'atelier': 'Indien je kiest voor personaliseren, dan wordt de tekst midden op het handvat geschreven, zie ook bijgaande foto.' en 'Personaliseren is handwerk, hierdoor kan het handschrift afwijken van het voorbeeld.' Dit is ook de laatste zin van de tekst |
| 34 | Dier Mug Cat Lover | `dier-mug-cat-lover` | online | P5 | Geen woord 'atelier': 'Maak de beker persoonlijk door er een eigen tekst op te laten zetten.', 'Indien je kiest voor personaliseren, dan wordt de tekst op het handvat gezet.' en 'De tekst wordt er met de hand opgeschreven, hierdoor kan het afwijken van het voorbeeld.' Dit is bijna de hele tekst na de eerste twee zinnen |
| 35 | Fit Girl | `fit-girl` | concept | D | Concept. De twee zinnen over personaliseren in ons atelier en over het handschrift gaan eruit |
| 36 | EB Pink Mini Mug 0,2L Hearts | `eb-pink-mini-mug-0-2l-hearts` | concept | D | Concept. De zin 'In ons atelier kun je de mok laten personaliseren met een naam, datum of eigen tekst.' gaat eruit |
| 37 | Happy Mug Rollerskate 0,35L | `happy-mug-rollerskate-0-35l` | concept | D | Concept. De zin 'Ook deze beker kun je in ons atelier laten personaliseren met een tekst op het handvat.' gaat eruit |
| 38 | Blond Hug Mug Tea | `blond-hug-mug-tea` | concept | D | Concept. De zin 'In ons atelier kun je de beker laten personaliseren met een naam of tekst op het handvat.' gaat eruit |

De nieuwe tekst per product is steeds de huidige beschrijving zonder de genoemde zinnen. Waar de tekst in een p-tag staat (Mazagran A Hug in a Mug), blijft de tag staan. De voorbeeldfoto's van een handgeschreven tekst op het handvat (zie bijgaande foto) horen bij dezelfde belofte; Mark moet beslissen of die afbeeldingen uit de productgalerij gaan.

### Beslissingen voor Mark (deel 2)

1. Bevestigen dat Optie A geldt voor alle 38 producten (geen personalisatie, geen atelier), ook bij de formuleringen "Het Blond Amsterdam atelier personaliseert elk item met de hand". Als Blond Amsterdam zelf wel personaliseert op bestelling bij Tante Rie, is dat een andere zaak (Optie B) en heb ik de voorwaarden nodig.
2. Of de concepten (4 producten) nu al worden aangepast, zodat de zin niet meekomt als ze online gaan.
3. Of de voorbeeldfoto's met een handgeschreven tekst uit de productgalerijen worden gehaald.
4. Of de wijziging in dezelfde batch gaat als de Blond-teksten uit actie 6. Per batch maximaal 20 producten: bij 34 online producten zijn dat twee batches, met een backup van de oude beschrijvingen voorafgaand aan elke batch in marketing/onpage/.

## Wat nog goedgekeurd moet worden

De Kwaliteitsredacteur beoordeelt de voorgestelde teksten in deel 1 (title, meta, tekst onder de kaarten) en de uitspraken over herkomst en voorraad. Mark beslist over de beslispunten hierboven. Pas daarna voert On-page de wijziging door, met eerst een backup van de oude waarden en daarna een regel in marketing/changelog.md. Meting van /collections/servies: 28 dagen na publicatie, vergelijking met de nulmeting hierboven (11 vertoningen, 0 klikken, positie 6,0) en naast /pages/serviezen.
