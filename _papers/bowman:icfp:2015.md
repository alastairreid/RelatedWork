---
ENTRYTYPE: article
added: 2020-02-14
address: New York, NY, USA
authors:
- William J. Bowman
- Amal Ahmed
doi: 10.1145/2858949.2784733
issn: 0362-1340
issue_date: December 2015
journal: SIGPLAN Not.
keywords: dependency, polymorphism, information flow, parametricity, fully abstract
  compilation, security, Noninterference, logical relations, secure compilation
layout: paper
month: August
number: '9'
numpages: '13'
pages: 101-113
publisher: Association for Computing Machinery
read: true
readings:
- 2021-04-23
title: Noninterference for free
url: https://doi.org/10.1145/2858949.2784733
volume: '50'
year: 2015
topics:
- types
notes:
- non-interference
papers:
---

This paper is so much more than the paper title suggests.
From the paper title, I was expecting something about parametricity
and non-interference and the conclusion does say

> It is folklore that noninterference can be encoded via parametricity
> but we are unaware of any work that successfully shows how to do that.

What they do is take Abadi et al.'s Dependency Core Calculus (DCC) and
show how to translate it to the richer language F-omega while preserving
a form of full abstraction so that translated terms can be distinguised
if and only if the original terms can be translated.
(The "a form of" is because, in the context of non-interference, the
level of the observer trying to distinguish the terms is significant.)

(An important omission is that they do not handle recursion.)

The idea of the DCC is to encode the secrecy level of a value in
its type. e.g., "T_l bool" is a bool that can be observed at level l
and above.
In this scheme, each level "l" in the lattice is represented by
a type constructor "T_l" and edges in the lattice are represented
by coercions.
Each "T_l" is a monad and the associated return and bind operations
are used to wrap and unwrap values.

An earlier attempt (later proved incorrect) translated the DCC
type "T_l s" to "alpha_l -> s+" where "alpha_l" is a type whose
values can only be constructed by code at level "l" or above.
This reminded me of capabilities: you can only access a value
if you have an appropriate capability.

Unfortunately, a counterexample was found.  This emphasized
the importance of having a "back translation" where every
value of the translated F-omega type is equivalent to a value of 
the original DCC type.

The key idea of this paper's correct translation is inspired by
a similarity between the typing rule for bind and the typing
rule for existential types which suggests that the encoding of
existential types uses continuations might work.
Their encoding is (roughly)

    T_l s ==> forall b. (("l <= b", (s+ -> b)) -> b

where "l <= b" is a proof (witness?) that "b" is high enough
in the lattice.

The bulk of the paper is a very detailed proof.
It is a hard read but full of helpful comments along the
lines of "normally, one would do X here but we do Y because ...".
(I love this kind of insight in papers!)

One thing that I had expected from the title of this paper was something like
Wadler's "Theorems for free!" paper that had lots of examples
of theorems that were normally laboriously proved by recursion but
that turned out to be a simple property of the function's type.
This paper isn't really that sort of paper.


{% include links.html %}
