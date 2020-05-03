---
ENTRYTYPE: inproceedings
added: 2020-02-14
address: New York, NY, USA
authors:
- Neel R. Krishnaswami
- Lars Birkedal
- Jonathan Aldrich
booktitle: Proceedings of the 5th ACM SIGPLAN Workshop on Types in Language Design
  and Implementation
doi: 10.1145/1708016.1708025
isbn: '9781605588919'
keywords: frame rule, functional reactive programming, ramification problem, separation
  logic, dataflow, subject-observer
layout: paper
location: Madrid, Spain
numpages: '14'
pages: 63-76
publisher: Association for Computing Machinery
read: true
readings:
- 2020-02-18
series: TLDI '10
title: Verifying event-driven programs using ramified frame properties
url: https://doi.org/10.1145/1708016.1708025
year: 2010
topics:
- verification
notes:
- permission-logic
- separation-logic
- frame-rule
- magic-wand
papers:
---

Separation logic's strength is that it let's you reason locally
about heap-manipulating programs by letting you split the
heap into disjoint parts.
But some data structures don't easily split into parts
and you have to maintain global consistency properties
across the structure because they "use mutation
and assignment as a way of globally broadcasting information
to the rest of the program state."
This paper tackles an example of such a structure:
an instance of the subject-observer pattern like that 
found in a spreadsheet where
each node contains a list of the nodes it depends on
and also of the nodes that depend on it
so that, when a node changes value, nodes that depend on it
can be invalidated/updated.

The approach taken in this paper has many parts

1. Push the "frame rule" of separation logic into each inference
   rule by making all rules universally quantified over possible
   extensions of the heap.
   
2. Define a small domain-specific separation logic specifically
   for reasoning about cell networks.
   
3. The big problem is that a change in one part of the heap
   can change the interpretation of other parts of the heap.
   To tackle this, they define a "ramification operator" that
   transforms the rest of the heap to match that change in
   interpretation.
   (This operator is specific to cell networks.)
   
This approach is then applied to the task of verifying
an imperative implementation of Functional Reactive
Programming by reasoning about an (inefficient)
pure implementation of causal stream transducers
and an imperative implementation based on cell networks.
   

   
   

   {% include links.html %}
