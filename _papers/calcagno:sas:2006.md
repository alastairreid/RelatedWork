---
ENTRYTYPE: inproceedings
abstract: Previous shape analysis algorithms use a memory model where the heap is composed of discrete nodes that can be accessed only via access paths
  built from variables and field names, an assumption that is violated by pointer arithmetic. In this paper we show how this assumption can be removed,
  and pointer arithmetic embraced, by using an analysis based on separation logic. We describe an abstract domain whose elements are certain separation
  logic formulae, and an abstraction mechanism that automatically transits between a low-level RAM view of memory and a higher, fictional, view that abstracts
  from the representation of nodes and multiword linked-lists as certain configurations of the RAM. A widening operator is used to accelerate the analysis.
  We report experimental results obtained from running our analysis on a number of classic algorithms for dynamic memory management.
added: 2021-04-25
address: Berlin, Heidelberg
authors:
- Cristiano Calcagno
- Dino Distefano
- Peter W. O'Hearn
- Hongseok Yang
booktitle: Static Analysis
editor: Yi, Kwangkeun
isbn: 978-3-540-37758-0
layout: paper
pages: 182-203
publisher: Springer Berlin Heidelberg
read: true
readings:
- 2021-04-24
title: 'Beyond reachability: Shape abstraction in the presence of pointer arithmetic'
year: 2006
notes:
- separation logic
- abstract interpretation
papers:
---

This paper combines [separation logic], [abstract interpretation] and some
custom abstract domains/transformations to show how separation logic can be
used to automatically verify low-level memory manipulation code of the
kind found in memory allocators.

They describe the verification of seven allocators (3 pairs of malloc-free
implementations plus another) that use acyclic or cyclic free lists and that
do/don't coalesce adjacent free blocks.
Their tools runs in time varying from a small fraction of a second to 9 minutes
(for "malloc_K&R").

The technique revolves around abstract interpretation using 

- a carefully chosen subset of separation logic terms as an abstract domain
  extended with predicates for describing the kinds of memory shapes
  found in memory allocators

- an abstraction function that is specifically designed to handle
  1. the type of memory shapes found in memory allocators (i.e., blocks of
     memory with all the metadata in the first few words)
  2. the types of reasoning found in memory allocators (i.e., merging
     adjacent blocks of memory and splitting large blocks of memory)

- a magic constant "n" (chosen as 4 in this paper) that captures the
  maximum offset in objects that they need to reason about

The core of the paper is really about going back and forth between
separation logic, logical reasoning, etc. and abstract interpretation,
widening operators, etc.: choosing particular representations
or abstraction operators based on the impact on abstract interpretation
and justifying / relating that choice to separation logic reasoning steps.

*[Aside: I saw a talk by Josh Berdine (a frequent collaborator with the paper
authors) at POPL 2020 about a new separation logic based tool where he moved continuously
between the two modes.  IIRC, every slide contained separation logic judgements
but most of the words he uttered were about this operational,
abstract-interpretation-based interpretation of the logic.]*

Although the choice of abstract domains, etc. enables automatic reasoning
about the programs of interest, it is not clear how well the particular choices
that they make would work on other code.
It seems that this is a demonstration of the *potential* of this combination
of spatial reasoning and abstract interpretation rather than a
general purpose tool.
(See [calcagno:popl:2009] for a somewhat more general tool that
builds on what was learned in this and other papers from the time.)


{% include links.html %}
