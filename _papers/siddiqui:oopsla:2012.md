---
ENTRYTYPE: inproceedings
abstract: 'This paper introduces a novel approach to scale symbolic execution -- a program analysis technique for systematic exploration of bounded execution
  paths--for test input generation. While the foundations of symbolic execution were developed over three decades ago, recent years have seen a real resurgence
  of the technique, specifically for systematic bug finding. However, scaling symbolic execution remains a primary technical challenge due to the inherent
  complexity of the path-based exploration that lies at core of the technique.Our key insight is that the state of the analysis can be represented highly
  compactly: a test input is all that is needed to effectively encode the state of a symbolic execution run. We present ranged symbolic execution, which
  embodies this insight and uses two test inputs to define a range, i.e., the beginning and end, for a symbolic execution run. As an application of our
  approach, we show how it enables scalability by distributing the path exploration--both in a sequential setting with a single worker node and in a parallel
  setting with multiple workers. As an enabling technology, we leverage the open-source, state-of-the-art symbolic execution tool KLEE. Experimental results
  using 71 programs chosen from the widely deployed GNU Coreutils set of Unix utilities show that our approach provides a significant speedup over KLEE.
  For example, using 10 worker cores, we achieve an average speed-up of 6.6X for the 71 programs.'
added: 2021-02-25
address: New York, NY, USA
authors:
- Junaid Haroon Siddiqui
- Sarfraz Khurshid
booktitle: Proceedings of the ACM International Conference on Object Oriented Programming Systems Languages and Applications
doi: 10.1145/2384616.2384654
isbn: '9781450315616'
keywords: test input as analysis state, klee, ranged analysis, parallel symbolic execution
layout: paper
link: https://doi.org/10.1145/2384616.2384654
location: Tucson, Arizona, USA
numpages: '14'
pages: 523-536
publisher: Association for Computing Machinery
read: true
readings:
- 2021-02-25
series: OOPSLA '12
title: Scaling symbolic execution using ranged analysis
url: https://doi.org/10.1145/2384616.2384654
year: 2012
notes:
- symbolic execution
- case-splitting
- KLEE verifier
- bounded model checking
papers:
- qiu:icse:2017
---

Key insights: a path can be encoded by a concrete test input;
a set of paths can be encoded by a pair of paths (all paths lexicographically between the two paths).

These insights enable *ranged symbolic execution*: partitioning the search space into a number of
ranges.
The only redundant work performed when using this approach to partition the set of paths is
redundant exploration of the boundaries between sets (i.e., the limits of the ranges).
This is most useful when doing a exhaustive exploration of all paths because it requires
a fixed branch exploration ordering which conflicts with use of search heuristics used
for partial explorations.

Some uses:

- Resumable symbolic execution: pausing SE at any time and restarting later.
- Parallel symbolic execution.
- Dynamic range refinement that performs parallel symbolic execution
  using work stealing.

Notes:

- When comparing two paths, it is best to exploit their common prefix to avoid
  repeating that work.
- Turning test inputs into paths seems to have some of the flavour of concolic
  execution.
- There is a restriction involving finite paths - not sure this is fundamental
  though.
- Evaluation
  - Implemented in KLEE, evaluated on standard KLEE testsuite of CoreUtils
    using the 71 programs where KLEE hits more than 100 paths in ten minutes.
  - Results are the min, max and (arithmetic?) average of five runs running on
    ten cores.
    - Average speedup (arithmetic? geometric?) on 10 cores is 6.6x.  Peak
      speedup is 17.7x due to improved hit rates in KLEE's internal caches.
  - To explore scaling on 1, 5, 10 and 20 cores, they use a subset of 5 worst,
    5 median, 5 best programs based on the ten core results.
    - The worst don't show any scaling, the best exhibit the same
      superlinear scaling and reach up to 22x.
    - Eyeballing the data, there seems to be an obvious knee in the curves
      around 8 cores.

Future work suggests other uses of *ranged symbolic execution* such as

- Using binary search to find the range of paths that encloses some code change
- Creating ensemble analysis tools that use paths to communicate what
  work each tool has succeeded or failed at so that tools can try where
  others have failed.
- Applying the technique to software model checking to divide the space
  "vertically" instead of the "horizontal" divisions used in [bounded model checking].

The conclusion makes the following interesting observation

> But [symbolic execution normally explores the connection between symbolic
> execution and tests] in just one direction: from symbolic
> execution to tests. The key novelty of our work is to establish
> the connection in the opposite direction—from a test input
> to symbolic execution—specifically, to use a test input to
> encode the state of a run of symbolic execution—and show
> how this direction enables a number of novel approaches for
> more effective symbolic execution for test input generation.


{% include links.html %}
