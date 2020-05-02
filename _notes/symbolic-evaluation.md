---
layout: note
title: Symbolic evaluation
wiki: https://en.wikipedia.org/wiki/Symbolic_execution
notes:
- bounded model checking
- symbolic execution
papers:
- nelson:sosp:2019
- bornholt:oopsla:2018
---

Following the terminology in section 3.1 of 
[bornholt:oopsla:2018], "symbolic evaluation" is a generalization
of [bounded model checking][bounded model checking] consisting of exploring some paths
through a program collecting symbolic path constraints from conditional
branches.

In [symbolic execution][symbolic execution], a single path is followed at a time which has the
advantage that states do not need to be merged at join points
and so many calculations involve concrete values and so can be
evaluated directly and efficiently.

In [bounded model checking][bounded model checking], all paths are followed at a time
so states have to be merged at join points resulting in many symbolic
values but, with the advantage that it avoids the path explosion
problem seen in [symbolic execution][symbolic execution].

{% include links.html %}
