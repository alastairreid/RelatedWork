---
ENTRYTYPE: inproceedings
abstract: In practice, software testing has been the established method for finding bugs in programs for a long time. But in the last 15 years, software
  model checking has received a lot of attention, and many successful tools for software model checking exist today. We believe it is time for a careful
  comparative evaluation of automatic software testing against automatic software model checking. We chose six existing tools for automatic test-case generation,
  namely AFL-fuzz, CPATiger, Crest-ppc, FShell, Klee, and PRtest, and four tools for software model checking, namely Cbmc, CPA-Seq, Esbmc-incr, and Esbmc-kInd,
  for the task of finding specification violations in a large benchmark suite consisting of 5 693 C programs. In order to perform such an evaluation, we
  have implemented a framework for test-based falsification (tbf) that executes and validates test cases produced by test-case generation tools in order
  to find errors in programs. The conclusion of our experiments is that software model checkers can (i) find a substantially larger number of bugs (ii) in
  less time, and (iii) require less adjustment to the input programs.
added: 2020-06-23
address: Cham
authors:
- Dirk Beyer
- Thomas Lemberger
booktitle: 'Hardware and Software: Verification and Testing'
editor: Strichman, Ofer and Tzoref-Brill, Rachel
isbn: 978-3-319-70389-3
layout: paper
pages: 99-114
publisher: Springer International Publishing
read: true
readings:
- 2020-06-23
title: 'Software verification: Testing vs. model checking'
year: 2017
notes:
- FQL
- Fuzz testing
- Test Competition
- SV Competition
- KLEE Verifier
- CBMC Verifier
papers:
- holzer:cav:2008
- holzer:hvc:2010
- cadar:cacm:2013
---

Compare test generators against model checkers.
The test generators are AFL-Fuzz, CPATiger, CREST-PPC, FShell, [KLEE verifier] and PRTest.
The model checkers are [CBMC verifier], CPA-seq, ESBMC-incr, ESBMC-kInd.

The benchmarks are all from the [SV competition].
These consist of 1490 programs with exactly one bug and 4293 programs with no
bugs.
The model checkers were developed using this benchmark suite to evaluate them
and the suite was designed to evaluate model checkers so there is some bias
in the choice of benchmarks.
Of the programs with one bug, 375 of them have some symbolic stub functions
that make them unusable with test programs.

To enable the comparision, all the tools were given a common interface
to convert tests into a standard format and to generate witnesses.

The results are presented in a cactus plot (as in [SV competition])
and then broken down in more detail in a table.
The clear winners are the model checkers although [KLEE verifier] is
competitive.
Well regarded fuzz testers like AFL-Fuzz find less than 80% of the bugs
found by the works of the model checkers. (That is 80% after excluding
the benchmarks that include symbolic stub functions.)

The results also present the total number of bugs found by all testers,
by all model checkers and by all tools.

- All the testers find around 7% more bugs than the best tester ([KLEE
  verifier]).
- All the model checkers find about 12-15% more bugs than the best
  model checker (ESBMC-incr).
- All the tools find 20-25% more bugs than the best tool (ESBMC-incr).

The observation that all the tools are better than the best tools
is an argument for portfolio test generators and hybrid fuzzer/model-checkers.

{% include links.html %}
