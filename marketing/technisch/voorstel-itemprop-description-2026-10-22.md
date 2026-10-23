# Voorstel: verouderde itemprop-description op de Joeff-collectie

Datum: 2026-10-22. Rol: technisch SEO. Status: alleen onderzoek en voorstel. Er is niets gewijzigd in Shopify, het live thema, metafields of instellingen, en er is niets gepusht. De changelog is niet aangeraakt.

## 1. Bron

De tekst staat hardgecodeerd in het themabestand `sections/tr-collection-joeff.liquid`, regel 183:

```
<meta itemprop="description" content="Joeff Muuss: modulair wandsysteem met basishouders en schakels, boorvrij op te hangen. Te koop bij Tante Rie in Borne, Twente. Verzending door heel Nederland, of gratis ophalen in de winkel.">
```

Dit is geen sectie-instelling en geen metafield:

- Templatebestand `templates/collection.joeff.json` bevat alleen lege instellingen (subtitle, brand_image, brand_text, seo_text allemaal leeg).
- Collectie gid://shopify/Collection/579105456392 (handle joeff, templateSuffix joeff) heeft alleen de metafields `global.title_tag` en `global.description_tag`. Beide zijn de nieuwe teksten van 22-10 en kloppen met `seo.title` en `seo.description`. De beschrijving (descriptionHtml) is leeg.
- De 22-10-wijziging werkt dus wel door in `<title>` en `<meta name="description">`, maar de sectie negeert die velden voor de microdata-regel.

Het blok zit in de wrapper `<div class="trjf-wrap" itemscope itemtype="https://schema.org/CollectionPage">`. De meta is daarmee een microdata-eigenschap (itemprop) van die wrapper en geen zichtbare of door Google als snippet gebruikte tekst. Hij staat wel in de HTML en dus in elke crawl en in tools die microdata uitlezen.

## 2. Versiecontrole lokaal tegen live

Live thema: #203153015048 "Agent-ready koppen 2026-10-09". Alleen-lezen gepulld naar de tijdelijke map `/private/tmp/claude-502/-Users-markvanwijk-Tante-Rie-SEO/1c751388-c258-4414-9897-6c2624328a37/scratchpad/livepull` (`shopify theme pull --only ... --nodelete`, geen push).

- `sections/tr-collection-joeff.liquid`: lokaal in `~/TanteRie-Theme-Editor` is byte-voor-byte gelijk aan live en gelijk aan `scripts/theme-live-2026-10-21`. Het voorstel is dus op de juiste versie gebaseerd. Let op: het bestand staat in die repo als untracked (nog niet gecommit), dus git blame helpt niet. Maak het voorstel als wijziging in een themakopie en commit het daar.
- `sections/tr-collection-bunzlau.liquid`: wijkt lokaal af van live (live heeft srcset/sizes op productkaarten, lokaal niet). De itemprop-regel is wel gelijk.
- `sections/tr-collection-redesign.liquid` en enkele `templates/collection.*.json` verschillen ook, maar de live templates beginnen met het Shopify-autogenerate-commentaar. Dat is ruis, geen inhoudelijk verschil voor dit onderwerp.
- `layout/theme.liquid` is gelijk.

## 3. Omvang

Hetzelfde patroon (vaste meta itemprop="description" met vaste tekst in de sectie) zit in 9 van de 11 collectiesecties. Met curl op live bevestigd:

| Collectie | Vaste itemprop-tekst bevat | Spanning met regels of met de pagina |
|---|---|---|
| joeff | "Verzending door heel Nederland, of gratis ophalen in de winkel" | Botst met de voorraadregel (belofte voor alle producten). |
| bunzlau | "Heel de collectie op bestelling beschikbaar. Afhalen in Borne" | Botst met de pagina zelf: keramiek is "uitsluitend af te halen", alleen melamine is online te bestellen. |
| blond | "Heel de collectie op bestelling beschikbaar. Afhalen in Borne" | Botst met de collectietekst: "uitsluitend af te halen in onze winkel". |
| rice | "Snel verzonden of afhalen in de winkel" | Vaste winkelbelofte voor alle producten. |
| groene-thee | "Afhalen of verzenden" | Vaste belofte, zachter geformuleerd. |
| zwarte-thee | "Afhalen in Borne" | Vaste belofte. |
| rooibos | "Afhalen of verzenden" | Vaste belofte. |
| kruidenthee | geen afhaalbelofte | Alleen hardgecodeerd, niet gekoppeld aan SEO-description. |
| witte-thee | geen afhaalbelofte | Idem. |
| vruchtenthee (sectie `tr-collection-vruchten-thee`) | geen afhaalbelofte | Idem. Op live bij `/collections/vruchten-thee` niet teruggevonden met curl; de collectie heeft handle `vruchtenthee`, controleer dat de microdata daar wel staat. |

Niet getroffen: `/collections/thee`, `/collections/thee-bewaarblikken`, `/collections/accessoires`, `/collections/servies` (sectie `tr-collection-redesign`, geen itemprop-description) en alle producttemplates (`tr-product-*`: de itemprop-description volgt daar uit `cur.description`, dus dynamisch).

Verwante bevindingen op dezelfde pagina (Joeff):

1. De JSON-LD CollectionPage in dezelfde sectie gebruikt `collection.description`, en die is voor Joeff leeg. Live staat dus `"description": ""` in het schema.
2. De microdata-wrapper `itemtype=CollectionPage` en het JSON-LD-blok beschrijven dezelfde pagina twee keer. Het is geen fout, maar dubbel werk dat uit elkaar kan lopen.
3. Dezelfde belofte staat ook zichtbaar op de pagina, hardgecodeerd: regel 242 ("Bezorgd thuis, of gratis ophalen in Borne" in de USP-balk), regel 429 (kop "Verzending & ophalen") en regel 500 ("Liever gratis ophalen? Kies daarvoor bij het afrekenen"). Daar kan het wel kloppen als afhalen een afrekenoptie is, maar de voorraadregel uit CLAUDE.md geldt ook hier. Zie beslispunt 3.

## 4. Oorzaak

De collectiesecties zijn per merk handmatig gebouwd met een vaste meta-regel. Die is nooit gekoppeld aan de SEO-description van de collectie in Shopify. Daardoor veranderen title en meta wel mee met de collectievelden, maar de microdata-tekst blijft staan op de oude, brede winkelbelofte.

## 5. Voorstel voor Joeff

Voorkeur: laat de itemprop-description volgen uit de SEO-description van de collectie (`page_description`, dus het `global.description_tag` dat op 22-10 is gezet), met de collectiebeschrijving als terugval, en laat de regel weg als beide leeg zijn. Dezelfde variabele vult daarna ook de JSON-LD, die nu leeg is. Zo is er één bron voor alle drie de plekken en kan tekst niet meer uit elkaar lopen.

Voor (live, regel 183):

```
<meta itemprop="description" content="Joeff Muuss: modulair wandsysteem met basishouders en schakels, boorvrij op te hangen. Te koop bij Tante Rie in Borne, Twente. Verzending door heel Nederland, of gratis ophalen in de winkel.">
```

Na (uitkomst voor Joeff vandaag):

```
<meta itemprop="description" content="Bestel Muuss van Joeff bij Tante Rie in Borne: het boorvrije wandsysteem met basishouder en schakels voor tegels, kaarten en kunstbloemen.">
```

en in JSON-LD `"description"` van `""` naar dezelfde zin.

Het volledige diff staat in `/Users/markvanwijk/Tante Rie SEO/marketing/technisch/voorstel-itemprop-description-2026-10-22.diff`:

```diff
--- a/sections/tr-collection-joeff.liquid
+++ b/sections/tr-collection-joeff.liquid
@@ -180,7 +180,8 @@
 
 <div class="trjf-wrap" itemscope itemtype="https://schema.org/CollectionPage">
   <meta itemprop="name" content="{{ collection.title }} – Muuss wandsysteem bij Tante Rie, Borne (Twente)">
-  <meta itemprop="description" content="Joeff Muuss: ... of gratis ophalen in de winkel.">
+  {%- assign _seo_desc = page_description | default: collection.description | strip_html | strip | truncate: 200 -%}
+  {%- if _seo_desc != blank -%}<meta itemprop="description" content="{{ _seo_desc | escape }}">{%- endif -%}
 
@@ -508,7 +509,7 @@
     "name": {{ collection.title | json }},
-    "description": {{ collection.description | strip_html | truncate: 200 | json }},
+    "description": {{ _seo_desc | json }},
```

Alternatief: de meta-regel helemaal weghalen. Het JSON-LD-blok dekt de CollectionPage al, en Google gebruikt de itemprop-meta niet voor het snippet. Dat is minder werk, maar laat de JSON-LD-description leeg, tenzij die regel ook wordt aangepast. Daarom raad ik de koppeling aan.

Voor de overige 8 collectiesecties raad ik hetzelfde patroon aan, in een tweede stap en per sectie getoetst. Prioriteit: Bunzlau en Blond (tegenstrijdig met de eigen paginatekst), daarna Rice en de theecollecties.

Uitvoering (nog niet gedaan, wacht op akkoord):

1. `shopify theme duplicate` van live #203153015048, wijziging in de kopie of in een aparte branch in `~/TanteRie-Theme-Editor`.
2. Diff laten zien, akkoord van Mark afwachten.
3. Controle na wijziging: curl op de previewcollectie (meta-description, itemprop en JSON-LD), Rich Results Test op `/collections/joeff`, daarna publicatie en een nieuwe crawl.
4. Pas daarna een regel in `marketing/changelog.md`.

## 6. Beslissingen voor Mark

1. Koppelen aan de SEO-description (voorkeur) of de meta-regel weghalen?
2. Alleen Joeff nu, of dezelfde aanpassing meteen voor alle 9 collectiesecties? Bunzlau en Blond spreken zichzelf tegen en zijn daarbij het meest urgent.
3. De zichtbare tekst op Joeff (regels 242, 429 en 500, "gratis ophalen") valt buiten dit voorstel. Moet die ook naar een voorraadafhankelijke formulering, of is afhalen via de kassa/checkout in orde? Dat is een tekstwijziging voor de on-page rol en de kwaliteitsredacteur.

## 7. Uitvoering op themakopie (update 22-10, na akkoord van Mark op optie koppelen, alle secties)

Er is niets live gezet. Het live thema #203153015048 is niet aangeraakt (live HTML van /collections/joeff bevat nog de oude itemprop, gecontroleerd).

Correctie op rubriek 3: het gaat om 10 secties, niet 9 (van de 11 collectiesecties heeft alleen `tr-collection-redesign` geen itemprop-description). Alle 10 zijn aangepast.

- Themakopie: "itemprop-description 2026-10-22", theme-id 203977687304, ongepubliceerd. Gemaakt met `shopify theme duplicate` van #203153015048, alleen de 10 collectiesecties gepusht met `--only` en `--nodelete`.
- Diff (10 bestanden, 20 hunks): `/Users/markvanwijk/Tante Rie SEO/marketing/technisch/itemprop-description-2026-10-22.diff`
- Gebruikte logica: `_seo_desc` = `page_description`, anders `collection.description`, ontdaan van HTML en van HTML-entiteiten. De meta krijgt `| escape`, de JSON-LD `| json`. Zijn beide leeg, dan vervalt de meta-regel. De eerste versie gaf dubbele escaping (`&amp;amp;` bij Rice, Bunzlau, Blond) en afkapping op 200 tekens; beide zijn gecorrigeerd en opnieuw gepusht en gecontroleerd.
- Preview: `https://tanterie.nl/collections/<handle>?preview_theme_id=203977687304` (cookie nodig, dus in de browser openen of met curl en cookie-jar).

| Collectie | Oude itemprop | Nieuwe itemprop (gelijk aan SEO-meta en JSON-LD) |
|---|---|---|
| joeff | Joeff Muuss: modulair wandsysteem ... gratis ophalen in de winkel. | Bestel Muuss van Joeff bij Tante Rie in Borne: het boorvrije wandsysteem met basishouder en schakels voor tegels, kaarten en kunstbloemen. (JSON-LD was leeg) |
| bunzlau | Bunzlau Castle aardewerk te koop ... Heel de collectie op bestelling beschikbaar. Afhalen in Borne, ... | Bunzlau Castle theepotten, mokken & servies bij Tante Rie in Borne, Twente. Handgemaakt Pools aardewerk in 40+ vormen. Bestel online, afhalen in de winkel. |
| blond | Blond Amsterdam woonaccessoires en cadeaus ... Heel de collectie op bestelling beschikbaar. Afhalen in Borne, ... | Vrolijk en eigenzinnig. Ontdek Blond Amsterdam mokken, servies & woonaccessoires bij Tante Rie in Borne, Twente. Bestel online, afhalen in de winkel. |
| rice | Rice woonaccessoires ... Snel verzonden of afhalen in de winkel. | Vrolijke Rice DK mokken, servies & woonaccessoires bij Tante Rie. Het kleurrijke Deense lifestylemerk. Online bestellen, bezorging in Nederland. |
| groene-thee | Groene thee kopen ... Afhalen of verzenden, bereikbaar vanuit Enschede, Hengelo en Almelo. | Meer dan 30 soorten losse groene thee: Japanse Sencha, Chinese Jasmijn, Marocco Mint en meer. Vers afgewogen in Borne, Twente. Binnen 1 tot 2 werkdagen in huis. |
| zwarte-thee | Zwarte thee kopen ... Afhalen in Borne, bereikbaar vanuit ... | Geen eigen SEO-description: Shopify genereert de meta uit de collectietekst (320 tekens, begint met "Zwarte thee is volledig gefermenteerde thee ..."). Itemprop en JSON-LD volgen die tekst. |
| rooibos | Rooibos thee kopen ... Afhalen of verzenden. | Cafeïnevrije rooibos uit Zuid-Afrika, in meer dan 20 blends. Pure naturel, fruitig of kruidig. Vers afgewogen in Borne, Twente. Binnen 1 tot 2 werkdagen in huis. |
| kruidenthee | Kruidenthee kopen ... Cafeïnevrij, puur natuur. | Cafeïnevrije kruidenthee: kamille, pepermunt, gember en zorgvuldig samengestelde blends. Vers afgewogen in Borne, Twente. Binnen 1 tot 2 werkdagen in huis. |
| witte-thee | Witte thee kopen ... zacht van smaak. | Witte thee van topkwaliteit: Pai Mu Tan BIO, Sunny White en meer. De minst bewerkte theesoort, vers afgewogen in Borne, Twente. |
| vruchtenthee (sectie vruchten-thee) | Vruchtenthee kopen ... ook lekker als ijsthee. | Geen eigen SEO-description: Shopify genereert de meta uit de collectietekst (320 tekens, begint met "Vruchtenthee is een cafeïnevrije infusie ..."). Itemprop en JSON-LD volgen die tekst. |

Controle op de preview, per collectie met curl: itemprop-description gelijk aan `<meta name="description">`, JSON-LD CollectionPage-description gelijk aan dezelfde tekst, alle JSON-LD-blokken geldig JSON, geen Liquid-fouten in de HTML. Resultaat: 10 van 10 gelijk, 0 ongeldige JSON, 0 Liquid-fouten. De Rich Results Test en een nieuwe crawl zijn nog niet gedaan (pas na publicatie zinvol, want de test heeft een publieke URL nodig).

Opvallend: zwarte-thee en vruchtenthee hebben geen ingevulde SEO-description in Shopify. De meta in Google is dus een automatisch afgekapt stuk van de collectietekst. Dat is een on-page taak (nieuwe description voorstellen), los van dit voorstel. Handle van de vruchtenthee-collectie is `vruchtenthee`, maar het template heet `vruchten-thee`.

## Status 22-10

Doorgevoerd op 22 oktober na akkoord van Mark: alleen de 10 collectiesecties uit kopie 203977687304 gepusht naar live thema 203153015048. Live gecontroleerd (curl op 10 collecties, Rich Results Test Joeff: 23 geldige items, geen fouten). Zie changelog.md. Kopie 203977687304 is op 22 oktober op verzoek van Mark verwijderd.
