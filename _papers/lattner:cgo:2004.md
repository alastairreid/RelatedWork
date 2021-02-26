---
ENTRYTYPE: inproceedings
abstract: 'We describe LLVM (low level virtual machine), a compiler framework designed to support transparent, lifelong program analysis and transformation
  for arbitrary programs, by providing high-level information to compiler transformations at compile-time, link-time, run-time, and in idle time between
  runs. LLVM defines a common, low-level code representation in static single assignment (SSA) form, with several novel features: a simple, language-independent
  type-system that exposes the primitives commonly used to implement high-level language features; an instruction for typed address arithmetic; and a simple
  mechanism that can be used to implement the exception handling features of high-level languages (and setjmp/longjmp in C) uniformly and efficiently. The
  LLVM compiler framework and code representation together provide a combination of key capabilities that are important for practical, lifelong analysis
  and transformation of programs. To our knowledge, no existing compilation approach provides all these capabilities. We describe the design of the LLVM
  representation and compiler framework, and evaluate the design in three ways: (a) the size and effectiveness of the representation, including the type
  information it provides; (b) compiler performance for several interprocedural problems; and (c) illustrative examples of the benefits LLVM provides for
  several challenging compiler problems.'
added: 2020-11-01
authors:
- Chris Lattner
- Vikram Adve
booktitle: International Symposium on Code Generation and Optimization, 2004. CGO 2004.
doi: 10.1109/CGO.2004.1281665
issn: ''
keywords: program diagnostics;virtual machines;C language;exception handling;optimising compilers;program analysis;program transformation;low level virtual
  machine;compiler framework;compiler transformations;code representation;static single assignment form;language-independent type-system;typed address arithmetic;exception
  handling;compiler performance;Information analysis;Program processors;Performance analysis;High level languages;Virtual machining;Runtime;Arithmetic;Application
  software;Software safety;Algorithm design and analysis
layout: paper
month: March
number: ''
pages: 75-86
read: false
readings: []
title: 'LLVM: a compilation framework for lifelong program analysis and transformation'
volume: ''
year: 2004
notes:
- LLVM compiler
papers:
---
{% include links.html %}
