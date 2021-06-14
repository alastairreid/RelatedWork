---
ENTRYTYPE: inproceedings
abstract: When a program is modified during software evolution, developers typically run the new version of the program against its existing test suite
  to validate that the changes made on the program did not introduce unintended side effects (i.e., regression faults). This kind of regression testing
  can be effective in identifying some regression faults, but it is limited by the quality of the existing test suite. Due to the cost of testing, developers
  build test suites by finding acceptable tradeoffs between cost and thoroughness of the tests. As a result, these test suites tend to exercise only a small
  subset of the program's functionality and may be inadequate for testing the changes in a program. To address this issue, we propose a novel approach called
  Behavioral Regression Testing (BERT). Given two versions of a program, BERT identifies behavioral differences between the two versions through dynamical
  analysis, in three steps. First, it generates a large number of test inputs that focus on the changed parts of the code. Second, it runs the generated
  test inputs on the old and new versions of the code and identifies differences in the tests' behavior. Third, it analyzes the identified differences and
  presents them to the developers. By focusing on a subset of the code and leveraging differential behavior, BERT can provide developers with more (and
  more detailed) information than traditional regression testing techniques. To evaluate BERT, we implemented it as a plug-in for Eclipse, a popular Integrated
  Development Environment, and used the plug-in to perform a preliminary study on two programs. The results of our study are promising, in that BERT was
  able to identify true regression faults in the programs.
added: 2021-06-14
authors:
- Wei Jin
- Alessandro Orso
- Tao Xie
booktitle: 2010 Third International Conference on Software Testing, Verification and Validation
doi: 10.1109/ICST.2010.64
issn: 2159-4848
keywords: ''
layout: paper
month: April
number: ''
pages: 137-146
read: false
readings: []
title: Automated behavioral regression testing
volume: ''
year: 2010
notes:
papers:
---
{% include links.html %}
