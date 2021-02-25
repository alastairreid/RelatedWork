---
ENTRYTYPE: inproceedings
abstract: Symbolic execution has proven to be a practical technique for building automated test case generation and bug finding tools. Nevertheless, due
  to state explosion, these tools still struggle to achieve scalability. Given a program, one way to reduce the number of states that the tools need to
  explore is to merge states obtained on different paths. Alas, doing so increases the size of symbolic path conditions (thereby stressing the underlying
  constraint solver) and interferes with optimizations of the exploration process (also referred to as search strategies). The net effect is that state
  merging may actually lower performance rather than increase it.We present a way to automatically choose when and how to merge states such that the performance
  of symbolic execution is significantly increased. First, we present query count estimation, a method for statically estimating the impact that each symbolic
  variable has on solver queries that follow a potential merge point; states are then merged only when doing so promises to be advantageous. Second, we
  present dynamic state merging, a technique for merging states that interacts favorably with search strategies in automated test case generation and bug
  finding tools.Experiments on the 96 GNU Coreutils show that our approach consistently achieves several orders of magnitude speedup over previously published
  results. Our code and experimental data are publicly available at http://cloud9.epfl.ch.
added: 2021-02-24
address: New York, NY, USA
authors:
- Volodymyr Kuznetsov
- Johannes Kinder
- Stefan Bucur
- George Candea
booktitle: Proceedings of the 33rd ACM SIGPLAN Conference on Programming Language Design and Implementation
doi: 10.1145/2254064.2254088
isbn: '9781450312059'
keywords: state merging, bounded software model checking, testing, symbolic execution, verification
layout: paper
link: https://doi.org/10.1145/2254064.2254088
location: Beijing, China
numpages: '12'
pages: 193-204
publisher: Association for Computing Machinery
read: true
readings:
- 2021-02-25
series: PLDI '12
title: Efficient state merging in symbolic execution
url: https://doi.org/10.1145/2254064.2254088
year: 2012
notes:
- symbolic execution
- symbolic evaluation
- bounded model checking
- verification condition generator
- KLEE verifier
- state merging
papers:
---

Classic [symbolic execution] suffers from path explosions due to forking the state on every conditional branch.
This paper explores how to selectively merge states to push symbolic execution further along the [symbolic evaluation]
spectrum while stopping short of merging states at every join point as in [bounded model checking].
By not merging at every join point, they aim to retain the benefits of high levels of concrete execution,
simpler solver queries and flexibility of search strategies to explore the most interesting paths first.

The main ideas are "Query Count Estimation" (estimating how often a variable will appear in future queries)
which is used to decide which differences between states matter most and "Dynamic State Merging"
which opportunistically merges similar states.

The paper has a nice overview of the design space of symbolic program analysis based on how the following
are handled: loops/recursion; whether and how feasibility of branches is checked to avoid encoding infeasible branches;
whether and how states from different paths are merged; and compositionality.
With the exception of compositionality, this is captured in Algorithm~1 that presents a generic algorithm parameterized by
a scheduling function, a state similarity relation and a branch checker.
This is able to capture search based [symbolic execution] (as in KLEE and DART), [bounded model checking],
static state merging of [verification condition generator]s, and function summaries (which can be seen as
merging states at the end of a function).

Query Count Estimation (QCE) uses a preprocessing step to count the number of times
each variable is used in a branch conditition in later parts of the CFG.
The calculation is parameterized by the fraction of branches that lead to solver queries,
the probability that branches are feasible, and an iteration bound.
There is an optional further parameter to handle the added query cost of ite expressions.

Dynamic State Merging (DSM) decides which states to schedule next by looking at
the predecessors of states (within some bound) and prioritizing execution of
states that are similar to that predecessor. This causes states that are
similar to the predecessor of a state to be fast-forwarded so that we can check
whether the successor state is similar with the idea that this deviation from
the primary search strategy will probably be worthwhile.
To reduce costs, DSM exploits knowledge of the QCE-based similarity relation
to only store relevant parts of predecessor states.

This was implemented in the [KLEE verifier] and evaluated on the standard KLEE benchmarks
(the CoreUtils suite of commands: cp, mv, sort, cut, test, etc. - 82 tools in total).
QCE+DSM improves scaling (number of paths explored in fixed time) to increase by orders of magnitude (up to 10^11).
(A few slow down a little (due to ite expressions) and a few crash.)
The paper measures the sensitivity to some of the QCE parameters and how much
DSM interferes with the primary search strategy (e.g., maximizing coverage).

They speculate that this approach can be adapted to other forms of symbolic evaluation.

{% include links.html %}
