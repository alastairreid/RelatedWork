---
ENTRYTYPE: inproceedings
added: 2019-10-13
authors:
- Frédéric Mangano
- Simon Duquennoy
- Nikolai Kosmatov
booktitle: International Conference on Risks and Security of Internet and Systems
doi: 10.1007/978-3-319-54876-0_9
layout: paper
organization: Springer
pages: 114-120
read: true
readings:
- 2019-11-25
title: 'Formal verification of a memory allocation module of Contiki with Frama-C: a case study'
year: 2016
topics:
- os
- tools
- verification
---

This paper describes the use of [Frama-C]({{ "papers/cuoq:sefm:2012.md" | relative_url }}) to specify and verify the
Contiki memory allocator.
The description is very clear and contains enough of the specification that
it should be easy to reproduce or adapt to other allocators.
Use of the specification is demonstrated on a simple program that allocates
two objects and then frees them.
The annotation burden is about 154 lines to 139 lines of code (around 110%) – which seems to be about normal for Frama-C.

One minor complaint is that,
although it describes in detail an inductive definition for calculating the number of free blocks,
it does not contain the definition.
And, it relies on some auxiliary lemmas proved in Coq but does not show the details to better explain how Coq and Frama-C are used together.
(However, it does cite a paper [2] that may contain that detail.)

Overall, a short, easy and rewarding read.
