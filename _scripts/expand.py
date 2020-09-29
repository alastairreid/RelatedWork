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
from urllib import parse

def name2ref(x):
    x = x.lower()
    x = x.replace(" ", "-")
    return x

def ref2url(x):
    x = x.replace(":", "-")
    x = x.replace("/", "-")
    return x

# Convert links from list of labels
# to (label: url) pairs
def patch_links(header):
    for c in ["isa", "examples", "notes", "papers"]:
        xs = header.get(c, [])
        if not xs: xs = []
        g = "notes" if c in ["examples", "isa"] else c
        xs = { x: name2ref(f"{g}/{x}") for x in xs }
        header[c] = xs

def patch_body(body):
    return [ l for l in body if not re.match("{% include ", l) ]

def read_md(f):
    # print(f"Reading file {f}", file=sys.stderr)
    with open(f) as file:
        ls = file.readlines()
        t = ls[1:].index("---\n")
        header = ls[1:t+1]
        body = ls[t+2:]
        header = yaml.safe_load("".join(header))
        return (header, body)

def add_links(links):
    for (x, ref) in links.items():
        print(f'[{x}]: #{ref2url(ref)}')

# for every link to a page, add a back reference
def add_backrefs(ps):
    ns = {}
    for p, (h, _) in ps.items():
        h["refs"] = {}
        for c in ["examples", "isa", "notes", "papers"]:
            for x, ref in h[c].items():
                rs = ns[ref] if ref in ns else {}
                link = None if p.startswith("notes") else p.split("/")[1] # todo - change style for papers?
                rs[p] = [h['title'], link]
                ns[ref] = rs
                # print(f"{ref} <- {p}", file=sys.stderr)
    for ref, xs in ns.items():
        if ref in ps:
            # print(f"{ref} -> {xs}", file=sys.stderr)
            ps[ref][0]["refs"] = xs
        else:
            print(f"Reference to missing page {ref} from {list(xs.keys())}", file=sys.stderr)
            header = {
                    "title": ref,
                    "layout": "note",
                    "isa": {},
                    "examples": {},
                    "notes": {},
                    "papers": {},
                    "refs": xs
                    }
            body = [
                    "This is a stub article"
                    ]
            ps[ref] = (header, body)

def pp_refs(label, xs):
    if xs:
        print(f"{label}: ")
        print(",\n".join([f"[{x}](#{ref2url(x)})" for x in xs]) + "\\")

def pp_link(text, url):
    if url:
        print(f"[{text}]({url})")

def pp_linkarg(text, url, k, v):
    if url:
        print(f"[{text}]({url}?{k}={parse.quote(v)})")

def print_file(i, header, body):
    print(f"# {header['title']}" +" {#"+ref2url(i)+"}")
    print()
    if 'logo' in header:
        print(f"![{header['title']}]({header['logo']})" +"{width=200px}")
    print()
    if 'authors' in header:
        print(", ".join(header['authors']))
    if 'ENTRYTYPE' in header:
        e = header['ENTRYTYPE']
        if e == "phdthesis":
            print("Ph.D. thesis")
        elif e == "mscthesis":
            print("Masters thesis")
        elif e == "manual":
            print("Manual")
        elif e == "techreport":
            print("Report")

    if 'booktitle' in header:
        print(header['booktitle'])
        if 'series' in header and 'volume' in header:
            print(f"{header['series']}, volume {header['volume']}")
        elif 'series' in header:
            print(header['series'])

    if 'school' in header and header['school']: print(header['school'])
    if 'institution' in header and header['institution']: print(header['institution'])
    if 'organization' in header and header['organization']: print(header['organization'])
    if 'location' in header and header['location']: print(header['location'])
    if 'publisher' in header and header['publisher']: print(header['publisher'])
    if 'address' in header and header['address']: print(header['address'])
    if 'pages' in header and header['pages']: print(f"Pages {header['pages']}")
    if 'day' in header and header['day']: print(header['day'])
    if 'month' in header and header['month']: print(header['month'])
    if 'year' in header and header['year']: print(header['year'])

    pp_linkarg("[Google Scholar]", "https://scholar.google.com/scholar", "q", f"{header['title']}")
    pp_link("[Website]", header.get("website"))
    pp_link("[Wikipedia]", header.get("wiki"))
    if header['layout'] == 'paper':
        pp_linkarg("[DBLP]", "https://dblp.org/search", "q", f"{header['title']}")
        pp_linkarg("[Citeseer]", "https://citeseer.ist.psu.edu/search", "q", f"{header['title']}")
    if 'doi' in header: pp_link("[doi]", f"https://doi.org/{header['doi']}")
    if 'eprint' in header: pp_link("[arXiv]", f"https://arxiv.org/{header['eprint']}")
    if 'isbn' in header: pp_linkarg("[ISBN]", "http://books.google.com/books", "vid", f"ISBN{header['isbn']}")
    if 'url' in header: pp_link("[url]", header['url'])
    print()

    pp_refs("Is a kind of", header["isa"])
    pp_refs("Examples", header["examples"])
    pp_refs("Notes", header["notes"])
    pp_refs("Papers", header["papers"])
    pp_refs("Referenced by", header["refs"])
    print()

    print("".join(body))
    print()

    add_links(header["notes"])
    add_links(header["papers"])

def get_authors(ps):
    authors = {}
    for p, (h, b) in ps.items():
        if 'authors' in h:
            for a in h['authors']:
                authors.setdefault(a, []).append(p)
    return authors

def read_files(fs):
    ps = { f[1:-3]: read_md(f) for f in fs }
    for p, (h, b) in ps.items(): patch_links(h)
    ps = { p: (h, patch_body(b)) for p, (h, b) in ps.items() }
    add_backrefs(ps)
    return ps

def pp_md(ps, authors):
    header = {
            "title": "Related Work",
            "author": "Alastair D. Reid",
            "toc": True
            }
    print("---")
    print(yaml.dump(header))
    print("---")
    print()

    for p, (h, b) in ps.items():
        print_file(p, h, b)

    print("# Author Index\n")
    for a in sorted(authors.keys(), key=lambda x: x.split(" ")[-1]):
        ps = authors[a]
        ps = [ f"[{p}](#{ref2url(p)})" for p in ps ]
        print(f"- {a}: {', '.join(ps)}")

def main():
    ps = read_files(sys.argv[1:])
    authors = get_authors(ps)
    pp_md(ps, authors)

    # generate data file: list of authors and papers
    with open("_data/authors.yaml", "w") as f:
        authors = [ {"name": a, "papers":authors[a]} for a in sorted(authors.keys(), key=lambda x: x.split(" ")[-1]) ]
        yaml.dump(authors, f)

    # generate references to each page
    with open("_data/backrefs.yaml", "w") as f:
        refs = {}
        for c in ["papers", "notes"]:
            refs[c] = { p: [ [r,l] for r,l in h["refs"].items() if r.startswith(c) ] for p, (h, _) in ps.items() }
        yaml.dump(refs, f)

main()
