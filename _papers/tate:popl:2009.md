---
ENTRYTYPE: inproceedings
abstract: 'Optimizations in a traditional compiler are applied sequentially, with each optimization destructively modifying the program to produce a transformed
  program that is then passed to the next optimization. We present a new approach for structuring the optimization phase of a compiler. In our approach,
  optimizations take the form of equality analyses that add equality information to a common intermediate representation. The optimizer works by repeatedly
  applying these analyses to infer equivalences between program fragments, thus saturating the intermediate representation with equalities. Once saturated,
  the intermediate representation encodes multiple optimized versions of the input program. At this point, a profitability heuristic picks the final optimized
  program from the various programs represented in the saturated representation. Our proposed way of structuring optimizers has a variety of benefits over
  previous approaches: our approach obviates the need to worry about optimization ordering, enables the use of a global optimization heuristic that selects
  among fully optimized programs, and can be used to perform translation validation, even on compilers other than our own. We present our approach, formalize
  it, and describe our choice of intermediate representation. We also present experimental results showing that our approach is practical in terms of time
  and space overhead, is effective at discovering intricate optimization opportunities, and is effective at performing translation validation for a realistic
  optimizer.'
added: 2023-06-21
address: New York, NY, USA
authors:
- Ross Tate
- Michael Stepp
- Zachary Tatlock
- Sorin Lerner
booktitle: Proceedings of the 36th Annual ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages
doi: 10.1145/1480881.1480915
isbn: '9781605583792'
keywords: equality reasoning, intermediate representation, compiler optimization
layout: paper
link: https://doi.org/10.1145/1480881.1480915
location: Savannah, GA, USA
numpages: '13'
pages: 264-276
publisher: Association for Computing Machinery
read: false
readings: []
series: POPL '09
title: 'Equality saturation: A new approach to optimization'
url: https://doi.org/10.1145/1480881.1480915
year: 2009
notes:
- egraphs
papers:
---
{% include links.html %}
