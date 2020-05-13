---
ENTRYTYPE: inbook
added: 2020-05-12
address: GBR
authors:
- K. L. McMillan
booktitle: Encyclopedia of Computer Science
isbn: 0470864125
layout: paper
numpages: '5'
pages: 1177-1181
publisher: John Wiley and Sons Ltd.
read: true
readings:
- 2020-05-13
title: Model checking
year: 2003
notes:
- survey
- model checking
papers:
- jhala:compsurv:2009
- clarke:cacm:2009
---

This is a good survey of model checking that lays out the main concepts and
why they matter:

- specification
  - temporal logic
    - branching time logic (BTL)
      - computation tree logic (CTL)
    - linear temporal logic (LTL)
  - automata-based specification and verification
- scaling and performance of implementation
  - the state explosion problem
  - symbolic model checking
  - exploitation of symmetry
  - partial order-based reductions
  - abstraction and compositional methods
    - abstraction
    - compositional methods

While this all remains very relevant, this article is from 2003 and the most
recent citation is from 1998 and most of them are from the '80s so this survey
needs to be supplemented with an update on the last 20 years.
(It also doesn't say much about how a model checker works internally.)

{% include links.html %}
