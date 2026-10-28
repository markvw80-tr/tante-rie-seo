#!/usr/bin/env python3
"""Mailbox tussen het SEO-, PIM- en Design-team (Tante Rie).

Berichten zijn Markdown-bestanden in mailbox/<team>/inbox/. Na verwerking gaan
ze naar mailbox/<team>/verwerkt/. Git is het transport: het script werkt in een
aparte werkkopie van origin/main (.git/mailbox-main), zodat de branch waarop je
werkt niet verandert, en zet verzonden of verwerkte berichten direct op main.

Gebruik:
  python3 scripts/mailbox.py lijst seo                 # ongelezen berichten voor het SEO-team (ook pim, design)
  python3 scripts/mailbox.py lees <bestand>            # één bericht tonen
  python3 scripts/mailbox.py stuur --van seo --aan pim --onderwerp "..." --tekst "..."
        [--antwoord-op <bestand>] [--prioriteit hoog|normaal|laag]
  python3 scripts/mailbox.py verwerkt <bestand> [--notitie "..."]
  python3 scripts/mailbox.py --geen-git ...            # zonder pull/commit/push (testen)
"""
import argparse
import datetime
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEAMS = ("seo", "pim", "design")
BRANCH = "main"
ROOT = REPO  # wordt de werkkopie van main zodra git gebruikt wordt
MAILBOX = os.path.join(ROOT, "mailbox")


def git(*args, check=True, cwd=None):
    p = subprocess.run(["git", "-C", cwd or ROOT, *args], capture_output=True, text=True)
    if check and p.returncode != 0:
        raise RuntimeError("git " + " ".join(args) + ": " + p.stderr.strip())
    return p


def ophalen():
    """Zet de werkkopie .git/mailbox-main op de laatste stand van origin/main."""
    global ROOT, MAILBOX
    gitdir = git("rev-parse", "--git-common-dir", cwd=REPO).stdout.strip()
    wt = os.path.join(os.path.abspath(os.path.join(REPO, gitdir)), "mailbox-main")
    git("fetch", "origin", BRANCH, cwd=REPO)
    if not os.path.isdir(os.path.join(wt, "mailbox")):
        git("worktree", "prune", cwd=REPO)
        git("worktree", "add", "--detach", wt, "origin/" + BRANCH, cwd=REPO)
    else:
        git("reset", "--hard", "origin/" + BRANCH, cwd=wt)
    ROOT, MAILBOX = wt, os.path.join(wt, "mailbox")


def vastleggen(paden, bericht):
    git("add", "-A", "--", *paden)
    git("commit", "-m", bericht, "--", *paden)
    for poging in range(3):
        if git("push", "origin", "HEAD:" + BRANCH, check=False).returncode == 0:
            return
        git("fetch", "origin", BRANCH)
        git("rebase", "origin/" + BRANCH, check=False)
    raise RuntimeError("push naar " + BRANCH + " mislukt; probeer later opnieuw")


def slug(tekst):
    s = re.sub(r"[^a-z0-9]+", "-", tekst.lower()).strip("-")
    return s[:50] or "bericht"


def kop(pad):
    """Lees de kop (key: value tussen ---) van een bericht."""
    velden = {}
    with open(pad, encoding="utf-8") as f:
        regels = f.read().split("\n")
    if regels and regels[0] == "---":
        for r in regels[1:]:
            if r == "---":
                break
            k, _, v = r.partition(":")
            velden[k.strip()] = v.strip()
    return velden


def zoek(bestand):
    """Vind een bericht op naam in alle inboxen en verwerkt-mappen."""
    naam = os.path.basename(bestand)
    for team in TEAMS:
        for map_ in ("inbox", "verwerkt"):
            pad = os.path.join(MAILBOX, team, map_, naam)
            if os.path.isfile(pad):
                return pad
    sys.exit("Bericht niet gevonden: " + bestand)


def cmd_lijst(a):
    inbox = os.path.join(MAILBOX, a.team, "inbox")
    namen = sorted(n for n in os.listdir(inbox) if n.endswith(".md"))
    if not namen:
        print("Geen nieuwe berichten voor " + a.team + ".")
        return
    for n in namen:
        k = kop(os.path.join(inbox, n))
        print("%s  [%s] van %s: %s" % (n, k.get("prioriteit", "normaal"),
                                      k.get("van", "?"), k.get("onderwerp", "")))


def cmd_lees(a):
    with open(zoek(a.bestand), encoding="utf-8") as f:
        print(f.read())


def cmd_stuur(a):
    if a.van == a.aan:
        sys.exit("Afzender en ontvanger zijn hetzelfde team.")
    tekst = a.tekst
    if tekst == "-":
        tekst = sys.stdin.read()
    nu = datetime.datetime.now()
    naam = "%s-%s-%s.md" % (nu.strftime("%Y-%m-%d-%H%M%S"), a.van, slug(a.onderwerp))
    pad = os.path.join(MAILBOX, a.aan, "inbox", naam)
    kopregels = ["---",
                 "van: " + a.van,
                 "aan: " + a.aan,
                 "datum: " + nu.strftime("%Y-%m-%d %H:%M"),
                 "onderwerp: " + a.onderwerp,
                 "prioriteit: " + a.prioriteit]
    if a.antwoord_op:
        kopregels.append("antwoord-op: " + os.path.basename(a.antwoord_op))
    kopregels.append("---")
    with open(pad, "w", encoding="utf-8") as f:
        f.write("\n".join(kopregels) + "\n\n" + tekst.strip() + "\n")
    if not a.geen_git:
        vastleggen([pad], "mailbox: %s -> %s: %s" % (a.van, a.aan, a.onderwerp))
    print("Verstuurd: " + os.path.relpath(pad, ROOT))


def cmd_verwerkt(a):
    bron = zoek(a.bestand)
    if os.path.basename(os.path.dirname(bron)) != "inbox":
        sys.exit("Dit bericht is al verwerkt.")
    doel = os.path.join(os.path.dirname(os.path.dirname(bron)), "verwerkt", os.path.basename(bron))
    with open(bron, encoding="utf-8") as f:
        inhoud = f.read()
    datum = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    inhoud = inhoud.rstrip("\n") + "\n\n---\nVerwerkt op " + datum
    inhoud += (": " + a.notitie + "\n") if a.notitie else "\n"
    with open(doel, "w", encoding="utf-8") as f:
        f.write(inhoud)
    os.remove(bron)
    if not a.geen_git:
        vastleggen([bron, doel], "mailbox: verwerkt " + os.path.basename(bron))
    print("Verplaatst naar " + os.path.relpath(doel, ROOT))


def main():
    p = argparse.ArgumentParser(description="Mailbox tussen SEO-, PIM- en Design-team")
    p.add_argument("--geen-git", action="store_true", help="geen pull, commit of push")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("lijst")
    s.add_argument("team", choices=TEAMS)
    s.set_defaults(fn=cmd_lijst)

    s = sub.add_parser("lees")
    s.add_argument("bestand")
    s.set_defaults(fn=cmd_lees)

    s = sub.add_parser("stuur")
    s.add_argument("--van", required=True, choices=TEAMS)
    s.add_argument("--aan", required=True, choices=TEAMS)
    s.add_argument("--onderwerp", required=True)
    s.add_argument("--tekst", required=True, help="berichttekst, of - om van stdin te lezen")
    s.add_argument("--antwoord-op")
    s.add_argument("--prioriteit", default="normaal", choices=("hoog", "normaal", "laag"))
    s.set_defaults(fn=cmd_stuur)

    s = sub.add_parser("verwerkt")
    s.add_argument("bestand")
    s.add_argument("--notitie")
    s.set_defaults(fn=cmd_verwerkt)

    a = p.parse_args()
    if not a.geen_git:
        ophalen()
    a.fn(a)


if __name__ == "__main__":
    main()
