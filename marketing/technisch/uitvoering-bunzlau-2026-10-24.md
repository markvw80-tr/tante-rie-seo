# Uitvoering Bunzlau-pakket (V118 en V117): themakopie met preview

Opgesteld door Technisch SEO op 24 oktober 2026. Status: themakopie gemaakt en gevuld, niet gepubliceerd. Wacht op Marks "ja" na de preview.

## De themakopie

| | |
|---|---|
| Naam | Bunzlau collectie V118 2026-10-24 |
| Theme-id | 204095619336 (gid://shopify/OnlineStoreTheme/204095619336) |
| Rol | UNPUBLISHED |
| Gemaakt als | duplicaat van het live thema 203153015048 ("Agent-ready koppen 2026-10-09", MAIN), via themeDuplicate |
| Live thema | niet aangeraakt; na afloop nog steeds MAIN met dezelfde checksums (collectiebestand 3f07cffe641114edaa32481c8ad5b4e9, productbestand 7c7cc6fb4384264d4808f8532f33e62b) |
| Niet gewijzigd in Shopify | collectiebeschrijving, title, meta, het blog en /pages/serviezen |

## Wat er in de kopie is aangepast

Er zijn twee bestanden gewijzigd (de eerste ronde). Zie hieronder voor de drie extra bestanden van 24-10 (gewicht en spatie).

| Bestand | Wijziging | Diff |
|---|---|---|
| sections/tr-collection-bunzlau.liquid | Alles uit marketing/technisch/voorstel-bunzlau-thema-2026-10-24.diff: eerste alinea van de beschrijving zichtbaar in de hero (witte tekst), nieuwe ondertitel, balk "Afhalen in Borne" en "Melamine laten bezorgen", knop "Bestelverzoek" op de kaart, nieuw merkblok, nieuwe tekst bij "Zoek je een ander decor?", en het vaste SEO-blok onderaan verwijderd | voorstel-bunzlau-thema-2026-10-24.diff |
| sections/tr-product-bunzlau.liquid | V117: "Bestellen" en "Bestel nu" worden "Bestelverzoek" op vier plekken (regel 383 hoofdknop, 494 sticky knop, 538 en 543 in de JavaScript bij wisselen van variant) | voorstel-bunzlau-product-bestelverzoek-2026-10-24.diff (nieuw) |

### Controle vooraf (afwijking? nee)

Het collectiebestand in de kopie was 45.180 bytes met checksum 3f07cffe641114edaa32481c8ad5b4e9, gelijk aan het live bestand en gelijk aan wat de diff verwacht (backup van 23-10 plus voorstel-winkelfotos-2026-10-23.diff geeft byte voor byte hetzelfde bestand). De diff paste schoon, zonder verschuiving of afgewezen delen. Het productbestand in de kopie was 42.312 bytes met checksum 7c7cc6fb4384264d4808f8532f33e62b; dat is de backup van 22-10 plus de productwijziging uit afhaalregels-2026-10-22.diff. De regelnummers 383, 494, 538 en 543 zijn in dat bestand bevestigd.

### Controle achteraf (teruggelezen uit de kopie)

| Bestand | Bytes | MD5 uit de kopie | Gelijk aan lokaal gepatcht bestand |
|---|---|---|---|
| sections/tr-collection-bunzlau.liquid | 43.815 | c9588790efece68e8e2c64018b99c408 | ja |
| sections/tr-product-bunzlau.liquid | 42.328 | 908625bd159118dd2a7bc0fcdf1847cd | ja |

In beide bestanden is de Liquid gecontroleerd op duidelijke syntaxfouten: elk `if`, `unless`, `for`, `comment` en `schema` heeft zijn sluittag, en het aantal openende en sluitende `{%` en `{{` klopt (collectie 198/198 en 52/52). In het productbestand staat een `}}` meer dan `{{` (62 tegen 63); dat zit in de JavaScript en in het bestaande JSON-blok en was in het live bestand al zo. In het collectiebestand komt "Bestel nu" niet meer voor, in het productbestand komen "Bestel nu" en "Bestellen" niet meer voor. De Liquid is niet gerenderd door Shopify als aparte test; dat gebeurt in de preview.

## Extra wijzigingen 24-10 (akkoord Mark): gewicht en ontbrekende spatie

Mark gaf op 24-10 akkoord om twee themafouten in de kopie te herstellen, voor Bunzlau en Blond. Alleen de ongepubliceerde kopie 204095619336 is gewijzigd; het live thema 203153015048 is niet aangeraakt (nog MAIN). De volledige diff staat in marketing/technisch/fix-gewicht-spatie-2026-10-24.diff.

### 1. Gewicht in de specificatietabel

Oorzaak: `variant.weight` geeft in Liquid het gewicht in gram terug (Shopify-documentatie bij het filter weight_with_unit: gewicht 200 wordt 0,2 kg). De code vermenigvuldigde dat nog met 1000, alsof het kilogram was, waardoor 189 gram als 189000 g werd getoond. De fout zat op twee plekken per bestand: in de tabelcel die de server rendert, en in de JSON met varianten die de JavaScript gebruikt bij het wisselen van variant (de JavaScript zelf plakt alleen " g" achter dat getal). In de winkelgegevens staat de kom Melamine Kom Wild Flowers Ø 15 cm (SKU 3653) op 189 GRAMS en de winkel gebruikt grammen als eenheid.

Nieuwe berekening: `{{ _vw | round }} g` in de tabel en `"weight":{{ v.weight | round }}` in de varianten-JSON. Het getal is dus het aantal gram uit Shopify, afgerond op een heel getal, met " g" erachter. Er is bewust niet gekozen voor het filter `weight_with_unit`: dat toont het gewicht in de eenheid uit de winkelinstellingen (nu gram, maar bij kilogram "0,189 kg"), kan niet in de JSON worden gebruikt en zou server en JavaScript een verschillende notatie geven. Met een expliciet getal in gram zijn beide gelijk en blijft de weergave stabiel als de instelling ooit wijzigt. De overige secties die het gewicht tonen (tr-product-redesign en tr-product-bakmix) gebruiken al `weight_with_unit` zonder vermenigvuldiging en zijn niet gewijzigd. tr-offer-policies rekent met gram (drempel 300) en klopt.

| Bestand | Regel | Wijziging |
|---|---|---|
| sections/tr-product-bunzlau.liquid | 348 (varianten-JSON), 437 (tabel) | `times: 1000` verwijderd |
| sections/tr-product-bunzlau-melamine.liquid | 353 (varianten-JSON), 408 (tabel) | `times: 1000` verwijderd |
| sections/tr-product-blond.liquid | 370 (varianten-JSON), 578 (tabel) | `times: 1000` verwijderd |

De JavaScript die bij het wisselen van variant het gewicht bijwerkt (trbzp-spec-weight in regel 548 van tr-product-bunzlau en 512 van tr-product-bunzlau-melamine, trbap-spec-weight in regel 766 van tr-product-blond) is ongewijzigd: die toont `v.weight + ' g'` en krijgt nu het juiste getal. In andere secties, snippets, blocks, templates en assets van de kopie komt de omrekening niet voor (alle 412 tekstbestanden doorzocht op `times: 1000` en op gewichtsverwijzingen).

Opmerking over de gegevens: bij vrijwel alle Bunzlau-aardewerkproducten (template bunzlau) en bij alle 40 online gepubliceerde Blond-producten staat het gewicht in Shopify op 0. Daar toont de tabel (ook na de fix) een streepje. Alleen de melamine-producten hebben een gewicht (bijvoorbeeld 189 g voor de kom en 249 g voor het bord). Bij Theetip Bloem staat 0,1 gram; dat zou als "0 g" verschijnen. Dit is geen themafout maar ontbrekende productgegevens; er is niets in Shopify aangepast.

### 2. Ontbrekende spatie voor "bij"

Oorzaak: in de reservetekst voor producten zonder beschrijving eindigde de voorwaarde met `{%- endif -%}`. Het streepje rechts haalt de spatie weg die erna komt, zodat "melamine" en "bij" aan elkaar kwamen ("melaminebij"). Hersteld in sections/tr-product-bunzlau-melamine.liquid regel 399: `{%- endif -%} bij Tante Rie in Borne.` is nu `{%- endif %} bij Tante Rie in Borne.` (alleen links gestript, rechts blijft de spatie staan). De reservetekst voor producten zonder beschrijving komt alleen in dit bestand voor; de Blond-sectie heeft een andere reservetekst zonder deze constructie, en tr-product-bunzlau heeft een vaste tekst zonder voorwaarde.

Gevonden maar niet gewijzigd (zelfde soort fout, ander effect): in de specificatietabel staat `</span> {%- if ... -%}Ja{%- else -%}...`. Het streepje links haalt de spatie tussen het vinkje en het woord weg, zodat er "✓Ja" en "✗Handwas aanbevolen" komt zonder tussenruimte. Het gaat om tr-product-bunzlau regel 444 tot en met 446 (vaatwasser, oven, magnetron) en tr-product-blond regel 591 (vaatwasser). Het vinkje is een opgemaakte ronde badge met eigen opvulling, dus het valt weinig op. Ook staat er in collectiesecties en de coldbrew-pagina (bijvoorbeeld tr-collection-kruidenthee regel 184, tr-collection-witte-thee regel 184, tr-page-cold-brew regel 144 tot en met 151) een icoon dat met `{%- render 'tr-icon' ... -%}` direct tegen de tekst erna aan staat. Dat zijn geen woorden die aan elkaar plakken. Wil Mark dat dit ook wordt rechtgezet, dan is dat een kleine vervolgwijziging (V-nummer toevoegen door de hoofdsessie).

### Controle na het schrijven

Elk bestand is uit de kopie teruggelezen en vergeleken met de bedoelde versie.

| Bestand | Bytes voor | Bytes na | MD5 uit de kopie na schrijven | Gelijk aan bedoelde versie |
|---|---|---|---|---|
| sections/tr-product-bunzlau.liquid | 42.328 | 42.300 | 50827bc6a8de29649e4b04254f208511 | ja |
| sections/tr-product-bunzlau-melamine.liquid | 37.155 | 37.126 | 106982503c08cfb82d02a87e89b56312 | ja |
| sections/tr-product-blond.liquid | 50.230 | 50.202 | 38e414b5f02d3e0dccbb7bb2524c8d93 | ja |

Het verschil in bytes is precies de verwijderde tekst ` times: 1000 |` (14 tekens per plek) en voor de melamine-sectie het ene streepje dat bij `endif` is weggehaald. Bij het eerste schrijven van de Blond-sectie weken negen decoratieve commentaarregels (lijnen van ─ tekens) af in lengte door een typefout van mij; dat is direct gezien aan de bytegrootte (50.721) en met een tweede schrijfactie hersteld. De uiteindelijke diff bevat alleen de bedoelde regels. De Liquid is niet door Shopify gerenderd (de preview-URL is vanuit deze omgeving niet bereikbaar); de weergave moet Mark in de preview bekijken.

## Preview-URL's

| Wat | URL |
|---|---|
| Collectie Bunzlau | https://tanterie.nl/collections/bunzlau?preview_theme_id=204095619336 |
| Productpagina met niet-beschikbare variant (Boeren mok 240 ml, variant Blue Eyes is niet beschikbaar) | https://tanterie.nl/products/boeren-mok-240-ml?variant=57953071857928&preview_theme_id=204095619336 |
| Productpagina met beschikbare variant, voor de winkelwagentest (zelfde product, variant Lace) | https://tanterie.nl/products/boeren-mok-240-ml?variant=57953071923464&preview_theme_id=204095619336 |
| Melamine voor de gemengde winkelwagen | https://tanterie.nl/products/melamine-kom-wild-flowers-o-15-cm?preview_theme_id=204095619336 |
| Gewicht en spatie: melaminekom, gewicht moet 189 g zijn (geen 189000 g); de beschrijving is leeg, dus onder Productomschrijving moet "Bunzlau Castle melamine bij Tante Rie in Borne." staan | https://tanterie.nl/products/melamine-kom-wild-flowers-o-15-cm?preview_theme_id=204095619336 |
| Gewicht: melaminebord, 249 g | https://tanterie.nl/products/melamine-bord-wild-flowers-o-25-cm?preview_theme_id=204095619336 |
| Bunzlau-aardewerk (Boeren mok): gewicht staat in Shopify op 0, dus de tabel toont een streepje; alleen controleren dat er geen "0 g" of ander gek getal staat | https://tanterie.nl/products/boeren-mok-240-ml?preview_theme_id=204095619336 |
| Blond (Love Green Girl): gewicht staat in Shopify op 0, de tabel toont een streepje; geen enkel online Blond-product heeft een gewicht | https://tanterie.nl/products/love-green-girl?preview_theme_id=204095619336 |

## Wat Mark in de preview moet controleren

1. **De witte introtekst op de herofoto.** Op de collectiepagina moet onder de ondertitel een alinea in witte tekst staan, goed leesbaar op de foto, op desktop en op telefoon. Let op de afstand tussen ondertitel, intro en de teller "producten". Let op: de preview toont nog de oude collectiebeschrijving, zie hieronder. Wat je nu ziet als intro is dus de oude eerste alinea ("Bij Tante Rie in Borne vind je een uitgebreid assortiment ..."), niet de nieuwe tekst. Het gaat nu om vorm en leesbaarheid.
2. **De knoppen.** Op de collectiekaarten moet bij een product dat niet beschikbaar is de knop "Bestelverzoek" staan (blauw), bij een beschikbaar product "In winkelwagen". Op de productpagina van de Boeren mok met variant Blue Eyes moet de hoofdknop "Bestelverzoek" heten, en na het kiezen van een beschikbare variant (bijvoorbeeld Lace) "In winkelwagen" en weer "Bestelverzoek" bij een niet-beschikbare. Controleer ook de plakkende knop onderaan op telefoon: die moet dezelfde naam tonen als de hoofdknop, ook na het wisselen van variant. Klik op "Bestelverzoek" en kijk of het formulier "Stuur een bestelverzoek" opent. Verstuur in de preview geen echt verzoek.
3. **Een winkelwagen met aardewerk plus melamine.** Dit kon ik uit de code niet vaststellen. Voeg een beschikbaar aardewerk (Boeren mok, variant Lace) en een melamine-product toe en ga naar de kassa zonder te betalen. Controleer drie gevallen: alleen aardewerk (bij aardewerk moet alleen ophalen als keuze verschijnen, geen verzendtarief), alleen melamine (verzenden voor 6,95 euro en ophalen), en beide samen (hoe Shopify de levering dan toont, per leveringsgroep of als één keuze). Voor deze test is geen betaling nodig. Aardewerk valt in verzendprofiel "Breekbare producten" zonder verzendzone en melamine in profiel "Pakket" (Nederland 6,95 euro), volgens de gegevens van 24-10.
4. **De rest van de pagina.** Het merkblok (reistijden 25, 15 en 20 minuten), de nieuwe balk "Afhalen in Borne" en "Melamine laten bezorgen", en dat het oude SEO-blok met de decorlijst onderaan weg is. Let op dat de kop van het ophaalblok "Alleen afhalen in de winkel" nog zo staat (V113 nee).

## De preview toont nog de oude collectiebeschrijving

De nieuwe collectiebeschrijving (body), de title en de meta staan niet in het thema maar in de collectie in Shopify. Die verander ik pas tegelijk met het live zetten van het thema, zodat bezoekers en Google niet een nieuwe tekst zien bij een oud thema of andersom. De preview combineert dus het nieuwe thema met de oude beschrijving. Door de wijziging in de hero komt de oude eerste alinea nu zichtbaar in beeld; dat is bewust niet vooraf aangepast. Op de live pagina verschijnt dus pas na de volgende stappen de nieuwe tekst.

## Stappen na Marks akkoord op de preview

1. Mark geeft "ja" op de preview (vorm van de intro, knoppen, winkelwagentest).
2. Thema 204095619336 publiceren. Dat kan niet via de Shopify-koppeling (themePublish is geblokkeerd), dus Mark of de hoofdsessie doet dat in Shopify admin onder Onlinewinkel, Thema's. Voor het publiceren een verse backup van het dan live thema in scripts/archief-themas/ zetten.
3. Direct erna, in dezelfde ronde: de nieuwe collectiebeschrijving, title en meta van de collectie Bunzlau zetten (voorstel van Content en On-page), plus het blog en /pages/serviezen zoals afgesproken. Vooraf de huidige waarden vastleggen voor terugdraaien.
4. Controle op de live pagina: https://tanterie.nl/collections/bunzlau en een Bunzlau-productpagina met niet-beschikbare variant (zichtbare tekst, knoppen, geen dubbele tekst, geen resten van het oude SEO-blok), Rich Results Test op een productpagina, en een nieuwe crawl van de collectie en enkele producten. Search Console: URL-inspectie op de collectiepagina en indexatie laten aanvragen.
5. Vastleggen in marketing/changelog.md: datum, URL's, wat veranderd is en waarom (bestanden, theme-id, nieuwe live thema-id, checksums). Dat doet de hoofdsessie, ik heb changelog.md en vragen-voor-mark.md in deze stap niet aangeraakt.
6. De themakopie bij terugdraaien: het vorige live thema (203153015048) blijft bestaan en kan direct weer gepubliceerd worden.

## Open punten, niet onderdeel van deze kopie

V115 (afhaaltijd 2 uur in de Shopify-locatie) en V116 (negatieve voorraad, waardoor "Op voorraad" kan verschijnen bij iets dat niet in de winkel ligt) blijven open. De Blond-pagina's hebben dezelfde teksten "Bestel nu" en "Bestellen" en zijn niet aangepast (alleen Bunzlau is gevraagd).
