---
ENTRYTYPE: inproceedings
added: 2020-06-23
authors:
- Dirk Beyer
- Thomas Lemberger
booktitle: 2019 34th IEEE/ACM International Conference on Automated Software Engineering (ASE)
doi: 10.1109/ASE.2019.00105
layout: paper
number: ''
pages: 1074-1077
read: true
readings:
- 2020-06-23
title: 'TestCov: Robust test-suite execution and coverage measurement'
volume: ''
year: 2019
notes:
- Test competition
- KLEE verifier
- Fuzz testing
- FQL
papers:
- beyer:hvc:2018
---

TestCov is a tool that measures the coverage of a test suites
and generates a reduced test suite.
It is used in the [Test competition] and can work with
all the tools that compete in that competition.

The input is a test suite (in the test suite interchange format (XML)),
a program and a specification of the coverage criterion (in [FQL]).

The tool is based on BenchExec and provides containerization (like Docker)
using Cgroups, etc.
so that program runs are isolated from each other.
The containerization has another benefit: it uses an in-memory filesystem
that is faster than a standard filesystem and so speeds up program execution.

The [testcov](https://gitlab.com/sosy-lab/software/test-suite-validator)
tool inserts instrumentation to measure block, branch and condition
coverage as well as calls to an error function.

{% include links.html %}
