# Werkvolgorde en overdracht

Kort overzicht van wie wie triggert. Bij verschil gaan CLAUDE.md en tante-rie-hq/team/werkafspraken-seo.md voor. Opgesteld 7 november 2026.

## Ketens

| Keten | Stappen |
|---|---|
| Tekst of productwijziging | Maker (Content of On-page) schrijft voorstel; maker schakelt de Kwaliteitsredacteur in; Kwaliteitsredacteur schrijft oordeel in marketing/review/ en past de tekst niet zelf aan; maker verwerkt; Mark geeft akkoord via marketing/vragen-voor-mark.md; On-page zet regels in marketing/pim-regels-concept.json; PIM voert uit; On-page of Technisch SEO schrijft de changelogregel met nulwaarde en meetdatum |
| Technische fix in het thema | Technisch SEO stuurt eisen aan Design via de mailbox (heading-structuur, schema, interne links); Design bouwt in een themakopie en laat een diff zien; Mark publiceert; Technisch SEO controleert met Rich Results Test en crawl; changelogregel |
| Technische fix in productgegevens | Technisch SEO levert regels aan On-page; verder als tekstketen |
| Bedrijfsprofiel, NAP, links | Autoriteit-lokaal levert voorstel met voor en na en een status per kans; Mark of PIM voert uit; changelogregel met datum |
| Zoekwoordkans | Zoekwoord-onderzoeker levert cluster met doelpagina; On-page of Content pakt op; Analist terugkoppeling in rapport |
| Meting | Analist meet elke wijziging uit de changelog eenmaal, na minimaal vier weken; geen tweede meting door On-page |

## Eigenaars

| Taak | Eigenaar |
|---|---|
| Maandplan en contentkalender | SEO Lead |
| Meetkalender | SEO Lead plant, Analist voert uit (marketing/meetkalender-JJJJ-MM.md) |
| Rank tracking per cluster | Analist |
| Controle dat PIM-regels live staan | Analist (Shopify alleen lezen) |
| PIM-regels bundelen en versturen | On-page |
| Interne links en schema-eisen | Technisch SEO, geleverd aan Design |
| Merchant Center en Bedrijfsprofiel | Autoriteit-lokaal levert voorstel; Mark of PIM voert uit |
| Linkkansen | Autoriteit-lokaal |
| Inbox seo leegmaken (`mailbox.py verwerkt`) | Degene die de sessie start |

## Buiten scope (besluit Mark)

- Geen aparte GEO-rol (31-10); Technisch SEO heeft al een GEO-analyse gedaan.
- Geen SEO-werk aan /pages/zakelijk.
