---
ENTRYTYPE: inproceedings
abstract: We describe a Guess-and-Check algorithm for computing algebraic equation invariants of the form \wedge {\th}inspaceifi(x1,{\l}dots,xn){\th}inspace={\th}inspace0,
  where each fiis a polynomial over the variables x1,{\l}dots,xnof the program. The ``guess'' phase is data driven and derives a candidate invariant from
  data generated from concrete executions of the program. This candidate invariant is subsequently validated in a ``check'' phase by an off-the-shelf SMT
  solver. Iterating between the two phases leads to a sound algorithm. Moreover, we are able to prove a bound on the number of decision procedure queries
  which Guess-and-Check requires to obtain a sound invariant. We show how Guess-and-Check can be extended to generate arbitrary boolean combinations of
  linear equalities as invariants, which enables us to generate expressive invariants to be consumed by tools that cannot handle non-linear arithmetic.
  We have evaluated our technique on a number of benchmark programs from recent papers on invariant generation. Our results are encouraging - we are able
  to efficiently compute algebraic invariants in all cases, with only a few tests.
added: 2019-07-01
address: Berlin, Heidelberg
authors:
- Rahul Sharma
- Saurabh Gupta
- Bharath Hariharan
- Alex Aiken
- Percy Liang
- Aditya V. Nori
booktitle: Programming Languages and Systems
doi: 10.1007/978-3-642-37036-6_31
editor: Felleisen, Matthias and Gardner, Philippa
isbn: 978-3-642-37036-6
layout: paper
pages: 574-592
publisher: Springer Berlin Heidelberg
read: false
readings: []
title: A data driven approach for algebraic loop invariants
year: 2013
topics:
notes:
- loop invariant
papers:
---

{% include links.html %}
