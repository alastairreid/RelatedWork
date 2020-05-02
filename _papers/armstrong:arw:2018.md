---
ENTRYTYPE: article
abstract: Processor instruction set architectures (ISAs) are typically specified using a mixture of prose and pseudocode. We present ongoing work on expressing
  such specifications rigorously and automatically trans- lating them to interactive theorem prover definitions, making them amenable to mechanised proof.
  Our ISA descriptions are written in Sail-a custom ISA specification language designed to support idioms from var- ious processor vendor's pseudocode,
  with lightweight dependent typing for bitvectors, targeting a variety of use cases including sequential and concurrent ISA semantics. From Sail we aim
  to portably generate usable theorem prover definitions for multiple provers, including Isabelle, HOL4, and Coq. We are focusing on the full ARMv8.3-A
  specification, CHERI-MIPS, and RISC-V, together with fragments of IBM POWER and x86.
added: 2019-06-01
ar_shortname: ARW 18
authors:
- Alasdair Armstrong
- Thomas Bauereiss
- Brian Campbell
- Shaked Flur
- Kathryn E. Gray
- Prashanth Mundkur
- Robert Norton
- Christopher Pulte
- Alastair Reid
- Peter Sewell
- Ian Stark
- Mark Wassell
booktitle: Automated Reasoning Workshop 2018
layout: paper
location: Cambridge, UK
month: April
read: false
readings: []
title: 'Detailed models of instruction set architectures: From pseudocode to formal semantics'
year: 2018
topics:
notes:
- arm-architecture
- isa-specification
- instruction-set-architecture
- dependent-type
---
