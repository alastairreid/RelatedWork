---
ENTRYTYPE: inproceedings
added: 2020-02-14
address: New York, NY, USA
authors:
- Cristiano Calcagno
- Dino Distefano
- Peter W. O'Hearn
- Hongseok Yang
booktitle: Proceedings of the 36th Annual ACM SIGPLAN-SIGACT Symposium on Principles
  of Programming Languages
doi: 10.1145/1480881.1480917
isbn: '9781605583792'
keywords: proof theory, abduction, program analysis
layout: paper
location: Savannah, GA, USA
numpages: '12'
pages: 289-300
publisher: Association for Computing Machinery
read: true
readings:
- 2020-02-15
series: POPL '09
title: Compositional shape analysis by means of bi-abduction
url: https://doi.org/10.1145/1480881.1480917
year: 2009
topics:
- permission-logic
- tools
- verification
notes:
- permission-logic
- biabduction
- smallfoot-verifier
- modular-verification
---

One of the big challenges in automated verification is the
annotation burden.
In particular, to make verification compositional, we need contracts
for all the functions but writing and maintaining
contracts for a large codebase is a significant overhead
and discovering the contracts for an existing codebase
is a lot of work.
This paper focusses on discovering contracts that describe
what parts of a heap-allocated data structure a function
depends on in order to support separation-logic based
verification of memory safety along the lines of
[Smallfoot]({{ "papers/berdine:fmco:2005" | relative_url }}).

In particular, they are interested in finding the
precondition of a function: what parts of a function's
arguments does a function depend on?
And they want the precondition discovered to be as small
as possible.
(This is a form of "shape analysis".)

The bulk of the paper deals with analysing individual functions.
A short section then describes the fixpoint calculation to
propagate analysis results from one function to another.

What stands out about this paper is the experimental results: they are able to
analyse device drivers, the Linux kernel, Gimp, OpenSSL, etc.  and infer
sufficiently strong contracts for between 42% and 61% of the functions in those
codebases.  There seem to be two key features of their analysis that lead to
this success (and the performance of their tool).

- They are able to cope with partial
  analyses: imprecision and issues such as function pointers
  have a local effect on analysis but they are able
  to keep going.

- The analysis tends to proceed bottom up whereas many
  alternative analyses they mention seem to have been
  top down.

  That said, they suggest that a top-down pass might be
  worth adding to further improve the precision of analysis.
  Presumably this helps propagate information that a function
  is always called with the data structure in some shape.
