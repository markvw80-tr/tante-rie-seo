# Voorstel thema /collections/bunzlau: intro zichtbaar, ondertitel, vaste teksten (V105)

Opgesteld door Technisch SEO op 24 oktober 2026. Status: alleen voorstel. Er is niets gewijzigd in Shopify, het live thema of changelog.md, en er is nog geen themakopie gemaakt. Mark gaf op 24-10 akkoord op V105 voor het maken van dit voorstel; publicatie wacht op een tweede akkoord op de voor-en-nawaarden hieronder.

Diff: marketing/technisch/voorstel-bunzlau-thema-2026-10-24.diff (één bestand: sections/tr-collection-bunzlau.liquid, 97 regels diff, pad t.o.v. de themawortel, toe te passen met `patch -p1`).

## Bronnen en controle

| Bron | Gebruik |
|---|---|
| Live thema 203153015048 (MAIN, "Agent-ready koppen 2026-10-09"), sections/tr-collection-bunzlau.liquid, alleen gelezen via de Shopify-koppeling op 24-10 | Basis van het voorstel. 664 regels, 45.180 bytes |
| scripts/archief-themas/winkelfotos-backup-2026-10-23-live-203153015048/sections/tr-collection-bunzlau.liquid (652 regels) plus marketing/technisch/voorstel-winkelfotos-2026-10-23.diff | Controle: backup plus die diff geeft byte voor byte (45.180) het live bestand. De regelnummers hieronder zijn die van het live bestand; ze liggen 12 hoger dan in de backup en in het concept van de Content-redacteur (die 161 tot 169 en 514 tot 527 noemt) |
| Collectie Bunzlau via de Shopify-koppeling (alleen lezen) | Huidige beschrijving, seo-title en meta, 136 producten, productsoorten |
| Verzendprofielen en locatie via de Shopify-koppeling (alleen lezen) | Uitleg over de knoppen (punt 3d) |
| marketing/content/concept-bunzlau-2026-10-29.md, marketing/onpage/voorstel-bunzlau-title-links-2026-10-29.md, changelog.md (22 en 23 oktober), plan-2026-11-vroege-start.md onderdeel 1 | Nieuwe teksten, volgorde, afhaalregels |

Geverifieerd met `patch --dry-run`: de diff past schoon op het live bestand. De Liquid is nog niet gerenderd; dat gebeurt pas in de themakopie (zie "Uitvoering").

## Punt 1. Eerste alinea van de collectiebeschrijving zichtbaar

**Oorzaak.** Regels 161 tot 169 splitsen de beschrijving in `_desc_first` (eerste `<p>`) en `_desc_rest` (de rest). Alleen `_desc_rest` wordt getoond (regel 520, in het SEO-blok onder de pagina). `_desc_first` wordt nergens uitgevoerd, hoewel het commentaar op regel 161 zegt "eerste alinea in header". Daardoor is de eerste alinea van de beschrijving voor bezoekers en voor Google (zichtbare tekst) onzichtbaar. De huidige eerste alinea in Shopify is "Bij Tante Rie in Borne vind je een uitgebreid assortiment Bunzlau Castle aardewerk: theepotten, mokken, bekers, schalen, soepkommen en dinerborden. Elk keramisch stuk wordt met de hand gegoten en afgewerkt in het Poolse Bolesławiec, ..." Dat is dus de alinea die zichtbaar wordt als het thema live gaat voordat On-page de tekst vervangt (zie volgorde onder "Uitvoering").

**Minimale wijziging.** `_desc_first` wordt in de hero uitgevoerd, direct onder de ondertitel. Er is niets aan de splitsing veranderd, dus `_desc_rest` bevat nooit de eerste alinea en er ontstaat geen dubbele tekst. Het is zes regels: vier regels CSS (witte tekst, onderstreepte links, geen eigen marge, ruimte onder de ondertitel) en een `if`-blok van drie regels in de hero. Zonder beschrijving of zonder eerste alinea verschijnt er niets.

| | Voor | Na |
|---|---|---|
| Regels 28 en 29 (CSS) | alleen `.trbz-hero-sub` | plus `.trbz-hero-intro` (4 regels, na regel 29) |
| Regels 195 tot 204 (hero) | h1, ondertitel, teller | h1, ondertitel, **intro (`{{ _desc_first }}` in `div.trbz-hero-intro`)**, teller |

**Wat dit betekent voor de tekst van de Content-redacteur.** Alinea 1 van de nieuwe intro ("Bunzlau Castle is aardewerk dat in Polen met de hand wordt beschilderd ... neem gerust een kopje of schoteltje mee", 3 zinnen, met link naar /pages/theewinkel-borne-twente) komt in de hero, boven de producten. Alinea 2 (afhalen, melamine, bestelverzoek, feestdagen en gesloten dagen) komt met de H2 Pools aardewerk en de FAQ in het tekstblok onder de pagina. Dat werkt als de body in Shopify begint met alinea 1 als eigen `<p>` en alinea 2 als tweede `<p>`, zoals in het concept. Afhalen staat boven de producten al drie keer (ondertitel, balk bovenaan, linker infoblok), dus de afhaalregel is zichtbaar zonder dat alinea 2 omhoog hoeft. Alternatief (niet voorgesteld): twee alinea's in de hero; dat duwt de producten op mobiel ver naar beneden.

## Punt 2. Hero-ondertitel

De ondertitel komt uit regel 199 (standaardtekst) omdat de themainstelling `subtitle` in templates/collection.bunzlau.json leeg is. Wijziging dus in de code, niet in de template-JSON (die wordt door de themabewerker overschreven).

| | Tekst | Regel |
|---|---|---|
| Voor | Handgeschilderd in Polen, te bestellen bij Tante Rie in Borne | 201 |
| Na | Handgeschilderd in Polen, af te halen bij Tante Rie in Borne. Het melamine versturen we wel. | 201 |

Reden: het aardewerk wordt niet verstuurd (afhaalregels 22-10, V18), het melamine wel (V3, V43). De formulering volgt de tekst op de productpagina's ("Dit product versturen we niet") en het concept ("het melamine sturen we wel op"). Geen voorraadbelofte, geen uitroepteken, geen em-dash. De vormgeving van "Borne" (vet en schuin) blijft.

Twee kleine aanvullingen in dezelfde lijn, omdat de collectie ook melamine en Rice toont (op 24-10 zijn 4 van de eerste 50 producten melamine of bewaarblik-melamine en 2 Rice):

| Regel | Voor | Na |
|---|---|---|
| 220 (balk onder de hero) | Alleen afhalen in Borne | Aardewerk alleen afhalen in Borne |
| 458 (kop infoblok) | Alleen afhalen in de winkel | Aardewerk afhalen in de winkel |

Zonder deze twee zou de pagina bovenaan "alleen afhalen" zeggen en in de ondertitel en intro dat melamine wel wordt verstuurd. Laat Mark ze liever weg, dan blijft het voorstel bij de ondertitel en verandert de rest niet.

## Punt 3. Vaste teksten die de regels raken

Wat de Content-redacteur noemt, heb ik in het live bestand teruggevonden en uitgebreid met de zelfde fouten op andere plekken.

### 3a. SEO-blok onder de producten (regels 521 tot 534): helemaal weg

Het blok staat direct onder `_desc_rest` en bevat vijf onderdelen. De nieuwe body (intro-alinea 2, H2 Pools aardewerk, FAQ) dekt de inhoud.

| Onderdeel (regel) | Probleem | Waar de inhoud nu staat |
|---|---|---|
| H2 "Bunzlau Castle kopen in Twente" (521 tot 522): "officieel reseller", "stukken die er niet staan, bestellen we voor je", "levertijd hangt af van de collectiecyclus" | "Officieel reseller" heeft geen bron in de repository; de levertijd is onbekend (concept: geen termijn beloven) | FAQ "Waar kan ik Bunzlau Castle kopen?" en "Welke winkel in Nederland ..." |
| H3 "Welke decors zijn er op voorraad?" (524 tot 525): lijst van 19 decors "op voorraad" plus "De volledige collectie is op bestelling verkrijgbaar" | Voorraadbelofte, in strijd met CLAUDE.md; de lijst veroudert met elke voorraadwijziging en is dus fout zodra een decor uitverkocht is | Intro-alinea 2: "zoek je een decor dat niet in de winkel staat, dan kunnen we het voor je bestellen" (goedgekeurd winkelfeit uit de theewinkelpagina). De decornamen zelf zijn ook te vinden via het filter en de productkaarten |
| H3 "Gebruik en onderhoud" (527 tot 528): "ovenbestendig tot 220°C", "tientallen jaren" | 220°C en "tientallen jaren" hebben geen bron; Mark bevestigde (V98) alleen vaatwasser en magnetron | FAQ "Kan Bunzlau in de vaatwasser?" (vaatwasser, magnetron, geen metalen schuursponsje) |
| H3 "Theepotten van Bunzlau Castle" (530 tot 531): link naar **/collections/losse-thee** | Die collectie bestaat niet (de Shopify-koppeling vindt de handle niet; de thee-hoofdcollectie is /collections/thee, "Losse Thee"). Er is ook geen Bunzlau-theepot online (V89) | Pools-aardewerkalinea linkt naar /collections/thee en /collections/theefilters-en-maatschepjes (beide bestaan) |
| H3 "Ophalen in Borne" (533 tot 534): "heeft de voorkeur" naast "uitsluitend afhalen", openingstijden, gratis parkeren | Tegenstrijdig met "alleen afhalen"; openingstijden staan al in het infoblok | Intro-alinea 2, FAQ en het infoblok "Openingstijden" |

Voor (regels 521 tot 534) is de volledige tekst hierboven gedeeltelijk geciteerd; de letterlijke tekst staat in de diff. Na: de regels vervallen, het `div.trbz-seo-inner` toont alleen `_desc_rest` (regel 520, ongewijzigd).

### 3b. Dezelfde voorraad- en bestellijn elders in de sectie

| Regel | Voor | Na | Reden |
|---|---|---|---|
| 234 tot 235 (derde balkitem) | Hele collectie op bestelling / Niet op voorraad? Gewoon bestelbaar | Melamine wordt verstuurd / Verstuurd binnen 1 tot 2 werkdagen | "Hele collectie op bestelling" is een belofte zonder bron; de termijn komt uit V64 |
| 507 (infoblok Contact) | Niet op voorraad? Heel de collectie is op bestelling beschikbaar. | Staat een stuk of decor er niet bij? Neem contact met ons op, dan kijken we of we het voor je kunnen bestellen. | Zelfde belofte; nieuwe zin is de goedgekeurde lijn uit de theewinkelpagina |
| 441 (Over het merk) | Bij Tante Rie vind je theepotten, mokken, ... Staat een stuk er niet? De hele collectie is op bestelling beschikbaar. Je haalt het op zodra het er ligt. | Bij Tante Rie vind je mokken, borden, schalen, kommen en decoratiestukken in meerdere decors. Staat een stuk of decor er niet bij, neem dan contact met ons op, dan kijken we of we het voor je kunnen bestellen. | Zelfde belofte; "theepotten" weg omdat er geen Bunzlau-theepot online staat (V89) |
| 440 (Over het merk) | ... gaat in de vaatwasser, magnetron én oven. Het glazuur is loodvrij en bestand tegen dagelijks gebruik. | ... gaat in de vaatwasser en de magnetron en is bestand tegen dagelijks gebruik. | "Oven" is dezelfde onbevestigde bewering als 220°C; "loodvrij" heeft geen bron |

### 3c. Gezien maar niet gewijzigd (buiten de afgesproken scope)

| Regel | Tekst | Opmerking |
|---|---|---|
| 434 en 439 | "meer dan 200 jaar ambacht", "meer dan twee eeuwen", "pauwenoog" | Geen bron in de repository; ook de Content-redacteur nam ze niet over. Vraag aan Mark staat in de samenvatting |
| 442 | "op een halfuur van Enschede, Hengelo en Almelo" | Geen bron. Zelfde vraag |
| 194 | Label "Authentiek handgemaakt aardewerk" | Melamine is niet handgemaakt (V43); het label zit boven de hele collectie. Kan blijven omdat het aardewerk handgemaakt is |
| 385 en 387 | Badges "Op voorraad" en "Te bestellen" | De badge komt uit `product.available` en is dus geen vaste tekst. Zie 3d voor een kanttekening |
| 415 | Knop "Bestel nu" bij niet-beschikbare producten | Die knop opent de productpagina met het formulier "Stuur een bestelverzoek"; "Bestelverzoek" zou eerlijker zijn. Niet voorgesteld; kleine volgende stap als Mark dat wil |

### 3d. Knoppen "In winkelwagen" (regel 411): laten staan, zo werkt het nu

Voorstel: **ongewijzigd laten staan.** Onderbouwing uit de live gegevens:

1. De knop staat alleen bij producten die `available` zijn (regel 410); anders staat er een link "Bestel nu" naar de productpagina met het bestelverzoek.
2. Het Bunzlau-aardewerk zit in het verzendprofiel "Breekbare producten". Dat profiel heeft geen enkele verzendzone (alleen een leeg locatiegroepje; gelezen op 24-10). Een winkelwagen met alleen aardewerk krijgt in de checkout dus geen verzendtarief en alleen de optie ophalen. Locatie "Tante Rie Borne" is actief en heeft lokaal ophalen aan staan. Zo wordt de afhaalregel in de checkout afgedwongen, niet alleen in de tekst. Dat wordt vastgelegd in changelog 23-10 (profiel Breekbare producten: "geen verzending, alleen afhalen").
3. Melamine, Rice en bewaarblik-melamine zitten in profiel "Pakket" (Nederland 6,95 euro), dus die kunnen wel verzonden worden; dezelfde knop is daar juist goed.
4. De productpagina gebruikt exact dezelfde knop en dezelfde logica en toont daarnaast het accordeon "Ophaalinformatie" ("Dit product versturen we niet. Je bestelt online en haalt het op in onze winkel in Borne."). De kaart op de collectiepagina heeft die zin niet naast de knop, maar de balk "Aardewerk alleen afhalen in Borne" en de ondertitel staan er direct boven en blijven in beeld (de balk is sticky).

Wat ik niet kon vaststellen en dus in de preview test: hoe de winkelwagen en de checkout het eruit laten zien met alleen aardewerk (geen verzendkeuze, wel "ophalen"), en wat er gebeurt in een gemengde winkelwagen (aardewerk plus melamine: verzenden voor melamine en ophalen voor aardewerk gaan niet in één bestelling mee; Shopify toont dan beide opties per leveringsgroep of vraagt om één keuze). Zie testlijst hieronder. Kanttekeningen die niet uit het thema komen: de locatie staat op "klaar voor afhalen binnen 2 uur" (Shopify-instelling, `pickupTime TWO_HOURS`), wat bij een product dat op voorraad ligt klopt maar niet bij een stuk dat nog besteld moet worden (dat gaat via het bestelverzoek, niet via de checkout); en een aantal Bunzlau-producten heeft negatieve totale voorraad (bijvoorbeeld rijstkom 500 ml -3), waardoor "Op voorraad" en de knop kunnen verschijnen bij iets dat niet in de winkel ligt. Dat is een voorraadkwestie (thema "Bunzlau eigen voorraad 2026-10-23" bestaat al als ongepubliceerde kopie), geen onderdeel van dit voorstel.

## Samengevat

| Onderdeel | Regels (live) | Omvang |
|---|---|---|
| CSS intro | 29/30 | +4 |
| Ondertitel plus intro in hero | 201 tot 204 | 1 gewijzigd, +3 |
| Balk Aardewerk alleen afhalen / Melamine wordt verstuurd | 220, 234, 235 | 3 gewijzigd |
| Over het merk | 440, 441 | 2 gewijzigd |
| Kop en contactregel infoblok | 458, 507 | 2 gewijzigd |
| SEO-blok | 521 tot 534 | 14 verwijderd |

Totaal 97 regels diff, één bestand. Het JSON-LD, de itemprop, de filters, de kaarten, de winkelfoto en de schema-instellingen blijven ongemoeid.

## Uitvoering na akkoord van Mark

Volgorde is belangrijk: het SEO-blok verdwijnt in dit voorstel en de nieuwe inhoud komt uit de collectiebeschrijving. Zonder de nieuwe body zou er onder de pagina te weinig tekst staan.

1. **Review.** De Kwaliteitsredacteur keurt de nieuwe teksten in deze diff goed (ondertitel, balk, infoblok, merkblok). De intro-, Pools- en FAQ-tekst staan al in het concept van de Content-redacteur en gaan via On-page naar Shopify.
2. **Themakopie.** `shopify theme list` en controleer dat live nog thema 203153015048 is en dat het bestand live nog gelijk is aan dit voorstel-uitgangspunt (45.180 bytes, geen wijzigingen sinds 23-10). Maak een kopie met `shopify theme duplicate --theme 203153015048 --name "bunzlau-intro-voorraadteksten 2026-10-xx"` (de winkel heeft op 24-10 18 thema's; limiet 20, dus ruimte voor één kopie, ruim een extra kopie niet zonder eerst een oude te archiveren). Pas de diff toe met `patch -p1` op een pull van de kopie, `shopify theme push --theme <kopie-id> --only sections/tr-collection-bunzlau.liquid`. Niet op het live thema.
3. **Preview.** Open de previewlink van de kopie op /collections/bunzlau (en op /collections/bunzlau?filter.p.product_type=Keramiek). Controleer: (a) met de oude body toont de hero nu de oude eerste alinea (verwacht gedrag, bewijst dat `_desc_first` werkt), (b) alinea 2 en verder staan eenmaal onder de pagina, (c) ondertitel, balk en infoblok kloppen, (d) geen Liquid-fouten, (e) mobiel (375 px): intro leesbaar, producten nog in beeld na één scherm scrollen, (f) JSON-LD CollectionPage geldig in de Rich Results Test, (g) in de preview een aardewerkproduct in de winkelwagen: checkout biedt alleen ophalen; een melamineproduct: verzenden 6,95; gemengde winkelwagen: vastleggen wat de klant ziet.
4. **Diff voor het publiceren.** Vergelijk live met de kopie (`diff` op het bestand) en laat precies deze diff aan Mark zien. Wacht op zijn akkoord op de gepubliceerde versie (V-nummer door de hoofdsessie).
5. **Publicatie in één werkgang.** Eerst On-page: backup van de huidige body (marketing/onpage/), nieuwe body met intro, Pools-alinea en FAQ, plus title en meta uit het On-page-voorstel (de eerste alinea blijft tot stap 6 onzichtbaar). Direct daarna `shopify theme push --live --only sections/tr-collection-bunzlau.liquid` uit de gecontroleerde kopie, na backup van het live bestand in scripts/archief-themas/bunzlau-intro-backup-<datum>-live-203153015048/. Tussen stap 5a en 5b geen uren laten zitten: tussendoor staan nieuwe FAQ en het oude SEO-blok kort allebei op de pagina.
6. **Controle live en nieuwe crawl.** Controleer met curl en de Rich Results Test: intro in de HTML boven de producten, geen "officieel reseller", "op voorraad" in een decorlijst, "220" of "losse-thee" meer in de pagina; precies één keer elke alinea; JSON-LD geldig; HTTP 200; geen Liquid-fouten; screenshot mobiel in assets/screenshots/. Vraag indexering aan via de URL-inspectie (gsc_inspect.py) en vergelijk een nieuwe crawl met de nulwaarden uit plan-2026-11-vroege-start.md.
7. **Changelog.** Eén regel in marketing/changelog.md met datum, URL, wat er veranderd is en waarom, verwijzing naar dit voorstel en de backup. Terugdraaien: `shopify theme push --live --only` met de backup, en de oude body uit het On-page-backupbestand.

## Nieuwe vragen voor Mark (alleen in de samenvatting, niet in vragen-voor-mark.md)

Zie het antwoord aan de hoofdsessie.
