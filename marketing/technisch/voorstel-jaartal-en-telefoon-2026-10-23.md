# Voorstel: openingsjaar 2014 (V13) en telefoon op de contactpagina (V77d)

Datum: 23-10-2026. Rol: technisch SEO-specialist. Status: alleen lezen en voorstel. Niets live gewijzigd, geen themakopie gemaakt, niets gecommit. Mark gaf op 23-10 akkoord op het principe (V13: 2014, eigenaarsnaam niet beantwoord; V77d: akkoord). Dit document is het voor-en-na dat hij nog kan nalopen.

## Wat ik wel en niet kon lezen

- Wel gelezen: de Shopify-koppeling (Admin API, lezen) voor het live thema 203153015048 ("Agent-ready koppen 2026-10-09", rol MAIN): alle thema-bestanden met eigen inhoud (templates, tr-sections, relevante snippets, layout, config, locales nl en en), alle pagina's incl. SEO-velden, 11 artikelen, 45 collecties, shopmetafields en een productzoekactie op "2024".
- Niet gelezen: de openbare site. https://tanterie.nl en https://tanterie.nl/llms.txt gaven vanuit deze sessie een proxyfout (403 op de tunnel, in WebFetch "ENOTFOUND"). De gerenderde pagina en de live llms.txt zijn dus niet getoetst. De bron van llms.txt is wel gevonden: `templates/llms.txt.liquid` in het live thema; die wordt door Shopify op /llms.txt gerenderd. Controle van de live uitvoer volgt na publicatie.
- Niet gelezen: niet-live themes (o.a. "SEO-audit-fixes 2026-09-25", #202361864456) en de ongeveer 700 productbeschrijvingen volledig; een productzoekactie op "2024" gaf 14 treffers, maar dat zijn producten met 2024 als modelcode of seizoensnaam (o.a. halloween, sint), geen openingsjaar. Dat is een steekproef, geen volledige controle van alle productteksten.

## Deel 1. V13: openingsjaar 2014

### Gevonden plekken

Belangrijk: de site noemt niet overal 2024. De homepage noemt 2012. Dat is een derde jaartal naast 2014 (Bedrijfsprofiel, 4 april 2014) en 2024.

| # | Bestand of resource | Wat er staat | Live zichtbaar? |
|---|---|---|---|
| 1 | `templates/llms.txt.liquid`, regel 9 | "De winkel opende in 2024 in het centrum van Borne" | Ja, op /llms.txt (niet getoetst, zie boven) |
| 2 | `templates/index.json`, `about_title` | "Onze theewinkel in Borne, sinds 2012" | Ja, kop op de homepage |
| 3 | `templates/index.json`, `about_text_1` | "Tante Rie opende in 2012 haar deuren in het centrum van Borne." | Ja, eerste alinea op de homepage |
| 4 | `sections/tr-homepage-redesign.liquid`, regel 370 | standaardwaarde "sinds 2024" | Nee, wordt overschreven door #2; wel een valstrik als de instelling ooit wordt leeggemaakt |
| 5 | `sections/tr-homepage-redesign.liquid`, regel 372 | standaardwaarde "opende in 2024" | Nee, idem door #3 |
| 6 | `sections/tr-homepage-redesign.liquid`, regel 454 | schema-default "sinds 2024" voor de themaeditor | Nee, alleen als nieuwe sectie wordt toegevoegd |

Structured data: nergens staat `foundingDate`, dus er staat ook geen verkeerd jaar in de JSON-LD. Gecontroleerd: `layout/theme.liquid` (WebSite en LocalBusiness), `snippets/schema-structured-data.liquid`, `snippets/tr-product-schema.liquid`, `snippets/tr-offer-policies.liquid` en het LocalBusiness-blok in `sections/tr-page-lokaal.liquid`. Het veld toevoegen is optioneel (zie 1.4).

Schoon bevonden (geen openingsjaar, geen "sinds"): de lokaalpagina (sinds de herschrijving van 23-10 zonder jaartal), alle pagina's in Shopify (Over ons en Over Tante Rie noemen geen jaar), de 11 artikelen (alleen "sinds 1870" over een Sri Lankaanse plantage), de 45 collecties (alleen Rice "opgericht in 1998", dat is het merk), footer, header, announcement-bar, settings_data, de SEO-titels en -omschrijvingen van de pagina's en de shopbeschrijving.

### Voor en na per plek

**1. `templates/llms.txt.liquid`, regel 9**

Voor: `De winkel opende in 2024 in het centrum van Borne en is vernoemd naar Rie Badart, de moeder van de oprichtster. Eigenaar is Nikkie.`
Na: `De winkel opende in 2014 in het centrum van Borne en is vernoemd naar Rie Badart, de moeder van de oprichtster. Eigenaar is Nikkie.`

Alleen het jaartal verandert. De zin "Eigenaar is Nikkie" laat ik staan; zie vraag 2 hieronder.

**2. `templates/index.json`, `about_title`**

Voor: `Onze theewinkel in Borne, sinds 2012`
Na: `Onze theewinkel in Borne, sinds 2014`

**3. `templates/index.json`, `about_text_1`**

Voor: `Tante Rie opende in 2012 haar deuren in het centrum van Borne. De winkel draagt de naam van Rie Badart, de moeder van de oprichtster: een vrouw die altijd met een kopje thee klaarzat als je binnenkwam.`
Na: `Tante Rie opende in 2014 haar deuren in het centrum van Borne. De winkel draagt de naam van Rie Badart, de moeder van de oprichtster: een vrouw die altijd met een kopje thee klaarzat als je binnenkwam.`

**4 tot en met 6. `sections/tr-homepage-redesign.liquid`**

Regel 370 en 454: `sinds 2024` wordt `sinds 2014`. Regel 372: `opende in 2024 haar deuren` wordt `opende in 2014 haar deuren`. Zo blijven de standaardwaarden gelijk aan de live instelling.

Diff voor 1 tot en met 6: `marketing/technisch/voorstel-openingsjaar-2014-2026-10-23.diff` (gemaakt van de bestandsinhoud van het live thema van vandaag, 23-10, 21:30 ongeveer; elk oud fragment komt exact één keer voor).

### 1.4 Optioneel: foundingDate in de LocalBusiness-markup

Voor: `"telephone": "+31638291189", "email": "webshop@tanterie.nl", "priceRange": ...` in `layout/theme.liquid` (regel 82 e.v.).
Na: tussen `email` en `priceRange` de regel `"foundingDate": "2014",`.

Alleen het jaar, geen datum, omdat Mark alleen het jaar bevestigde (het Bedrijfsprofiel noemt 4 april 2014). Het is een toevoeging, geen correctie, en geen vereiste voor Google. Ik raad het aan omdat het de feiten in markup, profiel en tekst op één lijn zet, maar het hoeft niet mee. Diff: `marketing/technisch/voorstel-openingsjaar-foundingdate-optioneel-2026-10-23.diff`.

### Niet gewijzigd

Geen eigenaarsnaam toegevoegd of verwijderd (V13 onbeantwoord). Bestaande vermeldingen van "Nikkie" blijven staan (homepage `about_text_2`, llms.txt).

### Uitvoering en controle (na akkoord)

1. Themakopie van 203153015048 (`shopify theme duplicate`), de drie bestanden in de kopie wijzigen, diff tonen, Mark akkoord.
2. Publiceren, daarna controleren: `curl -s https://tanterie.nl/llms.txt | grep -n "opende in"`, homepage-HTML op "sinds 2014", en `grep -c 2024` / `grep -c 2012` op beide moeten 0 geven. Voor een eventuele foundingDate daarna de Rich Results Test op de homepage.
3. Changelog door de hoofdsessie: drie regels (llms.txt, homepage-instellingen, sectiedefaults).

## Deel 2. V77d: telefoonnummer op de contactpagina

### Wat de contactpagina rendert

- URL: https://tanterie.nl/pages/contact (Shopify-pagina `contact`, id gid://shopify/Page/157979967752, template-suffix `contact`, laatst bijgewerkt 25-09-2026). De echte URL is dus /pages/contact.
- Template: `templates/page.contact.json`. Dat gebruikt sectie `main-page` met een tekstblok `title` (`<h1>{{ closest.page.title }}</h1>`) en een tekstblok `content` (`{{ closest.page.content }}`), gevolgd door een sectie met het contactformulier (`contact-form`).
- De paginatekst zelf is dus de **body van de Shopify-pagina**, niet thema-code. De wijziging is een tekstwijziging in Shopify-beheer onder Online winkel, Pagina's, Contact (of via `pageUpdate`). Er is geen themawijziging nodig, dus ook geen themakopie.
- Het nummer staat nu wel in de footer (custom_liquid in `sections/footer-group.json`), in de LocalBusiness-markup en in de body van de Blond-pagina, maar niet in de contactpagina zelf. Dat bevestigt de bevinding in de autoriteit-brief, paragraaf 4.
- De SEO-omschrijving van de pagina zegt al "bel ons" ("Mail naar webshop@tanterie.nl, bel ons of kom langs ..."), maar op de pagina staat geen nummer. Met de toevoeging klopt dat weer.

### Huidige tekst (body, volledig bij het onderdeel dat verandert)

```html
<p>Je kunt ons bereiken via e-mail of even langskomen in <a href="https://www.tanterie.nl" title="winkel in Borne">onze winkel</a> in het hart van Borne.</p>
<h4>📍 Bezoekadres</h4>
<p><strong>Tante Rie</strong><br>Bakkerssteeg 6<br>7622 GX Borne<br>Nederland</p>
<h4>✉️ E-mail</h4>
<p>webshop@tanterie.nl</p>
<h4>🕒 Openingstijden winkel</h4>
<p><strong>Dinsdag t/m zaterdag:</strong> 10:00 – 17:00<br><strong>Maandag en zondag:</strong> gesloten</p>
```

De openingstijden staan er al in (di t/m za 10:00 – 17:00, maandag en zondag gesloten). Die hoeven dus niet opnieuw. Alleen het nummer ontbreekt.

### Voorstel (nieuwe tekst)

```html
<p>Je kunt ons bereiken via e-mail, telefonisch of door even langs te komen in <a href="https://www.tanterie.nl" title="winkel in Borne">onze winkel</a> in het hart van Borne.</p>
<h4>📍 Bezoekadres</h4>
<p><strong>Tante Rie</strong><br>Bakkerssteeg 6<br>7622 GX Borne<br>Nederland</p>
<h4>✉️ E-mail</h4>
<p>webshop@tanterie.nl</p>
<h4>📞 Telefoon</h4>
<p>Bel ons gerust op <a href="tel:+31638291189">06 38 29 11 89</a>, van dinsdag tot en met zaterdag tussen 10:00 en 17:00 uur.</p>
<h4>🕒 Openingstijden winkel</h4>
```

Wat verandert: de inleidende zin noemt telefoon, en er komt één kop met één zin bij, in dezelfde opbouw als de bestaande blokken (kop met pictogram, daaronder een korte alinea). De rest van de body blijft ongewijzigd. Schrijfwijze van het nummer is dezelfde als op de Blond-pagina en de lokaalpagina: zichtbaar `06 38 29 11 89`, link `tel:+31638291189`. Geen em-dash, geen opsomming, geen uitroepteken.

Diff: `marketing/technisch/voorstel-telefoon-contactpagina-2026-10-23.diff`.

### Opmerkingen bij de contactpagina

1. De pictogrammen (📍 ✉️ 🕒) staan al in de bestaande koppen. Ik sluit daarop aan met 📞. Wil Mark ze liever niet, dan kan het pictogram bij alle vier de koppen weg; dat is een aparte, kleine wijziging.
2. Het e-mailadres is geen klikbare link. Een `mailto:` is een kleine, losse verbetering voor mobiel; niet meegenomen omdat het niet gevraagd is.
3. De link "onze winkel" gaat naar de homepage (`https://www.tanterie.nl`, met www, redirect werkt). Beter is `/pages/theewinkel-borne-twente`, passend bij de lokale-SEO-prioriteit. Ook dit is niet meegenomen; ik leg het voor als aanvullende suggestie.
4. De pagina is nog niet aangepast. Na akkoord: via Shopify-beheer of `pageUpdate`, daarna controleren dat het nummer en de `tel:`-link in de HTML staan (`curl -s https://tanterie.nl/pages/contact | grep -n "tel:"`) en een mobiele weergave controleren.

## Vragen voor Mark (niet in vragen-voor-mark.md gezet)

1. Homepage zegt 2012, niet 2024. Klopt het dat ook dit 2014 moet worden? Mogelijk is 2012 bewust (bijvoorbeeld het jaar waarin de oprichtster begon voordat de winkel in de Bakkerssteeg opende, of een eerdere eigenaar). Zonder antwoord neem ik 2014 over zoals bij V13 gevraagd, maar de homepage is het enige geval waar het jaartal niet "2024" was.
2. Eigenaar: llms.txt en de homepage noemen "Eigenaar Nikkie", de privacypagina noemt "mevr. A. Kamp, eigenaar van Tante Rie" en de pagina Over ons spreekt van "nieuwe eigenaar". Dit is V13-deel 2 (onbeantwoord); ik pas niets aan en voeg geen naam toe. Het is wel een inconsistentie die Google en AI-assistenten kunnen oppikken.
3. foundingDate in de markup (optioneel, zie 1.4): wel of niet meenemen?
4. De pictogrammen en de link "onze winkel" op de contactpagina: laten zoals ze zijn, of meenemen in deze ronde?
