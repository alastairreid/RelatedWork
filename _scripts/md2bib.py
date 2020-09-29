#! /usr/bin/env python3

import json
import yaml
from yaml import dump
# from yaml import CDumper as Dumper
from yaml import Dumper

import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.customization import homogenize_latex_encoding
from bibtexparser.customization import convert_to_unicode
from bibtexparser.bwriter import BibTexWriter

from datetime import date

import itertools
import re
import string
import sys

def main():
    output = sys.argv[1]
    mds = sys.argv[2:]
    es = []
    for fn in mds:
        # print(f"loading {fn}")
        with open(fn, "r", encoding='UTF-8') as f:
            ls = f.readlines()[1:]
            ls = itertools.takewhile(lambda x: x != "---\n", ls)
            e = yaml.load("".join(ls), Loader=yaml.FullLoader)
            e['ID'] = fn.split("/")[1][0:-3]
            for i in ['title', 'booktitle']:
                if i in e:
                    s = e[i]
                    s = s.replace("#", "\#")
                    s = s.replace("&", "\&")
                    e[i] = s
            e['title'] = "{" + e['title'] + "}"
            if 'authors' in e:
                e['author'] = " and ".join(e['authors'])
                del e['authors']
            for i in ['isbn', 'pages', 'volume', 'year']:
                if i in e: e[i] = str(e[i])
            for i in ['added', 'layout', 'notes', 'papers',
                    'read', 'readings', 'topics']:
                if i in e: del e[i]
            es.append(e)

    db = BibDatabase()
    db.entries = es

    writer = BibTexWriter()
    writer.contents = ['entries']
    writer.indent = '  '
    # writer.order_entries_by = ('ENTRYTYPE', 'author', 'year')
    bibtex_str = bibtexparser.dumps(db, writer)
    with open(output, "w") as f:
        print(bibtex_str, file=f)

main()
