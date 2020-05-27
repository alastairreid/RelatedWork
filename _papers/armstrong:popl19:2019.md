---
ENTRYTYPE: inproceedings
abstract: 'Architecture specifications notionally define the fundamental interface between hardware and software: the envelope of allowed behaviour for
  processor implementations, and the basic assumptions for software development and verification.  But in practice, they are typically prose and pseudocode
  documents, not rigorous or executable artifacts, leaving software and verification on shaky ground.  In this paper, we present rigorous semantic models
  for the sequential behaviour of large parts of the mainstream ARMv8-A, RISC-V, and MIPS architectures, and the research CHERI-MIPS architecture, that
  are complete enough to boot operating systems, variously Linux, FreeBSD, or seL4.  Our ARMv8-A models are automatically translated from authoritative
  ARM-internal definitions, and (in one variant) tested against the ARM Architecture Validation Suite.  We do this using a custom language for ISA semantics,
  Sail, with a lightweight dependent type system, that supports automatic generation of emulator code in C and OCaml, and automatic generation of proof-assistant
  definitions for Isabelle, HOL4, and (currently only for MIPS) Coq.  We use the former for validation, and to assess specification coverage.  To demonstrate
  the usability of the latter, we prove (in Isabelle) correctness of a purely functional characterisation of ARMv8-A address translation.  We moreover integrate
  the RISC-V model into the RMEM tool for (user-mode) relaxed-memory concurrency exploration.  We prove (on paper) the soundness of the core Sail type system.  We
  thereby take a big step towards making the architectural abstraction actually well-defined, establishing foundations for verification and reasoning.'
added: 2019-06-01
address: New York, NY, USA
ar_shortname: POPL 19
authors:
- Alasdair Armstrong
- Thomas Bauereiss
- Brian Campbell
- Alastair D. Reid
- Kathryn E. Gray
- Robert M. Norton
- Prashanth Mundkur
- Mark Wassell
- Jon French
- Christopher Pulte
- Shaked Flur
- Ian Stark
- Neel R. Krishnaswami
- Peter Sewell
booktitle: Proc. 46th ACM SIGPLAN Symposium on Principles of Programming Languages
day: 13-19
doi: 10.1145/3290384
journal: PACMPL
layout: paper
location: Cascais/Lisbon, Portugal
month: January
number: POPL
numpages: '31'
pages: 71:1-71:31
publisher: ACM
read: false
readings: []
title: ISA semantics for ARMv8-A, RISC-V, and CHERI-MIPS
volume: '3'
year: 2019
topics:
notes:
- Arm architecture
- RISCV architecture
- CHERI architecture
- MIPS architecture
- ISA specification
- instruction set architecture
- dependent type
- ASL
- SAIL language
papers:
---

{% include links.html %}
