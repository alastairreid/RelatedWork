---
doi: 10.1007/3-540-44829-2_17
ENTRYTYPE: inproceedings
abstract: Blast (the Berkeley Lazy Abstraction Software verification Tool) is a verification system for checking safety properties of C programs using automatic
  property-driven construction and model checking of software abstractions. Blast implements an abstract-model check-refine loop to check for reachability
  of a specified label in the program. The abstract model is built on the fly using predicate abstraction. This model is then checked for reachability.
  If there is no (abstract) path to the specified error label, Blast reports that the system is safe and produces a succinct proof. Otherwise, it checks
  if the path is feasible using symbolic execution of the program. If the path is feasible, Blast outputs the path as an error trace, otherwise, it uses
  the infeasibility of the path to refine the abstract model. Blast short-circuits the loop from abstraction to verification to refinement, integrating
  the three steps tightly through ``lazy abstraction'' [5]. This integration can offer significant advantages in performance by avoiding the repetition
  of work from one iteration of the loop to the next.
added: 2020-05-04
address: Berlin, Heidelberg
authors:
- Thomas A. Henzinger
- Ranjit Jhala
- Rupak Majumdar
- Grégoire Sutre
booktitle: Model Checking Software
editor: Ball, Thomas and Rajamani, Sriram K.
isbn: 978-3-540-44829-7
layout: paper
pages: 235-239
publisher: Springer Berlin Heidelberg
read: false
readings: []
title: Software verification with BLAST
year: 2003
notes:
- model checking
- CEGAR
papers:
- necula:cc:2002
- ball:pldi:2001
---
{% include links.html %}
