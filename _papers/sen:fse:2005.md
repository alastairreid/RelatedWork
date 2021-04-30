---
ENTRYTYPE: inproceedings
abstract: In unit testing, a program is decomposed into units which are collections of functions. A part of unit can be tested by generating inputs for
  a single entry function. The entry function may contain pointer arguments, in which case the inputs to the unit are memory graphs. The paper addresses
  the problem of automating unit testing with memory graphs as inputs. The approach used builds on previous work combining symbolic and concrete execution,
  and more specifically, using such a combination to generate test inputs to explore all feasible execution paths. The current work develops a method to
  represent and track constraints that capture the behavior of a symbolic execution of a unit with memory graphs as inputs. Moreover, an efficient constraint
  solver is proposed to facilitate incremental generation of such test inputs. Finally, CUTE, a tool implementing the method is described together with
  the results of applying CUTE to real-world examples of C code.
added: 2021-04-30
address: New York, NY, USA
authors:
- Koushik Sen
- Darko Marinov
- Gul Agha
booktitle: Proceedings of the 10th European Software Engineering Conference Held Jointly with 13th ACM SIGSOFT International Symposium on Foundations of
  Software Engineering
doi: 10.1145/1081706.1081750
isbn: '1595930140'
keywords: data structure testing, concolic testing, random testing, explicit path model-checking, unit testing, testing C programs
layout: paper
link: https://doi.org/10.1145/1081706.1081750
location: Lisbon, Portugal
numpages: '10'
pages: 263-272
publisher: Association for Computing Machinery
read: false
readings: []
series: ESEC/FSE-13
title: 'CUTE: A concolic unit testing engine for C'
url: https://doi.org/10.1145/1081706.1081750
year: 2005
notes:
- symbolic execution
papers:
- cadar:cacm:2013
---
{% include links.html %}
