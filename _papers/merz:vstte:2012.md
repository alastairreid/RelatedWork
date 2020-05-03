---
ENTRYTYPE: inproceedings
abstract: Bounded model checking (BMC) of C and C++ programs is challenging due to
  the complex and intricate syntax and semantics of these programming languages. The
  BMC tool LLBMC presented in this paper thus uses the LLVM compiler framework in
  order to translate C and C++ programs into LLVM\textquotesingle s intermediate representation.
  The resulting code is then converted into a logical representation and simplified
  using rewrite rules. The simplified formula is finally passed to an SMT solver.
  In contrast to many other tools, LLBMC uses a flat, bit-precise memory model. It
  can thus precisely model, e.g., memory-based re-interpret casts as used in C and
  static/dynamic casts as used in C++. An empirical evaluation shows that LLBMC compares
  favorable to the related BMC tools CBMC and ESBMC.
added: 2020-01-15
address: Berlin, Heidelberg
authors:
- Florian Merz
- Stephan Falke
- Carsten Sinz
booktitle: 'Verified Software: Theories, Tools, Experiments'
editor: 'Joshi, Rajeev and Müller, Peter and Podelski, Andreas'
isbn: 978-3-642-27705-4
layout: paper
pages: 146-161
publisher: Springer Berlin Heidelberg
read: false
readings: []
title: 'LLBMC: Bounded model checking of C and C++ programs using a compiler IR'
year: 2012
topics:
- tools
- verification
notes:
- LLVM compiler
- bounded model checking
papers:
---

{% include links.html %}
