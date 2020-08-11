---
ENTRYTYPE: misc
added: 2020-08-11
archiveprefix: arXiv
authors:
- Alexander Weigl
- Mattias Ulbrich
- Suhyun Cha
- Bernhard Beckert
- Birgit Vogel-Heuser
eprint: '1910.09068'
layout: paper
primaryclass: cs.LO
read: true
readings:
- 2020-08-11
title: 'Relational test tables: A practical specification language for evolution and security'
year: 2019
notes:
- test generation
- information flow
- kripke structure
- model checking
papers:
---

Relational test tables describe sets of traces and constraints on those traces
and (the relational part) between traces and support for stuttering (to allow
for timing differences).

Extends authors previous work that generalized "concrete test tables" to
support verification by replacing concrete input values with constraints.

They target reactive systems so test tables describe sequences of inputs and
outputs with timing constraints.

Compare with approaches from the [model checking] community based on [Kripke
structure]s.

Implementation uses nuXmv and IC3 model checkers and demonstration is based on
a Pick and Place Unit (PPU).


{% include links.html %}
