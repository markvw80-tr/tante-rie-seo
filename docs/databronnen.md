# Databronnen

Uitgebreide toegangsgegevens en voorbeelden, verplaatst uit CLAUDE.md (27-10-2026) om tokens te sparen. Lees dit alleen als de opdracht data ophaalt.

Search Console (property `sc-domain:tanterie.nl`) en PageSpeed/CrUX gaan via de scripts in `~/.claude/skills/seo/scripts/`, met credentials uit `~/.config/claude-seo/`. Voorbeelden:

```bash
cd ~/.claude/skills/seo/scripts && export PYTHONWARNINGS=ignore
python3 gsc_query.py --days 90 --dimensions query,page --limit 1000 --json   # zoekopdrachten en pagina's
python3 gsc_query.py sitemaps --json                                          # sitemapstatus
python3 gsc_inspect.py https://tanterie.nl/<pad> --json                 # indexatiestatus van één URL
python3 pagespeed_check.py https://tanterie.nl/ --json                  # Lighthouse + CrUX
```

GA4: property `properties/521523059` (Tante Rie), toegang via hetzelfde service-account; `python3 ga4_report.py --property properties/521523059 --json` in dezelfde scriptmap. Merchant Center: account 5716348221; lezen via de Merchant API (https://merchantapi.googleapis.com/products/v1/accounts/5716348221/products) met het service-account; project is op 23-10 als ontwikkelaar aangemeld. Chrome UX Report API is ingeschakeld op de bestaande API-sleutel. Google Ads API (Keyword Planner, voor zoekvolumes): Basic access sinds 24-10 (na merkverificatie van het OAuth-project). Zoekvolumes via `python3 scripts/zoekvolumes.py volumes|ideeen ...` (Nederlands, Nederland); ruwe uitvoer in `data/keyword-planner/`. Geen ontwikkelaarstoken nodig (afgeschaft per 9-9-2026, toegang hoort bij Cloud-project tante-rie); het script leest het klant-ID uit `~/.config/claude-seo/google-api.json` en de inlog uit `ads-token.json`, die Mark eenmalig aanmaakt. De invoerlijst staat in `marketing/zoekwoorden/keyword-planner-invoer-2026-10-23.txt`.

Sla ruwe exports op in `data/gsc/` als `JJJJ-MM-DD-<onderwerp>.json`. Shopify gaat via de Shopify-koppeling. Ahrefs (plan te laag) en Semrush (geen API-units) werken niet via de API; gebruik alleen handmatige exports in `data/ahrefs/` en `data/semrush/` als die er zijn.
