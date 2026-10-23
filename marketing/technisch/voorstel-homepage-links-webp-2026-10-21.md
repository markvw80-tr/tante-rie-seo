# Voorstel homepage-links en afbeeldingen, 21 oktober 2026

Status: voorbereid en getest in het preview-thema "SEO-fixes-hoog preview 2026-10-21" (203908153608, ongepubliceerd). Live is niets gepusht. Het werk staat in twee commits in `/Users/markvanwijk/Tante Rie SEO/scripts/theme-live-2026-10-21/`, bovenop afb8147. De volledige diff staat in `marketing/technisch/voorstel-homepage-links-webp-2026-10-21.diff`.

## A. Oude schema-thema's verwijderd

Het permissiesysteem blokkeerde dit niet, dus de thema's zijn verwijderd.

1. Controle volledigheid: een verse `shopify theme pull` van beide thema's naar een tijdelijke map gaf 498 bestanden (199507345672) en 495 bestanden (202361864456). Dat is gelijk aan de lokale mappen `theme-ref-199507345672/` en `theme-ref-202361864456/`; `diff -rq` toonde geen enkel verschil.
2. Archief: `scripts/archief-themas/theme-199507345672.zip` en `theme-202361864456.zip`, elk ongeveer 1,4 MB.
3. Controle met `shopify theme list`: live is "Agent-ready koppen 2026-10-09" (203153015048), geen van beide was live.
4. Verwijderd met `shopify theme delete --theme <id> --store 0qkm31-r6.myshopify.com --force`. Daarna: de lijst telt twee themas minder, preview-thema 203908153608 en het live thema staan er nog.
5. Changelog-regel geschreven.

## B. Homepage-links

Controle live: een verse pull van 203153015048 was gelijk aan de werkmap op afb8147, dus geen "sync live" nodig.

Plek: een rij met drie tekstlinks direct onder de collectieslider "Thee naar jouw smaak" in `sections/tr-homepage-redesign.liquid`. Titeltag, H1, alle bestaande teksten en bestaande links blijven ongewijzigd (gecontroleerd op live en preview: zelfde title en H1). Het aantal links op de pagina gaat van 70 naar 73.

| | Voor | Na |
|---|---|---|
| Links onder de collecties | geen | Theewinkel in Borne, Twente (/pages/theewinkel-borne-twente), Bunzlau servies (/collections/bunzlau), Serviezen en serviesstellen (/pages/serviezen) |

De ankerteksten volgen de zoektermen uit het Bedrijfsprofiel (servies, bunzlau servies) en de lokale pagina. De drie doelpagina's geven 200.

Preview gecontroleerd met curl (`home-preview.html` bevat het blok, `home-live.html` niet; opgeslagen in `data/homepage-2026-10-21/`) en een screenshot: `assets/screenshots/home-linkblok-preview-2026-10-21-desktop.png` en `-mobiel.png`.

## C. PNG's naar WebP

Bevinding: er is geen conversie nodig. De collectie-afbeeldingen komen via `image_url` van de Shopify-CDN (collectiekaarten, kaartafbeelding uit de collectie zelf), niet via `asset_url` en niet uit de Files. Shopify levert aan browsers die dat ondersteunen al WebP. De drie genoemde afbeeldingen uit de audit zijn dus geen PNG-transfers: 242, 229 en 111 KB zijn de WebP-groottes bij width=900 en width=600 (gemeten 240.596, 228.246 en 114.600 bytes). Er is daarom geen map `webp-2026-10-21` aangemaakt en er is niets geupload.

Gemeten met `curl -H "Accept: ..."` op de echte URL's (bytes):

| Afbeelding (collectie) | PNG, width 900 | WebP, width 900 | WebP, width 600 | WebP, width 400 |
|---|---|---|---|---|
| Rooibos | 1.375.043 | 240.596 | 114.600 | 46.148 |
| Kruidenthee | 1.310.346 | 228.246 | 95.682 | 34.776 |
| Witte thee | 1.002.325 | 109.496 | 34.278 | 9.002 |
| Vruchtenthee | 975.234 | 95.980 | 51.728 | 24.392 |
| Zwarte thee | 818.870 | 59.844 | 35.688 | 18.194 |
| Groene thee | 793.389 | 59.592 | 33.714 | 17.216 |

Content-type met `Accept: image/webp,image/avif,image/*` is `image/webp` (AVIF wordt voor deze bestanden niet geleverd); met alleen `Accept: image/png` komt de PNG terug.

De winst zit in de `sizes`-waarde. Die stond op `100vw` voor schermen onder 750 px, terwijl een kaart op mobiel ongeveer 67 procent van de breedte beslaat (de slider toont 1,35 kaart). Een telefoon van 412 px met schaal 1,75 koos daardoor de 900-versie. Met de juiste waarde kiest die telefoon de 600-versie, en desktop de 400-versie (gemeten in de preview).

| | Voor | Na |
|---|---|---|
| sizes collectiekaart | (min-width: 990px) 25vw, (min-width: 750px) 50vw, 100vw | (min-width: 901px) min(23vw, 350px), (min-width: 501px) 42vw, 67vw |
| Gekozen versie, telefoon 412 px, schaal 1,75 | 900 (zes kaarten samen ruim 790 KB) | 600 (zes kaarten samen ruim 360 KB) |
| Gekozen versie, desktop 1440 px, schaal 1 | 400 | 400 |

Een kaart onder de vouw wordt pas geladen bij scrollen (`loading="lazy"`), dus de besparing zit vooral in dataverbruik en minder in LCP.

De originele bestanden in Shopify hoeven niet te worden vervangen. Beslissing 9 uit het plan (PNG naar WebP of JPG) kan daarom met "niet nodig, wel de sizes-aanpassing" worden beantwoord.

## Diff

```
sections/tr-homepage-redesign.liquid

+.trh-more-links { display: flex; flex-wrap: wrap; justify-content: center; gap: 12px 32px; margin-top: 28px; }
+.trh-more-links a { font-size: 14px; color: var(--brown); text-decoration: none; border-bottom: 1px solid var(--brown-light); padding-bottom: 1px; }
+.trh-more-links a:hover { color: var(--brown-dark); }

-  sizes="(min-width: 990px) 25vw, (min-width: 750px) 50vw, 100vw"
+  sizes="(min-width: 901px) min(23vw, 350px), (min-width: 501px) 42vw, 67vw"

+    <nav class="trh-more-links" aria-label="Meer van Tante Rie">
+      <a href="/pages/theewinkel-borne-twente">Theewinkel in Borne, Twente</a>
+      <a href="/collections/bunzlau">Bunzlau servies</a>
+      <a href="/pages/serviezen">Serviezen en serviesstellen</a>
+    </nav>
```

Commits: b91fb65 (linkblok) en a903791 (sizes), los van elkaar terug te draaien.

## Push-commando's voor Mark

Eerst opnieuw controleren dat live nog gelijk is aan de basis (optioneel), daarna alleen dit ene bestand naar live:

```
cd "/Users/markvanwijk/Tante Rie SEO/scripts/theme-live-2026-10-21"
shopify theme push --theme 203153015048 --store 0qkm31-r6.myshopify.com --only sections/tr-homepage-redesign.liquid --allow-live
```

Let op: het bestand bevat ook de ene regel uit commit d848aed (srcset en sizes van de productkaarten op de homepage, Hoog 3). Die wijziging gaat dus mee naar live; zij is al in het preview-thema getest. De overige bestanden van 22d37d4, d848aed, 9926124 en afb8147 (schema en andere afbeeldingsmarkup) staan nog niet live en worden door dit commando niet geraakt. Wil je alleen het linkblok zonder de sizes-wijzigingen, vraag dan om een aparte versie.

Preview bekijken: https://tanterie.nl/?preview_theme_id=203908153608

## Open punten

1. Akkoord op het live pushen van B en de sizes-wijziging uit C (ja of nee per onderdeel).
2. Ankertekst: "Serviezen en serviesstellen" past bij de pagina (H1 "Serviezen"); zeg het als je een andere formulering wilt.
3. Hoewel titel en bestaande tekst niet veranderen, komen er drie nieuwe zichtbare linkteksten bij. Zie dat als het bedoelde effect van beslissing 7.
