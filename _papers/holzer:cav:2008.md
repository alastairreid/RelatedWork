---
ENTRYTYPE: inproceedings
abstract: Although the principal analogy between counterexample generation and white box testing has been repeatedly addressed, the usage patterns and performance
  requirements for software testing are quite different from formal verification. Our tool FShell provides a versatile testing environment for C programs
  which supports both interactive explorative use and a rich scripting language. More than a frontend for software model checkers, FShell is designed as
  a database engine which dispatches queries about the program to program analysis tools. We report on the integration of CBMC into FShell and describe
  architectural modifications which support efficient test case generation.
added: 2020-06-23
address: Berlin, Heidelberg
authors:
- Andreas Holzer
- Christian Schallhart
- Michael Tautschnig
- Helmut Veith
booktitle: Computer Aided Verification
doi: 10.1007/978-3-540-70545-1_20
editor: Gupta, Aarti and Malik, Sharad
isbn: 978-3-540-70545-1
layout: paper
pages: 209-213
publisher: Springer Berlin Heidelberg
read: true
readings:
- 2020-06-23
title: 'FShell: Systematic test case generation for dynamic analysis and measurement'
year: 2008
notes:
- BLAST verifier
- CBMC verifier
- FQL
- SV-competition
papers:
- holzer:hvc:2010
---

FShell adapts the "program as database" metaphor previously used by the [BLAST
verifier] from model checking to test generation.
It generates families of testcases based on coverage criteria
specified using the "FShell" query language ([FQL]) that (I think) was introduced
in this paper.

([FQL] is not described in detail in this paper.)

FShell uses CBMC as a backend (FQL was later used with many other tools in
[SV-Competition]).

FShell is compared against the [BLAST verifier] on five cases ranging from
4800 to 45,000 lloc (logical lines of code == number of semicolons).
(The benchmarks come from BLAST.)
FShell is faster though the paper admits that BLAST
is really a tool for full verification whereas FShell is optimized for
generating tests.
FShell generates more tests to achieve the same basic block coverage.

Also evaluated on three sorting algorithms (bubble, insertion, selection)
while varying the input size. Presented as speedup against a model checker
(probaby CBMC?).

{% include links.html %}
