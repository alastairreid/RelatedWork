---
ENTRYTYPE: inproceedings
added: 2021-07-09
authors:
- Shriram Krishnamurthi
- Benjamin S. Lerner
- Liam Elberty
booktitle: Summit on Advances in Programming Languages (SNAPL)
doi: 10.4230/LIPIcs.SNAPL.2019.9
isbn: ''
layout: paper
read: true
readings:
- 2021-07-09
title: 'The next 700 semantics: A research challenge'
year: 2019
notes:
papers:
---

As a step towards making it easier to construct a semantics
for all the languages found in the wild, this paper considers
the common practice of having a small(ish) core language and
a set of desugarings from the surface language.

The problem they tackle is learning the desugarings.
They try four different approaches:
naïve tree matching;
learning a tree transducer by Gibbs sampling;
genetic programming;
and
synthesis.
While none of these actually succeed, they
have a detailed analysis of why each fails.

{% include links.html %}
