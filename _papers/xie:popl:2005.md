---
ENTRYTYPE: inproceedings
abstract: We describe a software error-detection tool that exploits recent advances in boolean satisfiability (SAT) solvers. Our analysis is path sensitive,
  precise down to the bit level, and models pointers and heap data. Our approach is also highly scalable, which we achieve using two techniques. First,
  for each program function, several optimizations compress the size of the boolean formulas that model the control- and data-flow and the heap locations
  accessed by a function. Second, summaries in the spirit of type signatures are computed for each function, allowing inter-procedural analysis without
  a dramatic increase in the size of the boolean constraints to be solved.We demonstrate the effectiveness of our approach by constructing a lock interface
  inference and checking tool. In an interprocedural analysis of more than 23,000 lock related functions in the latest Linux kernel, the checker generated
  300 warnings, of which 179 were unique locking errors, a false positive rate of only 40\%.
added: 2021-04-18
address: New York, NY, USA
authors:
- Yichen Xie
- Alex Aiken
booktitle: Proceedings of the 32nd ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages
doi: 10.1145/1040305.1040334
isbn: 158113830X
keywords: boolean satisfiability, program analysis, error detection
layout: paper
link: https://doi.org/10.1145/1040305.1040334
location: Long Beach, California, USA
numpages: '13'
pages: 351-363
publisher: Association for Computing Machinery
read: false
readings: []
series: POPL '05
title: Scalable error detection using boolean satisfiability
url: https://doi.org/10.1145/1040305.1040334
year: 2005
notes:
- lazy initialization
- Saturn verifier
- symbolic execution
papers:
- ramos:cav:2011
- engler:issta:2007
- khurshid:tacas:2003
- calcagno:popl:2009
---
{% include links.html %}
