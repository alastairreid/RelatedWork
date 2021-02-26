---
layout: note
notes:
- verification performance
- verifier performance
- symbolic evaluation
- bounded model checking
- symbolic execution
- state merging
- case splitting
- Rosette solver
- KLEE verifier
papers:
- galea:arxiv:2018
- bornholt:oopsla:2018
- beyer:ase:2019
title: Verification profiling of code
---

Just as program execution has hotspots that we can use execution profiling
to identify, (automatic) verification of code has hotspots that
we would like to find using verification profilers.

[galea:arxiv:2018] identifies the following requirements: generality
(of profiling model), explainable (independent of internal details),
and actionable (finds root causes).

Profilers in existing systems

- [KLEE verifier] has profiling described in [galea:arxiv:2018]
  and in the detailed [KLEE testing CoreUtils] tutorial.

  KLEE dumps around 10 statistics about each line in the format
  used by [KCachegrind]: covered, uncovered, time, solver time,
  successful solver queries, unsuccessful solver queries, forks,
  etc.

- [Rosette solver] has the SymPro profiler described in
  detail by [bornholt:oopsla:2018] and based on a simple
  profiling API.

  This is based on some of the same metrics as KLEE but
  it adds more detail about the fan-in and fan-out of the
  graph to get more insight into splits and joins.
  It also tracks the number of terms created but never used.

- Jalanji also implements the SymPro profiler API.

Profiling seems to be a bit like profiling lazy functional
languages: you are often more interested in where a symbolic
term was constructed than in where it was evaluated and, like
lazy execution, just looking at where a verifier spends time
will tend to show you where it was evaluated (in a solver).





{% include links.html %}

[KLEE testing CoreUtils]: https://klee.github.io/tutorials/testing-coreutils/
[KCachegrind]: https://kcachegrind.github.io/html/Home.html
