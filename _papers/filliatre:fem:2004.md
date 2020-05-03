---
ENTRYTYPE: inproceedings
added: 2019-10-16
authors:
- Jean-Christophe Filliâtre
- Claude Marché
layout: paper
pages: 15-29
read: true
readings:
- 2019-10-16
title: Multi-prover verification of C programs
booktitle: Sixth International Conference on Formal Engineering Methods
doi: 10.1007/978-3-540-30482-1_10
organization: Springer
series: LNCS
volume: 3308
year: 2004
topics:
- tools
- verification
notes:
- why3-verifier
papers:
- cuoq:sefm:2012
---

Describes "Caduceus": a tool to translate C code to the WhyML specification
language lowering imperative code to pure code and handling pointers.
Introduced the specification notation that later became ACSL and a forerunner
to [Frama-C][cuoq:sefm:2012].

Given current understanding of undefined behaviour and implementation defined behaviour in C, the translation from C looks a bit naïve.

{% include links.html %}
