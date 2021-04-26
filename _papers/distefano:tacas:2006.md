---
ENTRYTYPE: inproceedings
added: 2020-01-28
authors:
- Dino Distefano
- Peter W. O'Hearn
- Hongseok Yang
booktitle: International Conference on Tools and Algorithms for the Construction and Analysis of Systems
layout: paper
organization: Springer
pages: 287-302
read: true
readings:
- 2021-04-26
title: A local shape analysis based on separation logic
year: 2006
topics:
- tools
- verification
notes:
- permission logic
- separation logic
- symbolic execution
- abstract interpretation
papers:
- berdine:aplas:2005
- calcagno:sas:2006
- calcagno:popl:2009
---

This paper moves beyond [berdine:aplas:2005] to support reasoning about loops
by augmenting [symbolic execution] with [abstract interpretation].
This allows them to reason about loops that reverse lists, deallocate entire lists,
append lists, copy lists, insert/delete from the middle of
a list, delete and filter circular lists, and deallocate ranges of values from sorted lists.

As in the slightly later paper with more authors [calcagno:sas:2006],
the idea is to use a fragment of separation logic as an abstract domain,
to define an abstraction operator ("canonicalization rules")
and then to use least fixpoint to infer loop invariants.

Unlike their later work ([calcagno:popl:2009]), they restrict themselves to
intra-procedural analyses although there is a slightly hard to follow
sketch near the end which may be an early form of what the later paper
called "biabduction".

This is a rather strange paper: it does not feel quite finished.  The paper
says that their shape analysis is less powerful than the state of the art at
the time, their canonicalization rewrite rules don't produce a minimal result,
they don't know if the rewrite rules are confluent so they apply rules in a
fixed order, the reporting on performance results is extremely vague, and some
definitions are (in their words) "not exactly pretty".  The argument they make
at the start of the paper (when comparing against the state of the art) is that
their approach "is of interest because it suggests a genuinely different
approach which has promise for the central problem of obtaining modular
analyses." (This promise was later kept in [calcagno:popl:2009].)

{% include links.html %}
