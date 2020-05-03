---
ENTRYTYPE: inbook
abstract: This paper argues that specified blocks have every advantage over the combination
  of assertions, preconditions, postconditions, invariants, and variants, both for
  verifying programs, and for program development. They are simpler, more general,
  easier to write, and they make proofs easier.
added: 2020-02-22
address: Berlin, Heidelberg
authors:
- Eric C. R. Hehner
booktitle: 'Verified Software: Theories, Tools, Experiments: First IFIP TC 2/WG 2.3 Conference, VSTTE 2005, Zurich, Switzerland, October 10-13, 2005, Revised Selected Papers and Discussions'
doi: 10.1007/978-3-540-69149-5\_41
editor: 'Meyer, Bertrand and Woodcock, Jim'
isbn: 978-3-540-69149-5
layout: paper
pages: 384-391
publisher: Springer Berlin Heidelberg
read: true
readings:
- 2020-02-21
title: Specified blocks
url: https://doi.org/10.1007/978-3-540-69149-5\_41
year: 2008
topics:
- tools
- verification
notes:
- loop-invariant
papers:
- tuerk:vstte:2010
- schwerhoff:ecoop:2015
---

Program verification based on assertions is fundamentally wrong.
Like Ptolemy's planetary theory of cycles within cycles, they
are overly complex and we need something as simple as
Galileo's theory of elliptical orbits.
This paper forcefully argues that they should be replaced
with "specified blocks" that form a specification of
an entire block of code.
That is, we should describe what a block of code
is intended to do instead of what is true at strategic points
in the code.

A specified block consists of a block of code plus a
predicate that relates the new and old values of any variables.
For example, a block that increments every element of an array
might have the specification

    (forall j: 0..n . L'[j] = L[j]+1)

while the obvious loop that implements this specification would have
the specification

    (forall j: 0,..i . L'[j] = L[j]) &&
    (forall j: i,..n . L'[j] = L[j]+1)

Compare this with the loop invariant that looks like this

    (forall j: 0,..i . L'[j] = L[j]+1) &&
    (forall j: i,..n . L'[j] = L[j]) &&
    0 ≤ i ≤ n

The loop invariant is different from the loop specification in three ways:

- The loop invariant describes what has been done so far
  whereas the loop specification describes what is still to be done.
  You can see this in the first line where the loop specification
  says that the loop does not change some initial segment of the loop
  while the loop invariant says that, so far, the initial segment
  has been incremented.

- Likewise, the second line of the loop specification says that the
  loop is going to increment the tail of the array while the loop
  invariant says that the loop has not yet been changed.

- Finally, the loop invariant describes a single iteration of the loop
  and so it has to say something about the range of i while the loop
  specification describes all remaining iterations of the loop
  and does not need to constrain i.

For loops, the difference of describing what is still to be done
enables local reasoning about loops because the focus is on
the action of the loop, not the code that comes before it.
This was
[independently rediscovered by Tuerk two years later][tuerk:vstte:2010]
in the context of separation logic
where it eliminates the need to invent predicates for describing
partial data structures.
This was later used as the motivation for supporting
[lightweight magic wands][schwerhoff:ecoop:2015].

The paper contains four examples to illustrate how specified blocks
are easier to work with: incrementing arrays, binary search, exponentiation
and product of power series.
The exponentiation example involves gotos: contradicting Dijkstra by saying
"Apparently, unstructured goto's pose no more verification problem
than structured loops."

This approach to specification has been implemented in HOL.

{% include links.html %}
