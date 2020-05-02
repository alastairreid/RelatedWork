---
ENTRYTYPE: article
added: 2020-02-14
authors:
- Thomas Tuerk
journal: VSTTE
layout: paper
pages: '29'
read: true
readings:
- 2020-02-19
title: Local reasoning about while-loops
volume: '2010'
year: 2010
topics:
- tools
- verification
notes:
- loop invariant
- separation logic
- magic wand
- Verifast verifier
---

As
[Hehner had previously discovered]({{ "papers/hehner:vstte:2008" | relative_url }}),
we are reasoning about loops in the wrong way.
Instead of using loop invariants that describe what the loop has done so far,
we should be using loop specifications that describe what the loop will do
in the future.
This change enables local reasoning (in the usual "separation logic" sense)
about loops because it focusses on what the loop does and because
it eliminates the need to describe partial data structures such as
the initial segment of a list.

The starting point of this paper is the observation that verifying
recursive functions is simpler than verifying loops even though we
can mechanically transform one into the other.
The difference is that the pre/post-conditions of a function
specify the complete behaviour of the function whereas
a loop invariant describes a series of states at the beginning/end
of each iteration of the loop.
In practice, this means that the loop invariant has to describe
what has been done so far and so invariants typically have the
form

    "Initial segment of data structure has been changed" &&
    "Remaining segment of data structure has not yet been changed"

whereas this paper argues that you should just specify

    "What change will be made to remaining segment of data structure"

Omitting the description of what has been done so far enables
local reasoning: we focus on the action of the remaining iterations
of the loop.

The paper describes how to generalize the classic Hoare-logic
rule for reasoning about loops.
The rule is more complex than we are used to but it is simpler
to use in practice.

The argument that it is simpler is made with examples including
list length, array increment, list filtering, list copy
and binary trees.
Of these, the killer argument is probably binary trees because,
while there are well-known ways of describing initial
segments of lists and arrays, describing a partial binary
tree is harder and this approach completely avoids the need.

This paper notes that "magic wands" could also have been used
to avoid the need to define partial datastructures but that
reasoning about this is harder.
(This might have changed with the later development of
[lightweight magic wands]({{ "papers/schwerhoff:ecoop:2015" | relative_url }})).

The approach in this paper is implemented in the author's
"Holfoot" tool and also in
[VeriFast]({{ "papers/jacobs:nfm:2011" | relative_url }}).

{% include links.html %}
