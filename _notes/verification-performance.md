---
layout: note
notes:
- verification profiling
- verifier performance
- symbolic evaluation
- bounded model checking
- symbolic execution
- state merging
- case splitting
- Rosette solver
- KLEE verifier
- Swarm verification
papers:
- galea:arxiv:2018
- bornholt:oopsla:2018
- goodman:ndss:2018
- holzmann:ieeetse:2011
- siddiqui:oopsla:2012
title: Verification performance of code
---

Optimizations of code to make it easier to verify.
(For optimizations performed automatically by an automatic verification tools, see [verifier performance].)

- [case splitting]
  - [goodman:ndss:2018]
- Parallelism
  - siddiqui:oopsla:2012
  - [Swarm verification]
    - [holzmann:ieeetse:2011]
    - [goodman:ndss:2018]
- [state merging]
- lazy symbolic execution
  - [trabish:icse:2018]

{% include links.html %}
