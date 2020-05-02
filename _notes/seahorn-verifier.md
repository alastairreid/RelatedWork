---
layout: note
title: SeaHorn verifier
website: https://seahorn.github.io
notes:
- LLVM compiler
- abstract interpretation
papers:
- gurfinkel:cav:2015
---

SeaHorn is a framework and tool for verification of safety properties in C programs.
It uses the [LLVM compiler] as a frontend and verification is based on [abstract
interpretation], constrained Horn clauses and PDR/IC3 based model checking.

{% include links.html %}
