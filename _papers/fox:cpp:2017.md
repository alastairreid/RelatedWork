---
ENTRYTYPE: inproceedings
abstract: 'This paper describes how the latest CakeML compiler supports verified compilation down to multiple realistically modelled target architectures.
  In particular, we describe how the compiler definition, the various language semantics, and the correctness proofs were organised to minimize target-specific
  overhead. With our setup we have incorporated compilation to four 64-bit architectures, ARMv8, x86-64, MIPS-64, RISC-V, and one 32-bit architecture, ARMv6.
  Our correctness theorem allows interference from the environment: the top-level correctness statement takes into account execution of foreign code and
  per-instruction interference from external processes, such as interrupt handlers in operating systems. The entire CakeML development is formalised in
  the HOL4 theorem prover.'
added: 2021-11-22
address: New York, NY, USA
authors:
- Anthony Fox
- Magnus O. Myreen
- Yong Kiam Tan
- Ramana Kumar
booktitle: Proceedings of the 6th ACM SIGPLAN Conference on Certified Programs and Proofs
doi: 10.1145/3018610.3018621
isbn: '9781450347051'
keywords: verified assembly, Compiler verification, ML
layout: paper
link: https://doi.org/10.1145/3018610.3018621
location: Paris, France
numpages: '13'
pages: 125-137
publisher: Association for Computing Machinery
read: false
readings: []
series: CPP 2017
title: Verified compilation of CakeML to multiple machine-code targets
url: https://doi.org/10.1145/3018610.3018621
year: 2017
notes:
- ISA specification
- Verified compilers
- CakeML compiler
papers:
---
{% include links.html %}
