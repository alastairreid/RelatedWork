---
layout: note
title: Fuzz testing
wiki: https://en.wikipedia.org/wiki/Fuzzing
notes:
- symbolic execution
- DART verifier
- KLEE verifier
papers:
- godefroid:cacm:2020
- manes:ieeetse:2019
- miller:cacm:1990
---

Testing a piece of code with a broad range of
unexpected inputs typically done to find security
vulnerabilities.
Unlike traditional testing, it uses less human understanding
of the program and is often performed by non-developers of the code.

See the surveys for more detail: [godefroid:cacm:2020], [manes:ieeetse:2019].

Programs are often instrumented to detect more errors (e.g.,
address/memory/UB/thread sanitizers, control-flow integrity, etc.).

Three types of fuzzer based on how much knowledge of
the program under test they exploit.

- blackbox fuzzing
- greybox fuzzing
  - coverage guided such as EFS, Randoop, AFL, VUzzer
- whitebox fuzzing
  - [symbolic execution] such as [DART verifier] and [KLEE verifier]
  - taint analysis that determines dependencies of branches on
    particular parts of input
- hybrid fuzzers alternate between white- and grey-box fuzzing
  e.g., Driller

Related concept of random test generation differs in that there
may be more focus on generating inputs that are restricted in
some way. For example, we might want to restrict to syntactically legal
inputs.
So we get concepts like

- "rejection sampling" – retry generating a value until it satisfies some
  predicate.
- grammar-based generation and discovering grammars
- use of dictionaries

{% include links.html %}
