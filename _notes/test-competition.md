---
layout: note
title: Software Testing Competition (Test-Comp)
website: https://test-comp.sosy-lab.org/2020/
notes:
- FQL
- KLEE verifier
- SV competition
---

TestComp is an annual competition between automated software
verification tools that has been running since 2019.
It uses the same tests and program annotations as [SV competition].
Results and tool descriptions are published in 

A subset of FQL is used to specify problems of two forms:

- Bug finding: generate tests that call the function "_VERIFIER_error".
- Coverage: generate tests that cover all branches of the program.
  - uses the
    [testcov](https://gitlab.com/sosy-lab/software/test-suite-validator)
    tool to evaluate test coverage

The test programs are taken from [SV competition] and are

- Reachability tests - I think on small programs
- Software systems tests - larger, more realistic code like busybox, Linux
  drivers, SQLite.
- Termination (on smaller programs?)

In 2020, the winners were VeriFuzz and LibKluzzer. Their
scores were very close. They were both based on combining fuzzers
with symbolic execution to handle complex conditions.


{% include links.html %}
