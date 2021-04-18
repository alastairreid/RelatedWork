---
ENTRYTYPE: article
added: 2020-06-23
address: New York, NY, USA
authors:
- Cristian Cadar
- Koushik Sen
doi: 10.1145/2408776.2408795
issn: 0001-0782
issue_date: February 2013
journal: Communications of the ACM
layout: paper
link: https://doi.org/10.1145/2408776.2408795
month: February
number: '2'
numpages: '9'
pages: 82-90
publisher: Association for Computing Machinery
read: true
readings:
- 2020-06-27
title: 'Symbolic execution for software testing: Three decades later'
url: https://doi.org/10.1145/2408776.2408795
volume: '56'
year: 2013
notes:
- symbolic execution
- DART verifier
- KLEE verifier
- EXE verifier
- CUTE verifier
- CREST verifier
- survey
papers:
- baldoni:compsurv:2018
---

This is a survey of symbolic execution with an emphasis on the [KLEE verifier].
It is probably a better introduction to the concepts of symbolic execution than the
[baldoni:compsurv:2018] survey but this makes it less complete.

Like [baldoni:compsurv:2018], this article describes some of the important
optimizations to make symbolic execution effective including

- Path optimizations such as
  random exploration,
  interleaving symbolic execution with random exploration,
  pruning redundant paths,
  lazy test generation (only exploring functions if their output is important to the constraint),
  static path merging (aka branch predication).

- Constraint optimizations such as
  irrelevant constraint elimination,
  incremental solving (e.g., counterexample caching),

It ends with a sketch of five symbolic execution tools:
the [DART verifier],
[CUTE][CUTE verifier],
[CREST][CREST verifier],
[EXE][EXE verifier] and
the [KLEE verifier].

{% include links.html %}
