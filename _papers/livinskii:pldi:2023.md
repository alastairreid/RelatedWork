---
ENTRYTYPE: article
abstract: Compilers are part of the foundation upon which software systems are built; they need to be as correct as possible. This paper is about stress-testing
  loop optimizers; it presents a major reimplementation of Yet Another Random Program Generator (YARPGen), an open-source generative compiler fuzzer. This
  new version has found 122 bugs, both in compilers for data-parallel languages, such as the Intel\textregistered  Implicit SPMD Program Compiler and the
  Intel\textregistered  oneAPI DPC++ compiler, and in C++ compilers such as GCC and Clang/LLVM. The first main contribution of our work is a novel method
  for statically avoiding undefined behavior when generating loops; the resulting programs conform to the relevant language standard, enabling automated
  testing. The second main contribution is a collection of mechanisms for increasing the diversity of generated loop code; in our evaluation, we demonstrate
  that these make it possible to trigger loop optimizations significantly more often, providing opportunities to discover bugs in the optimizers.
added: 2023-07-02
address: New York, NY, USA
articleno: '181'
authors:
- Vsevolod Livinskii
- Dmitry Babokin
- John Regehr
doi: 10.1145/3591295
issue_date: June 2023
journal: Proc. ACM Program. Lang.
keywords: compiler defect, automated testing, random testing, random program generation, YARPGen, compiler testing
layout: paper
link: https://doi.org/10.1145/3591295
month: jun
number: PLDI
numpages: '22'
publisher: Association for Computing Machinery
read: false
readings: []
title: Fuzzing loop optimizations in compilers for C++ and data-parallel languages
url: https://doi.org/10.1145/3591295
volume: '7'
year: 2023
notes:
- fuzz testing
- loop fusion
papers:
---

Fuzzing is an effective way of finding compiler bugs but it has been
hard to use them to find bugs in complex optimization passes such
as loop optimizations because these optimizations only trigger
in particular circumstances that random programs rarely satisfy.

This paper avoids these problems by identifying a number of common
templates that will trigger loop optimizations and generating
loops using these templates.
As usual when fuzzing compilers, a key part is avoiding generating
programs with undefined behavior.

Using this, they found 122 bugs in compilers.

{% include links.html %}
