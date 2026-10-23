"""Prioriteitsscore voor zoekwoordkansen (zie rapport, sectie Prioriteitsscore)."""


def pos_factor(pos):
    if pos < 4:
        return 0.2
    if pos <= 10:
        return 1.0
    if pos <= 20:
        return 0.8
    if pos <= 30:
        return 0.4
    return 0.15


def ctr_factor(ctr_pct):
    if ctr_pct < 0.5:
        return 1.0
    if ctr_pct < 2:
        return 0.6
    if ctr_pct < 5:
        return 0.3
    return 0.1


def score(impr, pos, ctr_pct):
    return impr * pos_factor(pos) * ctr_factor(ctr_pct)
