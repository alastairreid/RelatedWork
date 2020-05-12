---
ENTRYTYPE: inproceedings
added: 2020-02-14
authors:
- M. Lindner
- J. Aparicius
- P. Lindgren
booktitle: 2018 IEEE 16th International Conference on Industrial Informatics (INDIN)
doi: 10.1109/INDIN.2018.8471992
issn: 2378-363X
keywords: object-oriented programming;program compilers;program diagnostics;program
  verification;Rust programs;Rust language;type system;memory safety;safety conditions;raw
  array indexing;static analysis;runtime verification;partial correctness guarantees;safety
  violations;safety-critical applications;static program analysis;generic contract
  based verification process;KLEE symbolic execution engine;memory model;rustc compiler;panic
  handling;Safety;Runtime;Contracts;Program processors;Engines;Testing;Data models
layout: paper
month: July
number: ''
pages: 108-114
read: true
readings:
- 2020-05-12
title: No panic! Verification of Rust programs by symbolic execution
volume: ''
year: 2018
topics:
- tools
- verification
notes:
- Rust language
- symbolic execution
- extended static checking
- contract driven development
- modular verification
- KLEE verifier
papers:
- lindner:indin:2019
---

This paper describes the `cargo-Rust` that allows the [KLEE verifier]
to be used to verify Rust programs.
KLEE is a [symbolic execution] tool so using it to verify code leads
to a path explosion problem.
The solution taken in this paper is to use a [contract driven development]
approach to enable [modular verification].
This reduces the path explosion problem to only involve the number of
paths per function instead of the number of paths through the entire
program.

Two related approaches that are mentioned are the
[KLEE Rust crate]
and the
[Symbolic Execution Engine for Rust (SEER)][SEER].

[KLEE Rust crate]: https://github.com/jawline/klee-rust
[SEER]: https://github.com/dwrensha/seer

{% include links.html %}
