---
ENTRYTYPE: inproceedings
added: 2019-11-18
authors:
- Jonas Wagner
- Volodymyr Kuznetsov
- George Candea
booktitle: '14th Workshop on Hot Topics in Operating Systems'
layout: paper
read: true
readings:
- 2019-11-18
title: '-Overify: Optimizing programs for fast verification'
year: 2013
topics:
- tools
- verification
---

This paper explores the benefit of using different optimization options (or
even custom transformations) when compiling a program for optimization.
Their optimization options are over 5000x better than -O0 and 14x better than -O3
for verification using KLEE on their motivating example.
Compared with -O3, their main goal is to reduce the amount of information lost
during compilation.
They mention but do little to address the problem of undefined behaviour in C
causing different compilations to behave differently although they
did look for this in their evaluation and found that
they detected the same bugs with -O0, -O3 and -Overify.

The paper identifies transformations that have a positive or negative effect on verification.
Optimizations discussed are:

- unswitching loops
- loop unrolling
- function inlining
- copy propagation
- constant folding
- allocating variables in registers
- splitting large objects
- preserving information from the compiler: alias information, variable ranges, loop invariants, trip counts, type information
- inserting runtime checks
- using a simplified library (as KLEE already does).

And optimizations that make verification worse are CPU specific optimizations, cache optimizations, padding objects.

One of the payoffs from reading this paper is that I had naïvely expected that
the -O0 version would be easier to verify than the -O2 or -O3 version.  At
least when using KLEE, this is not true.
