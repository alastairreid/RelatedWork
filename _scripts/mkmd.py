#! /usr/bin/env python3

import json
import yaml
from yaml import dump
from yaml import CDumper as Dumper

import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.customization import homogenize_latex_encoding
from bibtexparser.customization import convert_to_unicode

import re
import string
import sys

def swapauth(x):
    xs = re.split(r'\s*,\s*', x)
    if len(xs) == 2:
        return xs[1] +' '+ xs[0]
    else:
        return x

# ToDo: use the following somehow
# LaTeX translations from here:
# https://stackoverflow.com/questions/4578912/replace-all-accented-characters-by-their-latex-equivalent
latexAccents = [
  [ u"à", "\\`a" ], # Grave accent
  [ u"è", "\\`e" ],
  [ u"ì", "\\`\\i" ],
  [ u"ò", "\\`o" ],
  [ u"ù", "\\`u" ],
  [ u"ỳ", "\\`y" ],
  [ u"À", "\\`A" ],
  [ u"È", "\\`E" ],
  [ u"Ì", "\\`\\I" ],
  [ u"Ò", "\\`O" ],
  [ u"Ù", "\\`U" ],
  [ u"Ỳ", "\\`Y" ],
  [ u"á", "\\'a" ], # Acute accent
  [ u"é", "\\'e" ],
  [ u"í", "\\'\\i" ],
  [ u"ó", "\\'o" ],
  [ u"ú", "\\'u" ],
  [ u"ý", "\\'y" ],
  [ u"Á", "\\'A" ],
  [ u"É", "\\'E" ],
  [ u"Í", "\\'\\I" ],
  [ u"Ó", "\\'O" ],
  [ u"Ú", "\\'U" ],
  [ u"Ý", "\\'Y" ],
  [ u"â", "\\^a" ], # Circumflex
  [ u"ê", "\\^e" ],
  [ u"î", "\\^\\i" ],
  [ u"ô", "\\^o" ],
  [ u"û", "\\^u" ],
  [ u"ŷ", "\\^y" ],
  [ u"Â", "\\^A" ],
  [ u"Ê", "\\^E" ],
  [ u"Î", "\\^\\I" ],
  [ u"Ô", "\\^O" ],
  [ u"Û", "\\^U" ],
  [ u"Ŷ", "\\^Y" ],
  [ u"ä", "\\\"a" ],    # Umlaut or dieresis
  [ u"ë", "\\\"e" ],
  [ u"ï", "\\\"\\i" ],
  [ u"ö", "\\\"o" ],
  [ u"ü", "\\\"u" ],
  [ u"ÿ", "\\\"y" ],
  [ u"Ä", "\\\"A" ],
  [ u"Ë", "\\\"E" ],
  [ u"Ï", "\\\"\\I" ],
  [ u"Ö", "\\\"O" ],
  [ u"Ü", "\\\"U" ],
  [ u"Ÿ", "\\\"Y" ],
  [ u"ç", "\\c{c}" ],   # Cedilla
  [ u"Ç", "\\c{C}" ],
  [ u"œ", "{\\oe}" ],   # Ligatures
  [ u"Œ", "{\\OE}" ],
  [ u"æ", "{\\ae}" ],
  [ u"Æ", "{\\AE}" ],
  [ u"å", "{\\aa}" ],
  [ u"Å", "{\\AA}" ],
  [ u"–", "--" ],   # Dashes
  [ u"—", "---" ],
  [ u"ø", "{\\o}" ],    # Misc latin-1 letters
  [ u"Ø", "{\\O}" ],
  [ u"ß", "{\\ss}" ],
  [ u"¡", "{!`}" ],
  [ u"¿", "{?`}" ],
  [ u"\\", "\\\\" ],    # Characters that should be quoted
  [ u"~", "\\~" ],
  [ u"&", "\\&" ],
  [ u"$", "\\$" ],
  [ u"{", "\\{" ],
  [ u"}", "\\}" ],
  [ u"%", "\\%" ],
  [ u"#", "\\#" ],
  [ u"_", "\\_" ],
  [ u"≥", "$\\ge$" ],   # Math operators
  [ u"≤", "$\\le$" ],
  [ u"≠", "$\\neq$" ],
  [ u"©", "\copyright" ], # Misc
  [ u"ı", "{\\i}" ],
  [ u"µ", "$\\mu$" ],
  [ u"°", "$\\deg$" ],
  [ u"‘", "`" ],    #Quotes
  [ u"’", "'" ],
  [ u"“", "``" ],
  [ u"”", "''" ],
  [ u"‚", "," ],
  [ u"„", ",," ],
]

parser = BibTexParser()
parser.customization = homogenize_latex_encoding
x = sys.stdin.read()
x = x.replace('$\{$', '{')
x = x.replace('$\}$', '}')
db = bibtexparser.loads(x, parser=parser)

for e in db.entries:
    author = e['author']

    author = author.replace("{\\'e}", 'é')
    author = author.replace("{\\`e}", 'è')
    author = author.replace("\\c c", 'ç')
    author = author.replace("\\textquotesingle ", u"’")
    author = author.replace("' ", u"’")
    author = author.replace("{\\l}", u"ł")
    author = author.replace("\n", " ")

    authors = re.split('\s+and\s+', author)
    authors = [ swapauth(a) for a in authors ]
    e['authors'] = authors
    del e['author']

    e['title'] = re.sub(r'[{}]', '', e['title'])
    e['year'] = int(e['year'])
    if 'pages' in e: e['pages'] = e['pages'].replace('--', '-')

    del e['ID']

    e['layout'] = 'paper'
    e['read'] = False

# print(json.dumps(db.entries, indent=4))
for e in db.entries:
    print(yaml.dump(e, Dumper=Dumper, explicit_start=True), end='')
    print('topics:')
    print('---')

    print("["+e['title']+"]({% link _papers/.md %})")
