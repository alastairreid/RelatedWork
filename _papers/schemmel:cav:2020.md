---
ENTRYTYPE: inproceedings
abstract: We describe a technique for systematic testing of multi-threaded programs. We combine Quasi-Optimal Partial-Order Reduction, a state-of-the-art
  technique that tackles path explosion due to interleaving non-determinism, with symbolic execution to handle data non-determinism. Our technique iteratively
  and exhaustively finds all executions of the program. It represents program executions using partial orders and finds the next execution using an underlying
  unfolding semantics. We avoid the exploration of redundant program traces using cutoff events. We implemented our technique as an extension of KLEE and
  evaluated it on a set of large multi-threaded C programs. Our experiments found several previously undiscovered bugs and undefined behaviors in memcached
  and GNU sort, showing that the new method is capable of finding bugs in industrial-size benchmarks.
added: 2021-06-03
address: Cham
authors:
- Daniel Schemmel
- Julian Büning
- César Rodríguez
- David Laprell
- Klaus Wehrle
booktitle: Computer Aided Verification
editor: Lahiri, Shuvendu K. and Wang, Chao
isbn: 978-3-030-53288-8
layout: paper
pages: 376-400
publisher: Springer International Publishing
read: false
readings: []
title: Symbolic partial-order execution for testing multi-threaded programs
year: 2020
notes:
papers:
---
{% include links.html %}
