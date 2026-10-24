# Voorstel thema /collections/bunzlau: intro zichtbaar, ondertitel, vaste teksten (V105)

Opgesteld door Technisch SEO op 24 oktober 2026. Status: alleen voorstel. Er is niets gewijzigd in Shopify, het live thema of changelog.md, en er is nog geen themakopie gemaakt. Mark gaf op 24-10 akkoord op V105 voor het maken van dit voorstel; publicatie wacht op een tweede akkoord op de voor-en-nawaarden hieronder.

**Versie 2 (24 oktober 2026).** Bijgewerkt na de review van de Kwaliteitsredacteur (marketing/review/review-bunzlau-2026-10-30.md, paragraaf 7: correcties T1, T2, T4 en T5 letterlijk overgenomen) en de antwoorden van Mark van 24-10: V113 nee (geen "Aardewerk"-aanvullingen, dus T3 vervalt), V114 (merkblok rust op de feiten van Mark, T6 verwerkt) en V117 ja ("Bestelverzoek" in plaats van "Bestel nu").

Diff: marketing/technisch/voorstel-bunzlau-thema-2026-10-24.diff (één bestand: sections/tr-collection-bunzlau.liquid, 107 regels diff, pad t.o.v. de themawortel, toe te passen met `patch -p1`). `patch --dry-run` op het live bestand geeft geen fouten.

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
| Na (T2 van de review) | Handgeschilderd aardewerk uit Polen, af te halen bij Tante Rie in Borne. Het melamine kun je laten bezorgen. | 201 |

Reden: het aardewerk wordt niet verstuurd (afhaalregels 22-10, V18), het melamine wel (V3, V43). "Kun je laten bezorgen" laat geen "niet" ontbreken waar "wel" tegenover staat, en "aardewerk" maakt duidelijk dat het afhalen bij het aardewerk hoort. Geen voorraadbelofte, geen uitroepteken, geen em-dash. De vormgeving van "Borne" (vet en schuin) blijft.

**Balk onder de hero (regels 220 en 234 tot 235), na V113 nee.** De aanvullingen "Aardewerk alleen afhalen in Borne" en de kop "Aardewerk afhalen in de winkel" (T3) vervallen. De kop in het infoblok (regel 458) blijft daarmee "Alleen afhalen in de winkel", zoals nu live. Omdat de reviewer terecht waarschuwt dat de balk zonder aanvulling "alleen afhalen" zegt terwijl het melamine wordt verstuurd, kies ik voor de balk een formulering zonder "alleen" en zonder tegenspraak:

| Regel | Voor | Na | Reden |
|---|---|---|---|
| 220 | Alleen afhalen in Borne | Afhalen in Borne | Waar: afhalen kan voor alles. Het woord "alleen" ontbreekt, dus het botst niet met het melamine dat wordt bezorgd |
| 234 tot 235 (T1) | Hele collectie op bestelling / Niet op voorraad? Gewoon bestelbaar | Melamine laten bezorgen / Verstuurd binnen 1 tot 2 werkdagen | Eén keer "verstuurd" in plaats van twee; termijn uit V64 |

De balk leest nu "Afhalen in Borne", "Openingstijden winkel", "Melamine laten bezorgen": consistent met de ondertitel ("af te halen" bij het aardewerk, "kun je laten bezorgen" bij het melamine). Restpunt voor Mark, geen onderdeel van de diff: de kop van het infoblok (regel 458) en de tekst "Alleen afhalen in de winkel" blijven "alleen" zeggen voor de hele collectie. Dat is de huidige live tekst en Mark koos bij V113 voor niet wijzigen.

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
| 234 tot 235 (derde balkitem) | Hele collectie op bestelling / Niet op voorraad? Gewoon bestelbaar | Melamine laten bezorgen / Verstuurd binnen 1 tot 2 werkdagen (T1) | "Hele collectie op bestelling" is een belofte zonder bron; de termijn komt uit V64 |
| 507 (infoblok Contact) | Niet op voorraad? Heel de collectie is op bestelling beschikbaar. | Zoek je een ander decor? Vraag ons gerust of we het voor je kunnen bestellen. (T4) | Zelfde belofte weg; korter, zodat het niet het merkblok herhaalt |
| 440 (Over het merk) | Bunzlau Castle aardewerk gaat in de vaatwasser, magnetron én oven. Het glazuur is loodvrij en bestand tegen dagelijks gebruik. Je koopt het niet voor één seizoen. | Het aardewerk van Bunzlau Castle mag in de vaatwasser en de magnetron, en het is stevig genoeg voor dagelijks gebruik. Je koopt het niet voor één seizoen. (T5) | "Oven" is dezelfde onbevestigde bewering als 220°C; "loodvrij" heeft geen bron (V98 bevestigt vaatwasser en magnetron) |
| 441 (Over het merk) | Bij Tante Rie vind je theepotten, mokken, borden, schalen, kommen en decoratiestukken in meerdere decors. Staat een stuk er niet? De hele collectie is op bestelling beschikbaar. Je haalt het op zodra het er ligt. | Bij Tante Rie vind je mokken, borden, schalen, kommen en decoratiestukken in meerdere decors. Staat een stuk of decor er niet bij, neem dan contact met ons op. We kijken graag of we het voor je kunnen bestellen. (T5) | Zelfde belofte weg |

Controle bij T5 (Shopify, alleen lezen, 24-10, alle 136 producten van de collectie): "decoratiestukken" kan blijven staan. Online gepubliceerd zijn onder meer Vaas 1600 ml, Vaas 2100 ml en Vaas 4400 ml en Keukenpot / Bloempot Ø 14 cm. Opmerking: ook Theepot 1300 ml, Theepot 2000 ml, Hanger Teapot en Theestoof voor theepot 1300 & 2000 ml staan nu online (de eerdere aanname "geen Bunzlau-theepot online", V89, is achterhaald). T5 laat "theepotten" weg; ik heb dat letterlijk overgenomen. Wil de Kwaliteitsredacteur "theepotten" terug in de opsomming, dan is dat één woord.

**Merkblok volgens V114 (T6, regels 434, 439 en 442).** Alleen wat Mark bevestigde: Bunzlau Castle bestaat sinds 1984, in de plaats in Polen waar het gemaakt wordt maakt men al sinds de 18e eeuw keramiek, en de reistijd naar de winkel is ongeveer 25 minuten vanuit Enschede, 15 vanuit Hengelo en 20 vanuit Almelo. "Pauwenoog" is niet bevestigd en gaat eruit. De kop "meer dan 200 jaar ambacht" paste niet bij "sinds 1984" en is mee aangepast.

| Regel | Voor | Na |
|---|---|---|
| 434 (kop) | Bunzlau Castle: meer dan 200 jaar ambacht | Bunzlau Castle: aardewerk uit Bolesławiec |
| 439 | In het Poolse stadje Bolesławiec schilderen pottenbakkers al meer dan twee eeuwen aardewerk met de hand. Ze gebruiken traditionele stempels en sponsjes om de patronen aan te brengen. Geen twee stukken zijn precies gelijk. Het klassieke blauwe patroon, het pauwenoog, staat al generaties lang symbool voor het merk. | Bunzlau Castle bestaat sinds 1984. Het aardewerk komt uit Bolesławiec, een plaats in Polen waar al sinds de 18e eeuw keramiek wordt gemaakt. De patronen worden met de hand aangebracht, met traditionele stempels en sponsjes, waardoor geen twee stukken precies gelijk zijn. |
| 442 | Borne ligt midden in Twente, op een halfuur van Enschede, Hengelo en Almelo. Loop binnen, kijk rond en neem het mee. | Borne ligt midden in Twente. Vanuit Enschede reis je ongeveer 25 minuten, vanuit Hengelo ongeveer 15 en vanuit Almelo ongeveer 20. Loop binnen, kijk rond en neem het mee. |

"Met de hand aangebracht, met traditionele stempels en sponsjes" en "geen twee stukken precies gelijk" komen uit de bestaande tekst en uit het concept van de Content-redacteur; ze zijn niet nieuw. "Reis je" laat het vervoermiddel open, want Mark noemde alleen de reistijd.

### 3b2. Knop "Bestel nu" wordt "Bestelverzoek" (V117 ja)

Waar de tekst vandaan komt: hardgecodeerd in de sectie, niet in een snippet of taalbestand.

| Plek | Regel (live) | Voor | Na | In deze diff |
|---|---|---|---|---|
| sections/tr-collection-bunzlau.liquid, knop bij niet-beschikbare producten op de collectiekaart | 415 | `aria-label="Bestel {{ product.title }}">Bestel nu</a>` | `aria-label="Doe een bestelverzoek voor {{ product.title }}">Bestelverzoek</a>` | Ja |

De knop leidt naar de productpagina met het formulier "Stuur een bestelverzoek", dus de nieuwe naam sluit aan. De screenreadertekst is meegenomen omdat "Bestel" daar dezelfde belofte deed.

**Apart onderdeel, buiten deze diff: de productpagina's.** De zelfde tekst staat ook in sections/tr-product-bunzlau.liquid (regels zoals in de themakopie van 23-10; bij het pullen opnieuw bevestigen, omdat ik dit bestand niet live heb teruggelezen):

| Regel | Voor | Na |
|---|---|---|
| 383 (hoofdknop, bij laden van de pagina) | `{%- if _available -%}In winkelwagen{%- else -%}Bestellen{%- endif -%}` | `... else -%}Bestelverzoek{%- endif -%}` |
| 494 (sticky knop onderaan) | `{%- if _available -%}In winkelwagen{%- else -%}Bestellen{%- endif -%}` | `... else -%}Bestelverzoek{%- endif -%}` |
| 538 (JS bij wissel van variant) | `atc.textContent=v.available?'In winkelwagen':'Bestel nu';` | `atc.textContent=v.available?'In winkelwagen':'Bestelverzoek';` |
| 543 (JS, sticky knop bij wissel van variant) | `if(sbEl)sbEl.textContent=v.available?'In winkelwagen':'Bestel nu';` | `if(sbEl)sbEl.textContent=v.available?'In winkelwagen':'Bestelverzoek';` |

Dat is een kleine reden om dit mee te nemen: op de productpagina staat nu bij het laden "Bestellen" en na het kiezen van een andere variant "Bestel nu", dus de knop wisselt van naam. Met de wijziging is het overal "Bestelverzoek". Alleen Bunzlau is gevraagd (V117). De Blond-pagina's hebben dezelfde teksten (sections/tr-collection-blond.liquid regel 384, sections/tr-product-blond.liquid regels 754 en 757); die laat ik ongemoeid tot Mark daar iets over zegt. Ik heb voor de productpagina geen aparte diff gemaakt; stuur ik die gewenst na akkoord in dezelfde themakopie mee, dan voeg ik hem toe.

### 3c. Gezien maar niet gewijzigd

| Regel | Tekst | Opmerking |
|---|---|---|
| 194 | Label "Authentiek handgemaakt aardewerk" | Melamine is niet handgemaakt (V43); het label zit boven de hele collectie. Kan blijven omdat het aardewerk handgemaakt is |
| 385 en 387 | Badges "Op voorraad" en "Te bestellen" | De badge komt uit `product.available` en is dus geen vaste tekst. Zie 3d voor een kanttekening |
| 458 | Kop infoblok "Alleen afhalen in de winkel" | Blijft zoals live (V113 nee), zie de opmerking onder punt 2 |

### 3d. Knoppen "In winkelwagen" (regel 411): laten staan, zo werkt het nu

Voorstel: **ongewijzigd laten staan.** Onderbouwing uit de live gegevens:

1. De knop staat alleen bij producten die `available` zijn (regel 410); anders staat er een link "Bestel nu" naar de productpagina met het bestelverzoek.
2. Het Bunzlau-aardewerk zit in het verzendprofiel "Breekbare producten". Dat profiel heeft geen enkele verzendzone (alleen een leeg locatiegroepje; gelezen op 24-10). Een winkelwagen met alleen aardewerk krijgt in de checkout dus geen verzendtarief en alleen de optie ophalen. Locatie "Tante Rie Borne" is actief en heeft lokaal ophalen aan staan. Zo wordt de afhaalregel in de checkout afgedwongen, niet alleen in de tekst. Dat wordt vastgelegd in changelog 23-10 (profiel Breekbare producten: "geen verzending, alleen afhalen").
3. Melamine, Rice en bewaarblik-melamine zitten in profiel "Pakket" (Nederland 6,95 euro), dus die kunnen wel verzonden worden; dezelfde knop is daar juist goed.
4. De productpagina gebruikt exact dezelfde knop en dezelfde logica en toont daarnaast het accordeon "Ophaalinformatie" ("Dit product versturen we niet. Je bestelt online en haalt het op in onze winkel in Borne."). De kaart op de collectiepagina heeft die zin niet naast de knop, maar de balk "Afhalen in Borne" en de ondertitel staan er direct boven en blijven in beeld (de balk is sticky).

Wat ik niet kon vaststellen en dus in de preview test: hoe de winkelwagen en de checkout het eruit laten zien met alleen aardewerk (geen verzendkeuze, wel "ophalen"), en wat er gebeurt in een gemengde winkelwagen (aardewerk plus melamine: verzenden voor melamine en ophalen voor aardewerk gaan niet in één bestelling mee; Shopify toont dan beide opties per leveringsgroep of vraagt om één keuze). Zie testlijst hieronder. Kanttekeningen die niet uit het thema komen: de locatie staat op "klaar voor afhalen binnen 2 uur" (Shopify-instelling, `pickupTime TWO_HOURS`), wat bij een product dat op voorraad ligt klopt maar niet bij een stuk dat nog besteld moet worden (dat gaat via het bestelverzoek, niet via de checkout); en een aantal Bunzlau-producten heeft negatieve totale voorraad (bijvoorbeeld rijstkom 500 ml -3), waardoor "Op voorraad" en de knop kunnen verschijnen bij iets dat niet in de winkel ligt. Dat is een voorraadkwestie (thema "Bunzlau eigen voorraad 2026-10-23" bestaat al als ongepubliceerde kopie), geen onderdeel van dit voorstel.

## Samengevat

| Onderdeel | Regels (live) | Omvang |
|---|---|---|
| CSS intro | 29/30 | +4 |
| Ondertitel plus intro in hero | 201 tot 204 | 1 gewijzigd, +3 |
| Balk Afhalen in Borne / Melamine laten bezorgen | 220, 234, 235 | 3 gewijzigd |
| Over het merk (kop, drie alinea's, vierde alinea) | 434, 439, 440, 441, 442 | 5 gewijzigd |
| Contactregel infoblok | 507 | 1 gewijzigd |
| Knop Bestelverzoek | 415 | 1 gewijzigd |
| SEO-blok | 521 tot 534 | 14 verwijderd |

Totaal 107 regels diff, één bestand. Het JSON-LD, de itemprop, de filters, de kaarten, de winkelfoto, de kop van het infoblok en de schema-instellingen blijven ongemoeid. De productpagina's staan als apart onderdeel onder 3b2.

## Uitvoering na akkoord van Mark

Volgorde is belangrijk: het SEO-blok verdwijnt in dit voorstel en de nieuwe inhoud komt uit de collectiebeschrijving. Zonder de nieuwe body zou er onder de pagina te weinig tekst staan.

1. **Review.** De Kwaliteitsredacteur keurt de nieuwe teksten in deze diff goed (ondertitel, balk, infoblok, merkblok). De intro-, Pools- en FAQ-tekst staan al in het concept van de Content-redacteur en gaan via On-page naar Shopify.
2. **Themakopie.** `shopify theme list` en controleer dat live nog thema 203153015048 is en dat het bestand live nog gelijk is aan dit voorstel-uitgangspunt (45.180 bytes, geen wijzigingen sinds 23-10). Maak een kopie met `shopify theme duplicate --theme 203153015048 --name "bunzlau-intro-voorraadteksten 2026-10-xx"` (de winkel heeft op 24-10 18 thema's; limiet 20, dus ruimte voor één kopie, ruim een extra kopie niet zonder eerst een oude te archiveren). Pas de diff toe met `patch -p1` op een pull van de kopie, `shopify theme push --theme <kopie-id> --only sections/tr-collection-bunzlau.liquid`. Niet op het live thema.
3. **Preview.** Open de previewlink van de kopie op /collections/bunzlau (en op /collections/bunzlau?filter.p.product_type=Keramiek). Controleer: (a) met de oude body toont de hero nu de oude eerste alinea (verwacht gedrag, bewijst dat `_desc_first` werkt), (b) alinea 2 en verder staan eenmaal onder de pagina, (c) ondertitel, balk, infoblok en merkblok kloppen, en de knop heet "Bestelverzoek" bij een niet-beschikbaar product, (d) geen Liquid-fouten, (e) mobiel (375 px): intro leesbaar, producten nog in beeld na één scherm scrollen, (f) JSON-LD CollectionPage geldig in de Rich Results Test, (g) in de preview een aardewerkproduct in de winkelwagen: checkout biedt alleen ophalen; een melamineproduct: verzenden 6,95; gemengde winkelwagen: vastleggen wat de klant ziet.
4. **Diff voor het publiceren.** Vergelijk live met de kopie (`diff` op het bestand) en laat precies deze diff aan Mark zien. Wacht op zijn akkoord op de gepubliceerde versie (V-nummer door de hoofdsessie).
5. **Publicatie in één werkgang.** Eerst On-page: backup van de huidige body (marketing/onpage/), nieuwe body met intro, Pools-alinea en FAQ, plus title en meta uit het On-page-voorstel (de eerste alinea blijft tot stap 6 onzichtbaar). Direct daarna `shopify theme push --live --only sections/tr-collection-bunzlau.liquid` uit de gecontroleerde kopie, na backup van het live bestand in scripts/archief-themas/bunzlau-intro-backup-<datum>-live-203153015048/. Tussen stap 5a en 5b geen uren laten zitten: tussendoor staan nieuwe FAQ en het oude SEO-blok kort allebei op de pagina.
6. **Controle live en nieuwe crawl.** Controleer met curl en de Rich Results Test: intro in de HTML boven de producten, geen "officieel reseller", "op voorraad" in een decorlijst, "220", "losse-thee", "pauwenoog", "200 jaar", "te bestellen bij", "Hele collectie op bestelling", "Heel de collectie" of "Bestel nu" meer in de pagina; precies één keer elke alinea; JSON-LD geldig; HTTP 200; geen Liquid-fouten; screenshot mobiel in assets/screenshots/. Vraag indexering aan via de URL-inspectie (gsc_inspect.py) en vergelijk een nieuwe crawl met de nulwaarden uit plan-2026-11-vroege-start.md.
7. **Changelog.** Eén regel in marketing/changelog.md met datum, URL, wat er veranderd is en waarom, verwijzing naar dit voorstel en de backup. Terugdraaien: `shopify theme push --live --only` met de backup, en de oude body uit het On-page-backupbestand.

## Open na versie 2

Beantwoord door Mark op 24-10 en verwerkt: V113 (nee), V114 (bronnen merkblok), V117 (Bestelverzoek). Nog open en niet in deze diff: V115 (afhaaltijd 2 uur) en V116 (negatieve voorraad), beide gevolgd door de hoofdsessie. Nieuw uit deze ronde: de theepotten staan online (zie 3b), dus de opsomming in het merkblok kan "theepotten" weer krijgen; en de kop van het infoblok blijft "Alleen afhalen in de winkel" terwijl het melamine wordt verstuurd.
