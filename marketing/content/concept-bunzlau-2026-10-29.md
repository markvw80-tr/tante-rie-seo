# Concept Bunzlau-collectie: intro en FAQ (vroege start, onderdeel 1)

Opgesteld door de content-redacteur op 24 oktober 2026 (leverdatum in het plan: donderdag 29 oktober). Hoort bij plan-2026-10 actie 7 en marketing/plan-2026-11-vroege-start.md, onderdeel 1.

**Status: concept, klaar voor de Kwaliteitsredacteur (review gepland 30 oktober).** Er is niets gewijzigd in Shopify, het thema of op live pagina's, en er staat niets in changelog.md. Title, meta en H1 zijn van On-page (marketing/onpage/voorstel-bunzlau-title-links-2026-10-29.md); mijn voorstel daarvoor in hoofdstuk 6 is alleen ter afstemming.

URL: https://tanterie.nl/collections/bunzlau

## 1. Bronnen

| Bron | Wat ik eruit gebruik |
|---|---|
| CLAUDE.md, marketing/vragen-voor-mark.md | Stijl- en voorraadregels; V18 (Bunzlau alleen afhalen, decors op bestelling), V3 (melamine wel verzenden), V14/V35 (gesloten 25 en 26 december en 1 januari), V64 (verstuurd binnen 1 tot 2 werkdagen), V80 (koopavonden onbekend, dus niet genoemd), V89 (hanger-teapot niet online) |
| marketing/plan-2026-10.md, actie 7 | Opdracht, nulmeting, FAQ-onderwerpen |
| marketing/plan-2026-11-vroege-start.md | Opdracht en gedeelde regels |
| marketing/zoekwoorden/clusters-2026-10-24.md | Cluster Bunzlau (bunzlau castle 5.400, bunzlau servies 1.900, bunzlau 1.600, bunzlau castle servies 320) en Pools aardewerk (pools servies 720, pools aardewerk 320, pools servies blauw 140, pools servies sale 110) |
| marketing/zoekwoorden/volumes-clusters-2026-10-24.md, data/gsc/2026-10-21-nulmeting-vorigemaand-querypage.json | Zoekvragen: bunzlau servies kopen in polen (90 per maand), bunzlau winkels nederland, bunzlau (castle) aanbieding, sale, outlet, goedkoopste |
| marketing/technisch/voorstel-afhaalregels-blond-bunzlau-2026-10-22.md en changelog 22-10 | Afhaalzin op productpagina's, bestelverzoek bij geen voorraad, melamine op eigen verzendbaar sjabloon |
| marketing/content/concept-theewinkel-borne-2026-10-22.md (live sinds 23-10) | Toon en goedgekeurde winkelfeiten: adres, tijden, telefoon, e-mail, "neem gerust een kopje of schoteltje mee", decors op bestelling, parkeren |
| assets/afbeeldingen/winkel-2026-10/bunzlau-wand.jpg en bunzlau-kast.jpg | Bekeken voor de alt-teksten |

**Bron van de huidige collectietekst.** De Shopify-koppeling was in deze sessie niet beschikbaar, dus ik heb de live waarden niet rechtstreeks gelezen. Ik gebruikte twee bronnen uit de repository:

1. De themasectie: scripts/archief-themas/winkelfotos-backup-2026-10-23-live-203153015048/sections/tr-collection-bunzlau.liquid (backup van live van 23-10). Volgens changelog 23-10 is daarna alleen een winkelfoto toegevoegd, "tekst ongewijzigd" (diff in marketing/technisch/voorstel-winkelfotos-2026-10-23.diff).
2. De collectiebeschrijving (body uit Shopify) zoals live getoond op 21-10: data/preview-2026-10-21/p_collections_bunzlau.html.

On-page moet de huidige body uit Shopify als backup kopiëren voordat er iets wordt doorgevoerd; zie ook de bevinding hieronder over de eerste alinea.

## 2. Bevindingen over de huidige pagina die On-page en Technisch SEO moeten weten

1. **De eerste alinea van de collectiebeschrijving is onzichtbaar.** De sectie splitst de beschrijving in `_desc_first` (bedoeld voor de header) en `_desc_rest` (SEO-blok onderaan), maar `_desc_first` wordt nergens weergegeven (regels 161 tot 169 van de sectie; geen enkele output van die variabele). Wat er nu als eerste `<p>` in de beschrijving staat, ziet niemand, ook Google niet. Ik weet daardoor niet wat die eerste alinea is. Gevolg voor dit concept: plakt On-page de nieuwe intro gewoon in de beschrijving, dan verdwijnt de eerste alinea van de intro. Er moet dus gekozen worden: ofwel Technisch SEO laat `_desc_first` boven de producten zien (zoals het commentaar in de sectie bedoelt), ofwel de beschrijving begint met een lege of korte eerste `<p>`. Mijn advies is het eerste, want de intro hoort bovenaan te staan en niet onder de producten.
2. **Het SEO-blok in het thema spreekt de regels tegen.** Onder de beschrijving staat hardgecodeerde tekst (regels 514 tot 527) met een H2 "Bunzlau Castle kopen in Twente" en vier H3's. Daarin staan een lijst met negentien decors "op voorraad" (voorraadbelofte, in strijd met CLAUDE.md), "officieel reseller" (geen bron in de repository), "ovenbestendig tot 220°C" en een link naar /collections/losse-thee in plaats van /collections/thee. Die blokken overlappen ook met de nieuwe FAQ. Advies: On-page neemt het weghalen of vervangen van dit blok mee in het voor-en-navoorstel, met akkoord van Mark. De nieuwe FAQ hieronder vervangt de inhoud.
3. **Het merkblok "Over het merk"** (regels 432 tot 440) noemt "meer dan 200 jaar ambacht", "loodvrij" en "op een halfuur van Enschede, Hengelo en Almelo". Geen van die drie heeft een bron in de repository. Ik heb ze niet overgenomen. Ze staan in de themacode, dus wijzigen hoort bij On-page en Technisch SEO; niet in deze opdracht, wel het melden waard.
4. De productkaarten van 21-10 tonen mokken, borden, kommen, rijstkommen, schalen, ovenschalen, theetips, een melkkan en een suikerpot, maar geen Bunzlau-theepot (de theepot hanger-teapot staat niet online, V89). De nieuwe tekst noemt daarom geen theepotten. On-page controleert via Shopify of de genoemde soorten nog online staan.

## 3. Voor: huidige tekst

### Collectiebeschrijving (Shopify-body, zichtbaar deel, 21-10)

> [Eerste alinea: onzichtbaar op de pagina, niet bekend; On-page leest die uit Shopify]
>
> De collectie telt meer dan 40 vormen, verkrijgbaar in uiteenlopende dessins. Van het klassieke blauw-witte patroon tot warmere aardetinten, elk stuk heeft het karakteristieke reliëfpatroon waarvoor Bunzlau Castle bekend staat. Vaatwasser- en magnetronbestendig, stevig genoeg voor dagelijks gebruik én uitgesproken genoeg voor een gedekte tafel.
>
> Naast het keramiek voeren wij ook Bunzlau Castle producten in melamine. Melamine artikelen kun je online bestellen en laten bezorgen in Nederland.
>
> Het keramisch servies is uitsluitend af te halen in onze winkel in Borne, Twente. Zo kun je de stukken in het echt bekijken, het gewicht voelen en de kleuren van nabij beoordelen voordat je een keuze maakt. Wij helpen je graag bij het samenstellen van een set of het vinden van het perfecte cadeau. Je vindt ons op Bakkerssteeg 6 in Borne.

### Hardgecodeerd SEO-blok in het thema (direct onder de beschrijving)

> **H2 Bunzlau Castle kopen in Twente.** Tante Rie in Borne is officieel reseller van Bunzlau Castle. Je kunt langskomen om de stukken te zien, of online bestellen en ophalen. Stukken die er niet staan, bestellen we voor je. Levertijd hangt af van de collectiecyclus van Bunzlau Castle. Vraag ernaar via het contactformulier of bel ons.
>
> **H3 Welke decors zijn er op voorraad?** Bij Tante Rie hebben we momenteel stukken op voorraad in de decors Lace, Belle Fleur, Flower Fountain, Harmony, Spring Ballet, Flower Crown, Spring Hill, Felicity, Blue Valentine, Dragonfly, Daydream, Indigo, Winter Garden, Ocean Breeze, Romance, Granada, Blossom Breeze, Porto, Blue Garden en enkele andere. (...) De volledige Bunzlau Castle collectie is op bestelling verkrijgbaar.
>
> **H3 Gebruik en onderhoud.** Bunzlau Castle aardewerk is vaatwasserbestendig, magnetronveilig en ovenbestendig tot 220°C. Gebruik geen metalen schuursponsjes op het glazuur. De stukken zijn zwaar en solide. Bij normaal gebruik gaan ze tientallen jaren mee.
>
> **H3 Theepotten van Bunzlau Castle.** De theepotten van Bunzlau Castle zijn gemaakt voor dagelijks gebruik. (...) combineren we ze graag met losse thee (/collections/losse-thee) en theefilters.
>
> **H3 Ophalen in Borne.** Bunzlau Castle is zwaar en breekbaar. Ophalen in de winkel heeft de voorkeur. Je vindt ons aan de Bakkerssteeg 6 in Borne, dinsdag tot en met zaterdag open van 10:00 tot 17:00. Gratis parkeren in de buurt van de winkel.

### Wat er mis is

Geen van de hoofdzoekwoorden 'Bunzlau servies' of 'Pools aardewerk' staat in de zichtbare tekst, de intro is onzichtbaar, er is geen link naar de theewinkelpagina, "uitsluitend" en "heeft de voorkeur" spreken elkaar tegen, er staat een voorraadlijst en de vragen uit de zoekdata (kopen in Polen, winkels in Nederland, aanbieding) worden niet beantwoord.

## 4. Na: nieuwe klanttekst

De H1 blijft de collectietitel (controle door On-page). Alles hieronder is bedoeld als collectiebeschrijving; zie bevinding 1 voor de plaatsing.

### Intro

Bunzlau Castle is aardewerk dat in Polen met de hand wordt beschilderd, en bij Tante Rie kun je dit Bunzlau servies in het echt bekijken. In onze [theewinkel aan de Bakkerssteeg in Borne](/pages/theewinkel-borne-twente) staan mokken, borden, kommen en schalen in veel decors naast elkaar, zodat je kleur en vorm kunt vergelijken met wat je thuis al hebt. Wil je een bestaande set aanvullen, neem dan gerust een kopje of schoteltje mee.

Het aardewerk van Bunzlau Castle is alleen af te halen in de winkel in Borne. Je koopt het ter plekke, of je bestelt online en haalt je bestelling daarna op. Staat een stuk niet op voorraad, dan stuur je via de productpagina een bestelverzoek en spreken we samen een ophaaldatum af, en zoek je een decor dat niet in de winkel staat, dan kunnen we het voor je bestellen. Het melamine van Bunzlau Castle sturen we wel op, verstuurd binnen 1 tot 2 werkdagen. Wil je Bunzlau voor de feestdagen afhalen, houd er dan rekening mee dat de winkel op 25 en 26 december en op 1 januari gesloten is; verder ben je van dinsdag tot en met zaterdag welkom van 10.00 tot 17.00 uur.

### H2: Pools aardewerk en Pools servies uit Bolesławiec

Bunzlau is de Duitse naam van Bolesławiec, de stad in Polen waar dit aardewerk vandaan komt, en daarom wordt Pools aardewerk ook wel gewoon Bunzlau genoemd. De patronen worden met stempels en sponsjes met de hand aangebracht, waardoor geen twee stukken precies gelijk zijn. Naast het klassieke blauw-witte Pools servies maakt Bunzlau Castle decors met bloemen en warmere tinten. Het aardewerk is stevig genoeg om elke dag te gebruiken, voor je ontbijt, een kom soep of een pot thee met [losse thee](/collections/thee) en een [theefilter](/collections/theefilters-en-maatschepjes). Zoek je ander servies, zoals Blond Amsterdam of Rice, kijk dan op onze pagina over [serviezen](/pages/serviezen).

### H2: Vragen over Bunzlau servies kopen

**Waar kan ik Bunzlau Castle kopen?**
Bij Tante Rie aan de Bakkerssteeg 6 in Borne. In de winkel neem je de stukken in handen en zie je de decors naast elkaar. Je kunt ook hier online bestellen en je bestelling in de winkel afhalen. Kom je voor een bepaald stuk, bel dan even naar 06 38 29 11 89 of mail naar webshop@tanterie.nl, dan weet je zeker dat het er voor je ligt.

**Welke winkel in Nederland verkoopt Bunzlau servies?**
Wij kunnen alleen voor onze eigen winkel spreken. In Twente vind je Bunzlau Castle bij Tante Rie in het centrum van Borne, tussen Hengelo en Almelo. Kom je van verder, bekijk de collectie dan eerst hier online en kom daarna langs om te kiezen of af te halen. Parkeren kan gratis in de buurt, met een parkeerschijf of in de parkeergarage.

**Moet ik naar Polen om Bunzlau te kopen?**
Nee. Het aardewerk wordt gemaakt en beschilderd in Bolesławiec in Polen, maar je kunt Bunzlau Castle ook in Nederland kopen. In onze winkel in Borne bekijk je het servies zonder de reis, en een decor dat er niet staat bestellen we voor je.

**Is Bunzlau servies weleens in de aanbieding?**
Twee keer per jaar houden we een kortingsweekend met 20 procent korting op het servies van Bunzlau Castle, Blond Amsterdam en Rice. Wil je weten wanneer het volgende kortingsweekend is, vraag het dan in de winkel of mail naar webshop@tanterie.nl.

**Kan Bunzlau in de vaatwasser?**
Ja, het aardewerk van Bunzlau Castle kan in de vaatwasser en in de magnetron. Gebruik geen metalen schuursponsje op het glazuur, dan blijft het decor mooi.

### Bewust weggelaten

| Onderdeel | Waarom |
|---|---|
| Data van de kortingsweekenden, tweede keus, outlet, "goedkoopste" | V97 noemt geen data en niets over tweede keus of outlet. De FAQ over aanbieding (toegevoegd op 24-10 na V97) noemt alleen de twee kortingsweekenden per jaar met 20 procent op Bunzlau, Blond en Rice, zonder datums en zonder korting buiten die weekenden te beloven. Of de korting alleen in de winkel of ook online geldt, staat er niet in, omdat V97 dat niet zegt |
| Oven, 220°C, loodvrij, "tientallen jaren" | Staat in het thema, maar zonder bevestiging van Mark en met een concreet getal; niet nodig voor de zoekvraag vaatwasser |
| "Officieel reseller", "meer dan 200 jaar", "meer dan 40 vormen", "pauwenoog" | Geen bron in de repository buiten de bestaande themateksten; niet nodig voor de zoekintentie |
| Theepotten | Geen Bunzlau-theepot zichtbaar online (V89) |
| Levertijd van een bestelling bij Bunzlau Castle | Onbekend ("hangt af van de collectiecyclus"); geen termijn beloven |
| Koopavonden | V80 open |

**Vaatwasser: bevestigd door Mark (V98, 24-10).** Bunzlau Castle-aardewerk mag in de vaatwasser en de magnetron. Aandachtspunt voor On-page: het productsjabloon toont "Handwas aanbevolen" als een product geen tag vaatwasser heeft, dus de tag op alle Bunzlau-aardewerkproducten moet worden gecontroleerd (zoals vastgelegd bij V98).

**Feit uit algemene kennis.** "Bunzlau is de Duitse naam van Bolesławiec" komt niet uit de repository maar is een vaststaand historisch gegeven; dat het aardewerk uit Bolesławiec komt staat al op de live pagina. Ter beoordeling door de Kwaliteitsredacteur.

## 5. Interne links

| Ankertekst | Doel | Opmerking |
|---|---|---|
| theewinkel aan de Bakkerssteeg in Borne | /pages/theewinkel-borne-twente | Verplicht volgens de opdracht; live sinds 23-10 |
| losse thee | /collections/thee | Vervangt de link naar /collections/losse-thee in het themablok |
| theefilter | /collections/theefilters-en-maatschepjes | Bestaat (10 producten op 22-10) |
| serviezen | /pages/serviezen | Servies-hub (actie 8) |

Geen productlinks: de Shopify-koppeling was niet beschikbaar om publicatie en voorraad te controleren. On-page kan bij doorvoeren een link naar een melamineproduct toevoegen als dat online staat en voorraad heeft. Inkomende links (blog, /pages/serviezen) zijn van On-page.

## 6. Title en meta (voorstel ter afstemming met On-page)

| | Tekst | Tekens |
|---|---|---:|
| Huidige title (21-10) | Bunzlau Castle Kopen \| Theepotten & Mokken \| Tante Rie Borne | 60 |
| Title, voorstel | Bunzlau Castle servies kopen in Borne \| Tante Rie | 49 |
| Huidige meta (21-10) | Bunzlau Castle theepotten, mokken & servies bij Tante Rie in Borne, Twente. Handgemaakt Pools aardewerk in 40+ vormen. Bestel online, afhalen in de winkel. | 155 |
| Meta, voorstel | Bunzlau Castle servies, handgeschilderd Pools aardewerk. Bekijk mokken, borden en kommen in onze winkel in Borne en haal je bestelling daar af. | 143 |

## 7. Afbeeldingen en alt-teksten

| Afbeelding | Huidige alt | Voorstel |
|---|---|---|
| Winkelfoto boven de afhaalkaarten (bunzlau-wand.jpg) | Wand met blauw Bunzlau Castle aardewerk in de winkel van Tante Rie | Houten wandkast vol blauw-wit Bunzlau Castle aardewerk in de theewinkel van Tante Rie in Borne |
| Merkfoto in "Over het merk" (ontbijtfoto, Jochem Boxem) | Bunzlau Castle aardewerk bij Tante Rie Borne Twente | Niet zelf bekeken (staat alleen in Shopify); On-page beschrijft wat er echt op staat, bijvoorbeeld "Ontbijttafel gedekt met Bunzlau Castle servies", alleen als dat klopt |
| Eventueel extra: bunzlau-kast.jpg | Nog niet op deze pagina | Witte buffetkast met Bunzlau Castle mokken, borden en kopjes in de winkel van Tante Rie in Borne |

## 8. Vragen voor Mark

De twee vragen uit de eerste versie zijn op 24-10 beantwoord en verwerkt:

| Vraag | Antwoord Mark | Verwerkt |
|---|---|---|
| V97 Bunzlau in de aanbieding | Twee keer per jaar een kortingsweekend met 20 procent korting op servies van Bunzlau, Blond en Rice; data niet genoemd | Nieuwe FAQ "Is Bunzlau servies weleens in de aanbieding?", zonder datums en zonder korting buiten de weekenden |
| V98 Bunzlau in vaatwasser en magnetron | Ja | Markering bij het vaatwasserantwoord weggehaald; antwoordtekst ongewijzigd |

Mogelijke vervolgvraag (⚪, alleen als de Kwaliteitsredacteur of On-page het nodig vindt): geldt de korting van het kortingsweekend alleen in de winkel of ook in de webshop? De FAQ zegt daar nu niets over.

## 9. Meting

Volgens het plan: 28 dagen na publicatie CTR minstens 1,8 procent en positie 18 of beter (nul: 1.329 vertoningen, 17 klikken, CTR 1,28 procent, positie 21,2); na zes weken 'bunzlau servies' op 25 of beter en 'bunzlau castle' op 15 of beter. Nulwaarden op de livedag legt de Analist vast.
