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

Er zijn twee bestanden gewijzigd en niets anders.

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

## Preview-URL's

| Wat | URL |
|---|---|
| Collectie Bunzlau | https://tanterie.nl/collections/bunzlau?preview_theme_id=204095619336 |
| Productpagina met niet-beschikbare variant (Boeren mok 240 ml, variant Blue Eyes is niet beschikbaar) | https://tanterie.nl/products/boeren-mok-240-ml?variant=57953071857928&preview_theme_id=204095619336 |
| Productpagina met beschikbare variant, voor de winkelwagentest (zelfde product, variant Lace) | https://tanterie.nl/products/boeren-mok-240-ml?variant=57953071923464&preview_theme_id=204095619336 |
| Melamine voor de gemengde winkelwagen | https://tanterie.nl/products/melamine-kom-wild-flowers-o-15-cm?preview_theme_id=204095619336 |

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
