---
ENTRYTYPE: inproceedings
abstract: Validating the correctness of binary lifters is pivotal to gain trust in binary analysis, especially when used in scenarios where correctness
  is important. Existing approaches focus on validating the correctness of lifting instructions or basic blocks in isolation and do not scale to full programs.
  In this work, we show that formal translation validation of single instructions for a complex ISA like x86-64 is not only practical, but can be used as
  a building block for scalable full-program validation. Our work is the first to do translation validation of single instructions on an architecture as
  extensive as x86-64, uses the most precise formal semantics available, and has the widest coverage in terms of the number of instructions tested for correctness.
  Next, we develop a novel technique that uses validated instructions to enable program-level validation, without resorting to performance-heavy semantic
  equivalence checking. Specifically, we compose the validated IR sequences using a tool we develop called Compositional Lifter to create a reference standard.
  The semantic equivalence check between the reference and the lifter output is then reduced to a graph-isomorphism check through the use of semantic preserving
  transformations. The translation validation of instructions in isolation revealed 29 new bugs in McSema - a mature open-source lifter from x86-64 to LLVM
  IR. Towards the validation of full programs, our approach was able to prove the translational correctness of 2254/2348 functions taken from LLVM's single-source
  benchmark test-suite.
added: 2021-11-05
address: New York, NY, USA
authors:
- Sandeep Dasgupta
- Sushant Dinesh
- Deepan Venkatesh
- Vikram S. Adve
- Christopher W. Fletcher
booktitle: Proceedings of the 41st ACM SIGPLAN Conference on Programming Language Design and Implementation
doi: 10.1145/3385412.3385964
isbn: '9781450376136'
keywords: Formal Semantics, Compiler Optimizations, LLVM IR, Translation Validation, Graph Isomorphism, x86-64
layout: paper
link: https://doi.org/10.1145/3385412.3385964
location: London, UK
numpages: '17'
pages: 655-671
publisher: Association for Computing Machinery
read: false
readings: []
series: PLDI 2020
title: Scalable validation of binary lifters
url: https://doi.org/10.1145/3385412.3385964
year: 2020
notes:
- ISA specification
- binary analysis
- binary lifter
- McSema tool
- Remill library
papers:
---
{% include links.html %}
