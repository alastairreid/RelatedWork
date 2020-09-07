---
ENTRYTYPE: inproceedings
added: 2020-09-07
address: New York, NY, USA
authors:
- Nikolai Tillmann
- Wolfram Schulte
booktitle: Proceedings of the 10th European Software Engineering Conference Held Jointly with 13th ACM SIGSOFT International Symposium on Foundations of
  Software Engineering
doi: 10.1145/1081706.1081749
isbn: '1595930140'
keywords: automatic test input generation, unit testing, constraint solving, algebraic data types, symbolic execution
layout: paper
link: https://doi.org/10.1145/1081706.1081749
location: Lisbon, Portugal
numpages: '10'
pages: 253-262
publisher: Association for Computing Machinery
read: true
readings:
- 2020-09-07
series: ESEC/FSE-13
title: Parameterized Unit Tests
url: https://doi.org/10.1145/1081706.1081749
year: 2005
notes:
- symbolic execution
- unit tests
- property-based testing
- SMT solver
papers:
---

Parameterized unit tests are a form of [property-based testing] that
generalizes traditional unit tests.  The tests can be instantiated with
concrete values to serve as traditional tests, they can be verified using
[symbolic execution] or, to support modular verification, they can be used as
axioms in the spirit of algebraic specification to use when verifying calls to
a library.

This was implemented for .NET on an early [symbolic execution] tool
using early [SMT solver]s.
It is evaluated on eight benchmarks (qsort, triangle, hashtable, bad,
linkedlist, red-black tree).

The paper has a lengthy related/future work section that cites lots of early
(forgotten?) work on test generation from formal specifications from the '90s.

{% include links.html %}
