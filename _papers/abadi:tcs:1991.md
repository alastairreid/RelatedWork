---
ENTRYTYPE: article
added: 2019-11-02
authors:
- Martín Abadi
- Leslie Lamport
doi: 10.1016/0304-3975(91)90224-P
journal: Theoretical Computer Science
layout: paper
number: '2'
pages: 253-284
publisher: Elsevier
read: true
readings:
- 2019-10-21
title: The existence of refinement mappings
volume: '82'
year: 1991
topics:
- verification
papers:
---

Theoretical paper justifying the practice of adding auxiliary variables (ghost
state) to an implementation to enable refinement proof by providing
a completeness proof that a refinement mapping from an implementation S1 to
a specification S2 exists if S1 refines S2 and three conditions hold
- S1 is "machine closed",
- S2 has "finite invisible nondeterminism", and
- S2 is "internally continuous".

A refinement mapping is a function from the implementation state (including
auxiliary variables) to the specification state.
The auxiliary variables can be either "history variables" or "prophecy
variables".

{% include links.html %}
