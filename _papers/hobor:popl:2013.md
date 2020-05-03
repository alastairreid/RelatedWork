---
ENTRYTYPE: inproceedings
added: 2020-02-14
address: New York, NY, USA
authors:
- Aquinas Hobor
- Jules Villard
booktitle: Proceedings of the 40th Annual ACM SIGPLAN-SIGACT Symposium on Principles
  of Programming Languages
doi: 10.1145/2429069.2429131
isbn: '9781450318327'
keywords: modularity, heap/shape, aliasing, separation logic
layout: paper
location: Rome, Italy
numpages: '14'
pages: 523-536
publisher: Association for Computing Machinery
read: true
readings:
- 2020-03-01
series: POPL '13
title: The ramifications of sharing in data structures
url: https://doi.org/10.1145/2429069.2429131
year: 2013
topics:
- verification
notes:
- magic wand
- permission logic
- separation logic
- frame rule
papers:
- krishnaswami:tldi:2010
---

This paper tackles a generalized form of the
[ramification problem][krishnaswami:tldi:2010].
That is, it tackles the problem that separation logic is good at
reasoning about pointer-based structures such as trees when you can split
the heap into disjoint parts but separation logic's weakness had been
reasoning about structures such as dags that rely on sharing.
In particular, reasoning about something like a garbage collector
has been hard.

The _power_ of separation logic comes from the FRAME rule

                 {P} c {Q}
    ———————————————————————————————————   FRAME
             {F ∗ P} c {F ∗ Q}

This rule lets us use local reasoning "{P} c {Q}" to reason about
a small part of the heap by separating this small part from "F" –
the rest of the heap.
The problem is that, sometimes, we cannot cleanly separate the two
– and that is the _weakness_ of separation logic.

The solution in this paper is a new verification rule that they call
RAMIFY that provides an alternative to separation logic's FRAME rule.

    {P} c {Q}       R ⊢ P ∗ (Q ——∗ R')
    ———————————————————————————————————   RAMIFY
                 {R} c {R'}

Like the FRAME rule, this let's us use local reasoning "{P} c {Q}"
about a small part of the heap.
But, unlike the FRAME rule, it does not require that we can cleanly
separate the local part "P" from the global part "Q".
Instead, we need to reason about the relationship between
the global pre/post-conditions "R"/"R'" and the local
pre/post-conditions "P"/"Q".

This paper uses reasoning about marking nodes in a DAG as the
main example to develop/illustrate this approach.
To demonstrate the power of the technique though, they
reason about the Cheney 2-space garbage collection algorithm.

{% include links.html %}
