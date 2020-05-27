---
ENTRYTYPE: inproceedings
added: 2019-11-09
authors:
- Patrick Cousot
- Radhia Cousot
- Francesco Logozzo
- Mike Barnett
booktitle: 'Proceedings of the 27th Annual ACM SIGPLAN Conference on Object-Oriented Programming, Systems, Languages, and Applications, OOPSLA 2012'
doi: 10.1145/2384616.2384633
isbn: 978-1-4503-1561-6
layout: paper
pages: 213-232
publisher: ACM
read: true
readings:
- 2019-11-09
title: 'An abstract interpretation framework for refactoring with application to extract methods with contracts'
year: 2012
topics:
- verification
notes:
- abstract interpretation
papers:
---

There is a lot to recommend Design by Contract where each function/method is equipped with contracts (pre/post-conditions).
But the cost is that you have to create and maintain all those contracts.
This paper addresses an interesting part of the problem that arises while refactoring code: creating a contract for any functions/methods extracted.
The insight here is that this is really a matter of refactoring the proof that the original code meets its contracts.
The goal they set is that the new contract must meet four criteria:
validity, safety, completeness and generality.

The basic approach taken is to use a combination of over- and under-approximation and forward and backward analyses to produce the weakest precondition and the strongest postcondition.

Their goal is a method that can work with a variety of specification logics: first order, separation logic, region logic, ...
So they create a generalization of Hoare logic to abstract over properties these all share: algebraic Hoare logic.

The main body is fairly dense with definitions: Galois connections, abstract domains, pre/post-condition abstract domains, predicate transformers, abstract Hoare logic, 
contracts, partial orders on contracts, etc.

There is also a section about the implementation and experiments that is about 2 pages long.  It would have been great to hear more here - it sounds like it was a *lot* of work.


{% include links.html %}
