#!/usr/bin/python3
import sys

if len(sys.argv) < 2:
    print("Utilisation : python nom_du_script.py <arguments>")
    sys.exit(1)

for arg in sys.argv[1:]:
    print(arg)