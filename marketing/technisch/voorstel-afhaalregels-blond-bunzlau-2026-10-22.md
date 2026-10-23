# Voorstel: verzendregels op afhaal-merken Blond en Bunzlau

Datum: 2026-10-22. Rol: technisch SEO, tekst af te stemmen met On-page. Status: alleen voorstel. Er is niets gewijzigd in Shopify of het live thema en er is geen themakopie gemaakt (wacht op goedgekeurde tekst). Changelog niet aangeraakt. Bron: alleen-lezen pull van live thema #203153015048 en curl op live pagina's.

## 1. Bronnen

| Tekst | Bron | Hoe het verschijnt |
|---|---|---|
| "Snelle verzending: 1-2 werkdagen!" | `sections/header-group.json` regel 21, blok `announcement_dKqRTL` in sectie `header-announcements` | Themabewerker-instelling (JSON), renderfile `blocks/_announcement.liquid` regel 30 (`{{ block.settings.text }}`). Eén vaste tekst voor de hele site. |
| "Verzendkosten vanaf €4,50" | `sections/header-group.json` regel 34, blok `announcement_BxgCk9` | Idem. |
| "Tante Rie verzendt niet. Je haalt alles op in de winkel." | `sections/tr-product-blond.liquid` regel 604 en `sections/tr-product-bunzlau.liquid` regel 454 | Hardgecodeerd in het accordeon "Ophaalinformatie" van het producttemplate. |

De announcementbalk zit in `layout/theme.liquid` (regel 130-131, `{% sections 'header-group' %}`) en staat dus op elke pagina. Het is geen USP-balk per merk en geen snippet. De overige "Snelle verzending" in het thema (`sections/product-cro.liquid` regel 713 en `templates/product.cro.json` regel 28, "✓ Snelle verzending") is een andere tekst, zonder uitroepteken, en op de gecontroleerde pagina's niet aanwezig.

Het thema markeert "alleen afhalen" op één manier: `template.suffix` is `blond` of `bunzlau` (zo in `snippets/tr-product-schema.liquid` regel 35, goed voor `doesNotShip` in het productschema). Andere merken zijn niet als afhalen gemarkeerd.

## 2. Betrokken pagina's (met curl op live bevestigd)

- Announcementbalk ("Snelle verzending: 1-2 werkdagen!" en "Verzendkosten vanaf €4,50"): op alle gecontroleerde pagina's, dus ook op de homepage, /collections/blond, /collections/bunzlau, /collections/thee, /collections/accessoires, /collections/rice, /pages/blond-amsterdam-servies, /pages/theewinkel-borne-twente, /pages/zakelijk, en op productpagina's. Het is dus alleen fout op pagina's van afhaal-merken. Op thee, accessoires en Rice klopt de regel (behalve het uitroepteken).
- "Tante Rie verzendt niet": alleen op producten met template blond of bunzlau, bevestigd op /products/eb-pink-mug-0-35l-hearts (Blond), /products/boeren-mok-240-ml (Bunzlau) en /products/melamine-bord-wild-flowers-o-25-cm (Bunzlau-template). Niet op /products/beste-van-borne (thee).
- De pagina /pages/blond-amsterdam-servies heeft template-suffix `page` (gedeeld), dus is alleen te herkennen aan de handle.

## 3. Oorzaak

De announcementbalk is een enkele, site-brede themainstelling zonder context. De productzin is een vaste tekst die bedoeld was voor "Blond en Bunzlau", maar spreekt in de eerste persoon van Tante Rie in het algemeen en leest daardoor als een uitspraak over de hele winkel. Het uitroepteken in de balk schendt de schrijfregel.

## 4. Voorstel

### A. Announcementbalk op afhaal-pagina's

Op pagina's met template `blond` of `bunzlau` en op de pagina `blond-amsterdam-servies` wordt de verzendregel vervangen en de kostenregel vervangen door praktische winkelinformatie. Daardoor blijven er twee slides, zodat de slider en pijlen werken.

| | Voor | Na (afhaal-pagina's) |
|---|---|---|
| Blok 1 | Snelle verzending: 1-2 werkdagen! | Alleen afhalen in Borne |
| Blok 2 | Verzendkosten vanaf €4,50 | Bakkerssteeg 6 in Borne, dinsdag tot en met zaterdag 10:00 tot 17:00 |

Op alle andere pagina's blijft de balk gelijk, maar zonder uitroepteken: "Snelle verzending: 1-2 werkdagen". Dat is een wijziging in de themabewerker-instelling in `header-group.json` en geldt site-breed.

### B. Productzin Blond en Bunzlau

| | Voor | Na |
|---|---|---|
| Voorraad aanwezig (`available`) | Tante Rie verzendt niet. Je haalt alles op in de winkel. | Dit product versturen we niet. Je bestelt online en haalt het op in onze winkel in Borne. |
| Niet op voorraad (bestelverzoek) | idem | Dit product versturen we niet. Je stuurt een bestelverzoek en haalt het product daarna op in onze winkel in Borne. |

Reden voor de splitsing: op deze templates is alleen een product op voorraad online te bestellen (knop "In winkelwagen"). Alle andere producten lopen via een bestelformulier ("Stuur een bestelverzoek", knop "Verstuur verzoek"). "Je bestelt online" zou daar niet kloppen. De richtingtekst van het coördinatiebericht is dus aangehouden voor de voorraadsituatie.

Teksten zonder uitroeptekens en zonder em-dashes. Definitieve formulering: On-page.

## 5. Diff

Pad t.o.v. het live thema. Ook als losse file: `/Users/markvanwijk/Tante Rie SEO/marketing/technisch/voorstel-afhaalregels-blond-bunzlau-2026-10-22.diff`. Niet uitgevoerd.

```diff
diff -u a/blocks/_announcement.liquid b/blocks/_announcement.liquid
--- a/blocks/_announcement.liquid
+++ b/blocks/_announcement.liquid
@@ -4,6 +4,16 @@
 {%- assign plain_text = block_settings.text | strip_newlines | strip_html | strip -%}
 {%- assign block_index = section.blocks | find_index: 'id', block.id -%}
 
+{%- comment -%} Afhaal-pagina's (template blond of bunzlau, plus de Blond-servicepagina): geen verzendregels tonen. {%- endcomment -%}
+{%- if template.suffix == 'blond' or template.suffix == 'bunzlau' or page.handle == 'blond-amsterdam-servies' -%}
+  {%- assign _lower = plain_text | downcase -%}
+  {%- if _lower contains 'verzendkosten' -%}
+    {%- assign plain_text = 'Bakkerssteeg 6 in Borne, dinsdag tot en met zaterdag 10:00 tot 17:00' -%}
+  {%- elsif _lower contains 'verzending' -%}
+    {%- assign plain_text = 'Alleen afhalen in Borne' -%}
+  {%- endif -%}
+{%- endif -%}
+
 {%- unless plain_text == '' -%}
   <slideshow-slide
     ref="slides[]"
@@ -27,7 +37,7 @@
     aria-hidden="{% if block_index == 0 %}false{% else %}true{% endif %}"
   >
     <p class="announcement-bar__text">
-      {{ block.settings.text }}
+      {{ plain_text }}
     </p>
 
     {% if block_settings.link != blank %}
diff -u a/sections/header-group.json b/sections/header-group.json
--- a/sections/header-group.json
+++ b/sections/header-group.json
@@ -18,7 +18,7 @@
           "type": "_announcement",
           "name": "t:names.announcement",
           "settings": {
-            "text": "Snelle verzending: 1-2 werkdagen!",
+            "text": "Snelle verzending: 1-2 werkdagen",
             "link": "/collections/all",
             "font": "var(--font-subheading--family)",
             "font_size": "0.75rem",
diff -u a/sections/tr-product-blond.liquid b/sections/tr-product-blond.liquid
--- a/sections/tr-product-blond.liquid
+++ b/sections/tr-product-blond.liquid
@@ -601,7 +601,7 @@
           </button>
           <div class="trbap-accordion-body" role="region">
             <div class="trbap-accordion-body-inner">
-              <p><strong>Tante Rie verzendt niet.</strong> Je haalt alles op in de winkel.</p>
+              <p><strong>Dit product versturen we niet.</strong> {% if _available %}Je bestelt online en haalt het op in onze winkel in Borne.{% else %}Je stuurt een bestelverzoek en haalt het product daarna op in onze winkel in Borne.{% endif %}</p>
               <p><strong>Adres:</strong> Bakkerssteeg 6, 7622 GX Borne (Twente)</p>
               <p><strong>Openingstijden:</strong><br>
                 Dinsdag t/m zaterdag &nbsp;10:00 – 17:00 uur<br>
diff -u a/sections/tr-product-bunzlau.liquid b/sections/tr-product-bunzlau.liquid
--- a/sections/tr-product-bunzlau.liquid
+++ b/sections/tr-product-bunzlau.liquid
@@ -451,7 +451,7 @@
         <div class="trbzp-accordion-item">
           <button type="button" class="trbzp-accordion-trigger" aria-expanded="false" data-trbzp-acc>Ophaalinformatie<span class="trbzp-chevron">▾</span></button>
           <div class="trbzp-accordion-body"><div class="trbzp-accordion-body-inner">
-            <p><strong>Tante Rie verzendt niet.</strong> Je haalt alles op in de winkel.</p>
+            <p><strong>Dit product versturen we niet.</strong> {% if _available %}Je bestelt online en haalt het op in onze winkel in Borne.{% else %}Je stuurt een bestelverzoek en haalt het product daarna op in onze winkel in Borne.{% endif %}</p>
             <p><strong>Adres:</strong> Bakkerssteeg 6, 7622 GX Borne</p>
             <p><strong>Openingstijden:</strong><br>Di t/m za 10:00–17:00<br>Ma &amp; zo gesloten</p>
             {%- unless _available -%}<p><strong>Op bestelling:</strong> Altijd te bestellen. Na je verzoek spreken we een ophaaldatum af.</p>{%- endunless -%}
```

Technische noot: `_announcement.liquid` gebruikt nu `plain_text` (zonder HTML) in plaats van `block.settings.text`. De huidige blokken bevatten geen opmaak, dus er verandert niets voor de andere pagina's.

## 6. Valkuilen en beslispunten voor Mark

1. Melamine van Bunzlau: collectie Bunzlau zegt "Melamine artikelen kun je online bestellen en laten bezorgen in Nederland", maar de melamine-producten gebruiken het template bunzlau en tonen dus "Alleen afhalen" en `doesNotShip` in het schema (bijvoorbeeld /products/melamine-bord-wild-flowers-o-25-cm). Een van beide is fout. Wordt melamine verzonden, dan moet die producten een ander template krijgen (of de afhaalregels vervallen voor melamine). Dat is een besluit over assortiment en kan ik niet uit het thema halen.
2. Tekst blok 2 ("Bakkerssteeg 6 in Borne, dinsdag tot en met zaterdag 10:00 tot 17:00") en de productzin: akkoord, of afstemmen met On-page?
3. Pagina `blond-amsterdam-servies` meenemen in de uitzondering (de handle is hardgecodeerd), of alleen de collectie- en producttemplates? Andere artikelen over Blond of Bunzlau op een gedeeld paginatemplate worden niet herkend.
4. Het uitroepteken in "Snelle verzending: 1-2 werkdagen!" is een site-brede tekstwijziging. Akkoord dat die los van het afhaalverhaal meegaat?
5. Verzendinformatie die elders hardgecodeerd staat (USP-teksten op Blond-collectie en -producten: "Alleen afhalen, geen verzending" is correct) is niet gewijzigd.

Na akkoord: themakopie maken (`shopify theme duplicate`), de 4 bestanden pushen, preview controleren met curl op Blond, Bunzlau, thee en accessoires (afhaal-pagina's tonen de nieuwe regels, andere pagina's de oude zonder uitroepteken), dan pas publiceren en changelog.


---

## 7. Uitvoering op themakopie (update 22-10, na akkoord V3 en V4)

Antwoorden van Mark verwerkt: V4 ja (teksten goedgekeurd), V3 melamine kan verzonden worden. V5 (Blond-gidspagina) en V6 (uitroepteken) zijn nog open en zijn dus niet gebouwd: de pagina blond-amsterdam-servies zit niet in de uitzondering en "Snelle verzending: 1-2 werkdagen!" op de andere pagina's is ongewijzigd. Rubriek 4 en 5 hierboven zijn daarmee op deze twee punten achterhaald.

Er is niets naar het live thema gepusht (#203153015048 onveranderd).

- Themakopie: "afhaalregels 2026-10-22", theme-id **203983913224**, ongepubliceerd. Eerst met `shopify theme list` gecontroleerd dat er nog geen kopie bestond. Gepusht met `--only`: `blocks/_announcement.liquid`, `sections/tr-product-blond.liquid`, `sections/tr-product-bunzlau.liquid`.
- Voorwaarde voor de balk: alleen `template.suffix` blond of bunzlau (collectie- en producttemplate).
- Preview-links (cookie nodig, dus in de browser openen):
  - https://tanterie.nl/collections/blond?preview_theme_id=203983913224
  - https://tanterie.nl/collections/bunzlau?preview_theme_id=203983913224
  - https://tanterie.nl/products/thank-you?preview_theme_id=203983913224 (Blond, op voorraad)
  - https://tanterie.nl/products/forever-young?preview_theme_id=203983913224 (Blond, niet op voorraad)
  - https://tanterie.nl/products/boeren-mok-240-ml?preview_theme_id=203983913224 (Bunzlau, op voorraad)
  - https://tanterie.nl/products/bord-diep-o-21-cm?preview_theme_id=203983913224 (Bunzlau, niet op voorraad)
  - https://tanterie.nl/products/beste-van-borne?preview_theme_id=203983913224 (thee, ongewijzigd)
  - https://tanterie.nl/?preview_theme_id=203983913224 (homepage, ongewijzigd)

### Diff (4 hunks, 3 bestanden)

Ook als losse file: `/Users/markvanwijk/Tante Rie SEO/marketing/technisch/afhaalregels-2026-10-22.diff`.

```diff
diff -u a/blocks/_announcement.liquid b/blocks/_announcement.liquid
--- a/blocks/_announcement.liquid
+++ b/blocks/_announcement.liquid
@@ -4,6 +4,16 @@
 {%- assign plain_text = block_settings.text | strip_newlines | strip_html | strip -%}
 {%- assign block_index = section.blocks | find_index: 'id', block.id -%}
 
+{%- comment -%} Afhaal-merken (template blond of bunzlau): geen verzendregels tonen. {%- endcomment -%}
+{%- if template.suffix == 'blond' or template.suffix == 'bunzlau' -%}
+  {%- assign _lower = plain_text | downcase -%}
+  {%- if _lower contains 'verzendkosten' -%}
+    {%- assign plain_text = 'Bakkerssteeg 6 in Borne, dinsdag tot en met zaterdag 10:00 tot 17:00' -%}
+  {%- elsif _lower contains 'verzending' -%}
+    {%- assign plain_text = 'Alleen afhalen in Borne' -%}
+  {%- endif -%}
+{%- endif -%}
+
 {%- unless plain_text == '' -%}
   <slideshow-slide
     ref="slides[]"
@@ -27,7 +37,7 @@
     aria-hidden="{% if block_index == 0 %}false{% else %}true{% endif %}"
   >
     <p class="announcement-bar__text">
-      {{ block.settings.text }}
+      {{ plain_text }}
     </p>
 
     {% if block_settings.link != blank %}
diff -u a/sections/tr-product-blond.liquid b/sections/tr-product-blond.liquid
--- a/sections/tr-product-blond.liquid
+++ b/sections/tr-product-blond.liquid
@@ -601,7 +601,7 @@
           </button>
           <div class="trbap-accordion-body" role="region">
             <div class="trbap-accordion-body-inner">
-              <p><strong>Tante Rie verzendt niet.</strong> Je haalt alles op in de winkel.</p>
+              <p><strong>Dit product versturen we niet.</strong> {% if _available %}Je bestelt online en haalt het op in onze winkel in Borne.{% else %}Je stuurt een bestelverzoek en haalt het product daarna op in onze winkel in Borne.{% endif %}</p>
               <p><strong>Adres:</strong> Bakkerssteeg 6, 7622 GX Borne (Twente)</p>
               <p><strong>Openingstijden:</strong><br>
                 Dinsdag t/m zaterdag &nbsp;10:00 – 17:00 uur<br>
diff -u a/sections/tr-product-bunzlau.liquid b/sections/tr-product-bunzlau.liquid
--- a/sections/tr-product-bunzlau.liquid
+++ b/sections/tr-product-bunzlau.liquid
@@ -451,7 +451,7 @@
         <div class="trbzp-accordion-item">
           <button type="button" class="trbzp-accordion-trigger" aria-expanded="false" data-trbzp-acc>Ophaalinformatie<span class="trbzp-chevron">▾</span></button>
           <div class="trbzp-accordion-body"><div class="trbzp-accordion-body-inner">
-            <p><strong>Tante Rie verzendt niet.</strong> Je haalt alles op in de winkel.</p>
+            <p><strong>Dit product versturen we niet.</strong> {% if _available %}Je bestelt online en haalt het op in onze winkel in Borne.{% else %}Je stuurt een bestelverzoek en haalt het product daarna op in onze winkel in Borne.{% endif %}</p>
             <p><strong>Adres:</strong> Bakkerssteeg 6, 7622 GX Borne</p>
             <p><strong>Openingstijden:</strong><br>Di t/m za 10:00–17:00<br>Ma &amp; zo gesloten</p>
             {%- unless _available -%}<p><strong>Op bestelling:</strong> Altijd te bestellen. Na je verzoek spreken we een ophaaldatum af.</p>{%- endunless -%}
```

### Controleresultaat (curl, preview tegen live)

| Pagina | Balk op preview | Productzin op preview | JSON-LD | Liquid-fouten |
|---|---|---|---|---|
| Blond met voorraad (thank-you) | Alleen afhalen in Borne / Bakkerssteeg 6 in Borne, dinsdag tot en met zaterdag 10:00 tot 17:00 | Dit product versturen we niet. Je bestelt online en haalt het op in onze winkel in Borne. | 4 blokken geldig | geen |
| Blond zonder voorraad (forever-young) | idem | Dit product versturen we niet. Je stuurt een bestelverzoek en haalt het product daarna op in onze winkel in Borne. | 4 geldig | geen |
| Bunzlau met voorraad (boeren-mok-240-ml) | idem | zoals Blond met voorraad | 4 geldig | geen |
| Bunzlau zonder voorraad (bord-diep-o-21-cm) | idem | zoals Blond zonder voorraad | 4 geldig | geen |
| /collections/blond | idem | n.v.t. | 4 geldig | geen |
| /collections/bunzlau | idem | n.v.t. | 4 geldig | geen |
| Thee (beste-van-borne) | ongewijzigd: Snelle verzending: 1-2 werkdagen! / Verzendkosten vanaf €4,50 | n.v.t. | 5 geldig | geen |
| Homepage | ongewijzigd | n.v.t. | 5 geldig | geen |

Op live staan op dezelfde Blond- en Bunzlau-pagina's nog de oude teksten (balk met verzending en "Tante Rie verzendt niet"). Thee en homepage verschillen niet van live, afgezien van de versienummers van thema-assets in de URL's (t/39 tegen t/43). De Rich Results Test en een nieuwe crawl volgen na publicatie.

Let op: de bestandsnaam van dit voorstel hoort bij het eerdere voorstel. Deze uitvoering staat alleen in rubriek 7.

## 8. Melamine (V3 en V37): voorstel, nog niets gewijzigd

Besluit V3: melamine kan verzonden worden. V37 (akkoord om door te voeren) is nog open. Er is aan de producten niets veranderd.

Probleem: alle onderstaande producten hebben template `bunzlau`. Daardoor tonen ze "Alleen afhalen", het bestelformulier voor niet-voorraad en `doesNotShip` in het schema. Dat spreekt de collectietekst en V3 tegen.

Voorstel: templateSuffix leegmaken, zodat ze het standaard producttemplate (`product.json`, sectie tr-product-redesign) krijgen. Gecontroleerd op de preview met een product op dat template (theezeef-met-uitlekschaaltje-rvs): het productschema heeft dan `shippingRate` en geen `doesNotShip`, en er staat geen "Alleen afhalen". De afhaalregels uit rubriek 7 raken deze producten dan niet meer, omdat die op `template.suffix` blond of bunzlau werken. Na de templatewissel tonen ze dus de normale balk met verzending en geen afhaalzin. De kopie bevat de wijziging van de producten niet, want template-instellingen zitten op het product (live data), niet in het thema.

Online gepubliceerde Bunzlau-melamine met template bunzlau (7 stuks, allemaal vendor Bunzlau Castle, gepubliceerd juni 2026):

| Handle | Product-ID | Voorraad | Template nu | Template voorstel |
|---|---|---|---|---|
| melamine-bord-wild-flowers-o-25-cm | 12017686184200 | 6 | bunzlau | standaard (leeg) |
| melamine-bord-dragonfly-garden-o-25-cm | 12017690444040 | 1 | bunzlau | standaard (leeg) |
| melamine-bord-fleur-fountain-o-25-cm | 12017690476808 | 5 | bunzlau | standaard (leeg) |
| melamine-bord-blooming-o-25-cm | 12017716461832 | 3 | bunzlau | standaard (leeg) |
| melamine-kom-wild-flowers-o-15-cm | 12017731141896 | 0 | bunzlau | standaard (leeg) |
| melamine-kom-fleur-fountain-o-15-cm | 12017731174664 | -2 | bunzlau | standaard (leeg) |
| melamine-beker-1 | 12038206816520 | 10 | bunzlau | standaard (leeg) |

Verder met template bunzlau maar niet online gepubliceerd (alleen kassa, niet aanraken): 2192-ricebowl-small, 1986-ricebowl-hoog, melamine-schaaltje, melamine-bord (actief); 2238-ricebowl-groot en melamine-beker (concept).

Aandachtspunten:
- Productvoorraad: de kom Wild Flowers (0) en kom Fleur Fountain (-2) hebben geen positieve voorraad. Op het standaardtemplate verschijnen ze dan als uitverkocht en niet meer als bestelverzoek. Dat is een keuze voor Mark: voorraad aanvullen of ze offline halen.
- Melamine Bord Fleur Fountain heeft productType "Keramiek" in plaats van "Melamine". Klopt waarschijnlijk niet; on-page of Mark kan dat rechtzetten.
- Op /collections/bunzlau staat de collectiesectie nog met de banner "Alleen afhalen in Borne" boven alle producten, inclusief melamine. Die tekst en de collectietekst moeten met On-page worden afgestemd, buiten deze opdracht.
- Het verzendprofiel moet deze producten daadwerkelijk toelaten (gewicht en tarief). Dat is nog niet gecontroleerd en hoort bij V37.
- Doorvoeren kan met een productUpdate (templateSuffix leeg) per product, met backup van de huidige waarden. Wacht op akkoord op V37.

## 9. Correctie op de themakopie (22-10): verborgen tekst en link van de balk

Fout gevonden door de coördinator: de zichtbare tekst was goed, maar de link van slide 1 bevatte nog de visually-hidden tekst "Snelle verzending: 1-2 werkdagen!" en wees naar /collections/all, zodat schermlezers de oude verzendbelofte voorlazen.

Aanpassing in `blocks/_announcement.liquid` (alleen in kopie 203983913224, niets naar live): de visually-hidden tekst gebruikt nu dezelfde `plain_text` als de zichtbare tekst, en op template blond en bunzlau wijst een slide die een link heeft naar /pages/theewinkel-borne-twente. Slide 2 had geen link en heeft er nog steeds geen. De bijgewerkte diff staat in `afhaalregels-2026-10-22.diff` (nu 4 hunks in 3 bestanden, inclusief `_link`).

Controle met curl op de preview (thank-you, forever-young, boeren-mok-240-ml, bord-diep-o-21-cm, /collections/blond, /collections/bunzlau): "Snelle verzending" en "Verzendkosten vanaf" komen nergens meer voor in de HTML, ook niet verborgen. Slide 1 heeft zichtbare en verborgen tekst "Alleen afhalen in Borne" en link /pages/theewinkel-borne-twente. Slide 2 heeft het adres met openingstijden en geen link. JSON-LD geldig, geen Liquid-fouten. Thee en homepage tonen nog de oude balk en link (/collections/all), gelijk aan live. Let op: na een push duurt het even voordat de preview alles toont; de eerste controle toonde voor drie pagina's nog de oude versie.
