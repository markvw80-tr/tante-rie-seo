# Voorstel: melamine-sjabloon en Rice (V37)

Datum: 2026-10-22. Rol: technisch SEO. Status: gebouwd in een ongepubliceerde themakopie. Er is niets naar het live thema gepusht, de templateSuffix van de producten is niet gewijzigd en changelog.md is niet aangeraakt. Basis: live thema #203153015048 na de push van de afhaalregels (gecontroleerd dat `_announcement.liquid` live de nieuwe link bevat).

## 1. Antwoord op de vraag van Mark: is er iets voor Rice?

Kort: Rice heeft al een eigen, verzendbaar sjabloon en heeft geen afhaal- of verzendlogica nodig. Rice-melamine staat nog niet online.

- Template: Rice-producten gebruiken template `rice` (sectie `tr-product-rice`, brand Rice). Gecontroleerd op /products/rice-a.
- Verzending: ja. Het schema heeft `shippingRate` en geen `doesNotShip`, de pagina toont geen "alleen afhalen" of "verzendt niet", en de balk is de normale. Het accordeon "Verzending & retour" zegt "Bestellingen worden dezelfde werkdag verwerkt", terwijl balk en schema 1 tot 2 werkdagen zeggen. Dat is een tekstverschil dat On-page moet rechtzetten, buiten dit voorstel.
- Rice-melamine: er zijn ruim 20 Rice-melamineproducten in Shopify (middelgrote bekers met template leeg, drie kommen met template bunzlau, bestek en een grote beker met template leeg), maar geen enkel daarvan is gepubliceerd op de Online winkel (`publishedAt` leeg). Het zijn dus kassaproducten. Een 404 daarop is correct (zie CLAUDE.md). De drie Rice-kommen (2192-ricebowl-small, 1986-ricebowl-hoog, 2238-ricebowl-groot) hebben wel template bunzlau en zouden bij publicatie ten onrechte "alleen afhalen" tonen. Advies: nooit publiceren zonder eerst template leeg of `bunzlau-melamine`, en niet zonder overleg met Mark.
- Advies: geen nieuw Rice-sjabloon. Het sjabloon `bunzlau-melamine` is bewust merkneutraal gehouden in de logica (alleen de teksten zeggen Bunzlau Castle).

## 2. Melamine-sjabloon

### Themakopie
- Naam: "melamine-sjabloon 2026-10-22", theme-id **203984994568**, ongepubliceerd, gemaakt van live nadat de afhaalregels live stonden.
- Nieuwe bestanden: `sections/tr-product-bunzlau-melamine.liquid` en `templates/product.bunzlau-melamine.json`. Aangepast: `snippets/schema-structured-data.liquid` (suffix `bunzlau-melamine` toegevoegd aan de lijst met secties die zelf het schema renderen, anders komt het schema dubbel). De eerste push gaf een fout (naam sectie langer dan 25 tekens); die is aangepast en opnieuw gepusht zonder fouten.
- De sectie is een kopie van `tr-product-bunzlau` (zelfde opmaak en klassen) met deze wijzigingen:
  - geen afhaalbalk en geen "Alleen afhalen in Borne" bij de prijs;
  - geen productzin "versturen we niet" en geen bestelverzoek-formulier;
  - beschikbaarheid: "Op voorraad, verzonden binnen 1 tot 2 werkdagen", anders "Uitverkocht, tijdelijk niet leverbaar";
  - koopknop "In winkelwagen" zoals bij andere verzendbare producten, en "Uitverkocht" (uitgeschakeld) zonder voorraad;
  - specificaties: materiaal Melamine, geen aardewerk-, vaatwasser-, oven- en magnetronregels en geen "Gemaakt in Polen" (voor melamine niet vastgelegd);
  - accordeon "Ophaalinformatie" vervangen door "Verzending en retour", met de regel over ophalen in de winkel alleen als het product op voorraad is;
  - USP's: verzending in Nederland en uniek decor, in plaats van "Alleen in Borne" en "Handgemaakt".
- Schema: omdat `template.suffix` `bunzlau-melamine` is, valt het niet onder `pickup_only` in `snippets/tr-product-schema.liquid`. Het Product-blok krijgt dus `shippingDetails` en `hasMerchantReturnPolicy`.

### Preview-links (cookie nodig, dus in de browser openen)
Tijdelijke weergave met `?view=bunzlau-melamine`, zonder de productdata te wijzigen:
- https://tanterie.nl/products/melamine-bord-wild-flowers-o-25-cm?view=bunzlau-melamine&preview_theme_id=203984994568 (op voorraad)
- https://tanterie.nl/products/melamine-beker-1?view=bunzlau-melamine&preview_theme_id=203984994568 (op voorraad)
- https://tanterie.nl/products/melamine-kom-wild-flowers-o-15-cm?view=bunzlau-melamine&preview_theme_id=203984994568 (voorraad 0)
- https://tanterie.nl/products/melamine-kom-fleur-fountain-o-15-cm?view=bunzlau-melamine&preview_theme_id=203984994568 (voorraad -2)
- Zonder `view` (huidig gedrag, ongewijzigd): https://tanterie.nl/products/melamine-bord-wild-flowers-o-25-cm?preview_theme_id=203984994568

### Controleresultaat (curl)
| Pagina | Resultaat |
|---|---|
| bord Wild Flowers, beker (met voorraad, view) | Knop "In winkelwagen" met `data-tr-atc`; schema met `shippingRate` 4,50 euro, `deliveryTime` 1 tot 2 plus 1 dag en retourbeleid 14 dagen; geen `doesNotShip`; geen "Alleen afhalen", "versturen we niet" of bestelverzoek; 1 Product-blok; 4 geldige JSON-LD-blokken; geen Liquid-fouten |
| kom Wild Flowers (0) en kom Fleur Fountain (-2), view | Knop "Uitverkocht", uitgeschakeld; verder gelijk aan hierboven |
| bord zonder view (huidig template) | Ongewijzigd: `doesNotShip`, "Alleen afhalen" en bestelverzoek aanwezig |
| Bunzlau (boeren-mok), Blond (thank-you) | Ongewijzigd met de nieuwe afhaalregels; geldig JSON-LD |
| Thee (beste-van-borne), Rice (rice-a), homepage | Ongewijzigd; schema met `shippingRate`, geen afhaaltekst; geldig JSON-LD |

Let op: de balk bovenaan de melamine-pagina blijft de normale ("Snelle verzending: 1-2 werkdagen!" en "Verzendkosten vanaf €4,50"), omdat die alleen op template blond en bunzlau wordt vervangen. Dat is gewenst.

### Diff
Volledige diff (3 bestanden): `/Users/markvanwijk/Tante Rie SEO/marketing/technisch/melamine-sjabloon-2026-10-22.diff`. Het verschil tussen de nieuwe sectie en `tr-product-bunzlau` staat in `/Users/markvanwijk/Tante Rie SEO/marketing/technisch/melamine-sjabloon-verschil-met-bunzlau-2026-10-22.diff` en hieronder.

Template (nieuw):
```json
{ "sections": { "trbzp_melamine": { "type": "tr-product-bunzlau-melamine", "settings": {} } }, "order": ["trbzp_melamine"] }
```

Schemalijst:
```diff
diff -u a/snippets/schema-structured-data.liquid b/snippets/schema-structured-data.liquid
--- a/snippets/schema-structured-data.liquid
+++ b/snippets/schema-structured-data.liquid
@@ -11,7 +11,7 @@
 
 {%- assign has_own_product_schema = false -%}
 {%- assign has_own_breadcrumb_schema = false -%}
-{%- assign section_schema_suffixes = ',bakmix,blond,bunzlau,rice,joeff,waterfles,' -%}
+{%- assign section_schema_suffixes = ',bakmix,blond,bunzlau,bunzlau-melamine,rice,joeff,waterfles,' -%}
 {%- assign layout_schema_suffixes = ',thee,accessoires,' -%}
 {%- assign suffix_key = ',' | append: template.suffix | append: ',' -%}
 {%- if template.name == 'product' -%}
```

Sectie, verschil met `tr-product-bunzlau`:
```diff
--- a/sections/tr-product-bunzlau.liquid
+++ b/sections/tr-product-bunzlau-melamine.liquid
@@ -1,4 +1,4 @@
-{% comment %} Tante Rie – Bunzlau Castle Productpagina {% endcomment %}
+{% comment %} Tante Rie – Bunzlau Castle melamine productpagina (verzendbaar, zelfde opmaak als tr-product-bunzlau) {% endcomment %}
 
 <style>
 :root {
@@ -305,41 +305,34 @@
 
       <!-- Titel -->
       <h1 itemprop="name">{{ cur.title }}</h1>
-      <p class="trbzp-tagline">{{ cur.type | default: 'Bunzlau Castle' }}, authentiek aardewerk</p>
+      <p class="trbzp-tagline">Melamine servies van Bunzlau Castle</p>
 
       <!-- Prijs -->
       <div class="trbzp-price-row" itemprop="offers" itemscope itemtype="https://schema.org/Offer">
         <meta itemprop="priceCurrency" content="EUR">
-        <meta itemprop="availability" content="{%- if _available -%}https://schema.org/InStock{%- else -%}https://schema.org/PreOrder{%- endif -%}">
+        <meta itemprop="availability" content="{%- if _available -%}https://schema.org/InStock{%- else -%}https://schema.org/OutOfStock{%- endif -%}">
         <span class="trbzp-price" id="trbzp-price">
           <meta itemprop="price" content="{{ cur.selected_or_first_available_variant.price | divided_by: 100.0 }}">
           {{ cur.selected_or_first_available_variant.price | money }}
         </span>
         {%- if cur.compare_at_price > cur.price -%}<span class="trbzp-price-compare">{{ cur.compare_at_price | money }}</span>{%- endif -%}
       </div>
-      <p class="trbzp-price-sub">Incl. BTW · Alleen afhalen in Borne</p>
+      <p class="trbzp-price-sub">Incl. BTW</p>
 
       <!-- Beschikbaarheid -->
       <div class="trbzp-avail trbzp-avail--in" id="trbzp-avail-in" role="status"{% unless _available %} hidden{% endunless %}>
         <span class="trbzp-avail-icon" aria-hidden="true">{%- render 'tr-icon', name: 'check' -%}</span>
-        <div class="trbzp-avail-text"><strong>Op voorraad</strong><span>Vandaag op te halen</span></div>
+        <div class="trbzp-avail-text"><strong>Op voorraad</strong><span>Verzonden binnen 1 tot 2 werkdagen</span></div>
       </div>
       <div class="trbzp-avail trbzp-avail--order" id="trbzp-avail-order" role="status"{% if _available %} hidden{% endif %}>
         <span class="trbzp-avail-icon" aria-hidden="true">{%- render 'tr-icon', name: 'package' -%}</span>
-        <div class="trbzp-avail-text"><strong>Te bestellen</strong><span>Wij bellen je zodra het klaar ligt</span></div>
-      </div>
-
-      <!-- Ophaalnotice -->
-      <div class="trbzp-pickup">
-        <span class="trbzp-pickup-icon" aria-hidden="true">{%- render 'tr-icon', name: 'store' -%}</span>
-        <span>Alleen afhalen · Bakkerssteeg 6, Borne · Di t/m za 10–17u</span>
+        <div class="trbzp-avail-text"><strong>Uitverkocht</strong><span>Tijdelijk niet leverbaar</span></div>
       </div>
 
       <!-- Specs strip -->
       <div class="trbzp-specs-strip">
-        <div class="trbzp-spec-pill"><span class="trbzp-spec-icon" aria-hidden="true">{%- render 'tr-icon', name: 'jar' -%}</span><span class="trbzp-spec-value">Aardewerk</span><span class="trbzp-spec-label">Materiaal</span></div>
-        <div class="trbzp-spec-pill"><span class="trbzp-spec-icon" aria-hidden="true">{%- render 'tr-icon', name: 'hand' -%}</span><span class="trbzp-spec-value">Handgemaakt</span><span class="trbzp-spec-label">Productie</span></div>
-        <div class="trbzp-spec-pill"><span class="trbzp-spec-icon" aria-hidden="true">{%- if _vaatwasser -%}{%- render 'tr-icon', name: 'check' -%}{%- else -%}{%- render 'tr-icon', name: 'hand' -%}{%- endif -%}</span><span class="trbzp-spec-value">{%- if _vaatwasser -%}Ja{%- else -%}Handwas{%- endif -%}</span><span class="trbzp-spec-label">Vaatwasser</span></div>
+        <div class="trbzp-spec-pill"><span class="trbzp-spec-icon" aria-hidden="true">{%- render 'tr-icon', name: 'jar' -%}</span><span class="trbzp-spec-value">Melamine</span><span class="trbzp-spec-label">Materiaal</span></div>
+        <div class="trbzp-spec-pill"><span class="trbzp-spec-icon" aria-hidden="true">{%- render 'tr-icon', name: 'package' -%}</span><span class="trbzp-spec-value">1 tot 2 dagen</span><span class="trbzp-spec-label">Verzending</span></div>
       </div>
 
       <!-- Varianten -->
@@ -376,56 +369,22 @@
       </div>
 
       <!-- CTA knop -->
-      <button type="button" id="trbzp-atc" class="trbzp-btn-primary{% unless _available %} bz-order{% endunless %}"
+      <button type="button" id="trbzp-atc" class="trbzp-btn-primary"
         data-variant-id="{{ cur.selected_or_first_available_variant.id }}"
         data-available="{{ _available }}"
-        {%- if _available %} data-tr-atc{% endif %}
-        {%- unless _available %} aria-expanded="false" aria-controls="trbzp-order-form-wrap"{% endunless %}>{%- if _available -%}In winkelwagen{%- else -%}Bestellen{%- endif -%}</button>
-      <div class="trbzp-order-form-wrap" id="trbzp-order-form-wrap" aria-live="polite">
-        <div class="trbzp-order-form">
-          <h3>Stuur een bestelverzoek</h3>
-          <p class="trbzp-order-form-sub">Wij bellen of mailen je zodra het klaar ligt.</p>
-          <div class="trbzp-order-sku"><span>Geselecteerd: <strong id="trbzp-sku-label">{{ cur.title }}{% if cur.selected_or_first_available_variant.title != 'Default Title' %} – {{ cur.selected_or_first_available_variant.title }}{% endif %}</strong></span></div>
-          <form method="post" action="/contact#trbzp-order-form-wrap" id="trbzp-contact-form" accept-charset="UTF-8">
-            <input type="hidden" name="form_type" value="contact">
-            <input type="hidden" name="utf8" value="✓">
-            <input type="hidden" name="contact[subject]" value="Bestelverzoek Bunzlau Castle – {{ cur.title }}">
-            <input type="hidden" name="contact[body_prefix]" id="trbzp-hidden-product" value="Product: {{ cur.title }} | SKU: {{ cur.selected_or_first_available_variant.sku }}">
-            <div class="trbzp-form-row">
-              <div class="trbzp-form-group"><label for="trbzp-naam">Naam</label><input type="text" id="trbzp-naam" name="contact[naam]" placeholder="Voor- en achternaam" required autocomplete="name"></div>
-              <div class="trbzp-form-group"><label for="trbzp-tel">Telefoon</label><input type="tel" id="trbzp-tel" name="contact[telefoon]" placeholder="06 12345678" required autocomplete="tel"></div>
-            </div>
-            <div class="trbzp-form-group"><label for="trbzp-email">E-mailadres</label><input type="email" id="trbzp-email" name="contact[email]" placeholder="jouw@email.nl" required autocomplete="email"></div>
-            <div class="trbzp-form-group"><label for="trbzp-adres">Adres <span class="trbzp-form-optional">(optioneel)</span></label><input type="text" id="trbzp-adres" name="contact[adres]" placeholder="Straat, postcode, plaats"></div>
-            <div class="trbzp-form-qty">
-              <label>Aantal</label>
-              <div class="trbzp-form-qty-ctrl">
-                <button type="button" class="trbzp-form-qty-btn" id="trbzp-form-qty-minus">−</button>
-                <span class="trbzp-form-qty-num" id="trbzp-form-qty-val">1</span>
-                <button type="button" class="trbzp-form-qty-btn" id="trbzp-form-qty-plus">+</button>
-              </div>
-              <input type="hidden" name="contact[aantal]" id="trbzp-form-qty-input" value="1">
-            </div>
-            <div class="trbzp-form-group"><label for="trbzp-opmerkingen">Opmerkingen <span class="trbzp-form-optional">(optioneel)</span></label><textarea id="trbzp-opmerkingen" name="contact[opmerkingen]" placeholder="Bijv. gewenste ophaaldatum…"></textarea></div>
-            <button type="submit" class="trbzp-btn-order-submit">Verstuur verzoek</button>
-          </form>
-          <div class="trbzp-form-success" id="trbzp-form-success" role="alert"><h4>Gelukt!</h4><p>We bellen of mailen je binnenkort.</p></div>
-        </div>
-      </div>
+        {%- if _available %} data-tr-atc{% else %} disabled{% endif %}>{%- if _available -%}In winkelwagen{%- else -%}Uitverkocht{%- endif -%}</button>
 
       <!-- USPs -->
       <div class="trbzp-usps">
-        <div class="trbzp-usp"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2C8 2 5 5 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-4-3-7-7-7z"/><circle cx="12" cy="9" r="2.5"/></svg><div class="trbzp-usp-text"><div class="trbzp-usp-label">Alleen in Borne</div><div class="trbzp-usp-sub">Afhalen in de winkel</div></div></div>
-        <div class="trbzp-usp"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3c-3 0-5.5 2.5-5.5 5.5 0 1.5.6 2.9 1.6 3.9L12 21l3.9-8.6c1-1 1.6-2.4 1.6-3.9C17.5 5.5 15 3 12 3z"/></svg><div class="trbzp-usp-text"><div class="trbzp-usp-label">Uniek decor</div><div class="trbzp-usp-sub">Elk stuk anders</div></div></div>
-        <div class="trbzp-usp"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17.5C5.3 16.2 4 14.2 4 12c0-4.4 3.6-8 8-8s8 3.6 8 8c0 2.2-1.3 4.2-3 5.5"/></svg><div class="trbzp-usp-text"><div class="trbzp-usp-label">Handgemaakt</div><div class="trbzp-usp-sub">Ambacht uit Polen</div></div></div>
-        <div class="trbzp-usp"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5M2 12l10 5 10-5"/></svg><div class="trbzp-usp-text"><div class="trbzp-usp-label">Steengoed</div><div class="trbzp-usp-sub">Duurzaam &amp; sterk</div></div></div>
+        <div class="trbzp-usp"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5M2 12l10 5 10-5"/></svg><div class="trbzp-usp-text"><div class="trbzp-usp-label">Verzending in Nederland</div><div class="trbzp-usp-sub">Binnen 1 tot 2 werkdagen</div></div></div>
+        <div class="trbzp-usp"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3c-3 0-5.5 2.5-5.5 5.5 0 1.5.6 2.9 1.6 3.9L12 21l3.9-8.6c1-1 1.6-2.4 1.6-3.9C17.5 5.5 15 3 12 3z"/></svg><div class="trbzp-usp-text"><div class="trbzp-usp-label">Uniek decor</div><div class="trbzp-usp-sub">Bloemen en patronen</div></div></div>
       </div>
 
       <!-- Accordion -->
       <div class="trbzp-accordion">
         <div class="trbzp-accordion-item">
           <button type="button" class="trbzp-accordion-trigger open" aria-expanded="true" data-trbzp-acc>Productomschrijving<span class="trbzp-chevron">▾</span></button>
-          <div class="trbzp-accordion-body open"><div class="trbzp-accordion-body-inner" itemprop="description">{%- if cur.description != blank -%}{{ cur.description }}{%- else -%}<p>Bunzlau Castle aardewerk bij Tante Rie in Borne.</p>{%- endif -%}</div></div>
+          <div class="trbzp-accordion-body open"><div class="trbzp-accordion-body-inner" itemprop="description">{%- if cur.description != blank -%}{{ cur.description }}{%- else -%}<p>Bunzlau Castle melamine bij Tante Rie in Borne.</p>{%- endif -%}</div></div>
         </div>
         <div class="trbzp-accordion-item">
           <button type="button" class="trbzp-accordion-trigger" aria-expanded="false" data-trbzp-acc>Specificaties<span class="trbzp-chevron">▾</span></button>
@@ -436,25 +395,19 @@
               <tr><td>Decor</td><td id="trbzp-spec-decor">{{ cur.selected_or_first_available_variant.title | replace: 'Default Title', '–' }}</td></tr>
               <tr><td>Gewicht</td><td id="trbzp-spec-weight">{%- assign _vw = cur.selected_or_first_available_variant.weight -%}{%- if _vw > 0 -%}{{ _vw | times: 1000 | round }} g{%- else -%}–{%- endif -%}</td></tr>
               <tr><td>Merk</td><td>Bunzlau Castle</td></tr>
-              <tr><td>Materiaal</td><td>Keramisch aardewerk (steengoed)</td></tr>
-              <tr><td>Gemaakt in</td><td>Polen</td></tr>
+              <tr><td>Materiaal</td><td>Melamine</td></tr>
               {%- if cur.metafields.custom.inhoud_ml != blank -%}<tr><td>Inhoud</td><td>{{ cur.metafields.custom.inhoud_ml }} ml</td></tr>{%- endif -%}
               {%- if cur.metafields.custom.hoogte_cm != blank -%}<tr><td>Hoogte</td><td>{{ cur.metafields.custom.hoogte_cm }} cm</td></tr>{%- endif -%}
               {%- if cur.metafields.custom.diameter_cm != blank -%}<tr><td>Diameter</td><td>{{ cur.metafields.custom.diameter_cm }} cm</td></tr>{%- endif -%}
-              <tr><td>Vaatwasserbestendig</td><td><span class="{%- if _vaatwasser -%}trbzp-icon--yes{%- else -%}trbzp-icon--no{%- endif -%}" aria-hidden="true">{%- if _vaatwasser -%}✓{%- else -%}✗{%- endif -%}</span> {%- if _vaatwasser -%}Ja{%- else -%}Handwas aanbevolen{%- endif -%}</td></tr>
-              <tr><td>Ovenbestendig</td><td><span class="{%- if _oven -%}trbzp-icon--yes{%- else -%}trbzp-icon--no{%- endif -%}" aria-hidden="true">{%- if _oven -%}✓{%- else -%}✗{%- endif -%}</span> {%- if _oven -%}Ja{%- else -%}Nee{%- endif -%}</td></tr>
-              <tr><td>Magnetronbestendig</td><td><span class="{%- if _magnetron -%}trbzp-icon--yes{%- else -%}trbzp-icon--no{%- endif -%}" aria-hidden="true">{%- if _magnetron -%}✓{%- else -%}✗{%- endif -%}</span> {%- if _magnetron -%}Ja{%- else -%}Niet aanbevolen{%- endif -%}</td></tr>
             </table>
-            <p style="margin-top:10px"><strong>Onderhoudstip:</strong> Was met de hand in warm water met mild zeep.</p>
           </div></div>
         </div>
         <div class="trbzp-accordion-item">
-          <button type="button" class="trbzp-accordion-trigger" aria-expanded="false" data-trbzp-acc>Ophaalinformatie<span class="trbzp-chevron">▾</span></button>
+          <button type="button" class="trbzp-accordion-trigger" aria-expanded="false" data-trbzp-acc>Verzending en retour<span class="trbzp-chevron">▾</span></button>
           <div class="trbzp-accordion-body"><div class="trbzp-accordion-body-inner">
-            <p><strong>Dit product versturen we niet.</strong> {% if _available %}Je bestelt online en haalt het op in onze winkel in Borne.{% else %}Je stuurt een bestelverzoek en haalt het product daarna op in onze winkel in Borne.{% endif %}</p>
-            <p><strong>Adres:</strong> Bakkerssteeg 6, 7622 GX Borne</p>
-            <p><strong>Openingstijden:</strong><br>Di t/m za 10:00–17:00<br>Ma &amp; zo gesloten</p>
-            {%- unless _available -%}<p><strong>Op bestelling:</strong> Altijd te bestellen. Na je verzoek spreken we een ophaaldatum af.</p>{%- endunless -%}
+            <p><strong>Verzending.</strong> Bestellingen verwerken we binnen 1 tot 2 werkdagen en bezorgen we de werkdag erna. Een pakket tot en met 300 gram kost 4,50 euro, zwaardere pakketten 6,95 euro.</p>
+            {%- if _available -%}<p><strong>Ophalen.</strong> Dit product ligt in onze winkel in Borne, Bakkerssteeg 6, dinsdag tot en met zaterdag van 10:00 tot 17:00.</p>{%- endif -%}
+            <p><strong>Retour.</strong> Retourneren kan binnen 14 dagen, mits ongebruikt en in de originele verpakking.</p>
             <p>Vragen? <a href="/pages/contact" style="color:var(--bz-blue)">Neem contact op</a>.</p>
           </div></div>
         </div>
@@ -480,7 +433,7 @@
             <div class="trbzp-related-card-body">
               <p class="trbzp-related-card-name">{{ rp.title }}</p>
               <p class="trbzp-related-card-price">{{ rp.price | money }}</p>
-              <span class="trbzp-related-card-badge {% if rp.available %}stock{% else %}order{% endif %}">{%- if rp.available -%}Op voorraad{%- else -%}Te bestellen{%- endif -%}</span>
+              <span class="trbzp-related-card-badge {% if rp.available %}stock{% else %}order{% endif %}">{%- if rp.available -%}Op voorraad{%- else -%}Uitverkocht{%- endif -%}</span>
             </div>
           </a>
         {%- endfor -%}
@@ -491,7 +444,7 @@
   <!-- Sticky ATC (mobiel) -->
   <div class="trbzp-sticky-atc">
     <span class="trbzp-sticky-price" id="trbzp-sticky-price">{{ cur.selected_or_first_available_variant.price | money }}</span>
-    <button type="button" class="trbzp-sticky-btn" id="trbzp-sticky-btn">{%- if _available -%}In winkelwagen{%- else -%}Bestellen{%- endif -%}</button>
+    <button type="button" class="trbzp-sticky-btn" id="trbzp-sticky-btn"{% unless _available %} disabled{% endunless %}>{%- if _available -%}In winkelwagen{%- else -%}Uitverkocht{%- endif -%}</button>
   </div>
 
   {%- render 'tr-product-schema', product: cur, brand_name: 'Bunzlau Castle' -%}
@@ -535,12 +488,11 @@
     if(atc){
       atc.dataset.variantId=v.id;
       atc.dataset.available=v.available?'true':'false';
-      atc.textContent=v.available?'In winkelwagen':'Bestel nu';
-      atc.classList.toggle('bz-order',!v.available);
-      if(v.available){atc.setAttribute('data-tr-atc','');atc.removeAttribute('aria-expanded');atc.removeAttribute('aria-controls');}
-      else{atc.removeAttribute('data-tr-atc');atc.setAttribute('aria-controls','trbzp-order-form-wrap');atc.setAttribute('aria-expanded',(ow&&ow.classList.contains('visible'))?'true':'false');}
+      atc.textContent=v.available?'In winkelwagen':'Uitverkocht';
+      atc.disabled=!v.available;
+      if(v.available){atc.setAttribute('data-tr-atc','');}else{atc.removeAttribute('data-tr-atc');}
     }
-    if(sbEl)sbEl.textContent=v.available?'In winkelwagen':'Bestel nu';
+    if(sbEl){sbEl.textContent=v.available?'In winkelwagen':'Uitverkocht';sbEl.disabled=!v.available;}
     if(availIn&&availOrder){availIn.hidden=!v.available;availOrder.hidden=v.available;}
     if(ow&&v.available){ow.classList.remove('visible');}
     if(v.image&&mainImg){mainImg.src=v.image;mainImg.alt=v.alt||'';}
@@ -556,5 +508,5 @@
 </script>
 
 {% schema %}
-{"name":"Bunzlau Productpagina","tag":"div","settings":[{"type":"text","id":"tagline","label":"Tagline","placeholder":"Laat leeg voor automatische tagline"}]}
+{"name":"Bunzlau Melamine","tag":"div","settings":[{"type":"text","id":"tagline","label":"Tagline","placeholder":"Laat leeg voor automatische tagline"}]}
 {% endschema %}
```

## 3. De 7 producten omzetten (na Marks akkoord op de preview)

Per product `templateSuffix` op `bunzlau-melamine` zetten, met backup van de huidige waarde (`bunzlau`) in `marketing/technisch/` en live controle per product.

| Handle | Product-ID | Voorraad | Nu | Voorstel |
|---|---|---|---|---|
| melamine-bord-wild-flowers-o-25-cm | 12017686184200 | 6 | bunzlau | bunzlau-melamine |
| melamine-bord-dragonfly-garden-o-25-cm | 12017690444040 | 1 | bunzlau | bunzlau-melamine |
| melamine-bord-fleur-fountain-o-25-cm | 12017690476808 | 5 | bunzlau | bunzlau-melamine |
| melamine-bord-blooming-o-25-cm | 12017716461832 | 3 | bunzlau | bunzlau-melamine |
| melamine-kom-wild-flowers-o-15-cm | 12017731141896 | 0 | bunzlau | bunzlau-melamine |
| melamine-kom-fleur-fountain-o-15-cm | 12017731174664 | -2 | bunzlau | bunzlau-melamine |
| melamine-beker-1 | 12038206816520 | 10 | bunzlau | bunzlau-melamine |

Het sjabloon moet eerst live staan (3 bestanden) voordat de producten omgezet worden, anders valt Shopify terug op het standaardtemplate. Zet de templatewissel dus pas na het publiceren van de bestanden.

## 4. De twee kommen zonder voorraad (0 en -2)

Na de wissel zijn ze online uitverkocht (knop uitgeschakeld, schema OutOfStock). Opties:
1. Voorraad corrigeren in Shopify. Een voorraad van -2 betekent dat er meer verkocht (waarschijnlijk via de kassa) is dan geboekt. Tel de kommen in de winkel en boek de echte voorraad. Is er voorraad, dan klopt alles vanzelf. Aanbevolen als eerste stap.
2. Zijn ze niet meer leverbaar of komen ze niet terug: online uit de verkoop halen (kanaal Online winkel uitzetten), zodat er geen uitverkochte pagina's blijven staan. Let op: dat geeft dan een 404 en vraagt om overleg (CLAUDE.md), eventueel met een redirect naar de bordencollectie.
3. Verkopen zonder voorraad toestaan (bestellen bij de leverancier): niet aangeraden, want het sjabloon heeft geen bestelverzoek meer en de levertijd klopt dan niet met het schema.
Beslissing voor Mark: voorraad tellen en corrigeren (1), of offline halen (2)?

## 5. Aandachtspunten voor Mark en On-page

- Gewicht: de varianten hebben geen gewicht (de specificatietabel toont een streepje). De verzendkosten in het schema zijn daardoor 4,50 euro (tot en met 300 gram). Een melamine bord van 25 centimeter weegt waarschijnlijk meer; dan hoort 6,95 euro in het schema en in de checkout. Gewicht invullen in Shopify.
- Het verzendprofiel moet melamine toelaten (nog niet gecontroleerd).
- Melamine Bord Fleur Fountain heeft productType "Keramiek" in plaats van "Melamine".
- De producten dragen de tag "Handgemaakt", wat op melamine niet klopt; die verschijnt als label op de pagina.
- Productbeschrijving: alleen het bord Wild Flowers heeft er een. De rest valt terug op "Bunzlau Castle melamine bij Tante Rie in Borne." On-page kan teksten schrijven.
- /collections/bunzlau toont nog de banner "Alleen afhalen in Borne" boven alle producten, ook boven melamine, en de collectietekst zegt anders. Dat moet On-page aanpassen.
- Rice: accordeontekst "dezelfde werkdag verwerkt" tegenover 1 tot 2 werkdagen elders.
