---
ENTRYTYPE: misc
added: 2021-06-12
archiveprefix: arXiv
authors:
- Joxan Jaffar
- Rasool Maghareh
- Sangharatna Godboley
- Xuan-Linh Ha
eprint: '2012.00556'
layout: paper
primaryclass: cs.PL
read: true
readings:
- 2021-06-12
title: 'TracerX: Dynamic symbolic execution with interpolation'
year: 2020
notes:
- symbolic execution
- interpolation
- KLEE verifier
- state merging
- SMT solver
- CBMC verifier
- LLBMC verifier
papers:
- kuznetsov:pldi:2012
---

The big problem with dynamic [symbolic execution] is the exponential path explosion
resulting from visiting each path independently.
One approach is [state merging] (e.g., [kuznetsov:pldi:2012]) which merges similar
states so that paths can be brought back together so that the merged path only needs to be explored once.

The approach in this paper is path pruning that works by recognizing that
sufficiently similar previously explored path did not fail and so it is not
necessary to explore the current path.  Specifically, they learn what paths are
safe (and therefore do not need to be explored again) as follows:

- after exploring a non-failing path from some program point, they calculate an
  approximate weakest precondition for the non-failing path and store this
  condition in a cache;
- on future visits to the same program point, they can skip the path if the
  current path condition matches a previously  learned precondition.

Interestingly, this requires them to alternate between the normal forwards
exploration used in dynamic symbolic execution and a backwards exploration used to
calculate the weakest precondition.


This approach builds on much earlier work by (some of) the same authors
but improves on it in two ways:

1. It is implemented on top of [KLEE][KLEE verifier] which makes it possible to
   apply it to larger, more interesting codebases.

2. There is a significant benefit in creating *conjunctive* queries for the SMT
   solver so the approximation goes to some lengths to avoid the more natural
   but significantly less efficient *disjunctions* that arise from program
   forks.
   (I think that I should re-read this discussion because it seems to be an important
   thing to understand about SMT solvers.)

The tool is compared against [CBMC verifier] and [LLBMC verifier] and found to
be sometimes significantly faster (100x), occasionally slower (0.1x) and,
overall, an improvement.


{% include links.html %}
