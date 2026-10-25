# Voorstel: Product-markup op de homepage en op collectiepagina's

Datum: 25-10-2026. Rol: technisch SEO-specialist. Status: alleen onderzoek en voorstel. Niets is gewijzigd in het live thema of in Shopify. Het bijbehorende diff staat in `marketing/technisch/voorstel-homepage-productmarkup-2026-10-25.diff` (11 bestanden, gemaakt tegen het live thema "Bunzlau collectie V118 2026-10-24", id 204095619336, gelezen via de Shopify-koppeling). Het diff is droog getest met `patch --dry-run` op de live bestanden.

Wat ik niet kon controleren: de live site (tanterie.nl) is vanuit deze omgeving niet bereikbaar (de proxy weigert de verbinding), dus er is geen HTML opgehaald en de Rich Results Test is niet gedraaid. De conclusies komen uit de themacode en uit Shopify- en Judge.me-gegevens. Search Console zelf is ook niet ingezien (de voorbeeld-URL's komen van Mark).

## Korte conclusie

1. Homepage (melding 4, Productfragmenten): de bron is niet de ItemList met uitgelichte producten (die heeft offers) maar de sectie `tr-reviews`. Die geeft een ItemList van Review-objecten uit met `itemReviewed` van het type Product, met alleen `name` en `url`. Google leest elk zo'n Product als een eigen Product-item zonder offers, review of aggregateRating. De drie items uit Search Console staan alle drie in die lijst.
2. Collectie Joeff (melding 2, Verkopersvermeldingen): elke productkaart in `tr-collection-joeff` is een microdata-Product (`itemscope itemtype=".../Product"`). Een product zonder foto geeft dan een Product zonder `image`. De drie items (Grote ring, Handdoekhaakje, Kleine ring) hebben geen enkele afbeelding.
3. Advies: keuze (a), geen Product-markup op overzichtspagina's. Op de homepage de Review-ItemList verwijderen, op de tien collectiesecties de Product-microdata van de kaarten halen.

## 1. Homepage: waar komt Product-markup vandaan

Onderzocht in het live thema: `templates/index.json` (secties tr-homepage-redesign, tr-reviews, tr-homepage-blog, tr-homepage-faq, tr-homepage-cta), `layout/theme.liquid`, `snippets/schema-structured-data.liquid`, alle snippets en blocks (205 bestanden) en alle secties (72 bestanden), op `itemscope`, `itemtype`, `itemprop` en `ld+json`.

| Plek | Soort | Product-items | Offers aanwezig |
|---|---|---|---|
| `sections/tr-homepage-redesign.liquid:299-340`, ItemList "Favorieten van onze klanten" | JSON-LD | 4 (eerste vier producten van collectie thee) | ja, met price, priceCurrency, availability, url |
| `sections/tr-reviews.liquid:~190-225`, ItemList "Klantbeoordelingen Tante Rie" | JSON-LD | tot 6 Review-objecten, daarin `itemReviewed` Product met alleen name en url | nee |
| `layout/theme.liquid:60-121` | JSON-LD | WebSite en LocalBusiness, geen Product | niet van toepassing |
| tr-homepage-blog, tr-homepage-faq (FAQPage), tr-homepage-cta | | geen Product | niet van toepassing |
| App-blokken op de homepage | | geen in `templates/index.json`; Judge.me JSON-LD staat sinds 23-10 uit | niet van toepassing |

Er is op de homepage geen microdata met itemscope en geen itemprop: de homepagekaarten (collectiekaarten en productkaarten) zijn gewone HTML.

## 2. Waarom precies deze drie items

De sectie `tr-reviews` leest `shop.metafields.judgeme.reviews_grid` (25 reviews, laatst bijgewerkt 23-10-2026 11:38 UTC), toont de eerste 6 reviews met minimaal 4 sterren en minimaal 40 tekens, en zet daarvan in de JSON-LD alle reviews die over een product gaan dat in de winkel staat (shopreviews vallen af). Doorgerekend op de metafield van vandaag levert dat vier Product-items op:

| Volgorde in de lijst | Product | Review van | Zit in zichtbare lijst | In JSON-LD |
|---|---|---|---|---|
| 1 | Theetip Rond | 20-10 | ja | ja |
| 2 | Boeren mok 240 ml | 15-10 | ja | ja |
| 3 | Ovenschaal Vierkant 1550 ml | 10-10 | ja | ja |
| 4 | Tante Rie (shopreview) | 10-10 | ja | nee, shopreview |
| 5 | Geluksthee | 29-08 | ja | ja |
| 6 | "Jij bent top" (product niet meer in de winkel) | 03-08 | ja | nee, `product_in_store` is onwaar |

De grafiek in Search Console toont 3 tot 4 items per dag, en Mark ziet er drie: Boeren mok, Geluksthee en Ovenschaal Vierkant. Dat past op deze lijst van vandaag (4 Product-items; Theetip Rond is dan het vierde item dat de grafiek meetelt, een afleiding, want het voorbeeld toont er drie). Een kanttekening: de reviews van Theetip Rond, Boeren mok en Ovenschaal zijn van oktober, terwijl de grafiek sinds begin september 3 tot 4 items toont. Alleen Geluksthee (review van 29-08) kan er al in september in hebben gestaan. De reviewlijst in de metafield verandert met elke nieuwe review, dus in september stonden er waarschijnlijk andere producten in dezelfde constructie; de oude samenstelling is niet meer te achterhalen. Het mechanisme (een lijst van 3 tot 4 producten met een review in de eerste zes) verklaart het constante aantal, de namen zijn van vandaag.

Waarom ze de fout geven: alle vier de producten zijn actief en online (Geluksthee, 15 op voorraad; Ovenschaal, 1; Boeren mok, 36; Theetip Rond, 4; alle vier hebben een foto), dus het ligt niet aan voorraad of aan het product zelf. De uitgelichte ItemList heeft offers en wordt niet gemeld. Het enige dat deze drie delen is dat ze als `itemReviewed` zonder offers in een Review staan. Dit is de meest waarschijnlijke oorzaak op basis van de code, niet bevestigd met een Rich Results Test, omdat de live pagina niet bereikbaar was.

Bijkomend: de melding "Kan niet doorgaan met validatieproces" past hierbij. Google test bij validatie direct opnieuw een steekproef van de getroffen URL's; omdat de markup nog ongewijzigd in de homepage staat, faalt dat meteen.

Waarom de eerdere fix de melding niet weghaalde: op 21-10 zijn alleen de vier uitgelichte producten in `tr-homepage-redesign` van offers voorzien (de "8 Product-items" uit de audit waren dus waarschijnlijk 4 uitgelichte plus 4 uit de reviewlijst). De reviewlijst is toen niet nagelopen.

## 3. Voorstel homepage: voor en na

Bestand: `sections/tr-reviews.liquid`. De zichtbare reviews blijven ongewijzigd. Alleen het `capture`-blok `reviews_ld` en het `<script type="application/ld+json">` worden verwijderd, en het commentaar bovenaan wordt aangepast.

Voor (kort):

```liquid
{%- capture reviews_ld -%} ... "@type": "Review", ... "itemReviewed": { "@type": "Product", "name": ..., "url": ... } ... {%- endcapture -%}
<script type="application/ld+json"> { "@type": "ItemList", "name": "Klantbeoordelingen Tante Rie", "itemListElement": [{{ reviews_ld }}] } </script>
```

Na: geen JSON-LD in deze sectie. De sectie toont de reviews als HTML.

Waarom (a) en niet (b):

1. Een Review met `itemReviewed` op de homepage is voor Google geen geldig reviewfragment van de homepage: de reviews gaan over producten die een eigen pagina hebben. De richtlijnen vragen dat de beoordeelde zaak op de pagina zelf staat en beschreven wordt.
2. De reviews staan al op de plek waar ze horen: het Product-blok van elke productpagina bevat `review[]` (tot 10) en `aggregateRating` (changelog 23-10, Productschema Pakket en reviews). Er gaat dus geen informatie verloren voor Google.
3. Optie (b) zou voor elk reviewproduct een volledig Product-blok met offers, verzend- en retourgegevens op de homepage zetten. Dat dupliceert prijs en voorraad van de productpagina (kans op afwijkingen tussen homepage en productpagina in Merchant Center) en maakt het kwetsbaar: bij elke nieuwe review kan een ander product binnenkomen, ook een uitverkocht, offline of kassa-only product.
4. Het verwijderen is de kleinste wijziging (één bestand, alleen JSON-LD) en lost de melding op. Voor de aantallen: 4 Product-items verdwijnen van de homepage.

Over de ItemList met de vier uitgelichte producten in `tr-homepage-redesign` (die werkt en is niet gemeld): laten staan. Dit is een eigen afweging voor later. Google raadt voor overzichtspagina's een ItemList met alleen `url` en `position` aan. De huidige variant met offers is geldig, maar valt uit zodra een uitgelicht product geen foto of prijs krijgt. Wil Mark die ook versoberen, dan is dat een tweede, kleine wijziging; ik stel die niet nu voor, omdat hij niet meldt.

## 4. Collectiepagina's: komt dit daar ook voor

Ja, maar het is een andere vorm en een andere fout.

1. De zes theecollecties groene-thee, zwarte-thee, kruidenthee, rooibos, witte-thee en vruchten-thee, plus rice, joeff, blond en bunzlau (10 secties, `sections/tr-collection-*.liquid`): elke productkaart is `itemscope itemtype="https://schema.org/Product"` met `itemprop` voor image, category, name en een Offer met prijs en valuta. Offers zijn er dus wel (geen melding "offers moet zijn gespecificeerd"), maar `image` valt weg zodra een product geen foto heeft. De kaart toont dan een pictogram en de microdata heeft geen `itemprop="image"`.
2. De generieke sectie `tr-collection-redesign` (gebruikt door onder meer de standaardcollectie) heeft geen Product-microdata op kaarten.
3. Extra risico op deze secties: de kaarten hebben geen `url` en geen `availability`, en Google behandelt een pagina met meerdere Product-microdata-items als een mogelijke productvermelding. Dat is precies de situatie die de Verkopersvermeldingen-melding oplevert.

Search Console meldt alleen /collections/joeff. Dat betekent niet dat de andere negen veilig zijn: zodra in een van die collecties een online product zonder foto staat, krijgen ze dezelfde melding. Bij bunzlau is dat het meest waarschijnlijk (27 online producten zonder foto volgens de Merchant-analyse van 23-10, waaronder bunzlau-textiel).

### De drie Joeff-items (melding 2)

Via de Shopify-koppeling, alleen lezen:

| Product | Status | Afbeeldingen | Aangemaakt | Laatst gewijzigd | Online winkel |
|---|---|---|---|---|---|
| Grote ring (grote-ring) | actief | 0 | 23-10 14:51 UTC | 24-10 08:10 UTC | niet gepubliceerd (geen online URL, `publishedAt` leeg) |
| Handdoekhaakje (handdoekhaakje) | actief | 0 | 23-10 14:50 UTC | 24-10 08:10 UTC | idem |
| Kleine ring (kleine-ring) | actief | 0 | 23-10 14:50 UTC | 24-10 08:10 UTC | idem |

Alle drie zitten in de collectie joeff, hebben voorraad (10, 12 en 10) en hebben nul afbeeldingen. Ze staan op dit moment niet op de Online winkel, dus ze horen als kassaproduct niet op de collectiepagina te staan en een 404 op hun productpagina is correct (niet doorsturen, niet publiceren zonder overleg met Mark).

Oorzaak, met een voorbehoud: de kaart van een product zonder foto geeft Product-microdata zonder image. De piek van eind oktober (ongeveer 3 items) valt precies na het aanmaken van de drie producten op 23-10. Mijn verklaring is dat ze rond 23 en 24 oktober kort online stonden (bijvoorbeeld door de collectie of een bulkactie) en dat Google ze in die tijd heeft gezien, waarna ze op 24-10 om 08:10 zijn teruggezet. Dat kan ik niet bevestigen: ik heb geen toegang tot de publicatiehistorie van het verkoopkanaal (de koppeling heeft de scope read_product_listings niet). Dat de producten pas op 23-10 zijn aangemaakt, betekent ook dat de pieken van eind juli tot eind augustus (4 tot 6 items per dag) door andere producten komen; welke, is uit de Shopify-gegevens niet te zeggen en staat alleen in het rapport Verkopersvermeldingen (voorbeeld-URL's, geschiedenis per item).

Verwacht gedrag: omdat de producten niet meer op de pagina staan, verdwijnt de melding vanzelf zodra Google de collectie opnieuw crawlt. Het structurele probleem blijft: elke nieuwe online product zonder foto in een collectie geeft opnieuw deze fout.

## 5. Voorstel collecties: voor en na

Bestanden (10): `sections/tr-collection-blond.liquid`, `-bunzlau`, `-groene-thee`, `-joeff`, `-kruidenthee`, `-rice`, `-rooibos`, `-vruchten-thee`, `-witte-thee`, `-zwarte-thee`.

Voor, per productkaart (voorbeeld Joeff):

```liquid
<article class="trjf-card" role="listitem" itemscope itemtype="https://schema.org/Product">
  ... <img ... itemprop="image"> ...
  <span class="trjf-card-type" itemprop="category">...</span>
  <p class="trjf-card-name" itemprop="name">...</p>
  <span class="trjf-card-price" itemprop="offers" itemscope itemtype="https://schema.org/Offer">
    <meta itemprop="priceCurrency" content="EUR">
    <meta itemprop="price" content="...">
```

Na: dezelfde HTML zonder `itemscope`, `itemtype` Product en Offer, `itemprop="image"`, `itemprop="category"`, `itemprop="name"`, `itemprop="offers"` en de twee `meta`-regels. Wat blijft staan: `CollectionPage` met `itemprop="name"` (meta), `description` (de SEO-description van 22-10) en `headline`. Het BreadcrumbList-blok uit `schema-structured-data.liquid` blijft ook. Zichtbaar verandert er niets: het zijn alleen attributen en onzichtbare `meta`-tags.

Alternatief (b), kleiner maar minder schoon: `itemscope` alleen omzetten als `product.featured_image` bestaat (`{% if product.featured_image %} itemscope itemtype=... {% endif %}`). Dit lost "ontbrekend image" op, maar houdt Product-markup zonder url, availability of shippingDetails op overzichtspagina's, en de microdata-Offer mist `availability` en `url`, waardoor Merchant listings-waarschuwingen blijven kans houden. Ik raad het af, behalve als Mark de microdata om een andere reden wil behouden.

Wat er mee verloren gaat: niets dat Google toont. Een collectiepagina kan geen Product-rijke resultaten krijgen; de productpagina's hebben hun eigen volledige JSON-LD (offers, review, aggregateRating, verzending, retour). Het voordeel van (a): geen risico meer op image-, offers- of brand-meldingen vanuit overzichtspagina's, nu of bij nieuwe producten.

## 6. Hoe te testen na akkoord

Volgens de vaste werkwijze, in een kopie van het thema (theme duplicate of aparte branch), nooit direct live, na akkoord van Mark:

1. Kopie van het live thema maken, diff toepassen (`patch -p1 < voorstel-homepage-productmarkup-2026-10-25.diff`), preview-URL openen.
2. Rich Results Test op de preview van de homepage (verwacht: geen Product-items meer, alleen ItemList van de vier uitgelichte producten, FAQ, LocalBusiness en WebSite), op /collections/joeff en op /collections/bunzlau (verwacht: geen Product-items, wel BreadcrumbList).
3. Controle dat de zichtbare reviewsectie en de kaarten visueel gelijk zijn (screenshot voor en na op mobiel).
4. Daarna pas pushen van deze 11 bestanden met `--only` naar het live thema, backup in `scripts/archief-themas/` zoals bij eerdere pushes, regel in `marketing/changelog.md`.
5. Daarna in Search Console in de rapporten Productfragmenten en Verkopersvermeldingen op "Oplossing valideren" klikken (handwerk Mark, V95); pas dan kan Google de validatie afronden. Verwacht wordt dat de validatie slaagt zodra Google de homepage en de collecties opnieuw heeft gecrawld.

## 7. Open punten en nieuwe vragen voor Mark

Niet in `vragen-voor-mark.md` gezet (opdracht), maar voor de hoofdsessie om toe te voegen:

1. Akkoord om de Review-JSON-LD van de homepage weg te halen en de Product-microdata van de kaarten in de 10 collectiesecties te verwijderen (keuze a), of liever de kleinere variant (b)?
2. Zijn Grote ring, Handdoekhaakje en Kleine ring rond 23-24 oktober bewust of per ongeluk even op de Online winkel gepubliceerd geweest? En komen er foto's voor deze producten als ze later wel online gaan? (Zonder foto niet publiceren.)
3. Mag de ItemList met de vier uitgelichte producten later worden teruggebracht naar alleen url en position (optioneel, geen haast)?
