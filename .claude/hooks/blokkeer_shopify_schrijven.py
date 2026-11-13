#!/usr/bin/env python3
"""PreToolUse-hook SEO: Shopify is alleen-lezen (werkafspraken-seo.md, 25-10-2026).

Blokkeert Shopify-schrijftools, GraphQL-mutaties en Shopify CLI-opdrachten die
iets wijzigen. Wijzigingen lopen via marketing/pim-regels-concept.json naar PIM
of via het Design-team voor themacode.
"""
import json
import re
import sys

SCHRIJFTOOLS = re.compile(
    r"(graphql_mutation|update-product|create-product|bulk-update-product-status|"
    r"set-inventory|update-collection|create-collection|add-to-collection|"
    r"create-discount|upload_file|digital-product)")
CLI = re.compile(r"shopify\s+(store\s+execute\b.*--allow-mutations|theme\s+(push|publish|delete)\b)")
MUTATIE = re.compile(r"^\s*mutation\b", re.M)


def weiger(reden):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": reden}}))
    sys.exit(0)


def strings(x):
    if isinstance(x, str):
        yield x
    elif isinstance(x, dict):
        for v in x.values():
            yield from strings(v)
    elif isinstance(x, list):
        for v in x:
            yield from strings(v)


data = json.load(sys.stdin)
naam = data.get("tool_name", "")
inv = data.get("tool_input", {})
uitleg = ("SEO werkt alleen-lezen in Shopify. Zet productwijzigingen als regel in "
          "marketing/pim-regels-concept.json (naar PIM) en themawijzigingen als opdracht naar Design.")

if naam.startswith("mcp__") and SCHRIJFTOOLS.search(naam):
    weiger(f"Geblokkeerd: {naam}. {uitleg}")
if naam.startswith("mcp__") and any(MUTATIE.search(s) for s in strings(inv)):
    weiger(f"Geblokkeerd: GraphQL-mutatie via {naam}. {uitleg}")
if naam == "Bash" and CLI.search(inv.get("command", "")):
    weiger(f"Geblokkeerd: Shopify CLI-schrijfopdracht. {uitleg}")
