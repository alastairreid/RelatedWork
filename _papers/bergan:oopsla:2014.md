---
ENTRYTYPE: inproceedings
abstract: We describe an algorithm to perform symbolic execution of a multithreaded program starting from an arbitrary program context. We argue that this
  can enable more efficient symbolic exploration of deep code paths in multithreaded programs by allowing the symbolic engine to jump directly to program
  contexts of interest.The key challenge is modeling the initial context with reasonable precision - an overly approximate model leads to exploration of
  many infeasible paths during symbolic execution, while a very precise model would be so expensive to compute that computing it would defeat the purpose
  of jumping directly to the initial context in the first place. We propose a context-specific dataflow analysis that approximates the initial context cheaply,
  but precisely enough to avoid some common causes of infeasible-path explosion. This model is necessarily approximate - it may leave portions of the memory
  state unconstrained, leaving our symbolic execution unable to answer simple questions such as "which thread holds lock A?". For such cases, we describe
  a novel algorithm for evaluating symbolic synchronization during symbolic execution. Our symbolic execution semantics are sound and complete up to the
  limits of the underlying SMT solver. We describe initial experiments on an implementation in Cloud 9.
added: 2021-05-05
address: New York, NY, USA
authors:
- Tom Bergan
- Dan Grossman
- Luis Ceze
booktitle: Proceedings of the 2014 ACM International Conference on Object Oriented Programming Systems Languages & Applications
doi: 10.1145/2660193.2660200
isbn: '9781450325851'
keywords: static analysis, multithreading, symbolic execution
layout: paper
link: https://doi.org/10.1145/2660193.2660200
location: Portland, Oregon, USA
numpages: '16'
pages: 491-506
publisher: Association for Computing Machinery
read: false
readings: []
series: OOPSLA '14
title: Symbolic execution of multithreaded programs from arbitrary program contexts
url: https://doi.org/10.1145/2660193.2660200
year: 2014
notes:
- symbolic execution
papers:
---
{% include links.html %}
