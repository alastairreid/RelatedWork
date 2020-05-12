---
layout: note
title: Bounded model-checking
notes:
- bounded verification
- model checking
- symbolic execution
- symbolic evaluation
papers:
- nelson:sosp:2019
- bornholt:oopsla:2018
- jhala:compsurv:2009
---

Bounded model checking is a variant of [model checking].

Following the terminology in section 3.1 of 
[bornholt:oopsla:2018], bounded model-checking is a form of
[symbolic evaluation] where all paths are followed at a time.

The benefit of following all paths at once is that it avoids the path explosion
problem seen in [symbolic execution].

The disadvantage of following all paths at once is that this
requires that states are merged at join points so many calculations
involve symbolic values requiring the use of a solver to resolve.

{% include links.html %}
