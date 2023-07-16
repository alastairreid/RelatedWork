---
ENTRYTYPE: article
abstract: Although functional programming languages simplify writing safe parallel programs by helping programmers to avoid data races, they have traditionally
  delivered poor performance. Recent work improved performance by using a hierarchical memory architecture that allows processors to allocate and reclaim
  memory independently without any synchronization, solving thus the key performance challenge afflicting functional programs. The approach, however, restricts
  mutation, or memory effects, so as to ensure "disentanglement", a low-level memory property that guarantees independence between different heaps in the
  hierarchy. This paper proposes techniques for supporting entanglement and for allowing functional programs to use mutation at will. Our techniques manage
  entanglement by distinguishing between disentangled and entangled objects and shielding disentangled objects from the cost of entanglement management.
  We present a semantics that formalizes entanglement as a property at the granularity of memory objects, and define several cost metrics to reason about
  and bound the time and space cost of entanglement. We present an implementation of the techniques by extending the MPL compiler for Parallel ML. The extended
  compiler supports all features of the Parallel ML language, including unrestricted effects. Our experiments using a variety of benchmarks show that MPL
  incurs a small time and space overhead compared to sequential runs, scales well, and is competitive with languages such as C++, Go, Java, OCaml. These
  results show that our techniques can marry the safety benefits of functional programming with performance.
added: 2023-07-02
address: New York, NY, USA
articleno: '170'
authors:
- Jatin Arora
- Sam Westrick
- Umut A. Acar
doi: 10.1145/3591284
issue_date: June 2023
journal: Proc. ACM Program. Lang.
keywords: memory management, functional programming, parallel, concurrent
layout: paper
link: https://doi.org/10.1145/3591284
month: jun
number: PLDI
numpages: '26'
publisher: Association for Computing Machinery
read: false
readings: []
title: Efficient parallel functional programming with effects
url: https://doi.org/10.1145/3591284
volume: '7'
year: 2023
notes:
- garbage collection
- parallelism
- effects
papers:
---

Problem: memory management overheads due to handling pointers between the heap used by each thread.
(Locking overheads, etc)

Key terminology: "entanglement": threads have to cooperate in order to perform garbage collection.
We want "disentangled" objects for performance and to be able to distinguish them from "entangled"
objects so that object sharing overheads are proportional to the amount of entanglement.
(Specifically, read/write barrier techniques only need to be used on entangled pointers.)

Threads in Parallel ML (MPL) form a hierarchy (I think because the language uses a form of fork-join
concurrency). We can classify entangled pointers as either up-pointers (it came from parent thread),
down-pointers (it points to child thread) or cross-pointers (everything else).

The bulk of the paper is about the cost model, GC implementation and the performance evaluation.
The evaluation compares performance against other (non-functional) parallel languages
and evaluates the relativecost of entangled and disentangled pointers.

{% include links.html %}
