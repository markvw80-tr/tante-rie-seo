#!/usr/bin/env python3
"""Doorverwijzing naar de mailbox in tante-rie-hq (zelfde opdrachten, zie daar)."""
import os
import sys

HQ = os.path.join(os.path.expanduser("~"), "tante-rie-hq", "scripts", "mailbox.py")
os.execv(sys.executable, [sys.executable, HQ, *sys.argv[1:]])
