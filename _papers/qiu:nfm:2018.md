---
ENTRYTYPE: inproceedings
abstract: 'Symbolic execution is a powerful systematic technique for checking programs, which has received a lot of research attention during the last decade.
  In practice however, the technique remains hard to scale. This paper introduces SynergiSE, a novel approach to improve symbolic execution by tackling
  a key bottleneck to its wider adoption: costly and incomplete constraint solving. To mitigate the cost, SynergiSE introduces a succinct encoding of constraint
  solving results, thereby enabling symbolic execution to be distributed among different workers while sharing and re-using constraint solving results among
  them without having to communicate databases of constraint solving results. To mitigate the incompleteness, SynergiSE introduces an integration of complementary
  approaches for testing, e.g., search-based test generation, with symbolic execution, thereby enabling symbolic execution and other techniques to apply
  in tandem. Experimental results using a suite of Java programs show that SynergiSE presents a promising approach for improving symbolic execution.'
added: 2021-02-24
address: Cham
authors:
- Rui Qiu
- Sarfraz Khurshid
- Corina S. Păsăreanu
- Junye Wen
- Guowei Yang
booktitle: NASA Formal Methods
editor: Dutle, Aaron and Mu{ñ}oz, César and Narkawicz, Anthony
isbn: 978-3-319-77935-5
layout: paper
pages: 416-434
publisher: Springer International Publishing
read: false
readings: []
title: Using test ranges to improve symbolic execution
year: 2018
notes:
- symbolic execution
- case splitting
- verifier performance
papers:
- qiu:icse:2017
---
{% include links.html %}
