---
ENTRYTYPE: inproceedings
abstract: In this paper, we describe the key principles of a dependent type system for low-level imperative languages. The major contributions of this work
  are (1) a sound type system that combines dependent types and mutation for variables and for heap-allocated structures in a more flexible way than before
  and (2) a technique for automatically inferring dependent types for local variables. We have applied these general principles to design Deputy, a dependent
  type system for C that allows the user to describe bounded pointers and tagged unions. Deputy has been used to annotate and check a number of real-world
  C programs.
added: 2021-06-14
address: Berlin, Heidelberg
authors:
- Jeremy Condit
- Matthew Harren
- Zachary Anderson
- David Gay
- George C. Necula
booktitle: Programming Languages and Systems
editor: De Nicola, Rocco
isbn: 978-3-540-71316-6
layout: paper
pages: 520-535
publisher: Springer Berlin Heidelberg
read: true
readings:
- 2021-06-14
title: Dependent types for low-level programming
year: 2007
notes:
- dependent type
- Cyclone language
papers:
- furr:pldi:2005
---

Deputy is a [dependent type] system for C that allows
programmers to annotate pointers and tagged unions,
infers annotations,
and mostly performs compile-time checks that array/pointer offsets are in bounds
but (to preserve decidability) falls back to run-time checks when necessary.

The type system is flow-insensitive (contrast with [furr:pldi:2005])
and the assignment rule is related to Hoare logic.
Unlike CCured and the [Cyclone language], Deputy does not need fat pointers.

The evaluation looked at 3 SPEC benchmarks, 9 Olden benchmarks, ptrdist
benchmarks, and TinyOS benchmarks and looked at the number of lines changed
(around 2-4% on average and up to 11%) and the runtime overhead (less than 25%
in half the tests but up to 100%).


{% include links.html %}
