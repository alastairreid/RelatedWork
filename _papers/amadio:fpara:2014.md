---
ENTRYTYPE: inproceedings
abstract: We provide an overview of the FET-Open Project CerCo (`Certified Complexity'). Our main achievement is the development of a technique for analysing
  non-functional properties of programs (time, space) at the source level with little or no loss of accuracy and a small trusted code base. The core component
  is a C compiler, verified in Matita, that produces an instrumented copy of the source code in addition to generating object code. This instrumentation
  exposes, and tracks precisely, the actual (non-asymptotic) computational cost of the input program at the source level. Untrusted invariant generators
  and trusted theorem provers may then be used to compute and certify the parametric execution time of the code.
added: 2021-11-22
address: Cham
authors:
- Roberto M. Amadio
- Nicolas Ayache
- Francois Bobot
- Jaap P. Boender
- Brian Campbell
- Ilias Garnier
- Antoine Madet
- James McKinna
- Dominic P. Mulligan
- Mauro Piccolo
- Randy Pollack
- Yann Régis-Gianas
- Claudio Sacerdoti Coen
- Ian Stark
- Paolo Tranquilli
booktitle: Foundational and Practical Aspects of Resource Analysis
editor: Dal Lago, Ugo and Pe{ñ}a, Ricardo
isbn: 978-3-319-12466-7
layout: paper
pages: 1-18
publisher: Springer International Publishing
read: false
readings: []
title: Certified complexity (CerCo)
year: 2014
notes:
- binary analysis
papers:
---
{% include links.html %}
