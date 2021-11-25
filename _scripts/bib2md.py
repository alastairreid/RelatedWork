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
    s = s.replace("{\\'a}",  'á')
    s = s.replace("{\\´a}",  'á')
    s = s.replace("{\\^a}",  'â')
    s = s.replace("{\\~a}",  'ã')
    s = s.replace("{\\\"a}", 'ä')
    s = s.replace("{\\r a}", 'å')

    s = s.replace("{\\`e}",  'è')
    s = s.replace("{\\'e}",  'é')
    s = s.replace("{\\^e}",  'ê')
    s = s.replace("{\\\"e}", 'ë')

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

    s = s.replace("{\\\"O}", 'Ö')

    s = s.replace("{\\`u}",  'ù')
    s = s.replace("{\\'u}",  'ú')
    s = s.replace("{\\^u}",  'û')
    s = s.replace("{\\\"u}", 'ü')

    s = s.replace("\\c{t}",  'ţ')
    s = s.replace("{\\ct}",  'ţ')
    s = s.replace("{\\c t}", 'ţ')

    s = s.replace("\\v{a}",  'ă')
    s = s.replace("{\\va}",  'ă')
    s = s.replace("{\\v a}", 'ă')

    s = s.replace("{\\v C}a",'Că')
    s = s.replace("{\\v c}",  'č')
    s = s.replace("{\\' c}",  'ć')
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

    s = s.replace("\\textasciitilde ", "~")
    s = s.replace("\\textasciigrave ", "`")
    s = s.replace("\\&", "&")
    s = s.replace("\\_", "_")

    s = s.replace("\n", " ")

    return s

def cleanup(e):
    """Cleanup data read from the BibTeX file"""

    for i in e: e[i] = e[i].strip()

    if 'authors' in e: e['author'] = e['authors']

    if 'author' in e:
        # bib entries for proceedings don't have an author
        author = e['author']
        author = replaceAccents(author)

        authors = re.split('\s+and\s+', author)
        authors = [ a.strip() for a in authors ]
        authors = [ swapauth(a) for a in authors ]
        e['authors'] = authors
        del e['author']
    else:
        print("No author ", e['ID'])

    if 'title' in e:
        e['title'] = re.sub(r'[{}]', '', e['title'])
    else:
        print("No title", e['ID'])

    if 'year' in e:
        e['year'] = int(e['year'])
    else:
        print("No year", e['ID'])

    for i in ['abstract', 'address', 'booktitle', 'day', 'doi', 'editor', 'institution', 'note', 'number', 'pages', 'school', 'series', 'title', 'url']:
        if i in e: e[i] = replaceAccents(e[i])

    if 'url' in e: e['link'] = e['url']

    e['layout'] = 'paper'
    e['read'] = False
    e['readings'] = []
    e['added'] = date.today()

def main():
    parser = BibTexParser(common_strings=True)
    parser.customization = homogenize_latex_encoding
    x = sys.stdin.read()
    x = x.replace('$\{$', '{')
    x = x.replace('$\}$', '}')
    # todo: this is a bodge to cleanup ACM use of abbreviated month names
    x = x.replace("month = jan", 'month = "January"')
    x = x.replace("month = feb", 'month = "February"')
    x = x.replace("month = mar", 'month = "March"')
    x = x.replace("month = apr", 'month = "April"')
    x = x.replace("month = may", 'month = "May"')
    x = x.replace("month = jun", 'month = "June"')
    x = x.replace("month = jul", 'month = "July"')
    x = x.replace("month = aug", 'month = "August"')
    x = x.replace("month = sep", 'month = "September"')
    x = x.replace("month = oct", 'month = "October"')
    x = x.replace("month = nov", 'month = "November"')
    x = x.replace("month = dec", 'month = "December"')
    # todo: cleanup ACM's pointless habit of abbreviating journal names
    x = x.replace("Commun. ACM", 'Communications of the ACM')
    db = bibtexparser.loads(x, parser=parser)

    for e in db.entries:
        cleanup(e)

    # print(json.dumps(db.entries, indent=4))

    for e in db.entries:
        name = e['ID']
        name = name.replace("/", ":")
        name = f'_staging/{name}.md'
        print(f'Writing to {name}')
        with open(name, 'w') as f:
            del e['ID']
            yaml.dump(e, Dumper=Dumper, explicit_start=True, allow_unicode=True, width=150, stream=f)
            print('notes:', file=f)
            print('papers:', file=f)
            print('---', file=f)
            print('{% include links.html %}', file=f)

main()
