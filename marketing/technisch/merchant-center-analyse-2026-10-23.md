# Merchant Center: analyse en opschoonvoorstel (23-10-2026)

Rol: technisch SEO-specialist. Aanleiding: vraag V68 in `marketing/vragen-voor-mark.md`, Mark zei ja op analyse plus voorstel. Dit document is alleen analyse en voorstel. Er is niets gewijzigd in Merchant Center of Shopify.

Bronnen: Merchant API (alleen lezen, account 5716348221), Shopify Admin API (alleen lezen), de openbare winkel (`products.json`, productpagina's, curl). Ruwe data staat in `data/merchant/2026-10-23-*.json`.

## 1. Samenvatting

1. De getallen in V68 geven een veel grotere indruk dan de werkelijkheid. Merchant Center telt elk probleem **zes keer** (zes bestemmingen: Shopping-advertenties, Display, gratis vermeldingen, Demand Gen, Video en Demand Gen Discover). Daarnaast zijn er twee webshopbronnen (NL en BE). Echte aantallen per bron: 175 regels met "Product page unavailable" (NL) tegenover de gemelde 2.016, en 187 regels met "Missing product image" tegenover 2.244. De 7.871 regels zijn drie bronnen van elk ongeveer 2.622 varianten, geen 7.871 verschillende producten.
2. Er zijn geen dubbele producten in de zin van oude en nieuwe feed. Alle links wijzen naar `tanterie.nl`, niet naar `webshop.tanterie.nl`. De drie bronnen zijn: Shopify-app voor Nederland (2.622 regels), dezelfde Shopify-app voor België (2.622 regels) en een lokale feed voor winkelvoorraad (2.627 regels). Het zijn dezelfde 2.622 varianten (564 producten), driemaal aangeboden.
3. De grootste oorzaak van afkeuringen is dat **kassaproducten** (alleen in Shopify POS) toch naar Google worden gestuurd. Het gaat om 169 producten (179 varianten), zoals Luminlique, kaarten, kaarsen, koffie en een aantal Bunzlau-stukken. Zij hebben een 404 op de site en meestal geen foto. Dat verklaart 175 van de 175 "Product page unavailable"-regels, 160 van de 187 "Missing product image"-regels en alle 8 "Invalid product price"-regels. Dit is volgens CLAUDE.md fout en moet uit de feed.
4. Van de online producten zijn er maar weinig echt kapot: 28 van 2.443 online varianten zijn afgekeurd voor gratis vermeldingen. Daarvan zijn 27 varianten van 27 producten zonder foto in Shopify. Dat is de enige echte online reparatie.
5. Omgekeerd ontbreken 27 online producten in Google (304 varianten): tien Bunzlau-producten met veel varianten en 17 losse theesoorten. Ze staan niet op het verkoopkanaal Google & YouTube.
6. "Mismatched availability" is geen fout in de data, maar een signaal: alle 411 regels (NL) zijn Bunzlau Castle. De feed zegt "op voorraad" (voorraad 0, te bestellen), de site toont "niet beschikbaar" en Google corrigeert dat zelf. Bunzlau is alleen af te halen in Borne.
7. Er zijn geen accountproblemen (account issues leeg). Wel staat de retourbeleid-link in Merchant Center op een adres dat nu een 404 geeft (zie 8).
8. Prijs per eenheid (losse thee, per 100 gram) ontbreekt bij 168 online varianten. In Shopify staat bij losse thee geen eenheidsprijs ingevuld. Dat is de oorzaak. Het is niet blokkerend.

## 2. Vraag 1: welke bronnen sturen producten in

| Bron | Gegevensbron-ID | Land / feedlabel | Regels | Unieke varianten | Producten | Bestemmingen |
|---|---|---|---|---|---|---|
| Shopify App API (NL) | 10606676973 | NL, EUR_107259592968 | 2.622 | 2.622 | 564 | Shopping, Display, gratis vermeldingen |
| Shopify App API (BE) | 10706837209 | BE, EUR_114053906696 | 2.622 | 2.622 | 564 | Shopping, Display, gratis vermeldingen, lokaal |
| Local Feed Partnership (legacy local) | 10681078097 | NL, EUR_107259592968 | 2.627 | 2.627 | 564 | Lokale vermeldingen en lokale voorraadadvertenties |
| Totaal | | | 7.871 | 2.627 | 564 | |

Bevindingen:

- Dubbelingen zijn structureel: dezelfde variant staat in drie bronnen. De BE-bron is een tweede kopie van de Nederlandse regels voor het Belgische land. De lokale bron heeft 5 varianten extra ten opzichte van de webshopbronnen.
- Alle productlinks gaan naar `tanterie.nl` (2.622 van 2.622). Geen enkele naar `webshop.tanterie.nl`. De vraag of oude webshop-URL's de oorzaak zijn kan dus met nee worden beantwoord.
- Het account zelf heeft nog `https://webshop.tanterie.nl` als website en als geclaimde homepage. Die redirect 301 naar `https://tanterie.nl/`, maar de claim hoort op het hoofddomein te staan.
- Shopify heeft 423 producten online (2.747 varianten). In Google staan 564 producten (2.622 varianten): 396 online producten, 168 kassaproducten, en 27 online producten ontbreken.
- De BE-bron laat 1.882 varianten op "niet op voorraad" zien tegenover 1.497 in de NL-bron. Dat verschil komt door de verzendregels per land.
- Lokale voorraad: slechts 525 van 2.627 lokale regels hebben een voorraadregel voor de winkel. 144 daarvan staan op "op voorraad" (128 online, 16 kassaproducten). Voor de overige 2.102 regels heeft Google geen winkelvoorraad, dus daar kan de lokale vermelding niet werken.

## 3. Vraag 2: Product page unavailable

| | NL-bron | BE-bron | Opmerking |
|---|---|---|---|
| Regels met fout | 175 | 161 | Weergave in Merchant Center: 2.016 (336 regels x 6 bestemmingen) |
| Waarvan online in Shopify | 0 | 0 | |
| Waarvan kassaproduct | 175 | 161 | 165 van 169 kassaproducten hebben deze fout |

Steekproef met curl (23-10-2026): `positivitea`, `kaart-nfc`, `kaars-hoera`, `sauce-bowl-50-ml` en `pouchbag-cava-sangria` geven allemaal HTTP 404. `rice-z` geeft 200 en is wel online.

Oorzaak: de producten hebben in Shopify het kanaal Point of Sale en Google & YouTube, maar niet het kanaal Webshop. Voorbeeld `positivitea`: kanalen Point of Sale, Shop en Google & YouTube, geen Webshop. Daardoor stuurt de Google-app ze toch door, terwijl de pagina niet bestaat. Een 404 is hier juist correct, de fout zit in de koppeling.

Verdeling van de 169 kassaproducten in Google: Tante Rie zelf 156, Bunzlau Castle 8, Luminlique 4, Joeff 1. Lijst: `data/merchant/2026-10-23-kassaproducten-in-google.json`.

Eén uitzondering: één variant van `rice-z` staat als goedgekeurd terwijl de variant niet meer in de openbare productlijst zit. Het product zelf is online (200). Controleer die variant in Shopify.

## 4. Vraag 3: Missing product image

| | NL-bron | Opmerking |
|---|---|---|
| Regels met fout | 187 | Weergave: 2.244 (374 regels x 6) |
| Kassaproducten | 160 | Verdwijnen mee met de opschoning uit stap 1 |
| Online producten | 27 (27 producten, 1 variant elk) | Echt te herstellen |

De 27 online producten zonder foto (Shopify: gepubliceerd, geen media): gouden-thee-bewaarblik-50-gram, knuffelbeer, pu-erh-thee, theezeefje-chacult, glutenvrije-basismix, glutenvrije-red-velvetmix, glutenvrije-cupcakemix, glutenvrije-boterkoekmix, glutenvrije-appeltaartmix, cheese-frosting-200-gram, bikkels-16, bikkels-10, bikkels-5, bunzlau-textiel, hibiscus-thee, chocoladebal, thee-filter-zonder-uitlekschaaltje, thee-ei, thee-ei-kat, thee-ei-bij, beker-paarse-bloem, beker-vogels, blikje-vogels, blikje-paarse-bloemen-rond, blikje-paarse-bloemen, blikje-herfst, blikje-bij. Bestand: `data/merchant/2026-10-23-online-zonder-foto.json`.

Oorzaak: er is voor deze producten nooit een foto geupload. De kassaproducten zonder foto zijn niet relevant zolang ze uit Google gaan.

Overige beeldmeldingen (niet het grootste punt): 132 varianten met een afbeelding kleiner dan 500x500 pixels (waarschuwing, niet blokkerend), 17 online varianten met "Image under review", 5 "Image processing" en 1 "Image not processed" (tijdelijk, lossen zichzelf op).

## 5. Vraag 4: Invalid product price

| | NL-bron | BE-bron | Opmerking |
|---|---|---|---|
| Regels | 8 | 8 | Weergave: 96 (16 regels x 6) |
| Online | 0 | 0 | |

De regels hebben prijs 0,00 euro. Het zijn 6 kassaproducten (8 varianten): sauce-bowl-50-ml, hanger-teapot, hanger-cup-and-saucer, bowl-square-70-ml, cake-dish-flat-o-15-5-cm en mug-cappuccino-400-ml. Dit zijn Bunzlau-artikelen zonder verkoopprijs in Shopify, die nog niet online verkocht worden.

Oorzaak: prijs 0 in Shopify bij kassaproducten. Verdwijnt met stap 1. Geen aparte prijsreparatie nodig.

## 6. Vraag 5: Mismatched availability en alleen-afhalen

| | NL-bron | BE-bron |
|---|---|---|
| Regels met melding | 411 | 219 |
| Weergave in Merchant Center | 3.780 voor beide bronnen samen (630 regels x 6) | |
| Merk | 100 procent Bunzlau Castle (46 producten) | Bunzlau Castle |

Wat er gebeurt: de feed meldt "op voorraad" met voorraad 0, de site meldt "niet beschikbaar". Google zet de status zelf om naar de siteversie. Dat is geen afkeuring en kost niets, maar het maakt het statusbeeld onbetrouwbaar.

Oorzaak, vastgesteld met de productpagina's: Bunzlau Castle en Blond Amsterdam zijn alleen af te halen in Borne. De productpagina toont "Alleen afhalen in Borne" en "Te bestellen, wij bellen je zodra het klaar ligt". Dit zijn bestelartikelen zonder voorraad (de voorraadinstelling per variant heb ik niet kunnen uitlezen; dit is afgeleid uit de feed met voorraad 0 en status "op voorraad"). In het gewone verzendprofiel "Breekbare producten" zijn geen verzendzones ingesteld, dus die producten zijn niet naar huis te laten bezorgen. De drie verzendprofielen (Algemeen, Thee, Breekbare producten, Pakket) zijn dus niet de directe oorzaak van het voorraadverschil. Het is het combineren van bestellen bij nul voorraad met alleen afhalen.

Aantal alleen-afhalen producten: 66 producten gecontroleerd en bevestigd (40 Blond Amsterdam, 26 Bunzlau Castle, samen 749 varianten). Bij nog 59 producten (vooral Bunzlau) kon de pagina niet worden gelezen omdat de site de aanvraag begrensde. Het werkelijke aantal ligt dus hoger en moet bij uitvoering volledig worden bepaald.

Moeten alleen-afhalen producten in Shopping? Mijn advies: nee voor Shopping-advertenties en gratis webvermeldingen. De klik komt op een pagina waar je niet kunt bezorgen, en in de feed krijgen deze producten toch de standaardverzendkosten van het account (4,50 en 6,95 euro) omdat ze geen eigen verzendregel hebben. Wel passend zijn de lokale vermeldingen met bestemming "ophalen in de winkel", als daar winkelvoorraad bij hoort. Dat sluit aan op de prioriteit van 70 procent voor de winkel en op de regel dat "ook verkrijgbaar in de winkel" alleen bij voorraad hoort.

## 7. Vraag 6: prijs per eenheid voor losse thee

| | Aantal |
|---|---|
| Regels met melding (NL) | 216 |
| Waarvan online | 168 varianten (168 producten) |
| Losse thee | 125 |
| Zonder producttype | 36 |
| Cadeau | 4 |
| Overig (keramiek, theemix, servetten) | 3 |
| Weergave in Merchant Center | 3.118 (216 NL x 6 + 227 BE x 6 + 230 lokaal x 2) |

Oorzaak: in Shopify is bij losse thee de eenheidsprijs leeg (bij `kamille` en `gemberwortel`: hoeveelheid 0, referentie 0). De feed bevat wel het gewicht (40, 75, 90 of 100 gram), maar geen eenheidsprijsmaat. De melding is niet blokkerend.

Oplossing: vul in Shopify per variant "Eenheidsprijs" in (bijvoorbeeld 40 g, met referentie 100 g). Dit is de standaard Shopify-instelling per variant. Mijn verwachting is dat de Shopify-app Google & YouTube dit overneemt als eenheidsprijsmaat, maar dat heb ik niet kunnen bevestigen zonder het te proberen. Test het daarom eerst op twee producten en controleer na de volgende synchronisatie in Merchant Center. Werkt het niet, dan is de terugvaloptie een aanvullende gegevensbron in Merchant Center met de maat per product. Een metafield helpt hier niet, want de Shopify-app leest geen vrij metafield voor dit veld. Dit is een inschatting, geen vastgesteld feit.

## 8. Vraag 7: accountproblemen en instellingen

| Onderdeel | Status |
|---|---|
| Account issues (accounts/v1 issues) | Leeg, geen openstaande accountproblemen |
| Programma's | Gratis vermeldingen aan, Shopping-advertenties aan, Checkout aan; productbeoordelingen niet in aanmerking |
| Website van het account en homepage | `https://webshop.tanterie.nl` (geclaimd). Leidt via 301 naar `tanterie.nl`, maar de claim voor het hoofddomein ontbreekt in deze instelling |
| Retourbeleid | Verwijst naar `webshop.tanterie.nl/retourbeleid`. Dat redirect naar `tanterie.nl/retourbeleid`, wat HTTP 404 geeft. De echte pagina is `https://tanterie.nl/pages/retourbeleid-tante-rie` (200) of `https://tanterie.nl/policies/refund-policy` (200) |
| Verzending | Twee diensten: Nederland op gewicht (4,50 euro tot 0,3 kg, 6,95 euro daarboven, geen verzending boven 5 kg) en Belgie vast 11,95 euro |
| Gegevensbron Shopify App API (NL) | Lokale vermeldingen uit, Shopping en gratis vermeldingen aan |

Een kapotte retourbeleid-link is een risico voor goedkeuring van Shopping en het toont geen retourinformatie bij vermeldingen. Dit staat daarom hoog in het voorstel.

## 9. Overzicht echte tegenover gemelde aantallen

| Probleem | Gemeld | Werkelijk NL-bron | Werkelijk BE-bron | Online producten geraakt |
|---|---|---|---|---|
| Missing product image | 2.244 | 187 | 187 | 27 |
| Product page unavailable | 2.016 | 175 | 161 | 0 |
| Invalid product price | 96 | 8 | 8 | 0 |
| Mismatched availability | 3.780 | 411 | 219 | 411 (Bunzlau) |
| Missing unit pricing measure | 3.118 | 216 | 227 | 168 |
| Gratis vermeldingen goedgekeurd | 4.822 | 2.411 | 2.411 | 2.410 |
| Gratis vermeldingen afgekeurd | 412 | 206 | 206 | 28 |

Zodra de 179 kassavarianten uit de feed zijn, zakt het aantal afgekeurde regels per bron van 206 naar ongeveer 28, en dat zijn bijna alleen de 27 producten zonder foto.

## 10. Opschoonvoorstel, gerangschikt op impact

| # | Stap | Wat moet er gebeuren | Wie | Effect |
|---|---|---|---|---|
| 1 | Kassaproducten uit Google halen | In Shopify bij de 169 kassaproducten het verkoopkanaal Google & YouTube uitzetten (alleen Point of Sale laten staan). Lijst staat in `data/merchant/2026-10-23-kassaproducten-in-google.json`. Dit kan in bulk via Shopify (producten filteren op "niet beschikbaar op Webshop" en kanaal wijzigen). Eerst een voor-en-nalijst aan Mark laten zien. | Mark keurt goed, team levert lijst, Shopify-wijziging door Mark of na akkoord door het team | Verwijdert ongeveer 175 plus 160 plus 8 fouten per bron en ruim 5 procent van de regels. Houdt de regel uit CLAUDE.md in stand |
| 2 | Retourbeleid-link herstellen | In Merchant Center de URL van het retourbeleid wijzigen naar `https://tanterie.nl/pages/retourbeleid-tante-rie` | Mark (of team na akkoord) | Voorkomt afwijzing en toont retourinfo |
| 3 | Website van het account naar tanterie.nl | Website-URL in Merchant Center zetten op `https://tanterie.nl` en dat domein claimen | Mark | Rondt de migratie af, geen eigen domein-claim op het oude subdomein |
| 4 | 27 online producten zonder foto | Foto toevoegen in Shopify (lijst in `2026-10-23-online-zonder-foto.json`). Zonder foto kunnen ze niet in Shopping | Mark levert foto's, team plaatst na akkoord | Haalt de laatste 27 afgekeurde online producten binnen |
| 5 | Alleen-afhalen producten uit Shopping en gratis webvermeldingen | Voor Bunzlau Castle en Blond Amsterdam (66 bevestigd, ongeveer 125 verwacht) de bestemming Shopping en gratis vermeldingen uitsluiten, maar de lokale vermelding behouden. Mogelijkheid A: in Merchant Center een regel in een aanvullende gegevensbron. Mogelijkheid B: kanaal Google & YouTube uitzetten voor deze producten (dan verdwijnen ze ook uit de lokale feed). Eerst Mark laten kiezen | Mark kiest, team richt in | Weg met 411 voorraadmeldingen en met verzoeken naar producten die niet te bezorgen zijn |
| 6 | Prijs per eenheid voor losse thee | Eerst testen op twee producten (eenheidsprijs per 100 g in Shopify), na synchronisatie controleren. Daarna voor alle 125 losse thee invullen | Mark of team na akkoord; Shopify-app doet de synchronisatie | Haalt ongeveer 168 meldingen weg en is nuttig voor thee op gewicht |
| 7 | Belgische bron beoordelen | Besluiten of de BE-bron blijft. Er is een BE-verzendtarief (11,95 euro), maar de webshop is vooral lokaal. Uitzetten halveert het aantal webregels en de meldingen | Mark | Minder ruis en een duidelijker overzicht |
| 8 | 27 online producten die ontbreken in Google | Tien Bunzlau-producten (304 varianten) en 17 losse theesoorten staan alleen op Webshop (of Webshop en Shop), niet op Google & YouTube. Voor de losse thee: kanaal Google & YouTube aanzetten zodra de eenheidsprijs er is. Voor Bunzlau geldt stap 5 | Mark | Meer thee in Shopping |
| 9 | Lokale vermeldingen en winkelvoorraad beoordelen | Slechts 525 van 2.627 lokale regels hebben winkelvoorraad (144 op voorraad). De 16 kassaproducten op voorraad zijn een kans voor lokale vermeldingen, maar horen volgens CLAUDE.md niet online. Mark beslist of lokale vermeldingen zonder webpagina gewenst zijn | Mark beslist | Direct gekoppeld aan het winkelbezoek (70 procent doel) |
| 10 | Kleine aandachtspunten | Hoofdletters in 12 titels, afbeeldingen onder 500x500 pixels (132 varianten), alcoholproducten zoals Pineut en likeur (aangemerkt voor gepersonaliseerde advertenties), geen aandacht nodig voor "Image processing" | Team, na akkoord | Lage prioriteit |

Na elke stap controleren we met een nieuwe uitlezing van de Merchant API of het aantal afgekeurde regels daalt. Wijzigingen worden pas in `marketing/changelog.md` gezet nadat ze zijn uitgevoerd.

## 11. Open punten en beperkingen

- De lokale voorraadregel is per product opgevraagd. Voor 59 producten (vooral Bunzlau) kon de "Alleen afhalen"-controle niet worden afgerond omdat de site te veel opeenvolgende verzoeken weigerde. Het aantal alleen-afhalen producten is dus een ondergrens.
- Of de Shopify-app een Shopify-eenheidsprijs overneemt als eenheidsprijsmaat is niet vastgesteld. Zie stap 6.
- Het kanaal Google & YouTube is per product vastgesteld voor vier voorbeelden (`kamille`, `eierdopje`, `positivitea`, `rice-z`). De uitspraak dat alle 169 kassaproducten dit kanaal hebben volgt uit het feit dat ze in de feed staan.
- Shopify gaf geen toegang tot `read_product_listings`, dus de kanalenlijst per product is niet in bulk opgehaald.

## 12. Vragen voor Mark (ja of nee)

1. Mogen de 169 kassaproducten (zoals Luminlique, kaarten, kaarsen) uit het kanaal Google & YouTube gehaald worden, zodat ze alleen nog in de kassa staan? Ja/nee
2. Mag de retourbeleid-link in Merchant Center verwezen worden naar `https://tanterie.nl/pages/retourbeleid-tante-rie`? Ja/nee
3. Mag de website van het Merchant Center-account veranderd en geclaimd worden op `https://tanterie.nl`? Ja/nee
4. Lever je foto's voor de 27 online producten zonder foto, of zullen we ze uit de webshop halen als er geen foto komt? Ja (foto's volgen) / nee (offline halen)
5. Moeten alleen-afhalen producten van Bunzlau Castle en Blond Amsterdam uit Shopping en de gratis webvermeldingen, met behoud van de lokale vermelding? Ja/nee
6. Mogen we de eenheidsprijs per 100 gram eerst testen op twee losse theesoorten in Shopify? Ja/nee
7. Blijft de Belgische bron (BE) aan? Ja/nee
8. Mogen kassaproducten die in de winkel op voorraad zijn (zoals de 16 stuks nu) als lokale vermelding zichtbaar zijn zonder webpagina? Ja/nee
