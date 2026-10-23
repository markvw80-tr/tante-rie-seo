# Review Blond Amsterdam-gidspagina (actie 6), 23 oktober 2026

Stuk: marketing/content/concept-blond-2026-10-22.md
URL: https://tanterie.nl/pages/blond-amsterdam-servies
Beoordeeld door: Kwaliteitsredacteur (skill marketing:brand-review)

## Oordeel

**Goedgekeurd met kleine aanpassingen.** De tekst zelf is klaar. Publicatie mag pas als aan één voorwaarde is voldaan: de specificatietabel en de onderhoudskaart op de Blond-productpagina's zeggen nog "Handwas aanbevolen" en "Handwas". Gaat de gidspagina nu live, dan spreekt ze elke Blond-productpagina tegen, en op de zeven aangepaste pagina's spreekt de productpagina zichzelf al tegen. Dat is geen fout in het concept en hoeft dus niet terug naar de maker, maar het blokkeert vraag 6: nee, de gidspagina kan vandaag nog niet live.

## 1. Stijlregels

Gecontroleerd: antwoordblok, intro, H2 met vier H3's, de aanvulling bij "Zo dek je er je tafel mee", alt-teksten, title en meta.

Geen em-dashes, geen uitroeptekens, geen opsommingen in de klanttekst, geen AI-vulwoorden of clichés van betekenis. Het proza loopt goed en is natuurlijk Nederlands. Drie kleine punten heb ik zelf in het concept aangepast (zie "Aanpassingen").

Laag, niet aangepast: het antwoordblok en de H3's zeggen grotendeels hetzelfde. Dat is bewust (kort antwoord bovenaan voor de snippet, uitleg eronder) en mag zo blijven.

## 2. Merkstem

Warm, deskundig en persoonlijk, met "onze winkel", de tip voor een mild programma en het advies de mok voorzichtig vast te pakken. "Kleurrijk" staat erin volgens het besluit van Mark. De bezorgvraag is eerlijk zonder negatief te klinken. Akkoord.

## 3. Feiten tegen de live pagina's (23-10)

| Punt | Concept | Live | Oordeel |
|---|---|---|---|
| Vaatwasser | Mokken, bekers en borden kunnen in de vaatwasser, mild programma | Beschrijving van de 7 aangepaste producten: "Geschikt voor de vaatwasser. Kies een mild programma ..." Maar de specificatietabel op alle Blond-producten toont "Vaatwasserbestendig ✗ Handwas aanbevolen" en de kaart "Onderhoud: Handwas" (gezien op /products/cup-of-sunshine en /products/mazagran-liefste-juf) | **Tegenstrijdig, blokkeert publicatie** |
| Magnetron | Alle mokken en bekers wel, theepot en thermosfles niet | Productteksten: "Je kunt het servies in de magnetron gebruiken, maar het kan snel warm worden." | Klopt. De borden (bijvoorbeeld ED Bord Tompouce) zeggen ook magnetron; het concept noemt borden bij de magnetron niet. Dat is weglaten, geen tegenspraak |
| Oven | Geen enkel stuk | "Niet geschikt voor in de oven." / "Niet ovenbestendig." | Klopt |
| Afhalen | Niet versturen, online bestellen en afhalen, bericht telefonisch of per mail | Balk "Alleen afhalen in Borne", productzin "Dit product versturen we niet. Je bestelt online en haalt het op in onze winkel in Borne.", Bakkerssteeg 6, di t/m za 10:00 tot 17:00 | Klopt. Telefoonnummer staat ook in het Bedrijfsprofiel |
| Te bestellen | Kan toch besteld worden, levertijd per merk | Productzin "Je stuurt een bestelverzoek ..." | Klopt |
| Wat er online staat | Mokken, mazagran-bekers, borden, theepot 1,5 liter, thermosfles | 40 producten, waarvan 3 borden (18 en 22 cm), Teapot 1,5L Blah, EB Thermo Bottle 0,5L Hearts; 5 op "Te bestellen" (Pink Mug Hearts, Forever Young, Graduated, Dad, Light House) | Klopt; geen kommen of theedoeken meer genoemd |
| Atelier en personalisatie | Zinnen vervallen | Productpagina's schoon; de gidspagina zelf zegt het nog (wordt met dit concept vervangen) | Klopt |
| Materiaal | Nieuwe H3: "Het servies is van keramiek" | Bestaande zin die blijft: "Alles is gemaakt van keramiek", in dezelfde sectie als de thermosfles | Aangepast naar "Het servies", materiaal thermosfles nog nagaan (zie Aanpassingen) |
| Gezondheidsclaims | Geen | n.v.t. | Akkoord |

Oorzaak van de tegenstrijdigheid: in sections/tr-product-blond.liquid (regels 208 tot 216, 347 tot 348 en 591) zet het thema "Vaatwasser ok" en "✓ Ja" alleen als het product een tag met "vaatwasser" heeft. De wijziging van 22-10 (changelog) paste alleen de beschrijving van 7 producten aan, niet de tags. Geen enkel Blond-product heeft die tag, dus alle 40 tonen "Handwas aanbevolen".

## 4. SEO-basis

| Onderdeel | Waarde | Oordeel |
|---|---|---|
| Title | Blond Amsterdam servies: vaatwasser en magnetron \| Tante Rie | 60 tekens, nageteld, op de grens. Title A volgens V11. Akkoord |
| Meta | Kan Blond Amsterdam servies in de vaatwasser of magnetron? Het korte antwoord, onderhoudstips en hoe je het kleurrijke servies afhaalt in Borne. | 144 tekens, nageteld. Akkoord |
| H1 | Blond Amsterdam servies (ongewijzigd) | Eén H1. Akkoord |
| Hoofdzoekwoord | kan Blond Amsterdam in de vaatwasser | In title (vaatwasser), eerste zin, H2 en H3. Natuurlijk geplaatst. Akkoord |
| Kannibalisatie /collections/blond | Collectie: "Blond Amsterdam Kopen \| Mokken & Woonaccessoires \| Tante Rie", H1 "Blond Amsterdam"; geen vaatwasser of magnetron | Intenties gescheiden (gebruik tegenover kopen). Geen kannibalisatie. Akkoord |
| Dubbele content | Antwoordblok en H3's overlappen binnen de pagina, niet met andere pagina's | Akkoord |

## 5. Interne links

Gecontroleerd op 23-10 via WebFetch (de site gaf regelmatig 429 bij snel achter elkaar ophalen; geen 404 gezien).

| Link | Doel | Controle |
|---|---|---|
| theewinkel in Borne | /pages/theewinkel-borne-twente | Laadt op 22-10 (concept) en staat in de live navigatie van de gidspagina |
| theepot van 1,5 liter | /products/teapot-1-5l-blah | In de live collectie, op voorraad |
| losse thee | /collections/thee | Laadt op 22-10 en staat in de live navigatie |
| theebereiding | /pages/theebereiding-faq | Laadt 23-10, H1 "Theebereiding" |
| serviezen | /pages/serviezen | Laadt 23-10. Let op: de Blond-zin zegt nog "altijd op voorraad" (actie 8) |
| Bestaande collectielink | /collections/blond | Laadt 23-10, 40 producten |
| Zes productlinks | mazagran-liefste-juf, mazagran-graduated-0-5l, forever-young, thank-you, dier-mug-cat-lover, eb-pink-mug-0-35l-hearts | Alle zes staan met deze handle in de live collectie; Liefste Juf apart geopend |

Alle links werken.

## 6. Kan de gidspagina nu live?

Nee, nog niet. Voorwaarde: op de Blond-productpagina's moeten de specificatietabel en de onderhoudskaart "Ja" en "Vaatwasser ok" tonen, behalve bij Teapot 1,5L Blah en EB Thermo Bottle 0,5L Hearts (daarvoor is de vaatwasser niet beantwoord, en de gidspagina noemt ze daar niet). De eenvoudigste route is een tag met "vaatwasser" op de 38 overige Blond-producten, zonder themawijziging. Dat is een wijziging aan live producten en vraagt een voorstel met voor en na en akkoord van Mark; ik heb daar niets aan gedaan. Na die wijziging kan de gidspagina live, bij voorkeur samen met actie 8, zodat /pages/serviezen niet langer "altijd op voorraad" zegt.

Ook nagaan voor publicatie: hoort Cozy Days Light House Stepped Gable Cozy bij "mokken, bekers en borden"? Zo niet, dan krijgt dat product de tag niet.

## Aanpassingen die ik zelf in het concept heb gedaan

1. Bezorgvraag, afhaalbericht. Was: "Ligt je bestelling klaar, dan laten we je dat telefonisch weten, of per mail als je dat liever hebt." Nu: "Ligt je bestelling klaar, dan krijg je van ons bericht, telefonisch of per mail." Reden: Mark zei "telefonisch of per mail"; de klant kiest dat niet, dus geen belofte die we niet doen.
2. Bezorgvraag, levertijd. Was: "dus vraag er gerust naar in de winkel." Nu: "dus vraag ernaar in de winkel." Reden: "gerust" staat al in de bestaande zin "Kom gerust langs".
3. Bezorgvraag, bellen. Was: "bel dan even op 06 38 29 11 89 of het stuk dat je zoekt in de winkel staat." Nu: "bel dan even naar 06 38 29 11 89 om te vragen of het stuk dat je zoekt in de winkel staat." Reden: correcter Nederlands.
4. Bestaande sectie "Materiaal en afwerking": "Alles is gemaakt van keramiek" wordt "Het servies is gemaakt van keramiek", tenzij On-page bevestigt dat de thermosfles ook van keramiek is (ik kon die productpagina niet ophalen door de 429).
5. Statusregel bovenaan het concept bijgewerkt.

Verouderd in het concept, geen actie nodig: de alinea "Vaatwasser: gidspagina en productpagina's" en de open punten over de afhaalbalk, de productzin en de atelierzinnen zijn sinds 22-10 live gedaan (changelog). De beschrijvingen zijn aangepast; alleen de specificatietabel nog niet.

Niets gepubliceerd. changelog.md en vragen-voor-mark.md niet aangeraakt.
