---
ENTRYTYPE: article
added: 2019-12-10
authors:
- Ernie Cohen
- Michał Moskal
- Stephan Tobies
- Wolfram Schulte
doi: 10.1016/j.entcs.2009.09.061
journal: Electronic Notes in Theoretical Computer Science
layout: paper
pages: 85-103
publisher: Elsevier
read: true
readings:
- 2019-12-10
title: A precise yet efficient memory model for C
volume: '254'
year: 2009
topics:
- tools
- verification
notes:
- VCC verifier
papers:
- cohen:cav:2010
---

A memory model (in this context) is basically "what is a pointer"?
Is a pointer an identifier for an object or an integer index into an array of bytes?
How do you handle fields of objects?
How do you handle pointer arithmetic?
etc.
After some experimentation (described in a lovely historical note in section 7), the authors came up with a model
that can handle many of the awkward features of C:
pointers into the middle of objects,
pointers past the end of objects,
pointer casts,
unions,
bitfields,
etc.
This formed part of the [VCC tool][cohen:cav:2010] that was used to reason about
real, complex OS-level code (that needed many of these features).

Most of the model is what you would expect (pointers, fields, casts, etc.).
The core of the model though is the addition of two operations "join" and "split".
"join" combines a sequence of memory bytes into an object of some type (e.g., an int, a struct or an array);
and "split" converts an object with some type back into the corresponding sequence of bytes.
"Join" might be used when an object is allocated while "split" might be used when accessing a different union field than last time.

An important part of this paper is the set of SMT axioms that are used to turn this model into an effective reasoning tool.

{% include links.html %}
