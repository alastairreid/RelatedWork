---
ENTRYTYPE: inbook
abstract: A powerful approach to finding errors in computer software is to translate a given program into a verification condition, a logical formula that
  is valid if and only if the program is free of the classes of errors under consideration. Finding errors in the program is then done by mechanically searching
  for counterexamples to the verification condition. This paper gives an overview of the technology that goes into such program checkers, reports on some
  of the progress and lessons learned in the past ten years, and identifies some remaining challenges.
added: 2020-09-19
address: Berlin, Heidelberg
authors:
- K. Rustan M. Leino
booktitle: 'Informatics: 10 Years Back, 10 Years Ahead'
doi: 10.1007/3-540-44577-3_11
editor: Wilhelm, Reinhard
isbn: 978-3-540-44577-7
layout: paper
link: https://doi.org/10.1007/3-540-44577-3_11
pages: 157-175
publisher: Springer Berlin Heidelberg
read: true
readings:
- 2020-09-17
title: 'Extended static checking: A ten-year perspective'
url: https://doi.org/10.1007/3-540-44577-3_11
year: 2001
notes:
- extended static checking
- decidability ceiling
- auto-active verification
- SMT lib format
- annotation burden
papers:
- cohen:cav:2010
---

Super-interesting background and explanation of the choices made in ESC/Modula-3
and ESC/Java.
Both a form of [auto-active verifier][auto-active verification] (although that
term was not used by the author for another 10 years.

Some key themes in the paper are

- the [decidability ceiling]: the boundary between analyses that consistently
  run in reasonable time and those that are more powerful but may not be
  decidable.

- allowing 'unsoundness in just the right places' to 'achieve a better position
  in the coverage-to-effort design space'.
  This is necessary because not all analyses are decidable so you either need
  to add a lot of annotations (taking programmer effort) or accept that
  a little unsoundness (by not trying to detect certain classes of bugs).

- Exploiting / imposing programming methodology such as requiring function
  contracts, etc., restricting the language to avoid poorly defined parts of
  the language.

- The need for an escape hatch to suppress static checking (again, driven by
  decidability).

Although the paper is mostly about technical details, it does sketch how
counterexamples from the SMT solver were used to generate error messages.
This is done by labelling subexpressions so that they can be related back
to parts of the original program.
(It's not clear but it's possible that the :named feature in [SMT lib format]
is the modern version of this.)
The paper says that they are not always successful at producing useful error
messages.

In Modula-3 and Java, they took different approaches to capturing object
invariants: using a convention in Modula-3 and building in direct support in
Java.
(IIRC, [cohen:cav:2010] used the convention approach as well.)

The [annotation burden] seems to be small –around 10%– but the startup cost is
high because one must add annotations to legacy code before getting much value
back and this, together with a need for training and the risk of a new
technology, limited adoption by people outside the projects.

Modular checking was a particular problem for Java – presumably because new
subclasses are easily added.
Another problem was aliasing and checking the 'modifies' clause.

{% include links.html %}
