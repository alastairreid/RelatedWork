---
ENTRYTYPE: article
abstract: While mixed integer linear programming (MILP) solvers are routinely used to solve a wide range of important science and engineering problems,
  it remains a challenging task for end users to write correct and efficient MILP constraints, especially for problems specified using the inherently non-linear
  Boolean logic operations. To overcome this challenge, we propose a syntax guided synthesis (SyGuS) method capable of generating high-quality MILP constraints
  from the specifications expressed using arbitrary combinations of Boolean logic operations. At the center of our method is an extensible domain specification
  language (DSL) whose expressiveness may be improved by adding new integer variables as decision variables, together with an iterative procedure for synthesizing
  linear constraints from non-linear Boolean logic operations using these integer variables. To make the synthesis method efficient, we also propose an
  over-approximation technique for soundly proving the correctness of the synthesized linear constraints, and an under-approximation technique for safely
  pruning away the incorrect constraints. We have implemented and evaluated the method on a wide range of benchmark specifications from statistics, machine
  learning, and data science applications. The experimental results show that the method is efficient in handling these benchmarks, and the quality of the
  synthesized MILP constraints is close to, or higher than, that of manually-written constraints in terms of both compactness and solving time.
added: 2023-07-02
address: New York, NY, USA
articleno: '184'
authors:
- Jingbo Wang
- Aarti Gupta
- Chao Wang
doi: 10.1145/3591298
issue_date: June 2023
journal: Proc. ACM Program. Lang.
keywords: Data Science, Statistics, Machine Learning, Syntax Guided Synthesis
layout: paper
link: https://doi.org/10.1145/3591298
month: jun
number: PLDI
numpages: '24'
publisher: Association for Computing Machinery
read: false
readings: []
title: Synthesizing MILP constraints for efficient and robust optimization
url: https://doi.org/10.1145/3591298
volume: '7'
year: 2023
notes:
- SMT solver
- MILP solver
papers:
---

Optimizes constraints that combine both integer and real constraints and use boolean operators.
(Boolean operators are especially tricky because they are highly non-linear.)

Three steps

1. Strengthen DSL by iterative decomposition
2. Select good candidates on convex hull
3. (Soundly) Prune infeasible candidates


{% include links.html %}
