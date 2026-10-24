# Mailbox SEO-team en PIM-team

Deze map is het communicatiekanaal tussen het SEO-team (deze repository) en het PIM-team (productinformatie en leveranciers). Elk team heeft een eigen inbox. Berichten zijn gewone Markdown-bestanden, dus Mark kan alles meelezen op GitHub.

| Map | Inhoud |
|---|---|
| `seo/inbox/` | Nieuwe berichten voor het SEO-team |
| `seo/verwerkt/` | Berichten die het SEO-team heeft afgehandeld |
| `pim/inbox/` | Nieuwe berichten voor het PIM-team |
| `pim/verwerkt/` | Berichten die het PIM-team heeft afgehandeld |

## Werkwijze

1. Begin elke opdracht met het lezen van de eigen inbox: `python3 scripts/mailbox.py lijst seo` (of `pim`). Het script haalt eerst de laatste stand op.
2. Een bericht sturen: `python3 scripts/mailbox.py stuur --van seo --aan pim --onderwerp "..." --tekst "..."`. Voor lange tekst gebruik je `--tekst -` en geef je de tekst via stdin. Het script zet het bericht direct op `main` en pusht het.
3. Antwoorden: stuur een nieuw bericht met `--antwoord-op <bestandsnaam>` zodat de draad te volgen is.
4. Afhandelen: `python3 scripts/mailbox.py verwerkt <bestandsnaam> --notitie "wat er mee gedaan is"`. Het bericht verhuist naar `verwerkt/`.

## Afspraken

Eén onderwerp per bericht. Schrijf wat je nodig hebt, waarom, en vóór wanneer. Gebruik `--prioriteit hoog` alleen als het andere team erop wacht. Een bericht is geen akkoord van Mark: zaken die Marks goedkeuring nodig hebben gaan nog steeds via `marketing/vragen-voor-mark.md`. Zet geen wachtwoorden, tokens of klantgegevens in een bericht.

Mailboxcommits gaan rechtstreeks naar `main` en raken alleen bestanden in `mailbox/`. Ander werk blijft via de gewone branches lopen.
