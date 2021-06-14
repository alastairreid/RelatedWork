---
ENTRYTYPE: inproceedings
abstract: Symbiotic  8 extends the traditional combination of static analyses, instrumentation, program slicing, and symbolic execution with one substantial
  novelty, namely a technique mixing symbolic execution with k-induction. This technique can prove the correctness of programs with possibly unbounded loops,
  which cannot be done by classic symbolic execution. Symbiotic  8 delivers also several other improvements. In particular, we have modified our fork of
  the symbolic executor Klee to support the comparison of symbolic pointers. Further, we have tuned the shape analysis tool Predator (integrated already
  in Symbiotic  7) to perform better on llvm bitcode. We have also developed a light-weight analysis of relations between variables that can prove the absence
  of out-of-bound accesses to arrays.
added: 2021-06-14
address: Cham
authors:
- Marek Chalupa
- Tomáš Jašek
- Jakub Novák
- Anna Řechtáčková
- Veronika Šoková
- Jan Strejček
booktitle: Tools and Algorithms for the Construction and Analysis of Systems
editor: Groote, Jan Friso and Larsen, Kim Guldstrand
isbn: 978-3-030-72013-1
layout: paper
pages: 453-457
publisher: Springer International Publishing
read: false
readings: []
title: 'Symbiotic 8: Beyond symbolic execution'
year: 2021
notes:
- symbolic execution
papers:
---
{% include links.html %}
