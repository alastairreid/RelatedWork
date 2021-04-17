---
ENTRYTYPE: inproceedings
abstract: 'Verifying code equivalence is useful in many situations, such as checking: yesterday''s code against today''s, different implementations of the
  same (standardized) interface, or an optimized routine against a reference implementation. We present a tool designed to easily check the equivalence
  of two arbitrary C functions. The tool provides guarantees far beyond those possible with testing, yet it often requires less work than writing even a
  single test case. It automatically synthesizes inputs to the routines and uses bit-accurate, sound symbolic execution to verify that they produce equivalent
  outputs on a finite number of paths, even for rich, nested data structures. We show that the approach works well, even on heavily-tested code, where it
  finds interesting errors and gets high statement coverage, often exhausting all feasible paths for a given input size. We also show how the simple trick
  of checking equivalence of identical code turns the verification tool chain against itself, finding errors in the underlying compiler and verification
  tool.'
added: 2021-04-17
address: Berlin, Heidelberg
authors:
- David A Ramos
- Dawson R. Engler
booktitle: Proceedings of the 23rd International Conference on Computer Aided Verification
isbn: '9783642221095'
layout: paper
location: Snowbird, UT
numpages: '17'
pages: 669-685
publisher: Springer-Verlag
read: false
readings: []
series: CAV'11
title: Practical, low-effort equivalence verification of real code
year: 2011
notes:
papers:
---
{% include links.html %}
