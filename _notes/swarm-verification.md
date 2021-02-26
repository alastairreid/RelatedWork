---
layout: note
notes:
- verifier performance
- verification performance
- bounded model checking
- case splitting
papers:
- holzmann:ieeetse:2011
- goodman:ndss:2018
- siddiqui:oopsla:2012
- qiu:icse:2017
title: Swarm verification
---

*[Todo: need to go back to [holzmann:ieeetse:2011] that introduced the term
and check that all the things I say below are "swarm" verification specifically
and not just "parallel verification".]*

Splitting a verification problem into pieces that can be tackled in parallel.
In particular, largely automatic techniques that exploit some parameter and
invoke multiple copies of the verifier with different parameter values and with
little/no overlap in what each instance is checking.

- In [bounded model checking] of hardware, I have seen this done by varying the bounds.
  in a so-called "B swarm".

  Each instance would check some range of bounds from `B` to `B+K`
  by unrolling the circuit `B-1` times without inserting checks
  and then unrolling the circuit a further `K` times with checks.

  This relied on the fact that the unrolled copies without checks would
  be evaluated faster than the copies with checks.

- The Swarm Verification paper ([holzmann:ieeetse:2011]) is interested
  in finding violations by maximizing coverage within some time limit and
  runs multiple diverse copies of the problem: using random seeds, 
  different parameters to heuristics, etc.
  to achieve diversity.

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
