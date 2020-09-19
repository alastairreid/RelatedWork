---
ENTRYTYPE: inproceedings
added: 2020-07-09
authors:
- David R. MacIver
- Alastair F. Donaldson
booktitle: 34th European Conference on Object-Oriented Programming (ECOOP 2020)
layout: paper
organization: Schloss Dagstuhl, Leibniz-Zentrum für Informatik
pages: 13:1–13:28
read: true
readings:
- 2020-07-09
title: "Test-case reduction via test-case generation: Insights from the Hypothesis reducer"
year: 2020
notes:
- fuzz testing
- test-case reduction
- unit tests
- property-based testing
papers:
- regehr:pldi:2012
---

This paper proposes a general purpose way of getting [test-case reduction] "for
free".  The paper shows that it "provides adequate reduction for any generated
test case, while avoiding the test-case validity problem."

There are three main ideas to achieve this.

The  key to avoiding creation of invalid values  is "internal reduction": the
reduction is integrated into the random generator instead of being performed by
an external tool as in C-reduce [regehr:pldi:2012].

The key to achieving this is to view a random generator as a "parser of choice
sequences" and to recover the structure of this parser (i.e., the generator) by
instrumenting the API. This  allows the reducer to perform optimizations such
as removing/replacing contiguous sequences of choices as seen in hierarchial
delta debugging.

The final ingredient is to have a generic notion of what makes one test-case
better than another.  This is defined as an ordering over the choice sequence
(not over some application-dependent rendering of the sequence).  They use
"shortlex order" where one sequence is ordered before another if it is shorter
or it is the same length but lexicographically earlier.

The "shortlex" order generally works well but for very carefully encoded data
types like binary floating point, you need to write a special generator to
arrange that a number like "1.0" will be preferred to a number like "5e-324".

The evaluation shows that this general purpose approach works about as well as
custom approaches on a broad range of cases.  (But the comparision with
C-reduce should be read carefully: my interpretation of the results is that _if
it really, really matters_ it may be worth putting in considerably more effort
to write a custom reducer.)

Perhaps the most important thing shown by the evaluation though is the ability
to apply the approach to many cases.

> This is an important selling point for internal reduction: it works at the
> level of choice sequences, and any randomized generator can be relatively
> easily adapted to consume a choice sequence instead of using
> a pseudo-random number generator, thus internal reduction has wide
> applicability.
> <br>
> – Section 4

The evaluation also reveals a scaling problem.  Their tool is fine generating
inputs up to about 8kB but, because the chance of triggering a bug is quite
low, CSmith is generally better with inputs of around 80kB.  It is not
completely clear whether this is fundamental to the way that Hypothesis works.

{% include links.html %}
