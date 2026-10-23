# Voorstel fixes Hoog, 21 oktober 2026

Status: alleen voorbereid. Er is niets gepubliceerd, geduplicatet of gewijzigd in Shopify, het thema of de store-data, en er is niets in changelog.md geschreven. De themawijzigingen staan in een lokale git-kopie van het live thema.

Bronnen en locaties:
- Live thema "Agent-ready koppen 2026-10-09" (#203153015048), alleen gelezen met `shopify theme pull`, in `/Users/markvanwijk/Tante Rie SEO/scripts/theme-live-2026-10-21/` (baseline-commit "live baseline 2026-10-21", daarna vier commits: Hoog 1 + Middel 3, Hoog 3, verzendtarief per gewichtsklasse, levertijd).
- Referentiethema's, alleen gelezen: `scripts/theme-ref-199507345672/` (SEO-fase4-schema-fixes preview 2026-07-26) en `scripts/theme-ref-202361864456/` (SEO-audit-fixes 2026-09-25).
- Volledige diff: `marketing/technisch/voorstel-fixes-hoog-2026-10-21.diff` (8 bestanden, 4 commits; zie `git diff 13aa7df..HEAD`).
- Hoog 2 (404's) is afgehandeld op basis van Marks besluit, zie onderaan.

## Samenvatting

1. Hoog 1 en Middel 3 (structured data): elk product krijgt nu precies een Product- en een BreadcrumbList-blok. Standaard thee- en accessoireproducten gaan via dezelfde bron (`tr-product-schema`) als de gespecialiseerde templates en krijgen daardoor shippingDetails en hasMerchantReturnPolicy. Rice-, joeff- en waterflesproducten krijgen geen tweede blok meer. Het grootste deel van deze oplossing bestond al in het thema "SEO-audit-fixes 2026-09-25", dat nooit live is gegaan. Ik heb die logica hergebruikt en een aantal dingen toegevoegd of aangepast (zie Hoog 1).
2. Hoog 3 (mobiele snelheid): het live thema heeft al veel van wat de audit voorstelde (srcset op de hoofdafbeelding, fetchpriority, preconnect, display=swap, niet-blokkerende lettertypen, defer en lage prioriteit op scripts). Ik heb daarom alleen kleine markupwijzigingen gedaan voor afbeeldingsmaten (srcset en sizes op productkaarten en de hoofdafbeelding). De grote winst zit in render-blocking CSS en apps en is een voorstel, geen wijziging.
3. Hoog 2 (404's): besluit van Mark, geen redirect, de 404 blijft staan. Luminlique-producten staan alleen in de POS voor de kassa in de winkel.

Afwijkingen tussen de audit (gebaseerd op ~/TanteRie-Theme-Editor) en het live thema:
- `schema-structured-data.liquid:11-13`: klopt, zelfde regelnummers.
- `product-cro.liquid`: het live Product-blok staat op regel 519 (audit: 522) en heeft helemaal geen `@id` (de audit noemde een relatieve `@id`). Er is ook geen enkel actief product dat dit template nodig heeft aangetoond: beste-van-borne gebruikt template `thee`, niet `cro`. Het live Product op beste-van-borne is dus het gewone blok uit `schema-structured-data`, zonder verzend- en retourgegevens.
- Homepage-ItemList: de live versie (`tr-homepage-redesign.liquid:299-340`) geeft alle 4 Product-items al een `offers`. De fout "8 Product-items zonder offers" komt uit een oudere crawl en is waarschijnlijk al weg. Controleer dat in de Rich Results Test.
- `tr-product-redesign.liquid:238` (hoofdafbeelding): live staat het op regel 233 en heeft al `srcset` (450 tot 1400) en `sizes`. De audit zei dat die ontbraken, dat klopt niet meer.
- HowTo staat live in `tr-product-redesign.liquid:512-535` (audit: 515-525).
- De regels voor Google Fonts staan live op `theme.liquid:41-44`, met preconnect, `display=swap` en niet-blokkerend laden (audit: 46-49).

## Akkoord nodig van Mark

### Besluiten van Mark op 21 oktober 2026 (verwerkt)

1. Levertijd: JA. Het schema volgt nu het verzendbeleid: verwerking 1 tot 2 werkdagen, bezorging 1 werkdag (commit afb8147).
2. Retour van ongeopende losse thee: NEE. Thee blijft "MerchantReturnNotPermitted" in het schema. OPEN PUNT VOOR MARK: het geschreven retourbeleid in Shopify (Instellingen, Beleid) staat ongeopende losse thee nog wel toe ("Deze artikelen mogen alleen worden geretourneerd wanneer de verpakking volledig ongeopend, intact en ongebruikt is"). Dat beleid moet Mark zelf aanpassen, anders wijkt het schema af van het beleid. Ik heb het beleid niet gewijzigd.
3. Testkopie: JA. Aangemaakt als ongepubliceerd thema "SEO-fixes-hoog preview 2026-10-21" (id 203908153608), zie het testrapport hieronder.
4. Gewichtenlijst: JA. Zie het onderdeel "Producten zonder gewicht".
5. Verzendtarief: brievenbuspakje 4,50 euro en grotere verpakkingen 6,95 euro, verwerkt per gewichtsklasse (commit 9926124).

### Nog te beantwoorden

1. Mag de wijziging van Hoog 1, Middel 3, verzendtarief en levertijd (commits 22d37d4, 9926124 en afb8147) live worden gezet na het testrapport (ja/nee)? Pas daarna publiceren. Er is niets live gezet.
2. Mag de afbeeldingswijziging voor Hoog 3 (commit d848aed) live mee (ja/nee)?
3. Controleer het verzendtarief in Shopify (Instellingen, Verzending en bezorging) tegen de checkout: klopt 4,50 tot en met 300 gram en 6,95 daarboven, en is het lege profiel "Thee" (4,25) bewust leeg (ja/nee)? Zie "Verzendtarief per productgroep".
4. Klopt het dat Bunzlau- en Blond-producten alleen afgehaald worden in Borne, zodat ze `doesNotShip` krijgen (ja/nee)? Hier heeft Mark nog niet over besloten; de preview toont `doesNotShip` voor Bunzlau en Blond. Antwoord je nee, dan haal ik die wijziging uit commit 22d37d4.
5. HowTo-blok op theeproducten laten staan (mijn advies) of verwijderen (ja = laten staan, nee = verwijderen)?
6. Mogen de collectie-afbeeldingen van de homepage (PNG, tot 240 KB per stuk) opnieuw worden aangemaakt als WebP of JPG (ja/nee)?
7. Wil je de voorstellen uit het onderdeel "Voorstellen met risico" bij Hoog 3 laten uitwerken (ja/nee per punt)?

## Testrapport preview-thema (ongepubliceerd)

Thema "SEO-fixes-hoog preview 2026-10-21", id 203908153608, aangemaakt met `shopify theme duplicate` van het live thema 203153015048. Voor het pushen is een nieuwe pull van live vergeleken met de baseline (13aa7df): geen enkel bestand was gewijzigd. Er zijn met `--only` alleen de 8 gewijzigde bestanden naar het preview-thema gepusht. Niets naar het live thema, geen publicatie.

Preview-URL: https://tanterie.nl/?preview_theme_id=203908153608 (of https://0qkm31-r6.myshopify.com?preview_theme_id=203908153608). Op 21 oktober 2026 per pagina opgehaald met curl (cookie bewaard, pauzes van 5 seconden, geen 429) en de HTML nagelopen op Liquid-fouten en de JSON-LD geparsed. De opgehaalde HTML staat in `/Users/markvanwijk/Tante Rie SEO/data/preview-2026-10-21/`.

| Pagina | Product | Breadcrumb | JSON geldig | Liquid-fouten | Offer: verzending | Levertijd (verwerking, bezorging) | Retour |
|---|---|---|---|---|---|---|---|
| Homepage | 0 (ItemList met offers) | 0 | ja | geen | niet van toepassing | niet van toepassing | niet van toepassing |
| Collectie bunzlau | 0 (CollectionPage) | 1 | ja | geen | niet van toepassing | niet van toepassing | niet van toepassing |
| rice-j (rice) | 1 | 1 | ja | geen | 4.50 | 1-2 en 1 dag | 14 dagen |
| earl-grey (thee) | 1 | 1 | ja | geen | 4.50 | 1-2 en 1 dag | NotPermitted |
| beste-van-borne (thee, uitverkocht) | 1 | 1 | ja | geen | 4.50 | 1-2 en 1 dag | NotPermitted |
| exotic-punch (standaard thee) | 1 | 1 | ja | geen | 4.50 | 1-2 en 1 dag | NotPermitted |
| ledkaars-schakel (joeff) | 1 | 1 | ja | geen | 4.50 | 1-2 en 1 dag | 14 dagen |
| waterfles-delfts-blauw (waterfles) | 1 | 1 | ja | geen | 4.50 (290 g) | 1-2 en 1 dag | 14 dagen |
| maatschepje (accessoires) | 1 | 1 | ja | geen | 4.50 | 1-2 en 1 dag | 14 dagen |
| love-green-girl (blond) | 1 | 1 | ja | geen | doesNotShip | niet van toepassing | 14 dagen |
| boeren-mok-240-ml (bunzlau) | 1 | 1 | ja | geen | doesNotShip | niet van toepassing | 14 dagen |
| aardbeien-cakemix-500-gram (bakmix 500 g) | 1 | 1 | ja | geen | 6.95 | 1-2 en 1 dag | 14 dagen |
| carrot-cakemix-500-gram (bakmix) | 1 | 1 | ja | geen | 4.50 (gewicht in Shopify is 0 of laag, zie twijfelgevallen) | 1-2 en 1 dag | 14 dagen |

Alle producten met een Product-blok hebben een absolute `@id`, `offers`, `shippingDetails` en `hasMerchantReturnPolicy`, een afbeelding, en slechts een Product en een BreadcrumbList. Geen dubbele merken meer op rice-j (merk Rice) en geen tweede BreadcrumbList. De `srcset` en `sizes` uit Hoog 3 staan in de homepage, de collectie en de productpagina.

Afwijkingen en beperkingen:
- De twee eerst gekozen testproducten bleken geen online product te zijn (boeren-cakemix-500-gram en 1060-theepot-1-3-liter zijn POS-only en geven een 404). Ik heb ze vervangen door aardbeien-cakemix-500-gram en boeren-mok-240-ml.
- Bakmix aardbeien-cakemix krijgt 6.95 (500 gram), carrot-cakemix 4.50. Beide heten "500 gram", maar het gewicht van carrot-cakemix staat in Shopify op 0. Zie "Producten zonder gewicht".
- De Rich Results Test is niet door mij gedraaid (geen toegang tot de tool). Open de links hieronder zelf. Let op: Google haalt de pagina zonder cookie op, en de `preview_theme_id` zet een cookie via een redirect. De test kan daardoor de live pagina tonen in plaats van het preview-thema. Als de uitkomst nog het oude schema laat zien (twee Product-blokken bij rice-j), plak dan de opgeslagen HTML uit de map `data/preview-2026-10-21/` in het tabblad "Code" van de Rich Results Test.

Rich Results Test-links:

- Homepage: https://search.google.com/test/rich-results?url=https%3A%2F%2Ftanterie.nl%2F%3Fpreview_theme_id%3D203908153608
- Collectie bunzlau: https://search.google.com/test/rich-results?url=https%3A%2F%2Ftanterie.nl%2Fcollections%2Fbunzlau%3Fpreview_theme_id%3D203908153608
- rice-j (rice): https://search.google.com/test/rich-results?url=https%3A%2F%2Ftanterie.nl%2Fproducts%2Frice-j%3Fpreview_theme_id%3D203908153608
- earl-grey (thee): https://search.google.com/test/rich-results?url=https%3A%2F%2Ftanterie.nl%2Fproducts%2Fearl-grey%3Fpreview_theme_id%3D203908153608
- ledkaars-schakel (joeff): https://search.google.com/test/rich-results?url=https%3A%2F%2Ftanterie.nl%2Fproducts%2Fledkaars-schakel%3Fpreview_theme_id%3D203908153608
- waterfles-delfts-blauw (waterfles): https://search.google.com/test/rich-results?url=https%3A%2F%2Ftanterie.nl%2Fproducts%2Fwaterfles-delfts-blauw%3Fpreview_theme_id%3D203908153608
- love-green-girl (blond): https://search.google.com/test/rich-results?url=https%3A%2F%2Ftanterie.nl%2Fproducts%2Flove-green-girl%3Fpreview_theme_id%3D203908153608
- boeren-mok-240-ml (bunzlau): https://search.google.com/test/rich-results?url=https%3A%2F%2Ftanterie.nl%2Fproducts%2Fboeren-mok-240-ml%3Fpreview_theme_id%3D203908153608
- beste-van-borne (thee): https://search.google.com/test/rich-results?url=https%3A%2F%2Ftanterie.nl%2Fproducts%2Fbeste-van-borne%3Fpreview_theme_id%3D203908153608
- aardbeien-cakemix-500-gram (bakmix): https://search.google.com/test/rich-results?url=https%3A%2F%2Ftanterie.nl%2Fproducts%2Faardbeien-cakemix-500-gram%3Fpreview_theme_id%3D203908153608
- carrot-cakemix-500-gram (bakmix): https://search.google.com/test/rich-results?url=https%3A%2F%2Ftanterie.nl%2Fproducts%2Fcarrot-cakemix-500-gram%3Fpreview_theme_id%3D203908153608
- maatschepje (accessoires): https://search.google.com/test/rich-results?url=https%3A%2F%2Ftanterie.nl%2Fproducts%2Fmaatschepje%3Fpreview_theme_id%3D203908153608
- exotic-punch (standaard): https://search.google.com/test/rich-results?url=https%3A%2F%2Ftanterie.nl%2Fproducts%2Fexotic-punch%3Fpreview_theme_id%3D203908153608

Publiceren gebeurt pas na dit testrapport en een laatste go van Mark. Het preview-thema blijft ongepubliceerd staan; verwijderen kan in Shopify (Online winkel, Thema's) als het niet meer nodig is.

## Producten zonder gewicht

Export: `/Users/markvanwijk/Tante Rie SEO/data/2026-10-21-producten-zonder-gewicht.csv` (alleen lezen via GraphQL en de publieke storefront-gegevens). Kolommen: titel, handle, product type, vendor, variant, sku, status, gepubliceerd online (ja/nee), en een extra kolom POS-only (ja/nee). Online gepubliceerde producten staan bovenaan, daarna de POS-only producten.

Inhoud: 2.739 regels. Dat zijn 2.448 variantregels voor 240 online producten en 291 regels voor 290 POS-only producten (actief, niet gepubliceerd in de online winkel). Voor een deel van de POS-only Bunzlau- en Rice-producten met veel varianten (bijvoorbeeld Tulp mok 200 ml met 59 varianten) staat een regel per product met het aantal varianten in de kolom variant, niet een regel per variant. Concept- (294) en gearchiveerde producten (5) zijn niet opgenomen, omdat ze nergens verkocht worden; zeg het als je ze ook wilt. Producten met een gewicht boven 0 zijn niet opgenomen (bijvoorbeeld de ricebowls met 100 gram).

## Hoog 1 en Middel 3. Product-schema dubbel en onvolledig

### Probleem (getallen uit de audit)

Op rice-j (en alle producten met template rice, joeff of waterfles) staan twee Product-blokken met verschillende merken (Tante Rie en Rice) en twee BreadcrumbList-blokken. Search Console geeft "Duplicate field brand". De standaard thee- en accessoireproducten missen shippingDetails en hasMerchantReturnPolicy (waarschuwing op bijna alle producten). Gemeten op de live pagina's op 21 oktober 2026:

| Pagina | Product-blokken | BreadcrumbList | Verzend en retour in Offer |
|---|---|---|---|
| /products/rice-j | 2 (merk Tante Rie en Rice) | 2 | alleen in het tweede blok |
| /products/ledkaars-schakel (joeff) | 2 (beide Joeff) | 2 | alleen in het tweede blok |
| /products/earl-grey (thee) | 1 | 1 | nee |
| /products/beste-van-borne (thee) | 1 | 1 | nee |

Alle JSON-LD op deze pagina's is geldig JSON (geen syntaxfouten, gecontroleerd op de opgehaalde HTML).

### Wat al eerder was gedaan

Thema "SEO-audit-fixes 2026-09-25" (#202361864456) bevat al de kern van deze oplossing en is nooit live gezet: de uitsluitingslijst voor rice, joeff en waterfles, het renderen van `tr-product-schema` vanuit de layout voor thee, accessoires en standaardproducten, en een afhaalvariant voor Bunzlau en Blond. Dit thema bevat ook andere wijzigingen (paginering van collecties op 48 producten, een nieuwe `tr-pagination`, een tekstwijziging op de lokaalpagina waarin "2024" is veranderd in "2014", een herformattering van `index.json`). Die heb ik bewust niet meegenomen. Let op de tekstwijziging naar 2014: controleer of dat klopt voordat dat thema ooit wordt gepubliceerd.

Thema "SEO-fase4-schema-fixes preview 2026-07-26" (#199507345672) is ouder: het sluit alleen `cro` uit en zou dus juist meer dubbele blokken geven bij de huidige secties. Het bevat geen schema-fix die nog bruikbaar is. Het verschilt ook op ruim 30 andere bestanden van live en is verouderd.

### Wat verandert (commit 22d37d4)

1. `snippets/schema-structured-data.liquid`: overgenomen uit audit-fixes. Rice, joeff en waterfles worden uitgesloten van het algemene blok (de sectie rendert zelf). Thee, accessoires en standaardproducten (geen template-suffix) renderen `tr-product-schema` vanuit de layout en slaan het algemene Product- en breadcrumbblok over. Het algemene blok blijft alleen als terugval voor onbekende templates, nu met shippingDetails en hasMerchantReturnPolicy.
2. Nieuw: `snippets/tr-offer-policies.liquid`. De verzend- en retourgegevens stonden hardcoded in `tr-product-schema`. Ze zijn verplaatst naar dit snippet (uitvoer bewezen identiek, zie Testen) zodat `tr-product-schema`, de terugval en `product-cro` een bron delen.
3. `snippets/tr-product-schema.liquid`: gebruikt het nieuwe snippet. Voor templates `bunzlau` en `blond` komt er `doesNotShip` en `availableDeliveryMethod: OnSitePickup` (idee uit audit-fixes). Het retourgedeelte van audit-fixes (`ReturnInStore`, `FreeReturn`) heb ik niet overgenomen, omdat dat een beleidskeuze is die nergens in de shopbeleid staat.
4. `sections/product-cro.liquid`: absolute `@id` (`request.origin` plus product-URL), en verzend- en retourgegevens via het gedeelde snippet.
5. Middel 3, dubbele BreadcrumbList: verdwijnt door punt 1, omdat rice, joeff en waterfles niet langer een tweede breadcrumb krijgen.
6. Middel 3, HowTo: laten staan (zie "Beoordeling HowTo").

Waarden voor verzending en retour komen uit het bestaande `tr-product-schema` en zijn gecontroleerd tegen de Shopify-instellingen (lezen via GraphQL):
- Verzendkosten: sinds commit 9926124 per gewichtsklasse, zie het onderdeel "Verzendtarief per productgroep" hieronder.
- Retourtermijn 14 dagen en retourkosten voor de klant: klopt met het retourbeleid.
- Levertijd: verwerkt op besluit van Mark (commit afb8147): verwerking 1 tot 2 werkdagen en bezorging 1 werkdag, conform het verzendbeleid.
- Losse thee: het schema blijft "NotPermitted" (besluit van Mark). OPEN PUNT VOOR MARK: het geschreven retourbeleid staat ongeopende thee nog wel toe en moet door Mark worden aangepast, anders wijkt het schema af van het beleid.

POS-only producten (zoals Luminlique) worden niet online gerenderd en hebben dus geen invloed op deze wijziging.

### Verzendtarief per productgroep (commit 9926124)

Besluit van Mark: brievenbuspakje 4,50 euro, grotere verpakkingen 6,95 euro. Het schema gebruikt nu die twee bedragen per product in plaats van een vast bedrag.

Gevonden in Shopify (alleen gelezen): het verzendprofiel "Algemeen profiel" (bevat onder meer alle thee, accessoires en Bunzlau-mokken; Shopify telt het aantal varianten hier tot 500) rekent in Nederland op totaal gewicht: "Standaard" 4,50 euro voor 0 tot en met 300 gram en "Pakket" 6,95 euro voor 301 tot en met 5000 gram. Het profiel "Thee" (met brievenbuspakket 4,25 en pakket 6,95) bevat geen enkel product (0 varianten) en wordt dus niet gebruikt. Daarmee is het eerder gemelde bedrag van 4,25 niet van toepassing; het tarief dat de checkout toepast is 4,50. Het profiel "Breekbare producten" (Bunzlau, Blond en andere keramiek) heeft helemaal geen verzendtarieven voor Nederland.

Gekozen kenmerk: het laagste variantgewicht van het product (`variant.weight` in gram). Tot en met 300 gram geldt 4.50 EUR, daarboven 6.95 EUR. Dat is dezelfde regel als in de Shopify-verzendinstellingen, dus de kans op een verschil met de checkout is klein. Product type, template of tag zijn niet gebruikt, omdat die niets zeggen over de pakketklasse (bijvoorbeeld losse thee en accessoires verschillen niet in tarief, de bakmixen van 500 gram wel). De drempel en bedragen staan op een plek: `snippets/tr-offer-policies.liquid`.

Resultaat op de huidige 422 producten (gewicht van de eerste variant): 416 krijgen 4.50 en 6 krijgen 6.95 (appeltaartmix 500 g, speculaasmix 850 g, fruitycakemix, stroopwafelcakemix, aardbeien-cakemix en wonder-cakemix, alle 500 g).

Twijfelachtige producten:
- 232 producten hebben gewicht 0 in Shopify (voornamelijk keramiek, Blond-mokken, verschillende accessoires en 6 "Maak je eigen theemix"). De checkout rekent die als 0 gram, dus 4,50 euro. Het schema doet hetzelfde en komt dus overeen met de checkout. Maar voor zware items (keramiek) is dat waarschijnlijk niet de echte verzendkostenklasse. Bunzlau en Blond krijgen later (als Mark akkoord geeft) toch `doesNotShip`. Voor overige producten zonder gewicht (bijvoorbeeld 'ovenwant', 'schort', 'glutenvrije mixen') is controle van het gewicht in Shopify de echte oplossing.
- De waterflessen wegen 284 tot 290 gram en vallen net onder de grens, dus 4.50. Een fles past waarschijnlijk niet in een brievenbus. Als Shopify voor een bestelling met een fles in werkelijkheid een pakket rekent (bij twee flessen komt de som boven 300 gram), dan klopt het schema voor een enkele fles maar niet voor meerdere.
- Een bestelling van meerdere producten telt de gewichten op. Het schema beschrijft altijd een enkele eenheid. Dat is een bekende beperking van schema.org en Google vergelijkt alleen met de verzendkosten voor een enkel product.
- `ontbijtbord-o-20-cm` heeft varianten van 0 en 510 gram. Het laagste gewicht bepaalt het tarief (4.50).
- Producten met template `bunzlau` en `blond`: tarief niet van belang zolang zij als afhaalproduct worden gedekt (zie vraag 4 bij "Nog te beantwoorden"), omdat dan geen tarief wordt getoond.

OPEN PUNT VOOR MARK: controleer in Shopify (Instellingen, Verzending en bezorging, profiel Algemeen) het tarief, omdat Google het schema vergelijkt met de checkout. Het profiel "Thee" met 4,25 euro bevat geen producten; verwijder of vul het zodat er geen verwarring ontstaat. De tekst "Vanaf 4,50" in de winkelwagen (`snippets/cart-summary.liquid`) is hierop afgestemd.

Test gedaan: met de lokale Liquid-engine zijn de gewichten 0, 100, 300 (4.50), 301, 500, 850 (6.95) en meerdere varianten (290 en 500 geeft 4.50) gerenderd voor de template thee en voor de terugvalroute.

### Voor en na (rice-j, samenvatting)

Voor (live, uit de HTML van 21 oktober):

```
Product  brand=Tante Rie   offers=Y  shippingDetails=N  hasMerchantReturnPolicy=N  (algemeen blok)
BreadcrumbList
BreadcrumbList
Product  brand=Rice        @id=https://tanterie.nl/products/rice-j  shippingDetails=Y  hasMerchantReturnPolicy=Y
```

Na (gerenderd met de nieuwe code, zie Testen):

```
BreadcrumbList
Product  brand=Rice  @id=https://tanterie.nl/products/rice-j  shippingDetails=Y  hasMerchantReturnPolicy=Y
```

Standaard theeproduct (earl-grey), voor en na, alleen de Offer:

```
Voor:  "offers": [ { "@type": "Offer", "name": "...", "price": ..., "availability": "...", "url": "...", "seller": {...} } ]
Na:    "offers": { "@type": "Offer", "url": "...", "price": "8.95", "priceCurrency": "EUR", "availability": "...",
          "itemCondition": "https://schema.org/NewCondition",
          "shippingDetails": { "@type": "OfferShippingDetails", "shippingRate": { "value": "4.50", "currency": "EUR" }, ... },
          "hasMerchantReturnPolicy": { "@type": "MerchantReturnPolicy", "applicableCountry": "NL",
                                       "returnPolicyCategory": "https://schema.org/MerchantReturnNotPermitted" } }
```

Gevolg om op te letten: het gedeelde blok heeft een enkele Offer met de laagste variantprijs, terwijl het oude algemene blok een Offer per variant had. Producten met meerdere varianten (zoals rice-j met 5 varianten) hadden dit al zo in `tr-product-schema`. Voor losse thee met meerdere gewichten verdwijnt de per-variant-lijst. Zet je dat liever anders, dan kan een AggregateOffer worden toegevoegd (extra werk, niet gedaan).

### Homepage-ItemList

De live homepage heeft twee ItemList-blokken. De ene (4 uitgelichte producten) heeft al `offers` bij elk Product-item, dus de fout "Either offers, review, or aggregateRating" is voor dat blok al opgelost in het live thema. De andere ItemList (klantbeoordelingen uit `tr-reviews.liquid`) bevat Review-items met een `itemReviewed` van het type Product zonder offers; dat is toegestaan voor een Review en niet gewijzigd. Veiligste keuze: niets aanpassen, en na publicatie de Rich Results Test op de homepage draaien. Verwijderen van de Product-typering had geen zin gehad, omdat de items al offers hebben en de Product-markup daar juist waarde heeft.

### Beoordeling HowTo (Middel 3)

Google toont geen HowTo-rich-results meer, maar het blok is geldig, schaadt niet en past bij de zichtbare zetadvies-sectie. Het scheelt ongeveer 1 KB HTML per theepagina. Advies: laten staan. Verwijderen kan later zonder risico (de sectie `tr-product-redesign.liquid` regel 512 tot 535).

### Testen en validatie die ik heb gedaan

- Alle JSON-LD-blokken van homepage, rice-j, ledkaars-schakel, earl-grey en beste-van-borne zijn opgehaald met pauzes van 3 seconden (geen 429) en parsen zonder fouten.
- Nieuwe logica gerenderd met een lokale Liquid-engine (python-liquid, met nagebootste Shopify-filters) voor suffix thee, accessoires, standaard, rice, joeff, bunzlau, blond, cro en onbekend: per template precies een Product en een BreadcrumbList, alle blokken geldig JSON. De uitvoer van `tr-product-schema` voor rice, joeff en thee is na het verplaatsen naar het nieuwe snippet identiek aan voor de wijziging. Alleen bunzlau en blond verschillen, zoals bedoeld.
- Beperking: de lokale engine is geen echte Shopify. Dit zijn geen live-gegevens. Een echte controle kan pas na een preview van het thema (zie hieronder). `shopify theme check` meldt geen nieuwe fouten in de gewijzigde bestanden (de bestaande fout `UnknownFilter` in `blocks/flavor-profile.liquid` was er al).

### Risico

Laag tot middel. De wijziging raakt de JSON-LD op alle productpagina's. Het grootste risico is een syntaxfout in Liquid of een ontbrekende komma, waardoor het schema van een template wegvalt. Dat is met de lokale test afgedekt, maar niet met een echte Shopify-render. Per-variant-offers voor standaardproducten verdwijnen. Bunzlau- en Blond-producten verklaren zich als "niet verzonden"; als die toch worden verzonden is dat een fout.

### Testen na publicatie

1. Rich Results Test op /products/rice-j, /products/earl-grey, /products/beste-van-borne, een accessoire, een bakmix, een Bunzlau-product en de homepage: een Product, een BreadcrumbList, geen "Duplicate field brand", Merchant listings zonder waarschuwing voor shippingDetails en hasMerchantReturnPolicy.
2. URL-inspectie in Search Console op dezelfde URL's, na een crawlverzoek, en na een week het rapport Verbeteringen, Producten en Merchant listings.
3. Eerst op een niet-gepubliceerde kopie testen: de thema-preview URL van een kopie, geen live-wijziging nodig.

### Type wijziging

Themawijziging.

## Hoog 3. Mobiele paginasnelheid

### Probleem (uit de audit)

Lighthouse mobiel: homepage 61 (LCP 6,9 s), collectie bunzlau 68 (LCP 5,1 s, Time to Interactive 11,9 s), product earl-grey 60 (LCP 11,3 s). Desktop is goed (87 tot 98). 72 procent van de klikken is mobiel. Dit is labdata; de CrUX-API gaf een 403.

### Wat de Lighthouse-data zegt (data/gsc/2026-10-21-pagespeed-*.json)

| Onderdeel | Cijfer | Pagina's |
|---|---|---|
| Render-blokkerende CSS: `compiled_assets/styles.css` (43 KB, ongeveer 40 KB ongebruikt), `base.css` | tot 1.651 ms en 970 ms wachttijd | alle drie |
| Ongebruikte CSS | 63 KiB (home en bunzlau), 74 KiB (product), geschatte besparing 150 tot 600 ms | alle drie |
| Afbeeldingen groter dan nodig | home 2 productafbeeldingen 84 KB en 78 KB teveel; product hoofdafbeelding 191 KB teveel (900 px JPEG) | home, product |
| Zware collectie-PNG's op de homepage | 242 KB, 229 KB en 111 KB per afbeelding | home |
| Hoofdthread (collectie) | 4,4 s, 11 lange taken | bunzlau |
| Scripts van apps | Judge.me loader 313 ms, Shopify trekkie, perf-kit, checkout-web | product, bunzlau |

### Wat al goed is in het live thema (geen actie nodig)

Hoofdafbeelding product: `fetchpriority="high"`, geen lazy loading, srcset 450 tot 1400. Homepage-hero: `loading="eager"`, `fetchpriority="high"`, srcset tot 1800. Google Fonts: preconnect, `display=swap` en niet-blokkerend via `rel=preload` met onload. Eigen scripts (`tr-cart.js` en andere): `defer`. Thema-scripts: ES-modules met `fetchpriority="low"`.

### Wat ik heb gewijzigd (commit d848aed, alleen markup)

Productkaarten renderden een afbeelding van 400 of 500 px op een plek van ongeveer 180 px (mobiel). Ze krijgen nu een `srcset` met kleinere varianten en `sizes`:
- `sections/tr-homepage-redesign.liquid`: uitgelichte producten (250, 375, 500 px; sizes 50vw tot 900 px, daarboven 280 px).
- `sections/tr-collection-redesign.liquid` en `sections/tr-collection-bunzlau.liquid`: collectiekaarten (250, 375, 500 px; sizes 100vw/50vw/33vw, daarboven 300 px, gelijk aan de rastergrootte van de CSS).
- `sections/tr-product-redesign.liquid`: gerelateerde producten (200 en 400 px) en `sizes` van de hoofdafbeelding houdt nu rekening met de 20 px padding (`calc(100vw - 40px)` onder 990 px).

Voor en na (fragment):

```diff
-<img src="{{ p.featured_image | image_url: width: 500 }}" alt=...>
+<img src="{{ p.featured_image | image_url: width: 500 }}" srcset="... 250w, ... 375w, ... 500w" sizes="(max-width: 900px) 50vw, 280px" alt=...>
```

Verwachte winst: Lighthouse noemt voor deze afbeeldingen ongeveer 60 tot 85 KB besparing per afbeelding op home en ongeveer 61 KB op de productpagina; totaal ruim 150 KB minder op de homepage op mobiel, ongeveer 100 KB minder op de productpagina. Dit raakt de LCP nauwelijks (de LCP-afbeelding was al geoptimaliseerd), maar verlaagt de totale paginagrootte en de dataverbruik. Ik verwacht een winst van maximaal enkele punten in Lighthouse, niet de 20 tot 30 punten die nodig zijn. De wijziging is gebruikt als laagrisico onderdeel, niet als oplossing van de snelheid.

### Voorstellen met risico (niet uitgevoerd)

| Voorstel | Verwachte winst | Type |
|---|---|---|
| Kritieke CSS inline en `compiled_assets/styles.css` en `base.css` asynchroon laden | 1.000 tot 1.650 ms minder blokkade; grootste hefboom voor FCP en LCP | Themawijziging met risico (flits van ongestijlde inhoud); aparte test in een kopie van het thema nodig |
| Ongebruikte CSS (ongeveer 40 KiB in `compiled_assets/styles.css`) verwijderen of per template laden | 150 tot 600 ms, 63 tot 74 KiB | Themawijziging met risico; deze bundel wordt door Shopify samengesteld uit blokken en secties |
| `view-transitions.js` (`blocking="render"`) laten vervallen of niet-blokkerend laden | 150 ms | Themawijziging, standaard Horizon-gedrag; het uitzetten verandert paginaovergangen. Beslissing van Mark |
| Homepage-collectie-afbeeldingen (PNG 111 tot 242 KB) opnieuw uploaden als WebP of JPG op ongeveer 900 px | ongeveer 300 tot 500 KB minder op de homepage, kan LCP op home helpen | Beslissing van Mark en contentwerk in Shopify (Collecties, afbeelding vervangen) |
| Zeer grote JPEG's op productpagina's (hoofdafbeelding 900 px, 213 KB) opnieuw exporteren op 1300 px met meer compressie | ongeveer 100 tot 150 KB per productpagina | Beslissing van Mark en contentwerk |
| Judge.me-loader (313 ms scripttijd op productpagina's) vertraagd laden of de Judge.me-instellingen voor widgets nalopen | ongeveer 300 ms hoofdthread op productpagina's | App-instelling |
| Apps en extensies die scripts in de header laden nalopen (Shopify, shop.app, Shoplift-lettertype op de collectie, 62 tot 64 scripts per pagina) en ongebruikte apps verwijderen | grootste mogelijke winst voor hoofdthread (4,4 s op de collectie) en TBT | App-instelling en beslissing van Mark |
| Product- en collectiepagina's: CrUX-meting activeren (Chrome UX Report API voor de sleutel inschakelen) | geen winst, wel veldgegevens om te meten | Instelling (Google Cloud), beslissing van Mark |
| Afbeeldingen van kaarten in `format: 'webp'` of 'pjpg' forceren | ongeveer 20 tot 30 procent op JPEG's | Themawijziging, laag risico, nog niet nodig omdat Shopify automatisch moderne formaten levert op basis van de browser |

Mijn advies voor de volgorde: eerst PNG's op de homepage vervangen (contentwerk, snelle winst), dan de app-scripts nalopen, dan pas kritieke CSS in een kopie van het thema uitproberen.

### Risico

Laag. Alleen `srcset` en `sizes` zijn toegevoegd. Als `sizes` te klein is gekozen, ziet een kaart er op een hoge-resolutie scherm iets minder scherp uit. Layout verandert niet (de `width` en `height` blijven gelijk).

### Testen na publicatie

1. Lighthouse mobiel (PageSpeed Insights) op de homepage, /collections/bunzlau en /products/earl-grey, drie keer, en vergelijk de totale paginagrootte (Total byte weight) met de oude waarden van 3.293, 2.531 en 3.150 KiB.
2. Visuele controle op een telefoon en een breed scherm van de kaarten (scherpte) en de hoofdafbeelding.
3. CrUX-veldgegevens controleren zodra de API is ingeschakeld.

### Type wijziging

Themawijziging (de wijzigingen); app-instelling en beslissing van Mark (de voorstellen).

## Hoog 2. Twee 404-producten staan nog als geindexeerd

### Besluit

Mark heeft aangegeven dat Luminlique en vergelijkbare producten alleen in Shopify staan voor de kassa in de fysieke winkel (Shopify POS) en bewust niet online worden verkocht. De 404 is daarom correct. Besluit: geen redirect, de 404 blijft staan. De redirect-mutation uit eerdere versies van dit document is vervallen en is hier verwijderd.

### Probleem en status (curl, 21 oktober 2026, met pauzes)

| URL | HTTP | Vertoningen 90d | Klikken 90d |
|---|---|---|---|
| /products/luminlique-3-opzetters | 404 | 46 | 9 |
| /products/luminlique-medium-5-opzetters | 404 | 86 | 7 |
| /products/luminlique-groot-7-opzetters | 404 | 6 | 0 |
| /products/luminlique-los | 404 | 31 | 0 |

Geen van de vier staat in de sitemap. De zoekterm "luminlique" levert 45 vertoningen en 3 klikken op in 90 dagen. Er is geen vervangend product en geen passende collectie gevonden, wat bij POS-only producten past.

### Wat er gebeurt

Niets in Shopify. Google verwerkt de verwijdering vanzelf. Optioneel kan in Search Console een tijdelijke verwijderingsaanvraag worden gedaan (Verwijderingen) voor de vier URL's, om ze sneller uit de resultaten te halen. Dat is Marks keuze.

### Risico en testen

Geen risico. Controleer na vier tot zes weken in de pagina-export van Search Console dat de vier URL's zijn verdwenen. De Hoog 1-melding "Missing field image" bij luminlique-3-opzetters verdwijnt mee.

### Type wijziging

Geen wijziging nodig (besluit van Mark).

## Open vragen voor Mark

1. Controle van het verzendtarief in de Shopify-instellingen (4,50 tot 300 gram, 6,95 daarboven) en het lege profiel "Thee" (4,25).
2. Het geschreven retourbeleid in Shopify staat ongeopende losse thee nog wel toe, terwijl het schema "NotPermitted" zegt. Beleid aanpassen of schema alsnog wijzigen.
3. Zijn Bunzlau en Blond echt alleen af te halen (nog geen besluit)?
4. Welke PNG's op de homepage mogen opnieuw worden aangemaakt als WebP of JPG?
5. Moet audit-fixes 2026-09-25 ooit nog worden gebruikt? Zo ja, eerst de tekstwijziging "2024" naar "2014" op de lokaalpagina nalopen.
6. Gewicht invullen bij de producten in de CSV, zodat verzendtarief in schema en checkout betrouwbaar zijn.

## Livegang 21 oktober 2026

Mark heeft de 8 bestanden zelf met `--only` naar het live thema 203153015048 gepusht (commits 22d37d4, 9926124, afb8147 en d848aed). Ik heb daarna dezelfde 13 pagina's live gecontroleerd, zonder preview-parameter en met pauzes van 5 seconden (geen 429), op dezelfde criteria als bij de preview.

Resultaat: alle 13 pagina's geven 200, de JSON-LD is overal geldig en er staan geen Liquid-fouten in de HTML. Elke productpagina heeft precies een Product en een BreadcrumbList met absolute `@id`. Verzending en levertijd kloppen: rice-j, earl-grey, beste-van-borne, exotic-punch, ledkaars-schakel, waterfles-delfts-blauw, maatschepje en carrot-cakemix 4.50 met verwerking 1-2 en bezorging 1 dag, aardbeien-cakemix 6.95, love-green-girl en boeren-mok-240-ml `doesNotShip`. Thee heeft "NotPermitted", de overige producten een retourtermijn van 14 dagen. Homepage en collectie bunzlau hebben geen Product-blok (homepage ItemList met offers, collectie BreadcrumbList en CollectionPage). Rice-j heeft geen dubbel merk en geen tweede BreadcrumbList meer. Er hoeft niets teruggezet te worden.

Sitemap: de beschikbare scripts (`gsc_query.py`, `gsc_inspect.py`) kunnen sitemaps alleen lezen en niet opnieuw indienen, dus dat is niet gedaan. De Indexing API is niet gebruikt, want die is alleen bedoeld voor JobPosting en BroadcastEvent. Mark kan de sitemap opnieuw indienen in Search Console (Sitemaps, https://tanterie.nl/sitemap.xml). Dat is niet strikt nodig voor een themawijziging, want Google crawlt de pagina's zelf opnieuw.

### Kern-URL's om te laten herindexeren (URL-inspectie, "Indexering aanvragen")

1. https://tanterie.nl/
2. https://tanterie.nl/collections/bunzlau
3. https://tanterie.nl/products/rice-j
4. https://tanterie.nl/products/earl-grey
5. https://tanterie.nl/products/beste-van-borne
6. https://tanterie.nl/products/ledkaars-schakel
7. https://tanterie.nl/products/waterfles-delfts-blauw
8. https://tanterie.nl/products/aardbeien-cakemix-500-gram

Controleer bij elke URL ook "Live URL testen" en het onderdeel Producten en Merchant listings.

### Meetmoment 18-11-2026

Kijk in Search Console bij Verbeteringen (Producten snippets en Merchant listings) en in de Rich Results Test: de fout "Duplicate field brand" op rice-j en vergelijkbare producten moet weg zijn, de waarschuwingen "Missing field shippingDetails" en "Missing field hasMerchantReturnPolicy" moeten sterk gedaald zijn, en er moeten geen nieuwe fouten bij zijn gekomen. Meet Hoog 3 opnieuw met PageSpeed Insights (mobiel) voor de homepage, /collections/bunzlau en /products/earl-grey, en vergelijk met 61, 68 en 60. Noteer de uitkomst in de maandrapportage van de Analist.
