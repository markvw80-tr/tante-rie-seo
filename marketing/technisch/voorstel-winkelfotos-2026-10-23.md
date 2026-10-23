# Voorstel winkelfoto's plaatsen (V51), 23-10-2026

Status: preview klaar, niets live. Wacht op akkoord van Mark.

## Preview
- Thema: "winkelfotos 2026-10-23", id 203996496136, ongepubliceerd, kopie van live thema 203153015048.
- Preview-links (de myshopify-link zet de preview-cookie, daarna werkt tanterie.nl):
  - https://0qkm31-r6.myshopify.com/pages/theewinkel-borne-twente?preview_theme_id=203996496136
  - https://0qkm31-r6.myshopify.com/collections/bunzlau?preview_theme_id=203996496136
  - https://0qkm31-r6.myshopify.com/collections/rice?preview_theme_id=203996496136
- Theme-editor: https://0qkm31-r6.myshopify.com/admin/themes/203996496136/editor

## Wat er verandert
- Theewinkelpagina (sections/tr-page-lokaal.liquid + templates/page.lokaal.json): gevel onder de intro bovenaan (eager, fetchpriority high), theewand aan het eind van "Losse thee kiezen", Bunzlau-wand aan het eind van "Servies bekijken en afhalen". Drie nieuwe image_picker-instellingen, zodat Mark ze in de editor kan wisselen.
- /collections/bunzlau en /collections/rice: Bunzlau-wand resp. Rice-wand bovenaan het blok "Alleen afhalen in de winkel" resp. "Kopen bij Tante Rie in Borne", onder de kop, boven de drie kaarten. Nieuwe image_picker `foto_winkel`.
- Alle afbeeldingen via image_url + image_tag met srcset (360 tot 900 px), sizes, width/height (900x1200), loading lazy; alleen de gevel eager. Alt-tekst komt uit Shopify Bestanden (V51-teksten). Er is geen tekst aangepast.
- Blond-gidspagina: nieuwe body in marketing/content/blond-body-met-foto-2026-10-23.html (foto direct na het antwoordblok). Niets in Shopify gezet. Diff: voorstel-winkelfotos-2026-10-23-blond-body.diff.

## Diff
voorstel-winkelfotos-2026-10-23.diff (thema) en voorstel-winkelfotos-2026-10-23-blond-body.diff.

## Controle (curl op de preview, vergeleken met live)
- Afbeeldingen: srcset-URL's (360 en 900 px) geven 200 image/jpeg, ook voor de Blond-foto.
- Alt-teksten in de gerenderde HTML kloppen met V51 en met de eigen teksten.
- JSON-LD: 4 blokken per pagina als live, alle geldig te parsen.
- Liquid-fouten: geen.
- Zichtbare tekst: identiek aan live (0 verschillen) op alle drie de pagina's.
- Mobiele screenshots (390 px, cookiebanner afgewezen, geen horizontale scroll): assets/screenshots/theewinkel-preview-winkelfotos-mobiel-boven-2026-10-23.png en ...-volledig-2026-10-23.png.
- Niet gedaan: Rich Results Test (geen API) en een nieuwe crawl; doen na livegang.

## Aandachtspunten
- De lokale kopie ~/TanteRie-Theme-Editor wijkt af van live (o.a. tr-page-lokaal.liquid). Ik heb vanaf live gewerkt, niet vanuit die map.
- Afbeeldingen zijn staand (3:4) en daarom begrensd op 420 px (pagina) en 360 px (collecties).
- Bij livegang: theme 203996496136 publiceren via Mark of de editor; daarna de Blond-body zetten en changelog bijwerken.
