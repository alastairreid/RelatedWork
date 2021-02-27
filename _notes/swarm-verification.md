---
layout: note
notes:
- verifier performance
- verification performance
- bounded model checking
- case splitting
papers:
- holzmann:ieeetse:2011
- groce:issta:2012
- goodman:ndss:2018
- siddiqui:oopsla:2012
- qiu:icse:2017
title: Swarm verification
---

Splitting an automated verification problem into pieces that can be tackled in parallel
using a diverse set of configurations so that they can explore the search space
more quickly and thoroughly.
In the [original paper][holzmann:ieeetse:2011], the different runs were overlapping
and there was some probablity of duplicated effort.

I think that a part of the benefit comes from increased search velocity early in
a run so a small number of runs exploring different parts of the search space will
have higher coverage.

- The Swarm Verification paper ([holzmann:ieeetse:2011]) is interested
  in finding violations by maximizing coverage within some time limit and
  runs multiple diverse copies of the problem: using random seeds, 
  different parameters to heuristics, etc.
  to achieve diversity.

- In [bounded model checking] of hardware, I have seen this done by varying the bounds.
  in a so-called "B swarm".

  Each instance would check some range of bounds from `B` to `B+K`
  by unrolling the circuit `B-1` times without inserting checks
  and then unrolling the circuit a further `K` times with checks.

  This relied on the fact that the unrolled copies without checks would
  be evaluated faster than the copies with checks.

An interesting variant of swarm *verification* is swarm *testing*
([groce:issta:2012]) that relies on "feature omission diversity" to improve
testing: generating tests that only exercise a subset of the features of the
system. The key insight there is that features can *suppress* bugs as well as
*activating* bugs so tests that randomly omit some features from testing can
have a higher chance of catching some bugs. They suggest that this can also be
used with model-checking and/or combined with swarm verification.

Some slightly different techniques to achieve parallelism achieve diversity by
configuring verification so that there is no overlap (not just *probably* no
overlap).  Like swarm verification, there is no need to coordinate between jobs
running in parallel but I am not clear whether they are really 'swarm
verification' or just parallel verification that scales well.

- The Ranged Analysis paper ([siddiqui:oopsla:2012]) dynamically decides how
  to partition a symbolic execution task using work-stealing.

  They did not combine it with [bounded model checking] but they suggest
  doing so in the future work section comparing the "horizontal"
  divisions created by bounded model checking with the "vertical"
  divisions created by ranged analysis.

  [qiu:icse:2017] adds an initial phase of uniprocessor execution using
  a breadth-first(ish) schedule to
  identify/eliminate infeasible paths. This allows some sharing of the
  discoveries of the constraint solver.

- [Case splitting] can be used to split a problem into parallel instances
  ([goodman:ndss:2018]) although this takes more manual intervention
  and understanding of the problem.

{% include links.html %}
