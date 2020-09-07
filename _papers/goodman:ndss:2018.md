---
ENTRYTYPE: inproceedings
added: 2020-09-04
authors:
- Peter Goodman
- Alex Groce
booktitle: NDSS Workshop on Binary Analysis Research
doi: 10.14722/bar.2018.23009
layout: paper
read: true
readings:
- 2020-09-04
title: "DeepState: Symbolic unit testing for C and C++"
day: 18
month: February
year: 2018
location: San Diego, California, USA
pages: 7
notes:
- fuzz testing
- symbolic execution
- binary analysis
- property-based testing
- unit tests
papers:
---

DeepState seeks to narrow the gap between techniques that programmers are
familiar with (e.g., testing) and symbolic execution / binary analysis tools by
enabling the use of parameterized unit tests with a variety of symbolic
execution backends (angr, Manticore and Dr. Fuzz) and fuzzers and making it
easy to switch between backends.

The interface is a DSL that extends
[GoogleTest](https://github.com/google/googletest).

A key challenge is handling "debug printfs" in the code being tested since that
causes a path explosion.
Their solution is to provide a streaming log interface that defers printing log
output until the end of the test.

They enable "swarm testing" in their DSL by providing constructs like "OneOf"
that select one of several code blocks to execute.  Each member of the swarm
can disable some subset of the code blocks or change their relative probability
to increase the diversity of testing.
_(I have seen a similar approach in hardware model checking before.)_

They tackle problems around symbolic loop bounds and symbolic array accesses by
forking particular concrete values to reduce the state (path?) explosion
problem. They call this "pumping".
_(I want to know more about this.)_

The code is [available on github](https://github.com/trailofbits/deepstate)
under an open-source license;
and
there are [blog articles about DeepState](https://github.com/trailofbits/deepstate#articles-describing-deepstate).

{% include links.html %}
