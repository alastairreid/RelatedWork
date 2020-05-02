---
layout: note
title: Symbolic execution
wiki: https://en.wikipedia.org/wiki/Symbolic_execution
notes:
- bounded model checking
- symbolic evaluation
- symbolic execution
papers:
- nelson:sosp:2019
- bornholt:oopsla:2018
---

Following the terminology in section 3.1 of 
[bornholt:oopsla:2018], [symbolic execution] is a form of
[symbolic evaluation] where a single path is followed at a time.

Following a single path has the advantage that states do not need to be merged
at join points and so many calculations involve concrete values and so can be
evaluated directly and efficiently.  The price paid for this advantage is that
there can be an exponential number of paths.

See also [bounded model checking] and [symbolic evaluation].

<https://en.wikipedia.org/wiki/Concolic_testing>

{% include links.html %}
