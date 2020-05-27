---
ENTRYTYPE: article
abstract: 'An important correctness criterion for software running on embedded microcontrollers is stack safety: a guarantee that the call stack does not
  overflow. Our first contribution is a method for statically guaranteeing stack safety of interrupt-driven embedded software using an approach based on
  context-sensitive dataflow analysis of object code. We have implemented a prototype stack analysis tool that targets software for Atmel AVR microcontrollers
  and tested it on embedded applications compiled from up to 30,000 lines of C. We experimentally validate the accuracy of the tool, which runs in under
  10 sec on the largest programs that we tested. The second contribution of this paper is the development of two novel ways to reduce stack memory requirements
  of embedded software.'
added: 2019-06-01
affiliation: University of Utah
ar_shortname: TECS 05
authors:
- John Regehr
- Alastair D. Reid
- Kirk Webb
doi: 10.1145/1113830.1113833
journal: ACM Transactions Embedded Computing Systems
layout: paper
number: '4'
pages: 751-778
read: false
readings: []
title: Eliminating stack overflow by abstract interpretation
volume: '4'
year: 2005
topics:
notes:
- abstract interpretation
- ISA specification
papers:
---

{% include links.html %}
