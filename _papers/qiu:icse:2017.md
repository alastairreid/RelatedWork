---
ENTRYTYPE: inproceedings
abstract: Symbolic execution is a systematic program analysis technique that has received a lot of attention in the research community. However, scaling
  symbolic execution continues to pose a major challenge. This paper introduces Synergise, a novel two-fold integration approach. One, it integrates distributed
  analysis and constraint re-use to enhance symbolic execution using feasible ranges, which allow sharing of constraint solving results among different
  workers without communicating or sharing potentially large constraint databases (as required traditionally). Two, it integrates complementary techniques
  for test input generation, e.g., search-based generation and symbolic execution, for creating higher quality tests using unexplored ranges, which allows
  symbolic execution to re-use tests created by another technique for effective distribution of exploration of previously unexplored paths.
added: 2021-02-25
authors:
- Rui Qiu
- S. Khurshid
- C. S. Pasareanu
- Guowei Yang
booktitle: 2017 IEEE/ACM 39th International Conference on Software Engineering Companion (ICSE-C)
doi: 10.1109/ICSE-C.2017.116
issn: ''
keywords: constraint handling;distributed processing;program diagnostics;program testing;software reusability;distributed symbolic execution;test ranges;systematic
  program analysis;synergistic approach;two-fold integration;SynergiSE approach;distributed analysis;constraint reuse;feasible ranges;constraint databases;test
  input generation;search-based generation;unexplored ranges;Tools;Testing;Standards;Databases;Java;Software engineering;Systematics
layout: paper
month: May
number: ''
pages: 130-132
read: true
readings:
- 2021-02-25
title: A synergistic approach for distributed symbolic execution using test ranges
volume: ''
year: 2017
notes:
- symbolic execution
- case splitting
- verifier performance
papers:
- siddiqui:oopsla:2012
- qiu:nfm:2018
---

Test ranges (from [siddiqui:oopsla:2012]) compactly represent sets of program paths.
using a pair of paths to define a range of paths
based on lexicographic ordering of the paths and can be used to divide the symbolic
execution tree into a number of subtrees that can be explored in parallel.

This paper adds feasible ranges and unexplored ranges

- **Feasible ranges** start with a shallow exploration of the tree up to a small depth
  detecting infeasible branches as it goes
  and then splits the tree into subtrees that only contain feasible paths.
  This shares constraint solving results without sharing large constraint databases.

- **Unexplored ranges** start with the results of some other test generation tool
  and identifies unexplored ranges for SE to explore.

Implemented using work-stealing, in Symbolic PathFinder



{% include links.html %}
