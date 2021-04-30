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
read: true
readings:
- 2021-04-30
series: CAV'11
title: Practical, low-effort equivalence verification of real code
year: 2011
notes:
- lazy initialization
- symbolic execution
- symbolic memory
- differential testing
- KLEE verifier
papers:
- engler:issta:2007
- ramos:sec:2015
- person:fse:2008
- khurshid:tacas:2003
- xie:popl:2005
- calcagno:popl:2009
- yang:pldi:2011
---

Performs [differential testing] using the [KLEE][KLEE verifier] [symbolic execution] tool
extended with [symbolic memory] and [lazy initialization] to enable under-constrained symbolic execution (see [ramos:sec:2015]).

They demonstrate that differential symbolic execution (see [person:fse:2008]) can be used to compare
different implementations of the same library API (NewLib vs. ucLibC),
different versions of the same library (ucLibC),
different compiler optimization levels (cf. [yang:pldi:2011]),
and to find bugs in the tool itself.

In addition to (the substantial tasks of) adding [symbolic memory] and [lazy initialization] to KLEE, the main change
was extending the KLEE API with the ability

- to take a snapshot of the address space;
- to restore the address space;
- to explicitly invoke the KLEE evaluator on a statement capturing any errors (I think this includes errors like
division by zero or null pointer dereference);
- to compare errors; and
- to compare objects in memory.

Comparing objects in memory is challenging because the objects may have been allocated in different
orders, at different addresses, etc.
A mark-sweep algorithm is used to compare the structure of the heap rather than the concrete addresses.

As in their later work ([ramos:sec:2015]) but unlike the original lazy initialization work ([khurshid:tacas:2003]),
the lazy initialization implementation does not explore object sharing so doubly linked lists or overlapping arguments
to memcpy would not be explored.

Determining the size of objects is also hard: when an array of unknown size is generated, they initially
guess a size of 8 and then keep doubling it if that fails.

They cap the number of objects allocated by lazy initialization.

Their evaluation showed that this was very effective at finding bugs and differences.

{% include links.html %}
