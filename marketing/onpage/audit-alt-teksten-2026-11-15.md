# Audit alt-teksten uitgelichte afbeelding, 15 november 2026

Opdracht: directie, 15-11 (punt 1). Bron: Shopify, alleen gelezen, 447 online gepubliceerde actieve producten, veld featuredMedia.alt. Er is niets gewijzigd. Overige afbeeldingen per product zijn alleen steekproefsgewijs bekeken (Bunzlau tulp-mok-330: alles goed; Rice A: twee SKU-codes als alt).

## Uitkomst

| Groep | Aantal | Toelichting |
|---|---|---|
| Uitgelichte alt goed (type, naam, merk) | ca. 380 | Alle losse thee, Bunzlau, Rice-alfabet, theepakketten, bewaarblikken, Pineut en proefpakketten. De handles met "-kopie" bij Pineut en proefpakketten wijken af van de titel, maar de alt klopt met de titel |
| Alt leeg | 25 | Zie tabel A |
| Alt alleen een SKU-code | 12 | Clip-producten (Hanger): zie tabel B |
| Alt klopt niet | 2 | lavendel (noemt Mama & Baby Thee), pepermunt (noemt Kruizemunt Nana Mint, foto heet kruizemunt) |
| Alt bevat verkeerde tekens of dubbele tekst | 2 | theestoof Bunzlau toont "&amp;"; Rice Z herhaalt zichzelf |
| Alt te kaal (alleen de titel of één woord) | ca. 30 | Blond (Meester, Dad, Papa, 50 jaar, Groom, Mazagran-reeks), Exotic Punch, Bornse Oase ("Love from the Caribbean"), Rooibos Lemon Cheesecake (type ontbreekt) |
| Product zonder enige afbeelding | 20 | Online maar zonder foto: o.a. hibiscus-thee, kerstthee-red-nose-rudolph-gluhwein, twee Bunzlau-theeglazen, 7 Joeff-onderdelen, 5 bakmixen. Geen alt-probleem, wel een PIM-punt |

## Tabel A, lege alt (25)

Blond Amsterdam (10, loopt via PIM batch 01 en de Handwas-verrijking, niet apart doorvoeren): congratulations-party, miss-creativity, best-friend, game-on, ed-bord-18-cm-tompouce, cozy-days-light-house-stepped-gable-cozy, mama, the-man, i-do, miss-brains.

Joeff (10), Pineut (2) en overig (3) staan hieronder met een conceptalt. Concepten zijn op titel en merk gebaseerd; de foto is nog niet bekeken. Mark of de kwaliteitsredacteur toetst ze aan de foto voor ze naar PIM gaan.

| Handle | Concept-alt |
|---|---|
| kaarthouderschakels | Kaarthouderschakels van Joeff om kaarten aan de muur te hangen |
| tegeltje-kunsthouderschakel | Tegeltje kunstschakel van Joeff voor een persoonlijke wand |
| tentoonstellingshaakje | Tentoonstellingshaakje van Joeff voor wanddecoratie |
| ledkaars-schakel | Ledkaars schakel van Joeff voor op een kunstwand |
| joeff-kunstbloem-vaasje | Kunstbloem vaasje van Joeff voor een persoonlijke wand |
| joeff-kaarthouder | Kaarthouder TOON van Joeff voor kaarten aan de wand |
| tegelhouder-joeff | Tegelhouder van Joeff voor een tegel aan de wand |
| handdoekhaakje | Haakje van Joeff voor hand- en theedoeken |
| spiegel | Spiegeltje van Joeff voor een persoonlijke wand |
| plateau | Plateau van Joeff voor persoonlijke wanddecoratie |
| pineut-cake-pouchbag-lemon-poppy-cake | Pineut Lemon Poppy Cake in een pouchbag |
| pineut-cake-pouchbag-lemon-poppy-cake-kopie | Pineut Passionfruit Martini Cake in een glazen pot |
| houten-honinglepel | Houten honinglepel van Arelo |
| tante-rie-cadeaubon | Cadeaubon van Tante Rie |
| mug-tulip-400-ml | Mok Tulip 400 ml van Bunzlau Castle |

## Tabel B, alt alleen een SKU-code (12, Clip-leverancier, PIM-verrijking loopt via het Clip-portaal)

bowl-square-70-ml (1604-2341), hanger-teapot, hanger-cup-and-saucer, cake-dish-flat-o-15-5-cm, sauce-bowl-50-ml, mug-cappuccino-400-ml, serveerschaal-100-ml, kom-50-ml, pastabord-o-25-cm, melk-mok-230-ml, melamine-beker-1, plus de Rice-extra afbeeldingen met codes (MELCU-...). Hanger Teapot en Cup and Saucer wachten ook op verrijking door PIM.

## Voorstel volgorde

1. Mark keurt de aanpak goed (V-vraag hieronder).
2. Tabel A (niet-Blond) en de twee onjuiste alt (lavendel, pepermunt) gaan als regels met veld alt_tekst naar `marketing/pim-regels-concept.json`, na toets op de foto en akkoord van de kwaliteitsredacteur.
3. Blond en Clip-producten: bericht aan PIM dat de alt in hun lopende batch meegaat, met de regel (merk, productsoort, naam, kenmerk).
4. Kale alt van Exotic Punch, Bornse Oase en Rooibos Lemon Cheesecake: open sinds 28-10 (vier producten nog niet doorgevoerd). Eerst theetype per eerste ingrediënt vaststellen.
5. 20 producten zonder foto: aan PIM melden.

SEO wijzigt niets in Shopify.
