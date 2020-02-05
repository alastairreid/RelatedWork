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

from datetime import date

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

def replaceAccents(s):
    """
    Replaces LaTeX symbols with extended ASCII equivalents.
    (It avoids using Unicode because that doesn't render well.)
    """

    s = s.replace("{\\`a}",  'à')
    s = s.replace("{\\´a}",  'á')
    s = s.replace("{\\^a}",  'â')
    s = s.replace("{\\~a}",  'ã')
    s = s.replace("{\\\"a}", 'ä')
    s = s.replace("{\\r a}", 'å')

    # s = s.replace("{\\`e}",  'è')
    # s = s.replace("{\\'e}",  'é')
    # s = s.replace("{\\^e}",  'ê')
    # s = s.replace("{\\\"e}", 'ë')

    s = s.replace("{\\`i}",  'ì')
    s = s.replace("{\\'i}",  'í')
    s = s.replace("{\\^i}",  'î')
    s = s.replace("{\\\"i}", 'ï')

    s = s.replace("{\\`o}",  'ò')
    s = s.replace("{\\'o}",  'ó')
    s = s.replace("{\\^o}",  'ô')
    s = s.replace("{\\\"o}", 'ö')
    s = s.replace("{\\~o}",  'õ')
    s = s.replace("{\\u o}", 'ð')

    s = s.replace("{\\`u}",  'ù')
    s = s.replace("{\\'u}",  'ú')
    s = s.replace("{\\^u}",  'û')
    s = s.replace("{\\\"u}", 'ü')

    s = s.replace("\\c c",   'ç')
    s = s.replace("\\~n",    'ñ')
    s = s.replace("\\o",     'ø')
    s = s.replace("{\\'y}",  'ý')
    s = s.replace("{\\\"y}", 'ÿ')

    # s = s.replace("{\\l}",   u"ł")

    s = s.replace("--", '-')
    s = s.replace("\\textendash ", '-')
    s = s.replace("\\textemdash ", '-')
    # s = s.replace("--", '–')
    # s = s.replace("\\textendash ", '–')
    # s = s.replace("\\textemdash ", '—')

    s = s.replace('’', '\'')
    s = s.replace("\\textquotesingle ",   '\'')
    s = s.replace("\\textquoteleft ",     '\'')
    s = s.replace("\\textquoteright ",    '\'')
    s = s.replace("\\textquotedouble ",   '\"')
    s = s.replace("\\textquotedblleft ",  '\"')
    s = s.replace("\\textquotedblright ", '\"')
    # s = s.replace("\\textquotedblleft ",  "“")
    # s = s.replace("\\textquotedblright ", "”")
    # s = s.replace("\\textquoteleft ",     '‘')
    # s = s.replace("\\textquoteright ",    '’')

    s = s.replace("\n", " ")

    return s

parser = BibTexParser()
parser.customization = homogenize_latex_encoding
x = sys.stdin.read()
x = x.replace('$\{$', '{')
x = x.replace('$\}$', '}')
db = bibtexparser.loads(x, parser=parser)

for e in db.entries:
    author = e['author']
    author = replaceAccents(author)

    authors = re.split('\s+and\s+', author)
    authors = [ swapauth(a) for a in authors ]
    e['authors'] = authors
    del e['author']

    e['title'] = re.sub(r'[{}]', '', e['title'])
    e['year'] = int(e['year'])
    for i in ['abstract', 'note', 'number', 'pages', 'series']:
        if i in e: e[i] = replaceAccents(e[i])

    del e['ID']

    e['layout'] = 'paper'
    e['read'] = False
    e['readings'] = []
    e['added'] = date.today()

# print(json.dumps(db.entries, indent=4))
for e in db.entries:
    print(yaml.dump(e, Dumper=Dumper, explicit_start=True), end='')
    print('topics:')
    print('---')

