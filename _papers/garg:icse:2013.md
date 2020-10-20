---
ENTRYTYPE: inproceedings
abstract: In industry, software testing and coverage-based metrics are the predominant techniques to check correctness of software. This paper addresses
  automatic unit test generation for programs written in C/C++. The main idea is to improve the coverage obtained by feedback-directed random test generation
  methods, by utilizing concolic execution on the generated test drivers. Furthermore, for programs with numeric computations, we employ non-linear solvers
  in a lazy manner to generate new test inputs. These techniques significantly improve the coverage provided by a feedback-directed random unit testing
  framework, while retaining the benefits of full automation. We have implemented these techniques in a prototype platform, and describe promising experimental
  results on a number of C/C++ open source benchmarks.
added: 2020-09-07
authors:
- Pranav Garg
- Franjo Ivančić
- Gogul Balakrishnan
- Naoto Maeda
- Aarti Gupta
booktitle: Proceedings of the 2013 International Conference on Software Engineering
doi: 10.1109/ICSE.2013.6606559
isbn: '9781467330763'
layout: paper
location: San Francisco, CA, USA
numpages: '10'
pages: 132-141
publisher: IEEE Press
read: true
readings:
- 2020-09-07
series: ICSE '13
title: Feedback-directed unit test generation for C/C++ using concolic execution
year: 2013
notes:
- fuzz testing
- symbolic execution
- unit tests
papers:
---

This paper describes a test generation tool based on a hybrid of [symbolic
execution] and [fuzz testing].
The goal is to generate high coverage sequences of method calls.

An interesting technical detail is that use unsat core to generate "conflict sequences":
unsatisfiable branch sequences.
This is used to reduce the number of SMT queries required.

The tool is evaluated on eight benchmarks based primarily on coverage metrics.

{% include links.html %}
