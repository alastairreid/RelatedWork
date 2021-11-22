---
ENTRYTYPE: article
abstract: 'In this article, we consider the semantic design and verified compilation of a C-like programming language for concurrent shared-memory computation
  on x86 multiprocessors. The design of such a language is made surprisingly subtle by several factors: the relaxed-memory behavior of the hardware, the
  effects of compiler optimization on concurrent code, the need to support high-performance concurrent algorithms, and the desire for a reasonably simple
  programming model. In turn, this complexity makes verified compilation both essential and challenging.We describe ClightTSO, a concurrent extension of
  CompCert''s Clight in which the TSO-based memory model of x86 multiprocessors is exposed for high-performance code, and CompCertTSO, a formally verified
  compiler from ClightTSO to x86 assembly language, building on CompCert. CompCertTSO is verified in Coq: for any well-behaved and successfully compiled
  ClightTSO source program, any permitted observable behavior of the generated assembly code (if it does not run out of memory) is also possible in the
  source semantics. We also describe some verified fence-elimination optimizations, integrated into CompCertTSO.'
added: 2021-11-22
address: New York, NY, USA
articleno: '22'
authors:
- Jaroslav Ševčík
- Viktor Vafeiadis
- Francesco Zappa Nardelli
- Suresh Jagannathan
- Peter Sewell
doi: 10.1145/2487241.2487248
issn: 0004-5411
issue_date: June 2013
journal: J. ACM
keywords: semantics, verified compilation, Relaxed memory models
layout: paper
link: https://doi.org/10.1145/2487241.2487248
month: jun
number: '3'
numpages: '50'
publisher: Association for Computing Machinery
read: false
readings: []
title: 'CompCertTSO: A verified compiler for relaxed-memory concurrency'
url: https://doi.org/10.1145/2487241.2487248
volume: '60'
year: 2013
notes:
- verified compilers
- weak memory
- ISA specification
- TSO
- CompCert compiler
papers:
---
{% include links.html %}
