# Handwerk voor Mark, 23 oktober 2026

Je antwoorden op V65 (alles ja) en V69 (alles volgens advies) staan in vragen-voor-mark.md. Het team kon de wijzigingen niet zelf doorvoeren: de veiligheidscontrole van deze sessie blokkeert schrijfacties in Merchant Center en Shopify. Daarom staan hieronder de stappen, met de exacte teksten. Update 23 oktober: met de toestemmingsregels heeft het team A1, B2, C1 en C2 zelf doorgevoerd. Schrijf achter elke stap "gedaan", dan controleert het team de uitkomst en zet het in de changelog.

Backups van de huidige stand: marketing/onpage/backup-eenheidsprijs-test-2026-10-23.json. Retourbeleid nu: https://webshop.tanterie.nl/retourbeleid, homepage nu: https://webshop.tanterie.nl (geclaimd).

## A. Merchant Center (V69)

**A1. Retourbeleid-link herstellen.** GEDAAN door het team (23-10). Merchant Center > Instellingen (tandwiel) > Retourneren > beleid voor Nederland > Retourbeleid-URL wijzigen in `https://tanterie.nl/pages/retourbeleid-tante-rie`. Opslaan.
Status:

**A2. Website naar tanterie.nl.** Merchant Center > Instellingen > Bedrijfsgegevens > Website. Wijzig `https://webshop.tanterie.nl` in `https://tanterie.nl` en klik op Claimen (verificatie gaat via Search Console, waar tanterie.nl al geverifieerd is). Let op: tussen wijzigen en claimen zijn producten even niet goedgekeurd; doe het in één keer.
Status: GEDAAN door het team (23-10), na V70: claim van tweede account 5819585029 ingetrokken, tanterie.nl geclaimd op 5716348221.

**A3. Bedrijfsadres controleren (nieuw, geen actie zonder jou).** In Merchant Center staat als bedrijfsadres Bleekweg 34, 7512 BZ Enschede en als klantenservice webshop@tanterie.nl. Is dat bewust (administratief adres), of moet het Bakkerssteeg 6, Borne zijn? Zet je antwoord hier.
Antwoord:

**A4. Alleen-afhalen producten uit Shopping en gratis webvermeldingen, lokale vermelding behouden.** Akkoord Mark 23-10. Het team heeft in Shopify op alle 143 producten van het verzendprofiel "Breekbare producten" (Bunzlau-aardewerk, Blond Amsterdam, ook de Blond-producten die onder merk Tante Rie staan, en de Pineut-karaffen) het verborgen Google-label custom_label_0 = alleen-afhalen gezet (GEDAAN 23-10, staat al in Merchant Center). Klanten zien dit niet. Status: GEDAAN door het team (23-10). Regels en bestandsupload bleken niet beschikbaar voor de Shopify-bron, daarom via de API een aanvullende bron "Alleen afhalen (team)" gemaakt die 2.036 varianten uitsluit van Shopping en gratis vermeldingen; lokaal blijft. Nieuwe afhaalproducten later: het team maakt een nieuwe lijst en draait scripts/merchant_schrijf.py afhalen opnieuw.

**A5. België blijft aan.** Het advies was niet uitgesproken; omdat het Pakket-profiel een tarief voor België heeft (11,95 euro), blijft de BE-bron aan. Geen actie.

## B. Shopify (V69)

**B1. Kassaproducten uit Google & YouTube (grootste opschoning).** Akkoord Mark 23-10. Het team kan dit niet zelf: de Shopify-koppeling weigert het weghalen van producten van een kanaal. Het team heeft gecontroleerd dat 168 producten niet in de webshop staan en dus weg mogen uit Google; rice-z staat wel online en blijft staan. De lijst met handles staat in marketing/technisch/b1-kassaproducten-google-2026-10-23.txt, de stand vooraf in marketing/technisch/backup-kanalen-kassaproducten-2026-10-23.json.
Snelste manier in Shopify: Producten > filter Verkoopkanaal, kies "Webshop" en zet het filter op "niet opgenomen". Je ziet dan precies de kassaproducten. Selecteer alles (ook "alle producten selecteren" bovenaan) > Meer acties > Uitsluiten van verkoopkanalen > vink alleen Google & YouTube aan > Uitsluiten. Point of Sale en Shop blijven staan. Controleer daarna dat rice-z niet in de selectie zat (die staat in de webshop, dus valt buiten dit filter).
Bunzlau textiel (V63): open het product > Verkoopkanalen beheren > vink Webshop, Shop en Google & YouTube uit, laat Point of Sale aan.
Status: GEDAAN door Mark (23-10), gecontroleerd door het team op 24-10. 159 van de 168 staan niet meer op Google & YouTube; Point of Sale staat bij alle 168 nog aan. De overige negen staan inmiddels in de webshop met voorraad en blijven dus terecht op Google (tegelhouder-joeff, teeli-flip-l-theefilter en zes Bunzlau Castle-producten). Uitzondering: hanger-teapot staat niet in de webshop maar nog wel op Google (V89). De zes Bunzlau-producten zitten in het verzendprofiel Algemeen (V88).

**B2. Eenheidsprijs testen op twee theesoorten.** Producten > Kamille > variant > Prijs per eenheid aanzetten: totale hoeveelheid 40 g, eenheid 100 g. Producten > Gemberwortel: totale hoeveelheid 100 g, eenheid 100 g. Het team controleert na de volgende synchronisatie (1 tot 2 dagen) of Merchant Center de melding "Missing unit pricing measure" voor deze twee kwijt is; daarna volgen de overige 123 losse theesoorten.
Status: GEDAAN door het team (23-10); controle in Merchant Center rond 25-10.

**B3. Foto's voor 27 online producten.** Lijst in data/merchant/2026-10-23-online-zonder-foto.json. Advies: houden en foto's aanleveren; zonder foto komen ze niet in Shopping. Lever foto's aan wanneer het uitkomt, het team plaatst ze.
Status:

## C. Bedrijfsprofiel (V65)

Alle teksten zijn goedgekeurd door de Kwaliteitsredacteur (marketing/review/review-gbp-teksten-2026-10-23.md). Gebruik de teksten daar, niet die in het voorstel.

**C1. Categorieën.** Profiel bewerken > Bedrijfscategorie. Hoofd: Theewinkel. Extra: Cadeauwinkel, Koffiewinkel (blijft, vraag 3), Porseleinwinkel, Winkel in aardewerk, Kookwinkel, Woonwinkel. Noteer de datum en wijzig deze maand verder niets aan de categorieën.
Status: GEDAAN door het team (23-10).

**C2. Beschrijving.** Profiel bewerken > Beschrijving, vervang door:

Tante Rie is de theewinkel in Borne, aan de Bakkerssteeg 6. Aan de theewand vind je ruim 130 soorten losse thee, en je kunt de thee ruiken en eventueel proeven voordat je kiest. Daarnaast hebben we servies van Bunzlau Castle en Blond Amsterdam, melamine en servies van Rice, cadeaus, bakmixen en koffiebonen. Het aardewerk van Bunzlau Castle en het servies van Blond Amsterdam haal je af in de winkel. Melamine en Rice sturen we ook op. Parkeren kan in de buurt met een parkeerschijf of in de gratis parkeergarage. De winkel is rolstoeltoegankelijk.

Status: GEDAAN door het team (23-10).

**C3. Producten (handmatig, de API kan dit niet).** Profiel bewerken > Producten > vier categorieën: Losse thee (https://tanterie.nl/collections/thee), Bunzlau Castle (https://tanterie.nl/collections/bunzlau), Blond Amsterdam (https://tanterie.nl/pages/blond-amsterdam-servies), Servies (https://tanterie.nl/pages/serviezen). Zet achter elke link `?utm_source=gbp&utm_medium=organic&utm_campaign=producten`. Per categorie drie tot vijf producten die in de winkel op voorraad liggen, zonder prijs.
Status:

**C4. Berichten.** Het team plaatst elk bericht op de dag zelf met scripts/gbp_schrijf.py (het script weigert vóór de geplande datum); jij hoeft alleen te controleren of het verschijnt. Teksten staan in de review, paragrafen 2 tot en met 5. Foto's: de bestanden uit marketing/technisch/winkelfotos-shopify-2026-10-23.json.
- dinsdag 27 oktober: theewand, foto theewand-losse-thee.jpg
- dinsdag 3 november: Bunzlau Castle, foto bunzlau-wand.jpg
- dinsdag 10 november: Blond Amsterdam, foto blond-amsterdam-wand.jpg
- dinsdag 17 november: feestdagen, foto cadeautafel-winkel.jpg, herhaling rond 15 december

Knop steeds Meer informatie met de link en UTM uit het voorstel (paragraaf 5). Komen er koopavonden in december (V35), dan gaat bericht 4 eerst opnieuw langs review.
Status:

**C5. Reviewbeleid en QR-code.** Het profiel maakt zelf een QR-code: Bedrijfsprofiel > Reviews vragen > QR-code downloaden. Print die voor bij de kassa. Het beleid staat in het voorstel, paragraaf 6.
Status:

**C6. Twee API's aanzetten (vraag 10).** In Google Cloud, project 28634605562: zet "My Business Verifications API" en "My Business Notifications API" aan (APIs & Services > Library > zoeken > Enable).
Status:
