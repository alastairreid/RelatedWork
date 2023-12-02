#! /usr/bin/env python3

import json
import yaml
from yaml import dump
# from yaml import CDumper as Dumper
from yaml import Dumper

from datetime import date

import re
import string
import sys

def main():
    name = sys.argv[1]
    title = " ".join(sys.argv[2:])
    entry = {
        "title": title,
        "layout": "note",
        # "isa": {},
        # "examples": {},
        "notes": {},
        "papers": {}
        }
    file = f"_notes/{name}.md"
    with open(file, 'w') as f:
        yaml.dump(entry, Dumper=Dumper, explicit_start=True, allow_unicode=True, width=150, stream=f)
        print("---", file=f)
        print("{% include links.html %}", file=f)
    print(f"Created note {file} with title '{title}'")

main()
