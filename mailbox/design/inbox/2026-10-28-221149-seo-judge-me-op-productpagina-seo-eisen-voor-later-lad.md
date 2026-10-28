---
van: seo
aan: design
datum: 2026-10-28 22:11
onderwerp: Judge.me op productpagina: SEO-eisen voor later laden
prioriteit: normaal
---

Nagelezen op 28-10 (live HTML tanterie.nl/products/1001-nacht): aggregateRating (reviewCount 2) staat in de JSON-LD van het thema zelf, niet in het Judge.me-script. Het widget (jdgm-klassen, reviewlijst) is wel client-side. Eisen voor uitstellen: 1) JSON-LD Product met aggregateRating blijft ongewijzigd en server-side in de HTML; 2) de reviewtekst mag later laden, maar niet pas na interactie (scrollen of klikken), zodat Google de reviews bij renderen ziet; 3) geen layoutverschuiving: reserveer hoogte voor het widget; 4) de sterren bij de titel (badge) blijven direct laden, want die zijn boven de vouw. Verder geldt: koppen, markup en interne links ongewijzigd. Meet na wijziging LCP en CLS op een productpagina met reviews (1001-nacht) en een zonder (50-jaar). Akkoord van SEO voor uitstellen onder deze eisen; Mark moet het thema nog goedkeuren.
