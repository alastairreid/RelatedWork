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
read: true
readings:
- 2021-04-18
series: POPL '05
title: Scalable error detection using boolean satisfiability
url: https://doi.org/10.1145/1040305.1040334
year: 2005
notes:
- lazy initialization
- Saturn verifier
- bounded model checking
- CBMC verifier
papers:
- ramos:sec:2015
- engler:issta:2007
- khurshid:tacas:2003
- calcagno:popl:2009
---

[Saturn][Saturn verifier] is a SAT-based bug-finding tool for checking temporal logic formulae (expressed as state machines)
on C programs and, in particular, for checking for locking errors in Linux kernel code.
A key part of its design is the generation of function summaries using [lazy initialization]
to infer the precondition of functions.
It achieves a false positive rate of only 40%.
A problem (that it shares with successors such as [engler:issta:2007] and [ramos:sec:2015]) is its handling of pointer aliases:
the function summaries generated are always trees, not DAGs.

Saturn is based on forward symbolic execution with merging at join points.
Loops are handled by unrolling a bounded number of times.
Function summaries are used to enable a bottom-up interprocedural analysis.
That is, Saturn is a compositional [bounded model checker][bounded model checking].

Saturn uses BDDs to represent boolean formualae used as guards in order to simplify the guards generated at join points.
Program slicing is used (but not thoroughly described).

When used on Linux, it generated 179 new bug reports involving locks.

The related work section is interesting.
For example, comparing with [CBMC][CBMC verifier], they emphasize the compositional analysis
and the ability to use the particular errors being checked for to simplify the
analysis and reduce the size of the function summaries: enabling Saturn to be used
on very large codebases such as the Linux kernel.
In contrast, they characterize CBMC as a whole-program assertion checker.

{% include links.html %}
