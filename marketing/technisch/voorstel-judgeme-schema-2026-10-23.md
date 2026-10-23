# Voorstel: één Product-blok per productpagina (V47, Judge.me)

Datum: 23-10-2026. Rol: technisch SEO-specialist. Status: alleen onderzoek en voorstel, niets live gewijzigd, ook niet in Judge.me. Mark zei bij V47: "zoek maar uit".

## Korte conclusie

1. Op 26 van de 422 producten in de productsitemap staan twee Product-blokken. Het zijn precies de producten met reviews in de Judge.me-widget.
2. Het tweede blok komt uit de Judge.me-appblok in de productpagina, niet uit thema-code. Het thema kan het niet uitzetten zonder de zichtbare reviewwidget te verwijderen.
3. Judge.me heeft een app-instelling om de JSON-LD uit te zetten. Daarmee verdwijnt blok 2. Dan raakt Google wel de losse reviews kwijt, want die zitten alleen in blok 2.
4. Aanbevolen is daarom een combinatie in twee stappen: eerst het themablok uitbreiden met de losse reviews (themewerk, diff hieronder), daarna in Judge.me de JSON-LD uitzetten (app-instelling, stappen voor Mark hieronder).
5. Blok 1 en blok 2 zijn nu inhoudelijk consistent (zelfde score, zelfde aantal). Er is dus geen datafout, alleen een dubbele entiteit.

## 1. Welke producten hebben twee blokken

Methode: alle 422 product-URL's uit https://tanterie.nl/sitemap_products_1.xml met curl opgehaald (23-10-2026), alle JSON-LD-scripts uitgelezen en geteld per @type Product. Alle 422 pagina's gaven een themablok; 396 hebben er maar een, 26 hebben er twee.

De 26 producten (allemaal Judge.me-blok zonder offers, themablok met offers, verzending en aggregateRating):

1001-nacht, arts-craft-thee-bewaarblik-100-gram, arts-craft-thee-bewaarblik-100-gram-1, beste-van-borne, geluksthee, groene-citroen, kamille, marocco-mint, oud-borne, perzik, pineut-cake-pouchbag-lemon-poppy-cake, proefpakket-groene-thee, proefpakket-groene-thee-kopie, rooibos-vanille, rooibos-voor-de-open-haard, sinaasappel-chai, sinas-gember, slaap-lekker, sterke-vrouw, sterrenmunt, teeli-flip-s-theefilter, thee-van-oma, theelepelzeef-met-draaifunctie, theezeefje-rvs-met-uitlekschaaltje, zoete-verleiding, zomer-munt.

Aanvulling: vier producten hebben wel een aggregateRating in het themablok maar geen Judge.me-JSON-LD op de pagina: boeren-mok-240-ml, dinerbord-o-25-5-cm-1, ovenschaal-vierkant-1550-ml, theetip-rond. Daar is dus geen dubbel blok. De oorzaak (de widget staat er wel) is niet uitgezocht; het vraagt geen actie.

Let op: de sitemap bevat 422 online producten, Shopify heeft 718 actieve producten. De rest staat alleen op de kassa en hoort niet in deze lijst (404 online is daar correct).

Bij nieuwe reviews komen er vanzelf producten bij. Het probleem groeit dus mee met het aantal reviews.

## 2. Waar zit het Judge.me-blok

- Op de live pagina staat het in `<div id="shopify-block-...__judge_me_review_widget" class="shopify-block shopify-app-block">`, direct onder `jdgm-review-widget`. Het is een `<script type="application/ld+json" class="jdgm-server-jld">`.
- In de templates is dat een appblok: `shopify://apps/judge-me-reviews/blocks/review_widget/61ccd3b1-...` (onder meer in templates/product.json, product.thee.json, product.rice.json, product.accessoires.json, product.waterfles.json, product.bakmix.json). Het script wordt dus door de app zelf gerenderd binnen dat blok. Er staat geen JSON-LD-code van Judge.me in een snippet van het thema.
- Verder staat de app-embed `judgeme_core` aan in config/settings_data.json. Die laadt de scripts en de instellingen (`window.jdgmSettings`).
- De snippets `judgeme_widgets.liquid` en `judge-me-review-widget.liquid` bevatten alleen lege mount-divs, geen schema.
- Het themablok komt uit `snippets/tr-product-schema.liquid` (live versie, dus mét `tr-offer-policies`; let op: de lokale map ~/TanteRie-Theme-Editor loopt achter op live, werk daarom vanaf het live thema).

Gevolg: het appblok verwijderen uit het thema zou ook de zichtbare reviews en sterren op de pagina laten verdwijnen. Dat is dus niet de route.

## 3. Kan het blok uit zonder dat reviews en sterren verdwijnen

Volgens de Judge.me-helpdocumentatie ("Displaying product ratings in Google search results", https://judge.me/help/en/articles/8409296-displaying-product-ratings-in-google-search-results) staat de instelling hier:

Judge.me-beheer, Settings, Google, SEO and AI, SEO Rich Snippets. Daar zijn twee selectievakjes:

- Add JSON-LD snippets (Default)
- Add microdata snippets

Uitzetten van "Add JSON-LD snippets" is beschikbaar op het gratis plan. Er is een extra keuze "Advanced" (alleen met JSON-LD aan, betaald plan) om per product ook de reviewteksten mee te sturen. Het Judge.me-blok bevat nu wel losse reviews (zie punt 4), dus controleer in het scherm wat daar is ingesteld.

Wat uit de live pagina blijkt (jdgmSettings): `disable_json_ld: false` (dus JSON-LD staat aan) en `remove_microdata_snippet: true` (microdata staat al uit). Alleen het JSON-LD-vakje hoeft dus uit.

Blijven sterren en reviews zichtbaar? De helpdocumentatie zegt dit niet met zoveel woorden. Wat wel vaststaat: de zichtbare reviews worden gerenderd uit andere data (`jdgm-ssr-reviews` en de metafield `judgeme.review_widget_data`), niet uit het JSON-LD-script, en de sterren in de themaweergave komen uit `judgeme.badge` en de widget. Het is dus zeer waarschijnlijk dat niets zichtbaars verdwijnt, maar dit is niet bevestigd. Daarom staat in de stappen hieronder een controle op één productpagina na het uitzetten, met een eenvoudige terugdraaiing (vakje weer aan).

## 4. Zelfde bron, zelfde aantal, losse reviews

- Bron: het themablok leest `product.metafields.reviews.rating` en `reviews.rating_count` (de standaard Shopify-reviewmetafields die Judge.me schrijft). Het Judge.me-blok komt uit Judge.me's eigen data (`judgeme.review_widget_data`). Zelfde app, twee metafields.
- Vergelijking over alle 26 producten: ratingValue en reviewCount zijn gelijk. Het enige verschil is afronding: sinas-gember heeft 4.3 in het themablok en 4.33 in Judge.me. Het aantal reviews in `review[]` is gelijk aan reviewCount bij alle 26 (maximaal 5 per product nu).
- Losse reviews: alleen het Judge.me-blok heeft `review[]` (Review, author, reviewBody, datePublished, reviewRating). Het themablok heeft geen losse reviews. Als Judge.me-JSON-LD uit gaat zonder aanpassing in het thema, ziet Google dus alleen nog aggregateRating en geen losse reviews meer.
- Beperking: de metafield bevat de eerste pagina reviews (per_page 5). Bij meer dan 5 reviews per product stuurt ook Judge.me nu maximaal die eerste pagina. In het voorstel is de limiet 10.

## 5. Beoordeling Rich Results Test (op basis van Google-documentatie, test niet gedraaid)

Afgesproken is dat de browser niet gebruikt wordt. De beoordeling hieronder volgt de Google-documentatie voor Product-structured data (productfragmenten en merchantvermeldingen):

- Het Judge.me-blok heeft een relatief `@id` (`/products/beste-van-borne#product`) en geen `url`, dus Google koppelt het niet aan het themablok (`@id` = volledige URL). Google ziet twee losse Product-entiteiten op dezelfde pagina.
- De entiteit zonder `offers` kan geen prijs, voorraad of verzendinformatie tonen en geeft in de test bij merchantvermeldingen meldingen over ontbrekende velden (`offers`). Voor productfragmenten is `aggregateRating` of `review` voldoende, dus dat blok is op zich geldig maar nutteloos naast het themablok.
- Google raadt één Product-entiteit per pagina aan met `offers` en `aggregateRating` (en `review`). Dat is de voorkeur en wat dit voorstel oplevert.
- Verwacht gedrag nu: Google kan de sterren uit blok 2 en prijs uit blok 1 combineren, maar dat is niet gegarandeerd. Het risico is dat sterren en prijs niet bij hetzelfde product in de resultaten komen, of dat Search Console meldingen geeft. Er is geen indexatieschade vastgesteld; het is een kwaliteitsrisico.
- Na livegang: controleer één URL (beste-van-borne) in de Rich Results Test. Verwacht: één Product met Review snippets en Merchant listings, zonder waarschuwingen over ontbrekende velden. Deze controle is nog niet uitgevoerd.

## Voorstel (voor en na)

### Voor (nu, beste-van-borne)

Twee Product-blokken: thema (offers, shippingDetails, brand, sku, aggregateRating 5.0 uit 5) en Judge.me (name, image, aggregateRating 5.00 uit 5, 5 losse Review-objecten, geen offers).

### Na

Een Product-blok: thema met offers, shippingDetails, brand, sku, aggregateRating en nu ook `review[]` met dezelfde 5 reviews uit `judgeme.review_widget_data`. Judge.me-blok weg door de JSON-LD-instelling uit te zetten.

### Stap A: themawerk (diff in `/Users/markvanwijk/Tante Rie SEO/marketing/technisch/voorstel-judgeme-schema-2026-10-23.diff`)

Wijziging in `snippets/tr-product-schema.liquid` (live versie van thema #203153015048): een variabele `jm_reviews` uit `product.metafields.judgeme.review_widget_data.value.reviews` en, binnen de bestaande aggregateRating-voorwaarde, een `review`-array (max 10, velden reviewRating, author, name indien een titel bestaat, reviewBody, datePublished). Geen wijzigingen aan offers.

De Liquid is lokaal getest met liquidjs op de echte reviewdata van beste-van-borne: de uitvoer is geldige JSON met 5 Review-objecten. Dat is een simulatie, geen Shopify-render.

Wat nog niet gelukt is: de ongepubliceerde themakopie. `shopify theme duplicate` van #203153015048 geeft "Failed to duplicate theme", omdat de winkel op het maximum van 20 themas zit (1 live en 19 ongepubliceerd). Er is niets verwijderd. De diff is gemaakt tegen een verse pull van het live bestand. Zodra er ruimte is, maak ik de kopie, push het bestand, controleer met preview-URL en laat de definitieve diff zien.

### Stap B: Judge.me-instelling (door Mark, na stap A live is)

Volgorde is belangrijk. Zet Judge.me pas uit nadat het thema met `review[]` live staat, anders mist Google tijdelijk de losse reviews.

1. Open het Judge.me-beheer via Shopify-beheer, Apps, Judge.me Product Reviews.
2. Ga naar Settings, dan Google, SEO and AI, dan SEO Rich Snippets.
3. Haal het vinkje weg bij "Add JSON-LD snippets (Default)". Laat "Add microdata snippets" uit (staat al uit).
4. Klik op Save.
5. Controle: open https://tanterie.nl/products/beste-van-borne in een nieuw venster (na een paar minuten, cache), kijk of de sterren onder de titel en de reviews onderaan er nog staan, en vraag mij de broncode-controle te herhalen (tel de Product-blokken, verwacht 1).
6. Als de sterren of reviews verdwijnen: vinkje weer aan, opslaan, en meld het mij.

## Risico's en open punten

- De metafield `judgeme.review_widget_data` is niet door mij te controleren op bijwerking nadat de JSON-LD uit staat. Het is dezelfde data waarmee de widget zelf reviews toont, dus dit is een zeer klein risico. Controle: laat een product met een nieuwe review een dag draaien en tel in de bron het aantal Review-objecten.
- Reviews in schema moeten op de pagina zichtbaar zijn (Google-richtlijn). Dat zijn ze, in de widget.
- Reviews van klanten over het product zelf, niet over de winkel: dat klopt (alle reviews zijn per product).
- Judge.me's eigen "Advanced"-optie (betaald plan) is niet nodig.
- Ruimte voor de themakopie: Mark beslist welk oud ongepubliceerd thema weg mag. Kandidaten op naam: "Backup pre-audit-fixes 2026-07-06", "Audit-fixes-preview 2026-07-06", "Audit-round2-preview 2026-07-06", "Audit-round3-preview 2026-07-07", "Sprint7-LookFeel". Ik verwijder niets zonder akkoord.

## Bronnen en bestanden

- Ruwe pagina's en analyse: /private/tmp/claude-502/scratch/pages/ en /private/tmp/claude-502/scratch/rows.json
- Diff: /Users/markvanwijk/Tante Rie SEO/marketing/technisch/voorstel-judgeme-schema-2026-10-23.diff
- Judge.me-helpartikel: https://judge.me/help/en/articles/8409296-displaying-product-ratings-in-google-search-results
- changelog.md en vragen-voor-mark.md zijn niet aangeraakt.
