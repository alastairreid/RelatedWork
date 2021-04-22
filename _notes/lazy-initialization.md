---
layout: note
notes:
- Java PathFinder
papers:
- khurshid:tacas:2003
- xie:popl:2005
- engler:issta:2007
- calcagno:popl:2009
- ramos:sec:2015
title: Lazy initialization of symbolic values
---

A technique for dealing with code that manipulates pointer data structures.
As the name suggests, instead of constructing an input data structure first and then symbolically
executing the code, the data structure is constructed *on demand*: each dereference of an uninitialized pointer
either constructs a fresh object or chooses one of the previously constructed objects that the pointer
could potentially refer to.

The original version ([khurshid:tacas:2003]) could handle shared data structures and cycles because
it tracked previously initialized objects and allowed the pointer to refer to one of them or to a fresh object.

Later uses of the idea (e.g., [xie:popl:2005], [engler:issta:2007]) always created a fresh object and so
could not reason about shared/cyclic data structures.

{% include links.html %}
