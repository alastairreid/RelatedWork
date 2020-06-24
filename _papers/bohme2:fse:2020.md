---
ENTRYTYPE: inproceedings
added: 2020-05-22
authors:
- Marcel Böhme
- Brandon Falk
booktitle: Proceedings of the 2020 28th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering
layout: paper
number: ''
pages: 11
read: true
readings:
- 2020-06-24
title: 'Fuzzing: On the exponential cost of vulnerability discovery'
volume: ''
year: 2020
notes:
- fuzz testing
papers:
---

Using a large empirical study of fuzzing (using AFL and libFuzzer),
this paper explores the cost of finding vulnerabilities (or
increasing coverage).

They produce some empirical laws:

- Random fuzzers take exponentially more time to find each
  additional vulnerability.
  "Intuitively, when collecting baseball cards, the first
  couple of cards are easy to find, but collecting the next
  new card gets progressively more difficult."

- Finding the same vulnerabilities in half the time requires
  only half as many machines.
  "Intuitively, if each day you buy twice as many packs of
  baseball cards, you could have collected the same cards that
  you now have in half the time."

These both assume zero cost for synchronization across fuzzers
running in parallel.
In an experiment with greybox fuzzers where the fuzzers shared
their seeds as they discovered them and where they did
not share seeds, they found that sharing significantly improved
discovery rate.

They also produce mathematical models to help explain the patterns in their
empirical data.
A key part of those models is an assumption of a power-law distribution
of bugs/features.

Their models are for purely random (blackbox) fuzzers but they suggest that, in
the limit, graybox fuzzers turn into random fuzzers.


{% include links.html %}
