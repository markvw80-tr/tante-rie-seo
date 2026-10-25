# Uitvoering productmarkup (V119, keuze a): themakopie met preview

Opgesteld door Technisch SEO op 25 oktober 2026. Status: themakopie gemaakt en gevuld, niet gepubliceerd. Wacht op Marks publicatie in Shopify admin. Het live thema is niet aangeraakt.

Basis: akkoord van Mark op 25-10 op V119, keuze (a) uit marketing/technisch/voorstel-homepage-productmarkup-2026-10-25.md, uitgevoerd met marketing/technisch/voorstel-homepage-productmarkup-2026-10-25.diff.

## De themakopie

| | |
|---|---|
| Naam | Productmarkup V119 2026-10-25 |
| Theme-id | 204118262024 (gid://shopify/OnlineStoreTheme/204118262024) |
| Rol | UNPUBLISHED |
| Gemaakt als | duplicaat van het live thema 204095619336 ("Bunzlau collectie V118 2026-10-24", rol MAIN, gecontroleerd vlak voor het dupliceren) via themeDuplicate |
| Live thema | niet aangeraakt; na afloop nog steeds 204095619336 met rol MAIN. Alle schrijfacties zijn themeFilesUpsert op 204118262024 |

## Controle vooraf: waren de bestanden gelijk aan wat de diff verwacht?

Ja, alle elf. Van elk bestand is in de kopie de MD5 opgevraagd en vergeleken met de lokale uitgangsversie waarop de diff is gemaakt (zelfde tekst als live V118). Alle elf waren gelijk. De diff paste daarna schoon op de lokale versies (patch --dry-run en patch zonder verschuiving of afgewezen delen). Er is dus geen afwijking gevonden en er is niet gestopt.

## Gewijzigde bestanden (teruggelezen uit de kopie)

Per bestand: schrijven met themeFilesUpsert, daarna de MD5 en de grootte uit de kopie teruggelezen en vergeleken met het lokaal gepatchte bestand. Alle elf zijn gelijk.

| Bestand | MD5 voor (live V118) | Bytes voor | MD5 na (uit de kopie) | Bytes na | Gelijk aan gepatcht bestand |
|---|---|---|---|---|---|
| sections/tr-reviews.liquid | be31e7ee7f1e0bd76617e57add7a4ecd | 8.781 | 147a2bf59a2029877692e4522e052a54 | 7.240 | ja |
| sections/tr-collection-blond.liquid | 9dee9266235166c778e7cf67dac84ff2 | 40.867 | b8c1cf8e1e375e061bcbe364e9568a97 | 40.528 | ja |
| sections/tr-collection-bunzlau.liquid | c9588790efece68e8e2c64018b99c408 | 43.815 | 13a65f2d265dcb33848dc9deb1c519ce | 43.476 | ja |
| sections/tr-collection-groene-thee.liquid | 3bccded44c82e14489af64c3ae4eb357 | 39.043 | 09f631d9e3c6549310a3c77e6b299cbb | 38.704 | ja |
| sections/tr-collection-joeff.liquid | eb99c40135dc14de78d24b12acf470a8 | 43.869 | f2f64f2bceb76b36359f7de9f3426916 | 43.530 | ja |
| sections/tr-collection-kruidenthee.liquid | 74d9cca03f3e1e183025bbf6fb0d30f9 | 38.802 | a5cfa8b6a8434103fed3386c5391c91b | 38.463 | ja |
| sections/tr-collection-rice.liquid | 3609c8ec8d1e31fb7616e57c62063069 | 40.146 | 9eac536b92cef534a299af18d2fc5dbf | 39.825 | ja |
| sections/tr-collection-rooibos.liquid | c7ddfaccb006bbbae58e61ab0c54cc51 | 38.834 | 379387fedb9466972a85127afcbc7642 | 38.495 | ja |
| sections/tr-collection-vruchten-thee.liquid | 6f7c7b9496764618fb03178216040d9c | 38.805 | b1139c59d4a5f890b42ecaa689268005 | 38.466 | ja |
| sections/tr-collection-witte-thee.liquid | 05b728f604c9453008ad55e9d4cc9d3f | 38.846 | 386e27d68e5ffa85d9fa8e38918c29e7 | 38.507 | ja |
| sections/tr-collection-zwarte-thee.liquid | 1b08affcb9e5e9dce2b9fdd81d185ea1 | 38.988 | 970a0dfea655810598596e10f0a920c8 | 38.649 | ja |

Wat de wijziging is, per bestand: in `tr-reviews` is het hele Review-JSON-LD-blok (ItemList met `itemReviewed` van het type Product) verwijderd en is de uitleg bovenin het bestand aangepast. In de tien collectiesecties zijn bij elke productkaart `itemscope itemtype=".../Product"` en de `itemprop`-attributen (image, category, name, offers met priceCurrency en price) verwijderd; de kaarten zelf, hun tekst en de opmaak zijn ongewijzigd. De CollectionPage-microdata op de wrapper (`itemprop="name"`, `"description"`, `"headline"`) blijft.

Over het schrijven: de koppeling kan alleen een bestand als geheel schrijven, dus elk bestand is in zijn geheel opnieuw uitgestuurd. Vier bestanden kwamen de eerste keer niet exact terug: de lijnen met decoratieve tekens in de commentaarregels waren in tr-collection-bunzlau (twee regels), -groene-thee (vier regels) en -rice (een regel) te lang of te kort overgenomen, en in tr-collection-zwarte-thee ontbrak een instellingsblok in het schema. Dat is bij de MD5-controle direct gezien, het bestand is daarna opnieuw geschreven en opnieuw teruggelezen. De bedoelde, goedgekeurde inhoud is verder nergens afgeweken. De uitkomst in de tabel hierboven is de tweede, juiste schrijfronde.

## Controle in de code van de kopie (stap 3)

Gecontroleerd op de kopie 204118262024: alle secties, snippets, blocks en het layout in de kopie (de lokale exportmap van het live thema plus de elf gewijzigde bestanden, met de bestandschecksums van de kopie als controle) en de templates die de homepage en de collectiepagina's samenstellen (templates/index.json en alle templates/collection.*.json, rechtstreeks uit de kopie gelezen).

1. Geen sectie op de homepage of op een collectiepagina geeft nog `itemtype` Product of `itemReviewed` Product uit. `itemReviewed` komt nog maar op een plek voor, en dat is de uitlegtekst in `tr-reviews`.
2. Wat blijft staan, zoals gevraagd:
   - ItemList met de vier uitgelichte producten: `sections/tr-homepage-redesign.liquid` (regel 339, inclusief Offer met price, priceCurrency, availability en url, en image).
   - CollectionPage: in alle tien de collectiesecties (JSON-LD, plus de microdata op de wrapper), en ook in `main-collection` en `tr-collection-redesign`.
   - LocalBusiness: `layout/theme.liquid` regel 76 (naast WebSite).
3. De productpagina's houden hun Product-blok. Microdata `itemtype` Product staat alleen nog in de vier productsecties `tr-product-blond`, `tr-product-bunzlau`, `tr-product-bunzlau-melamine` en `tr-product-joeff` (de producttemplates). JSON-LD Product en Offer staat alleen in `snippets/tr-product-schema.liquid` (alle producttemplates), `snippets/schema-structured-data.liquid` (alleen als `template.name == 'product'`), `sections/product-cro.liquid` (producttemplate cro) en de ItemList op de homepage. Er zijn geen wijzigingen aan die bestanden gedaan.
4. Gezocht in andere secties en snippets naar `itemscope` die op overzichtspagina's terechtkomt: er is niets gevonden. `itemscope` komt in het hele thema alleen voor in de tien collectiesecties (alleen als CollectionPage op de wrapper) en de vier productsecties hierboven. De productkaarten in `snippets/product-card.liquid`, `blocks/_product-card.liquid`, `sections/main-collection.liquid`, `tr-search`, `tr-servies-hub` en `tr-accessoires-redesign` bevatten geen `itemscope`. De Judge.me-snippets en `blocks/review.liquid` bevatten geen `itemscope`, `ld+json` of schema.org-verwijzing. `sections/tr-page-cadeau.liquid` heeft een eigen ItemList met ListItems zonder Product (alleen name, description en url); die staat op /pages/thee-cadeau, geen homepage of collectiepagina, en is niet aangeraakt.
5. De templates: `index.json` gebruikt tr-homepage-redesign, tr-reviews, tr-homepage-blog, tr-homepage-faq en tr-homepage-cta; elke `collection.<naam>.json` gebruikt precies zijn eigen tr-collection-sectie. Geen enkele extra sectie of app-blok.

Een aandachtspunt, geen fout: de vier Product-items in de ItemList op de homepage hebben image en offers maar geen review of aggregateRating. Die velden zijn optioneel, maar als Google daarover een niet-kritieke waarschuwing toont bij Productfragmenten, dan komt die van deze lijst. Controleer dat in de Rich Results Test.

Beperking: de live site (tanterie.nl) is vanuit deze omgeving niet bereikbaar, dus er is geen HTML opgehaald van de preview en de Rich Results Test is niet gedraaid. De conclusies hierboven komen uit de themacode. De Liquid is niet door Shopify gerenderd als aparte test; dat gebeurt in de preview.

Een kanttekening bij de lokale exportmap: die is van 24-10 21:58 en wijkt op enkele bestanden af van de kopie (de drie productsecties met de gewichtsfix van 24-10, `templates/index.json` en een aantal templates). Voor de controle in stap 3 is daarom `templates/index.json` en alle collectietemplates rechtstreeks uit de kopie gelezen. De secties, snippets, blocks en het layout zijn bestand voor bestand met de checksums van de kopie vergeleken; daar waren geen andere verschillen dan de bekende (de elf gewijzigde bestanden en de drie productsecties met de gewichtsfix).

## Preview-URL's

| Wat | URL |
|---|---|
| Homepage | https://tanterie.nl/?preview_theme_id=204118262024 |
| Collectie Joeff | https://tanterie.nl/collections/joeff?preview_theme_id=204118262024 |
| Collectie Bunzlau | https://tanterie.nl/collections/bunzlau?preview_theme_id=204118262024 |

Wat Mark in de preview kan bekijken: de homepage moet er hetzelfde uitzien (reviewblok "Waarom klanten voor Tante Rie kiezen" met de zes beoordelingen, links "Over: ..." onder de reviews) en de productkaarten op Joeff en Bunzlau moeten er hetzelfde uitzien als nu. Er verandert voor de bezoeker niets zichtbaars; het gaat om de gestructureerde gegevens in de broncode.

## Wat Mark moet doen

1. De preview-URL's hierboven bekijken en controleren dat de pagina's er hetzelfde uitzien.
2. Het thema "Productmarkup V119 2026-10-25" publiceren in Shopify admin onder Onlinewinkel, Thema's. Dat kan niet via de Shopify-koppeling (themePublish is geblokkeerd). Voor het publiceren een verse backup van het dan live thema in scripts/archief-themas/ laten zetten (de hoofdsessie).
3. Terugdraaien kan direct: het vorige live thema 204095619336 ("Bunzlau collectie V118 2026-10-24") blijft bestaan en kan weer gepubliceerd worden.

## Wat daarna volgt

1. Rich Results Test op de drie URL's: https://tanterie.nl/, https://tanterie.nl/collections/joeff en https://tanterie.nl/collections/bunzlau, plus een productpagina (bijvoorbeeld https://tanterie.nl/products/geluksthee) als controle dat het Product-blok daar nog compleet is. Verwacht: op de homepage alleen de ItemList en geen losse Product-items uit de reviewsectie; op de collectiepagina's alleen CollectionPage en BreadcrumbList. Dat kan een sessie met toegang tot de site of Mark zelf in de test doen.
2. In Search Console op "Oplossing valideren" klikken bij Productfragmenten (de melding van 2 september, voorbeeldpagina de homepage) en bij Verkopersvermeldingen (de melding van 24 oktober, voorbeeldpagina /collections/joeff). Pas na publicatie, anders mislukt de validatie opnieuw. Voor "Dubbel veld brand" (16 oktober) staat de validatie nog open (V95). Google meldt de uitkomst per mail; die komt in het Search Console-logboek.
3. De changelog (marketing/changelog.md) vullen door de hoofdsessie, op het moment van publicatie: datum, URL's (/, /collections/joeff en de overige collecties), wat veranderd is, waarom, het theme-id 204118262024, het vorige live thema 204095619336 en de checksums uit de tabel hierboven. Die is in deze stap niet aangeraakt.
4. Een nieuwe crawl van de homepage en de tien collectiepagina's na publicatie, en in Search Console de rapporten Productfragmenten en Verkopersvermeldingen na een paar dagen controleren op een dalend aantal items.
5. Search Console-logboek: meldingen 2 en 4 zijn bijgewerkt met de status "in themakopie, wacht op publicatie" (marketing/technisch/search-console-meldingen.md). Na publicatie en validatie de status daar bijwerken.

## Open punten, niet onderdeel van deze kopie

Foto's voor de 27 online producten zonder foto blijven nodig voor Merchant Center (B3). De drie Joeff-producten die de melding van 24 oktober gaven (Grote ring, Handdoekhaakje, Kleine ring) zijn niet online gepubliceerd en blijven dat; er is niets gepubliceerd of aangepast in Shopify-producten. Bij de Blond-collectiepagina staat nog "Bestel nu" op de knop van niet-beschikbare producten; dat valt buiten deze opdracht.
