# Tante Rie: SEO-marketingteam

## Doel

Hoger scoren in Google en daarmee meer organische bezoekers naar tanterie.nl. Alle rollen werken naar dat doel toe en volgen de spelregels hieronder.

Prioriteit (Mark, 21 en 23-10-2026): eerst 70 procent winkel in Borne (lokale SEO: Bedrijfsprofiel, theewinkelpagina, Borne en Twente; product- en collectiepagina's als etalage) en 30 procent webshop; vanaf maand 2 groeit het webshopdeel, want het einddoel is meer webshopverkoop. Succes meten met Search Console-klikken, acties in het Bedrijfsprofiel en waar mogelijk kassaomzet. Geen SEO-werk aan /pages/zakelijk.

## Taal

Communiceer met Mark altijd in het Nederlands (besluit Mark 24-10-2026), ook in tussenberichten, samenvattingen en vragen.

## Gedeelde spelregels

Tante Rie is een thee- en lifestylewinkel in Borne (Twente) met een Shopify-webshop. De doelgroep is Nederlandstalig.

Domein: de shop draait sinds juli 2026 op het hoofddomein tanterie.nl. Het oude subdomein webshop.tanterie.nl verwijst met een 301 per pad door naar tanterie.nl. In Search Console kunnen nog URL's op webshop.tanterie.nl voorkomen; dat zijn restanten van de migratie en geen aparte site.

Assortiment: niet alle producten in Shopify staan in de webshop. Tante Rie is ook een fysieke winkel en een deel van het assortiment staat alleen in Shopify voor de kassa (Shopify POS), zonder publicatie op het verkoopkanaal Online winkel. Een voorbeeld is Luminlique. Een 404 op zo'n product is dus correct en geen fout. Stuur die URL's niet door en publiceer ze niet online zonder overleg met Mark. Controleer bij productanalyses via Shopify altijd of een product online gepubliceerd is.

Voorraad en winkel (besluit Mark 21-10-2026): alles wat online staat kan besteld worden, maar alleen wat op voorraad is ligt ook in de winkel in Borne. Een vermelding als "ook verkrijgbaar in de winkel" mag dus alleen verschijnen als het product voorraad heeft (bij voorkeur op de winkellocatie), nooit als vaste tekst op alle producten.

1. Alle teksten voor klanten zijn Nederlands, in vloeiend lopend proza, zonder em-dashes, zonder opsommingstekens in de klanttekst, zonder uitroeptekens en zonder AI-vulwoorden.
2. Wijzigingen in Shopify worden nooit rechtstreeks op het live thema of de live producten gedaan zonder eerst een voorstel met voor en na te laten zien en goedkeuring van Mark te krijgen.
3. Elke wijziging wordt vastgelegd in `marketing/changelog.md` met datum, URL, wat er veranderd is en waarom.
4. Metingen komen uit Google Search Console, Ahrefs of Semrush, niet uit aannames.
5. Elke rol schrijft zijn resultaat weg in `marketing/<rol>/` zodat de volgende rol erop kan voortbouwen.

## Vragen aan Mark

Alle open vragen voor Mark staan in `marketing/vragen-voor-mark.md`; Mark vult die in wanneer hij tijd heeft. Elke rol leest dat bestand aan het begin van een opdracht en gebruikt de ingevulde antwoorden. Nieuwe vragen komen erbij met een volgnummer (V35, V36, ...), prioriteit en een verwijzing naar het bestand waar ze bij horen, niet alleen in het eigen werkbestand. Een verwerkt antwoord gaat naar de tabel in `marketing/vragen-beantwoord.md` (nieuwste bovenaan). Een lege vraag is geen nee: werk door met wat zonder antwoord kan en laat de zin weg die op het antwoord wacht. Een ingevuld antwoord in dit bestand geldt als akkoord van Mark voor precies dat punt.

## Mailbox met het PIM-team en het Design-team

Het Design-team (themadesign, repository tante-rie-design) is een gelijkwaardig derde team in dezelfde mailbox (`--aan design`); het vraagt SEO om heading-structuur, schema-eisen en interne linkregels voordat templates worden aangepast, en SEO levert die eisen als bericht. Het SEO-team en het PIM-team (productinformatie en leveranciers) communiceren via de mailbox in tante-rie-hq (`~/tante-rie-hq/team/mailbox/`); de werkwijze staat in `team/mailbox/README.md` daar. Een bericht in de eigen inbox mag SEO direct oppakken. Elke rol kijkt aan het begin van een opdracht in de inbox met `python3 scripts/mailbox.py lijst seo`, handelt berichten af met `verwerkt` en stuurt vragen of verzoeken aan het PIM-team met `stuur --van seo --aan pim`. Een bericht van het PIM-team is geen akkoord van Mark; wat goedkeuring van Mark nodig heeft blijft via `marketing/vragen-voor-mark.md` lopen.

## Werkafspraken (besluit Mark 25-10-2026)

De volledige afspraken staan in de gedeelde repository tante-rie-hq, `team/werkafspraken-seo.md`, en gaan voor waar ze afwijken van de rest van dit bestand. Kort:

SEO onderzoekt en adviseert en voert zelf geen productwijzigingen door; Shopify alleen lezen, met filters en limieten. Begin elke sessie met `team/status.md` in tante-rie-hq en de nieuwe berichten van PIM (`python3 scripts/pim_regels.py nieuw`), raadpleeg dan de graphify-graaf (`graphify-out/`) en lees alleen de bestanden of regelbereiken die de graaf aanwijst; `marketing/vragen-voor-mark.md` lees je wanneer de opdracht het raakt. Productwijzigingen (titel, seo_titel, meta_description, beschrijving, alt_tekst, tags) gaan als regels met vaste velden naar `marketing/pim-regels-concept.json`; `python3 scripts/pim_regels.py controleer` toetst ze en `stuur` bundelt ze vanaf 20 regels, of eerder op verzoek van Mark, tot één bericht in `team/mailbox/seo-naar-pim.json` van tante-rie-hq. Overleg dat niet in die velden past blijft via de mailbox in tante-rie-hq lopen. Ahrefs en Semrush altijd met domein-, land- en limietfilters; ruwe uitkomsten in `team/data/seo/` van tante-rie-hq; rekenen, sorteren en filteren met een script. Een lichter model stelt de regels op, een zwaarder model alleen strategie en zoekintentie. Elke batch eindigt met maximaal tien regels in `team/status.md`: verstuurd, open, volgende stap, geschat verbruik uit /cost.

## Team

De agents staan in `.claude/agents/`.

| Rol | Agent | Map | Kernvraag | Skill |
|---|---|---|---|---|
| SEO Lead | `seo-lead` | `marketing/` (plan-JJJJ-MM.md) | Wat doen we deze maand, in welke volgorde? | marketing:campaign-plan |
| Technisch SEO-specialist | `technisch-seo` | `marketing/technisch/` | Kan Google de shop goed crawlen en begrijpen? | marketing:seo-audit |
| Zoekwoord- en zoekintentie-onderzoeker | `zoekwoord-onderzoeker` | `marketing/zoekwoorden/` | Waar zoeken klanten naar en waar liggen kansen? | data:analyze |
| Contentstrateeg en redacteur | `content-redacteur` | `marketing/content/` | Welke content wint posities? | marketing:draft-content |
| On-page en conversietekstschrijver | `onpage-copy` | `marketing/onpage/` | Zijn product- en collectiepagina's aantrekkelijk en klikbaar? | design:ux-copy |
| Autoriteit- en lokale SEO-specialist | `autoriteit-lokaal` | `marketing/autoriteit/` | Hoe worden we groter en betrouwbaarder in Google? | marketing:competitive-brief |
| Analist en rapporteur | `analist` | `marketing/rapporten/` | Werkt het, en wat leren we? | marketing:performance-report |
| Merk- en kwaliteitsredacteur | `kwaliteitsredacteur` | `marketing/review/` | Klopt het met de stijl en de regels? | marketing:brand-review |

## Werkvolgorde

De SEO Lead bepaalt per maand de volgorde in `marketing/plan-JJJJ-MM.md`; dat plan gaat voor. Vaste regels: de Kwaliteitsredacteur keurt elke klanttekst vóór publicatie, de Analist rapporteert maandelijks, en pagina's met vertoningen maar weinig klikken gaan voor.

## Databronnen

Search Console, PageSpeed, CrUX en GA4 via `~/.claude/skills/seo/scripts/`, Merchant Center via de Merchant API, zoekvolumes via `python3 scripts/zoekvolumes.py`, Shopify via de Shopify-koppeling. Ahrefs en Semrush alleen gefilterd of als handmatige export. Ruwe exports in `data/<bron>/JJJJ-MM-DD-<onderwerp>.json`. Commando's, property-ID's en accounts: `docs/databronnen.md` (alleen lezen als je data ophaalt).

## Zuinig werken (besluit Mark 27-10-2026)

Tokens zijn schaars; elke rol werkt zo:

1. Eerst de graaf: `graphify query "<vraag>" --budget 1500` of het deel van `graphify-out/GRAPH_REPORT.md` dat je nodig hebt. Open daarna alleen de bestanden of regelbereiken die de graaf aanwijst (Read met offset/limit, of grep op een V-nummer of handle), nooit hele mappen.
2. Grote gedeelde bestanden nooit volledig lezen. `marketing/changelog.md`: alleen de bovenste 30 regels (nieuwste staan bovenaan) of grep op URL of datum. `marketing/vragen-voor-mark.md`: alleen open vragen; afgehandelde staan in `marketing/vragen-beantwoord.md` en lees je alleen bij een concrete V-vraag.
3. Shopify, Search Console en andere API's: altijd met filters, `first`/limiet en alleen de velden die je nodig hebt. Rekenen, sorteren en filteren doe je met een script, niet door ruwe data in het gesprek te laden.
4. Subagents alleen als het werk echt parallel of zwaar is; geef ze een korte, complete opdracht met bestandsnamen. Een licht model (Sonnet) voor uitvoering en teksten, een zwaar model (Opus) alleen voor strategie en zoekintentie.
5. Antwoorden en rapporten kort: wat gedaan, wat open, volgende stap. Geen samenvattingen van wat al in een bestand staat; verwijs naar het bestand.
6. `graphify-out/` bijwerken met `/graphify --update` na een flinke batch documenten, zodat de graaf actueel blijft.

## Overige mappen

`data/` bevat ruwe exports (gsc, ga4, ahrefs, semrush), `assets/` afbeeldingen en screenshots, `scripts/` hulpscripts, `notities/` losse notities. Theme-code staat in `~/TanteRie-Theme-Editor`, niet hier.
