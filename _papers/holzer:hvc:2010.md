---
ENTRYTYPE: inproceedings
abstract: In a recent series of papers, we introduced a new framework for white-box testing which aims at a separation of concerns between test specifications
  and test generation engines. We believe that establishing a common language for test criteria will have similar benefits to testing as temporal logic
  had to model checking and SQL had to databases. The main challenge was to find a specification language which is expressive, simple, and precise. This
  paper gives an introduction to the test specification language FQL and its tool environment.
added: 2020-06-23
address: Berlin, Heidelberg
authors:
- Andreas Holzer
- Michael Tautschnig
- Christian Schallhart
- Helmut Veith
booktitle: 'Hardware and Software: Verification and Testing'
doi: 10.1007/978-3-642-19583-9_5
editor: Barner, Sharon and Harris, Ian and Kroening, Daniel and Raz, Orna
isbn: 978-3-642-19583-9
layout: paper
pages: 9-22
publisher: Springer Berlin Heidelberg
read: true
readings:
- 2020-06-23
title: An introduction to test specification in FQL
year: 2011
notes:
- FQL
papers:
- holzer:cav:2008
---

Proposes a query language [FQL] for specifying coverage goals that can be used for

- testcase generation
- coverage measurement
- generating code (?)
- hybrid testing tools based on model checking
- distributed testcase generation
- testsuite improvement tools that detect gaps and generate tests to fill them

Path patterns is a good approach for individual tests but not for entire test
suites.
They need a language for specifying all the path patterns of interest:
a meta-regex that specifies sets of regexps using quoted regexps.

The FQL language is specified (see [FQL]) and there are a number of examples to
illustrate the language.

FShell 2 was an interactive frontend and used CBMC as a backend.
FShell 3 builds on CPAChecker and can measure the coverage of existing
testsuites.

{% include links.html %}
