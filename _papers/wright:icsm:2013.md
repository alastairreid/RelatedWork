---
ENTRYTYPE: inproceedings
added: 2020-09-10
authors:
- Hyrum K. Wright
- Daniel Jasper
- Manuel Klimek
- Chandler Carruth
- Zhanyong Wan
booktitle: 2013 IEEE International Conference on Software Maintenance
doi: 10.1109/ICSM.2013.93
issn: 1063-6773
keywords: application program interfaces;C++ language;parallel programming;program compilers;software maintenance;large-scale automated refactoring;ClangMR;large
  C++ codebases;Clang compiler framework;MapReduce parallel processor;API update;Google;Google;Indexes;Standards;Semantics;Conferences;Transforms;Software
  systems
layout: paper
month: Sep.
number: ''
pages: 548-551
read: true
readings:
- 2020-09-21
title: Large-scale automated refactoring using ClangMR
volume: ''
year: 2013
notes:
- google
papers:
- potvin:cacm:2016
---

ClangMR is a refactoring tool that scales to systems of the size of
Google's monorepo ([potvin:cacm:2016]).
It consists of three phases:

1. Collect a list of all the commands needed to compile code in the entire
   repo.

2. Compile using a modified compiler that stores the AST in memory (of many
   machines running in parallel).

   > it is roughly as fast to compile C++ code into a memory-held AST as it is
   > to read a completely annotated AST out of distant storage

3. Apply transformation rules based on AST pattern matching and substitutions.

Transformations are limited to changes within the same translation units.

The paper gives an example of a transformation that changed calls to an old,
error-prone string splitting API into calls to a better API.
The transformation was able to take advantage of constant arguments, etc.
in the old code to produce a better/cleaner output.

{% include links.html %}
