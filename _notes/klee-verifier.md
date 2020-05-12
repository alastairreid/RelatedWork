---
layout: note
title: KLEE verifier
logo: https://klee.github.io/images/klee.svg
website: https://klee.github.io
notes:
- LLVM compiler
- symbolic execution
papers:
- lindner:indin:2018
- lindner:indin:2019
---

KLEE is a symbolic virtual machine built on top of the [LLVM compiler].  KLEE
uses [symbolic execution] to generate tests by constructing the "path
conditions" associated with paths through the program and, for each path, using
a constraint solver to solve those conditions to generate inputs that would
cause the program to follow that path.

{% include links.html %}
