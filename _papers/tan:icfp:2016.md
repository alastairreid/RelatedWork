---
ENTRYTYPE: inproceedings
abstract: 'We have developed and mechanically verified a new compiler backend for CakeML. Our new compiler features a sequence of intermediate languages
  that allows it to incrementally compile away high-level features and enables verification at the right levels of semantic detail. In this way, it resembles
  mainstream (unverified) compilers for strict functional languages. The compiler supports efficient curried multi-argument functions, configurable data
  representations, exceptions that unwind the call stack, register allocation, and more. The compiler targets several architectures: x86-64, ARMv6, ARMv8,
  MIPS-64, and RISC-V. In this paper, we present the overall structure of the compiler, including its 12 intermediate languages, and explain how everything
  fits together. We focus particularly on the interaction between the verification of the register allocator and the garbage collector, and memory representations.
  The entire development has been carried out within the HOL4 theorem prover.'
added: 2021-11-22
address: New York, NY, USA
authors:
- Yong Kiam Tan
- Magnus O. Myreen
- Ramana Kumar
- Anthony Fox
- Scott Owens
- Michael Norrish
booktitle: Proceedings of the 21st ACM SIGPLAN International Conference on Functional Programming
doi: 10.1145/2951913.2951924
isbn: '9781450342193'
keywords: verified optimisations, Compiler verification, ML
layout: paper
link: https://doi.org/10.1145/2951913.2951924
location: Nara, Japan
numpages: '14'
pages: 60-73
publisher: Association for Computing Machinery
read: false
readings: []
series: ICFP 2016
title: A new verified compiler backend for CakeML
url: https://doi.org/10.1145/2951913.2951924
year: 2016
notes:
- ISA specification
- Verified compilers
- CakeML compiler
- x86 architecture
- Arm architecture
- RISCV architecture
- MIPS architecture
papers:
---
{% include links.html %}
