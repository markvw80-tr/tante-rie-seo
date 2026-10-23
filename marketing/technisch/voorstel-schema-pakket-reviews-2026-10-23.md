# Voorstel: verzendtarief Pakket en reviews in het productschema (V57 en V47 stap A)

Datum: 23-10-2026. Rol: technisch SEO-specialist. Status: preview klaar, niets naar live gepusht, geen tags gezet. Mark heeft V57 met "Ja" beantwoord en V47 stap B (Judge.me-vinkje) doet hij zelf.

## 1. Tagcontrole: de tag "pakket" zou zichtbaar worden

Daarom is de tag NIET op de 48 producten gezet. Er is niets aan Shopify-producten gewijzigd, dus ook geen backup-tags-bestand en geen regel in changelog.md.

In het live thema (#203153015048) tonen deze secties ruwe `cur.tags` als label boven de titel:

- `sections/tr-product-rice.liquid` (eerste 3 tags) voor alle 27 rice-producten
- `sections/tr-product-waterfles.liquid` (eerste 3) voor de 5 waterflessen
- `sections/tr-accessoires-redesign.liquid` (eerste 3)
- `sections/tr-product-redesign.liquid` (eerste 4) en `sections/tr-product-bakmix.liquid` (eerste 4), de standaardtemplate van onder meer coldbrew, pineut-cake, ovenwant, schort en bunzlau-textiel

De meeste van de 48 producten hebben nu geen tags, dus "pakket" zou direct als eerste label op de pagina verschijnen. De secties `tr-product-bunzlau` en `tr-product-bunzlau-melamine` (melamine, servetten, theemutsen, bewaarblik) filteren op een vaste lijst en tonen "pakket" niet. De collectiesecties tonen alleen een vaste lijst keurmerken.

## 2. Preview

Ongepubliceerde kopie van live: **schema-pakket-reviews 2026-10-23**, thema-ID 204007932168 (nu 15 thema's).

- Preview: https://0qkm31-r6.myshopify.com?preview_theme_id=204007932168
- Product in preview: https://tanterie.nl/products/beste-van-borne?preview_theme_id=204007932168
- Editor: https://0qkm31-r6.myshopify.com/admin/themes/204007932168/editor

Gewijzigde bestanden (diff: `voorstel-schema-pakket-reviews-2026-10-23.diff`):

1. `snippets/tr-offer-policies.liquid`: tag "pakket" (hoofdletterongevoelig) zet shippingRate op 6.95 voor NL, ongeacht gewicht. Alleen afhalen (doesNotShip) gaat nog voor. Dit is de enige plek waar shippingRate wordt bepaald; `tr-product-schema`, `product-cro` en `schema-structured-data` renderen allemaal dit snippet, dus Rice, waterfles en melamine (`tr-product-bunzlau-melamine`) komen vanzelf mee zonder eigen wijziging.
2. `snippets/tr-product-schema.liquid`: `review[]` (maximaal 10) uit `judgeme.review_widget_data`, binnen het aggregateRating-blok.
3. Vijf secties (rice, waterfles, accessoires-redesign, product-redesign, bakmix): de tag "pakket" wordt overgeslagen in het zichtbare tag-label. Dit is een aanvulling op de opdracht, nodig om de tag later veilig te kunnen zetten. De limiet van 3 of 4 labels blijft gelden voor de andere tags.

## 3. Controle op de preview (curl met cookie-jar, thema-ID in de pagina bevestigd)

| Product | Resultaat |
|---|---|
| beste-van-borne | themablok shippingRate 4.50, 5 Review-objecten, aggregateRating 5 |
| geluksthee | 4.50, 1 Review-object |
| theemuts-streep (Bunzlau-keramiek) | doesNotShip, ongewijzigd |
| melamine-bord-wild-flowers-o-25-cm, rice-a, waterfles-delfts-blauw, coldbrew-theefles-kaki | 4.50 (geen tag gezet, zoals live) |

Voor alle geteste pagina's: alle JSON-LD-blokken parsen als geldige JSON, nul Liquid-fouten. De Judge.me-appblok staat er nog (stap B volgt door Mark), dus op producten met reviews staan nu nog twee Product-blokken.

**Niet verifieerbaar op de preview: de 6.95 voor melamine, Rice en waterfles.** Zonder tag op het product is dat niet te testen, en de tag mag pas na akkoord. De logica is wel getest met liquidjs op het echte snippet: tag "pakket" bij 100 g geeft 6.95, "Pakket" bij gewicht 0 geeft 6.95, geen tag bij 100 g geeft 4.50, geen tag bij 500 g geeft 6.95, tag plus alleen-afhalen geeft doesNotShip. Dat is een simulatie, geen Shopify-render. Rich Results Test is nog niet gedraaid.

## 4. Voorstel voor de volgorde

1. Mark keurt de diff goed, daarna gaat het thema live (push naar live alleen na akkoord).
2. Daarna worden de 48 tags gezet (met backup van de oude tags). Dan geldt "pakket" overal waar het label nu verborgen wordt.
3. Controle op live met curl: melamine, Rice, waterfles op 6.95, thee op 4.50, Bunzlau-keramiek doesNotShip; Rich Results Test op beste-van-borne en een melaminebord.
4. Mark zet het Judge.me-JSON-LD-vakje uit (V47 stap B), daarna telling: één Product-blok.

Alternatief als de tag-aanpak niet gewenst is: een product-metafield in plaats van een tag (nooit zichtbaar). Dat vraagt een metafielddefinitie en vulling van de 48 producten.

## Open punten

- Akkoord op de diff en op de volgorde hierboven.
- Producten die later bij het verzendprofiel "Pakket" komen, hebben ook de tag nodig, anders blijft het schematarief op gewicht staan.
