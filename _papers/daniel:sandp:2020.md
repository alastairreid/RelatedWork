---
ENTRYTYPE: inproceedings
abstract: The constant-time programming discipline (CT) is an efficient countermeasure against timing side-channel attacks, requiring the control flow and
  the memory accesses to be independent from the secrets. Yet, writing CT code is challenging as it demands to reason about pairs of execution traces (2-hypersafety
  property) and it is generally not preserved by the compiler, requiring binary-level analysis. Unfortunately, current verification tools for CT either
  reason at higher level (C or LLVM), or sacrifice bug-finding or bounded-verification, or do not scale. We tackle the problem of designing an efficient
  binary-level verification tool for CT providing both bug-finding and bounded-verification. The technique builds on relational symbolic execution enhanced
  with new optimizations dedicated to information flow and binary-level analysis, yielding a dramatic improvement over prior work based on symbolic execution.
  We implement a prototype, BINSEC/REL, and perform extensive experiments on a set of 338 cryptographic implementations, demonstrating the benefits of our
  approach in both bug-finding and bounded-verification. Using BINSEC/REL, we also automate a previous manual study of CT preservation by compilers. Interestingly,
  we discovered that gcc -O0 and backend passes of clang introduce violations of CT in implementations that were previously deemed secure by a state-of-the-art
  CT verification tool operating at LLVM level, showing the importance of reasoning at binary-level.
added: 2021-06-14
authors:
- Lesly-Ann Daniel
- Sébastien Bardin
- Tamara Rezk
booktitle: 2020 IEEE Symposium on Security and Privacy (SP)
doi: 10.1109/SP40000.2020.00074
issn: 2375-1207
keywords: ''
layout: paper
month: May
number: ''
pages: 1021-1038
read: false
readings: []
title: 'Binsec/Rel: Efficient relational symbolic execution for constant-time at binary-level'
volume: ''
year: 2020
notes:
- information flow
- symbolic execution
- self composition
- binary analysis
papers:
---
{% include links.html %}
