---
ENTRYTYPE: inproceedings
abstract: 'Separation logic is a program logic for reasoning about programs that manipulate
  pointer data structures. We describe Smallfoot, a tool for checking certain lightweight
  separation logic specifications. The assertions describe the shapes of data structures
  rather than their detailed contents, and this allows reasoning to be fully automatic.
  The presentation in the paper is tutorial in style. We illustrate what the tool
  can do via examples which are oriented toward novel aspects of separation logic,
  namely: avoidance of frame axioms (which say what a procedure does not change);
  embracement of \textasciigrave \textasciigrave dirty\textquotesingle \textquotesingle  features
  such as memory disposal and address arithmetic; information hiding in the presence
  of pointers; and modular reasoning about concurrent programs.'
added: 2020-01-28
address: Berlin, Heidelberg
authors:
- Josh Berdine
- Cristiano Calcagno
- Peter W. O'Hearn
booktitle: Formal Methods for Components and Objects
editor: 'de Boer, Frank S.
  and Bonsangue, Marcello M.
  and Graf, Susanne
  and de Roever, Willem-Paul'
isbn: 978-3-540-36750-5
layout: paper
pages: 115-137
publisher: Springer Berlin Heidelberg
read: true
readings:
- 2020-02-15
title: 'Smallfoot: Modular automatic assertion checking with separation logic'
year: 2006
topics:
- tools
- verification
notes:
- separation logic
- permission logic
- smallfoot verifier
- symbolic execution
- VeriFast verifier
papers:
- berdine:aplas:2005
- jacobs:nfm:2011
- parkinson:popl:2005
- bornat:popl:2005
---

Smallfoot is a tool for automatically verifying both sequential
and concurrent heap-manipulating programs
that is based on (concurrent) separation logic and symbolic
execution.
The proof theoretic foundations of the tool are described
in a
[companion paper][berdine:aplas:2005].

One of the key tricks in enabling automation is to greatly
simplify the expressive power of the logic so that the
symbolic state consists of a set of pure formulae
about non-heap values plus a list of spatial formulae
that describe the heap.

The paper explicitly avoids describing how conditionals are handled but,
I believe that it works like the later
[VeriFast][jacobs:nfm:2011]
by path splitting: separately exploring the path that
starts with the "then" branch and the path that starts with the "else" branch.
This seems to be necessary because there is no mention of what to do at join
points and because there seems to be no way to represent disjunctions of
spatial formulae.

The version of Smallfoot described here did not have support for

- [defining predicates][parkinson:popl:2005].
  Instead predicates for lists, trees and xor-lists were hardwired in the tool.
- [permission accounting][bornat:popl:2005]

And there seems to be no arithmetic in the examples so I suspect
that it was not using an SMT solver in the background.

{% include links.html %}
