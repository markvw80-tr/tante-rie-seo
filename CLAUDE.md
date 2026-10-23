# Tante Rie: SEO-marketingteam

## Doel

Hoger scoren in Google en daarmee meer organische bezoekers naar tanterie.nl. Alle rollen werken naar dat doel toe en volgen de spelregels hieronder.

Prioriteit (besluit Mark 21-10-2026): 70 procent van de inzet gaat naar meer bezoekers in de fysieke winkel in Borne, 30 procent naar groei van de webshop. Reden: de winkel levert ruim 99 procent van de omzet (nulmeting sept-okt 2026: 698 kassabestellingen tegenover 2 online bestellingen in vier weken). Lokale SEO (Google Bedrijfsprofiel, de theewinkelpagina, zoektermen rond Borne en Twente) gaat daarom voor, en product- en collectiepagina's dienen ook als etalage voor de winkel. Meet succes vooral met Search Console-klikken, acties in het Bedrijfsprofiel (route, bellen, website) en waar mogelijk kassaomzet, niet alleen met online omzet. Zakelijke verkoop (/pages/zakelijk) breidt Mark voorlopig niet uit via Tante Rie; daar wordt geen SEO-werk aan gedaan. Aanvulling Mark 23-10: de 70/30-verdeling is een eerste stap; het uiteindelijke doel is meer verkoop via de webshop, dus vanaf maand 2 groeit het webshopdeel.

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

Alle open vragen voor Mark staan in `marketing/vragen-voor-mark.md`; Mark vult die in wanneer hij tijd heeft. Elke rol leest dat bestand aan het begin van een opdracht en gebruikt de ingevulde antwoorden. Nieuwe vragen komen erbij met een volgnummer (V35, V36, ...), prioriteit en een verwijzing naar het bestand waar ze bij horen, niet alleen in het eigen werkbestand. Een verwerkt antwoord gaat naar de tabel "Beantwoord" onderaan. Een lege vraag is geen nee: werk door met wat zonder antwoord kan en laat de zin weg die op het antwoord wacht. Een ingevuld antwoord in dit bestand geldt als akkoord van Mark voor precies dat punt.

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

Tweede keus: brand-voice:enforce-voice bij alle schrijvende rollen, data:create-viz en data:build-dashboard bij de Analist, anthropic-skills:deep-research bij de zoekwoordonderzoeker.

## Werkvolgorde

Maand 1: Technisch SEO-specialist doet een volledige audit en de Zoekwoordonderzoeker een eerste kansenanalyse op basis van Search Console (parallel). De SEO Lead maakt daaruit een prioriteitenlijst van maximaal tien acties. Maand 1 en 2: Contentstrateeg en Conversietekstschrijver pakken de grootste kansen op, namelijk collecties en topproducten die al op positie 5 tot 20 staan. Vanaf maand 2 draait de Autoriteit- en lokale SEO-specialist mee. De Analist rapporteert elke maand, de Kwaliteitsredacteur keurt alles goed vóór publicatie. Begin met pagina's die al vertoningen hebben maar weinig klikken.

## Databronnen

Search Console (property `sc-domain:tanterie.nl`) en PageSpeed/CrUX gaan via de scripts in `~/.claude/skills/seo/scripts/`, met credentials uit `~/.config/claude-seo/`. Voorbeelden:

```bash
cd ~/.claude/skills/seo/scripts && export PYTHONWARNINGS=ignore
python3 gsc_query.py --days 90 --dimensions query,page --limit 1000 --json   # zoekopdrachten en pagina's
python3 gsc_query.py sitemaps --json                                          # sitemapstatus
python3 gsc_inspect.py https://tanterie.nl/<pad> --json                 # indexatiestatus van één URL
python3 pagespeed_check.py https://tanterie.nl/ --json                  # Lighthouse + CrUX
```

GA4: property `properties/521523059` (Tante Rie), toegang via hetzelfde service-account; `python3 ga4_report.py --property properties/521523059 --json` in dezelfde scriptmap. Merchant Center: account 5716348221; lezen via de Merchant API (https://merchantapi.googleapis.com/products/v1/accounts/5716348221/products) met het service-account; project is op 23-10 als ontwikkelaar aangemeld. Chrome UX Report API is ingeschakeld op de bestaande API-sleutel. Google Ads API (Keyword Planner, voor zoekvolumes) is op 23-10 aangezet; het ontwikkelaarstoken heeft Explorer access. Explorer blokkeert de Keyword Planner-diensten (KeywordPlanIdeaService), daarvoor is Basic access nodig. Tot Basic access er is werkt de zoekwoordonderzoeker met handmatige Keyword Planner-exports in `data/keyword-planner/`; de invoerlijst staat in `marketing/zoekwoorden/keyword-planner-invoer-2026-10-23.txt`.

Sla ruwe exports op in `data/gsc/` als `JJJJ-MM-DD-<onderwerp>.json`. Shopify gaat via de Shopify-koppeling. Ahrefs (plan te laag) en Semrush (geen API-units) werken niet via de API; gebruik alleen handmatige exports in `data/ahrefs/` en `data/semrush/` als die er zijn.

## Overige mappen

`data/` bevat ruwe exports (gsc, ga4, ahrefs, semrush), `assets/` afbeeldingen en screenshots, `scripts/` hulpscripts, `notities/` losse notities. Theme-code staat in `~/TanteRie-Theme-Editor`, niet hier.
