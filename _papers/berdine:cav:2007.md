---
ENTRYTYPE: inproceedings
abstract: 'We propose a shape analysis that adapts to some of the complex composite data structures found in industrial systems-level programs. Examples
  of such data structures include ``cyclic doubly-linked lists of acyclic singly-linked lists'''', ``singly-linked lists of cyclic doubly-linked lists with
  back-pointers to head nodes'''', etc. The analysis introduces the use of generic higher-order inductive predicates describing spatial relationships together
  with a method of synthesizing new parameterized spatial predicates which can be used in combination with the higher-order predicates. In order to evaluate
  the proposed approach for realistic programs we have performed experiments on examples drawn from device drivers: the analysis proved safety of the data
  structure manipulation of several routines belonging to an IEEE 1394 (firewire) driver, and also found several previously unknown memory safety bugs.'
added: 2021-04-25
address: Berlin, Heidelberg
authors:
- Josh Berdine
- Cristiano Calcagno
- Byron Cook
- Dino Distefano
- Peter W. O'Hearn
- Thomas Wies
- Hongseok Yang
booktitle: Computer Aided Verification
editor: Damm, Werner and Hermanns, Holger
isbn: 978-3-540-73368-3
layout: paper
pages: 178-192
publisher: Springer Berlin Heidelberg
read: false
readings: []
title: Shape analysis for composite data structures
year: 2007
notes:
- separation logic
papers:
---
{% include links.html %}
