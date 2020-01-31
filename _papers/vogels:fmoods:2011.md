---
ENTRYTYPE: inproceedings
abstract: 'With the years, program complexity has increased dramatically: ensuring
  program correctness has become considerably more difficult with the advent of multithreading,
  security has grown more prominent during the last decade, etc. As a result, static
  verification has become more important than ever.'
added: 2020-01-30
address: Berlin, Heidelberg
authors:
- Frédéric Vogels
- Bart Jacobs
- Frank Piessens
- Jan Smans
booktitle: Formal Techniques for Distributed Systems
editor: 'Bruni, Roberto and Dingel, Juergen'
isbn: 978-3-642-21461-5
layout: paper
pages: 319-333
publisher: Springer Berlin Heidelberg
read: true
readings:
- 2020-01-19
title: Annotation inference for separation logic based verifiers
year: 2011
topics:
- verification
---

One of the challenges in automatic program verification
tools such as
[VCC]({{"papers/leinenbach:fm:2009"|relative_url}})
and
[VeriFast](https://github.com/verifast/verifast)
is the amount of annotation required to 
write the specification and 
guide the verification tool to construct a proof.

The VeriFast tool's initial goal was to provide sound,
fast verification for C and Java.
This paper describes three extensions to reduce
the amount of annotation required.
These extensions are implemented outside the small core
and therefore any annotations added cannot cause VeriFast to
produce unsound results.

1. In VeriFast, one often "opens" a predicate
   at the start of a function to expand the predicate's definition
   and "closes" a predicate at the end of a function to trigger proof that
   the predicate holds,
   The first auto-annotations technique is to automatically open/close
   any predicates mentioned in the requires/assumes clauses
   provided the predicates are not recursive.
   The basis for this is a directed graph between predicates
   that mention each other where edges are labelled with side-conditions.

2. In VeriFast, one also explicitly applies lemmas.
   The second auto-annotation aggressively applies lemmas as soon as possible
   (i.e., as soon as they can be triggered) to make all consequences
   available to the prover unless doing so could lead to an exponential
   explosion or would remove facts from the symbolic state.

3. Finally, they perform a shape analysis, which further drives
   open/close, lemma application and also loop invariant generation.


The overall effect of these three inference steps is a dramatic reduction in
the amount of annotation required.  Across eight functions totalling 113 lines
of code, the amount of annotation required drops from 205 lines of annotation
to just 8 lines of annotation.
