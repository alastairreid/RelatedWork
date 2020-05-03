---
ENTRYTYPE: inproceedings
added: 2020-02-14
authors:
- Malte Schwerhoff
- Alexander J Summers
booktitle: 29th European Conference on Object-Oriented Programming (ECOOP 2015)
layout: paper
organization: Schloss Dagstuhl, Leibniz-Zentrum für Informatik
pages: 614-638
read: true
readings:
- 2020-02-14
title: Lightweight support for magic wands in an automatic verifier
volume: '37'
year: 2015
topics:
- tools
- verification
notes:
- permission logic
- separation logic
- magic wand
- Viper verifier
- Prusti verifier
papers:
---

Verifying a loop that walks over a heap data structure is tricky.  At the
start, we might have a pointer to the root of the structure; in some
intermediate iteration of the loop, we have a pointer into the middle of the
structure and the nodes we have visited so far have been changed in some way;
and then, at the end, the entire structure from the root down has been fully
changed.  The difficulty is that, to verify the loop, we have to write an
invariant that describes the changes to the nodes that we have visited so far.
That is, we have to describe a partial data structure: from the root down to
the current position in the list.

There is a well understood way of doing this for lists: we write a “list
segment” predicate “lseg(p,q)” describing the list nodes from node “p” down to
node “q”, we prove some lemmas such as “lseg(p, q) ∗ lseg(q,r) ==> lseg(p, r)”
that say that if you have a list from p to q and a list from q to r then you
have a list from p to r.  And now we can talk about the partial list from the
root down to the current position in the list and we can talk about the
unvisited remainder of the list.

The problem with this is that (1)  we need to add these extra predicates and
lemmas; and (2) it only works for simple (linear?) data structures.  (I am not
sure what the appropriate variant would be for a binary tree.)

The solution is to use “magic wands” Magic wands are the “—∗” separated
implication operator of permission logics such as separation logic or dynamic
frame logic.  Suppose that our loop starts with the root satisfying some
recursive property “P” (i.e., “P(root)” holds) and, at the end of the loop, we
want some recursive property “Q” (i.e., “Q(root)” holds).  Using magic wands,
we would use a list invariant of the form:


P(rest) ∗ (Q(rest) ––∗ Q(root))

This says that

1. We know that the rest of the data structure (still) satisfies P.

2. Once we have transformed the rest of the structure (so that “Q(rest)”
   holds), we will be able to show that the entire structure has been
   transformed (so that “Q(root)” holds).

I think that this has been understood for a while now.  The problem is that it
has also been understood that supporting magic wands makes your logic
undecidable.  The contribution of this paper is

- explicit operations to introduce and eliminate magic wands (analogous to the
  fold/unfold operations used with recursive predicates.
- heuristics for automatically calculating the “footprint” of a magic wand

The “footprint” of a wand “A ––∗ B”

This support for [magic wand]s has been implemented in the [Viper verifier] (an
[intermediate verification language]) and is used in the [Prusti verifier].

{% include links.html %}
