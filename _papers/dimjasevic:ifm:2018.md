---
ENTRYTYPE: inproceedings
abstract: Testing is currently the main technique adopted by the industry for improving the quality, reliability, and security of software. In order to
  lower the cost of manual testing, automatic testing techniques have been devised, such as random and symbolic testing, with their respective trade-offs.
  For example, random testing excels at fast global exploration of software, while it plateaus when faced with hard-to-hit numerically-intensive execution
  paths. On the other hand, symbolic testing excels at exploring such paths, while it struggles when faced with complex heap class structures. In this paper,
  we describe an approach for automatic unit testing of object-oriented software that integrates the two techniques. We leverage feedback-directed unit
  testing to generate meaningful sequences of constructor+method invocations that create rich heap structures, and we in turn further explore these sequences
  using dynamic symbolic execution. We implement this approach in a tool called JDoop, which we augment with several parameters for fine-tuning its heuristics;
  such ``knobs'' allow for a detailed exploration of the various trade-offs that the proposed integration offers. Using JDoop, we perform an extensive empirical
  exploration of this space, and we describe lessons learned and guidelines for future research efforts in this area.
added: 2020-09-07
address: Cham
authors:
- Marko Dimjašević
- Falk Howar
- Kasper Luckow
- Zvonimir Rakamarić
booktitle: Integrated Formal Methods
editor: Furia, Carlo A. and Winter, Kirsten
isbn: 978-3-319-98938-9
layout: paper
pages: 89-109
publisher: Springer International Publishing
read: true
readings:
- 2020-09-07
title: Study of Integrating Random and Symbolic Testing for Object-Oriented Software
year: 2018
notes:
- fuzz testing
- symbolic execution
- unit tests
papers:
- garg:icse:2013
---

Describes and evaluates JDOOP: a hybrid fuzzer/symbolic executor for Java
that uses random search to quickly build coverage and symbolic execution to
hit hard to hit branch conditions.
JDOOP is a combination of RANDOOP and JDART.

As in [garg:icse:2013] the main goal is to generate sequences of method calls
that achieve high coverage.

One major barrier is the handling of non-Java code which, unfortunately
includes Java string functions `charAt` and `indexOf`.
These are not treated symbolically: the tool has a choice of either
returning a symbolic return value or of concretizing inputs and running
concretely.

{% include links.html %}
