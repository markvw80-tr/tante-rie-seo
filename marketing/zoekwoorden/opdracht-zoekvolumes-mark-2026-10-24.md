# Opdracht voor Mark: zoekvolumes ophalen (24 oktober 2026)

Sinds 24 oktober heeft het Cloud-project Basic access tot de Google Ads API. Het script scripts/zoekvolumes.py haalt daarmee de Keyword Planner-volumes op (taal Nederlands, locatie Nederland). In de cloudsessies zijn geen credentials, dus dit draai je op je eigen computer. Het kost ongeveer tien minuten, waarvan de eerste keer vijf voor het inloggen. Daarna is de handmatige export uit plan-2026-11 (actie 9, V75) niet meer nodig.

Doel: de volumes in data/keyword-planner/ krijgen, zodat de zoekwoordonderzoeker de clusters opnieuw kan berekenen met echte getallen in plaats van schattingen op basis van vertoningen.

## Eenmalig: installeren, account en inloggen

Ga naar de map van de repository en haal deze branch op:

```bash
cd "/Users/markvanwijk/Tante Rie SEO"
git fetch origin && git checkout claude/zoekwoord-volumes && git pull
pip3 install --upgrade google-ads google-auth-oauthlib
```

Voer daarna het klant-ID van Google Ads in (het account waarmee je de Zoekwoordplanner gebruikt, formaat 123-456-7890). Het managementaccount-ID laat je leeg tenzij je via een managementaccount inlogt:

```bash
python3 scripts/zoekvolumes.py account
```

Log in via de browser met het Google-account dat bij dat Google Ads-account hoort. Het token komt in ~/.config/claude-seo/ads-token.json:

```bash
python3 scripts/zoekvolumes.py inloggen
```

Een ontwikkelaarstoken is niet nodig; de toegang hangt aan het Cloud-project van de OAuth-client. Als de eerste opdracht hieronder een foutmelding over toegang geeft, stuur me de foutmelding.

## Volumes ophalen

1. Volumes voor alle zoekwoorden uit de invoerlijst van 23 oktober (212 regels, met maandcijfers voor het seizoenspatroon):

```bash
python3 scripts/zoekvolumes.py volumes --bestand marketing/zoekwoorden/keyword-planner-invoer-2026-10-23.txt --onderwerp invoerlijst
```

2. Nieuwe ideeën uit de seedlijst van 24 oktober (19 seeds, december, lokaal, webshop, Bunzlau, servies en Rice). Dit is een aanroep voor alle seeds samen en levert de volgende ideeën met volume op, zonder maandcijfers:

```bash
python3 scripts/zoekvolumes.py ideeen --bestand marketing/zoekwoorden/keyword-planner-ideeen-seeds-2026-10-24.txt --limiet 200 --onderwerp ideeen-seeds
```

3. Optioneel, alleen als je wilt zien welk idee bij welke seed hoort (de Keyword Planner geeft dat bij een gezamenlijke aanroep niet terug). Dit maakt per seed een eigen bestand en duurt iets langer:

```bash
python3 scripts/zoekvolumes.py ideeen "kerstpakket thee" --limiet 50 --onderwerp ideeen-kerstpakket-thee
python3 scripts/zoekvolumes.py ideeen "theewinkel twente" --limiet 50 --onderwerp ideeen-theewinkel-twente
python3 scripts/zoekvolumes.py ideeen "losse thee kopen" --limiet 50 --onderwerp ideeen-losse-thee-kopen
```

Stap 1 is het belangrijkste. Stap 2 is een goede tweede. Stap 3 is niet nodig voor de herberekening.

Elke aanroep print een lijst met volume, concurrentie en zoekwoord, en slaat de ruwe uitvoer op als data/keyword-planner/2026-10-24-<onderwerp>.json (de datum van de dag waarop je draait).

## Wat ik van je terug nodig heb

De json-bestanden committen en pushen naar deze branch:

```bash
git add data/keyword-planner/*.json
git commit -m "Keyword Planner: zoekvolumes en ideeen"
git push origin claude/zoekwoord-volumes
```

Meld daarna in de sessie dat het gepusht is (V92 in marketing/vragen-voor-mark.md).

## Wat ik daarna oplever

Zodra de bestanden op de branch staan:

1. Het script scripts/volumes_in_clusters.py koppelt de volumes aan de clustertabellen en geeft per cluster het totaalvolume per maand, het volume per zoekwoord naast vertoningen en positie, het aandeel zichtbaarheid en de piekmaanden. Uitvoer in marketing/zoekwoorden/volumes-clusters-<datum>.md.
2. marketing/zoekwoorden/clusters-<datum>.md met echte volumes in plaats van schattingen, en per cluster een advies (bestaande pagina aanpassen, nieuwe pagina maken of negeren) met het getal waarop het rust. De drie vragen uit plan-2026-11 actie 9 krijgen een antwoord: is een gids over theecadeaus of kruidenthee het waard, hoe groot is 'theewinkel' landelijk, en welke webshoptermen (losse thee, Rice, melamine) hebben genoeg volume.
3. Bijgewerkte prioriteiten voor de SEO Lead: de top 10 uit het clusterrapport opnieuw gerangschikt met volume, en een voorstel voor wat in december voorrang krijgt.

Waar een volume ontbreekt of de Keyword Planner alleen een bereik of een nul geeft, markeer ik dat als onzeker en verzin ik niets.

## Samengevat

| Stap | Opdracht | Eenmalig |
|---|---|---|
| 1 | pip3 install --upgrade google-ads google-auth-oauthlib | Ja |
| 2 | python3 scripts/zoekvolumes.py account | Ja |
| 3 | python3 scripts/zoekvolumes.py inloggen | Ja |
| 4 | python3 scripts/zoekvolumes.py volumes --bestand marketing/zoekwoorden/keyword-planner-invoer-2026-10-23.txt --onderwerp invoerlijst | Nee |
| 5 | python3 scripts/zoekvolumes.py ideeen --bestand marketing/zoekwoorden/keyword-planner-ideeen-seeds-2026-10-24.txt --limiet 200 --onderwerp ideeen-seeds | Nee |
| 6 | git add data/keyword-planner/*.json, committen en pushen | Nee |
