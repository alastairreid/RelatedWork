---
ENTRYTYPE: inproceedings
abstract: 'In this paper, we present a combination of existing and new tools that together make it possible to apply formal verification methods to programs
  in the form of \texttimes 86_64 machine code. Our approach first uses a decompilation tool (remill) to extract low-level intermediate representation (LLVM)
  from the machine code. This step consists of instruction translation (i.e. recovery of operation semantics), control flow extraction and address identification.The
  main contribution of this paper is the second step, which builds on data flow analysis and refinement of indirect (i.e. data-dependent) control flow.
  This step makes the processed bitcode much more amenable to formal analysis.To demonstrate the viability of our approach, we have compiled a set of benchmark
  programs into native executables and analysed them using two LLVM-based tools: DIVINE, a software model checker and KLEE, a symbolic execution engine.
  We have compared the outcomes to direct analysis of the same programs.'
added: 2021-06-14
authors:
- Lukáš Korenčik
- Petr Ročkai
- Henrich Lauko
- Jiří Barnat
booktitle: 2020 IEEE 20th International Conference on Software Quality, Reliability and Security (QRS)
doi: 10.1109/QRS51102.2020.00044
issn: ''
keywords: ''
layout: paper
month: Dec
number: ''
pages: 265-272
read: false
readings: []
title: On symbolic execution of decompiled programs
volume: ''
year: 2020
notes:
- symbolic execution
papers:
---
{% include links.html %}
