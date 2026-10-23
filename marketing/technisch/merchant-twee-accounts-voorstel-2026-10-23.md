# Twee Merchant Center-accounts: analyse en voorstel (23-10-2026)

Rol: technisch SEO-specialist. Aanleiding: de claim van https://tanterie.nl op account 5716348221 werd geweigerd omdat account 5819585029 een subdomein claimt. Mark heeft zichzelf beheerder gemaakt van 5819585029; dit document is alleen lezend opgesteld, er is niets gewijzigd. Ruwe data: data/merchant/2026-10-23-account-5819585029.json en -producten.json.

## Wat er is

| | Account 5716348221 | Account 5819585029 |
|---|---|---|
| Naam | Tante Rie | Tante Rie |
| Beheerders | markvw80@gmail.com (plus service-account team) | nikkiedekoning@hotmail.com, markvw80@gmail.com |
| Website (geclaimd) | https://webshop.tanterie.nl | http://www.tanterie.nl/ |
| Productbron | Shopify-app Google & YouTube (NL en BE) plus lokale winkelvoorraad | Automatische feed: Google leest de producten zelf van de site |
| Producten | 564 producten, 2.622 varianten per bron | 392 producten, vanaf 5 juli 2026 (de migratiedatum) |
| Status producten | Grotendeels goedgekeurd voor gratis vermeldingen | 387 van 392 staan sinds juli op "wacht op eerste beoordeling", dus niet zichtbaar; daarnaast ontbreken verzendgewichten |
| Productklikken (rapport) | augustus 89, september 43, oktober tot 22e 38 | geen klikken in het productrapport |
| Retourbeleid | sinds vandaag https://tanterie.nl/pages/retourbeleid-tante-rie | dezelfde link, maar ingesteld als levenslang retour, alleen in de winkel; klopt niet met het echte beleid |
| Bedrijfsadres | Bleekweg 34, Enschede | Bakkerssteeg 6, Borne |
| Bedrijfsprofiel gekoppeld | ja | ja |

Het overzicht van 5819585029 toont 311 klikken in 28 dagen. Het productrapport van dat account laat geen klikken zien. Waarschijnlijk telt het overzicht ook klikken via het gekoppelde Bedrijfsprofiel mee. Dat is een inschatting; het rapport zelf geeft geen productklikken.

## Conclusie

Account 5819585029 is rond de migratie in juli ontstaan (vermoedelijk via het Bedrijfsprofiel of de websitecontrole van Google) en draait op een automatische feed die nooit door de beoordeling is gekomen. Het levert geen productverkeer op, het houdt wel de claim op www.tanterie.nl vast. Daardoor kan het echte account, 5716348221 met de Shopify-feed, het hoofddomein niet claimen. Twee accounts met dezelfde producten van dezelfde site zijn bovendien een risico: Google kan ze als dubbel aanbod behandelen.

Account 5716348221 blijft het hoofdaccount: daar zit de Shopify-koppeling, de winkelvoorraad, de checkout en de klikgeschiedenis.

## Voorstel

1. In account 5819585029 de automatische feed uitzetten (Instellingen > Automatische feeds > Producten uit). De 392 wachtende producten verdwijnen dan.
2. In account 5819585029 de websiteclaim intrekken (Instellingen > Bedrijfsgegevens > Website > Claim intrekken).
3. Direct daarna claimt het team https://tanterie.nl op account 5716348221 met scripts/merchant_schrijf.py homepage.
4. Na twee weken, als account 5716348221 stabiel is, account 5819585029 sluiten. Tot die tijd laten staan, zodat we kunnen terugvallen.

Stap 1 en 2 kan het team ook via de API doen, nu Mark beheerder is, maar dat valt buiten het akkoord op V69 en vraagt dus een nieuw ja (V70).

## Bijvangst

De productklikken in account 5716348221 dalen in dezelfde week als de zichtbaarheid: 32 klikken van 1 tot 24 september, 11 klikken van 25 tot 30 september (3.218 tegenover 877 vertoningen). Dat bevestigt dat de val ook Shopping en gratis vermeldingen raakte, niet alleen de gewone zoekresultaten.
