#! /usr/bin/env python3

import json
import yaml
from yaml import dump
from yaml import CDumper as Dumper

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
        "isa": {},
        "examples": {},
        "notes": {},
        "papers": {}
        }
    with open(f"_notes/{name}.md", 'w') as f:
        yaml.dump(entry, Dumper=Dumper, explicit_start=True, allow_unicode=True, width=150, stream=f)
        print("---", file=f)
        print("{% include links.html %}", file=f)

main()
