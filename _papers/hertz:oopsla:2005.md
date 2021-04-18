---
ENTRYTYPE: inproceedings
abstract: 'Garbage collection yields numerous software engineering benefits, but its quantitative impact on performance remains elusive. One can compare
  the cost of conservative garbage collection to explicit memory management in C/C++ programs by linking in an appropriate collector. This kind of direct
  comparison is not possible for languages designed for garbage collection (e.g., Java), because programs in these languages naturally do not contain calls
  to free. Thus, the actual gap between the time and space performance of explicit memory management and precise, copying garbage collection remains unknown.We
  introduce a novel experimental methodology that lets us quantify the performance of precise garbage collection versus explicit memory management. Our
  system allows us to treat unaltered Java programs as if they used explicit memory management by relying on oracles to insert calls to free. These oracles
  are generated from profile information gathered in earlier application runs. By executing inside an architecturally-detailed simulator, this "oracular"
  memory manager eliminates the effects of consulting an oracle while measuring the costs of calling malloc and free. We evaluate two different oracles:
  a liveness-based oracle that aggressively frees objects immediately after their last use, and a reachability-based oracle that conservatively frees objects
  just after they are last reachable. These oracles span the range of possible placement of explicit deallocation calls.We compare explicit memory management
  to both copying and non-copying garbage collectors across a range of benchmarks using the oracular memory manager, and present real (non-simulated) runs
  that lend further validity to our results. These results quantify the time-space tradeoff of garbage collection: with five times as much memory, an Appel-style
  generational collector with a non-copying mature space matches the performance of reachability-based explicit memory management. With only three times
  as much memory, the collector runs on average 17\% slower than explicit memory management. However, with only twice as much memory, garbage collection
  degrades performance by nearly 70\%. When physical memory is scarce, paging causes garbage collection to run an order of magnitude slower than explicit
  memory management.'
added: 2021-04-17
address: New York, NY, USA
authors:
- Matthew Hertz
- Emery D. Berger
booktitle: Proceedings of the 20th Annual ACM SIGPLAN Conference on Object-Oriented Programming, Systems, Languages, and Applications
doi: 10.1145/1094811.1094836
isbn: '1595930310'
keywords: explicit memory management, garbage collection, oracular memory management, performance analysis, paging, throughput, time-space tradeoff
layout: paper
link: https://doi.org/10.1145/1094811.1094836
location: San Diego, CA, USA
numpages: '14'
pages: 313-326
publisher: Association for Computing Machinery
read: true
readings:
- 2021-04-18
series: OOPSLA '05
title: Quantifying the performance of garbage collection vs. explicit memory management
url: https://doi.org/10.1145/1094811.1094836
year: 2005
notes:
- memory management
- garbage collection
papers:
---

This paper uses CPU performance simulators and oracles to measure the impact of replacing
Java's garbage collectors with explicit memory management.
They conclude that you need around 5x more physical memory before GC performs better than
explicit memory management, it is 17% worse at a mere 3x and  70% worse at 2x memory.

Their basic setup is to

1. measure object lifetimes in a heavily instrumented initial run
2. determine the earliest and latest times that each object could possibly be deallocated
   by finding the last time the object is accessed and the time when the object first
   becomes unreachable
3. perform two measurement runs where a conventional malloc/free-style memory allocator
   is used to deallocate objects at either the earliest or the latest possible time

The measurement runs are repeated with a variety of state of the art conventional memory
allocators and compared against performance with a variety of garbage collectors
that use mark-sweep, copying, generational and hybrid approaches.

They avoid interference from  the cost of their oracles by running this all in
a modified version of the SimpleScalar CPU simulator which allows them to
remove oracle time.  (But do they do anything to model the actual costs that an
explicit memory allocation scheme needs to use to decide when to deallocate
(reference counts, etc.)?)

Some of the costs that they are concerned with are impact on L1-D$, L2$, L3$
and virtual memory paging.
In particular, they emphasize

- the benefits of reusing recently allocated objects on cache miss rates (though later it seems this is not as conclusive as expected)
when using explicit memory allocation
- the disadvantages of periodically evicting recent objects from the memory cache
- the significant cost of visiting virtual memory pages during garbage collection
  that are outside the working set of the application itself

They observe that

- the cost of explicit memory management does not depend on heap size and
  is linear in the number of objects allocated
- (as expected) the GC runtime is inversely proportional
  to the reachable heap size for non-generational collectors
- (new observation) the GC runtime is inversely proportional to the heap size
  for generational collectors

They suggest future work of looking at region based allocators, BiBoP allocators
(to remove overhead of object headers) and of comparing pauses in explicit
memory allocators (when per-size quicklists are refilled) with the pauses
in various GCs and of concurrent GCs.

Overall conclusion: if you are running in a memory constrained environment
(can't allocate 5x more memory than needed) or are running on a shared machine
with other processes competing for physical memory, think twice about GC-based
languages.

{% include links.html %}
