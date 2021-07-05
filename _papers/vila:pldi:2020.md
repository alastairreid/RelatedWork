---
ENTRYTYPE: inproceedings
abstract: We show how to infer deterministic cache replacement policies using off-the-shelf automata learning and program synthesis techniques. For this,
  we construct and chain two abstractions that expose the cache replacement policy of any set in the cache hierarchy as a membership oracle to the learning
  algorithm, based on timing measurements on a silicon CPU. Our experiments demonstrate an advantage in scope and scalability over prior art and uncover
  two previously undocumented cache replacement policies.
added: 2021-07-05
address: New York, NY, USA
authors:
- Pepe Vila
- Pierre Ganty
- Marco Guarnieri
- Boris Köpf
booktitle: Proceedings of the 41st ACM SIGPLAN Conference on Programming Language Design and Implementation
doi: 10.1145/3385412.3386008
isbn: '9781450376136'
keywords: Program Synthesis, Automata Learning, Reverse Engineering, Cache Replacement Policies
layout: paper
link: https://doi.org/10.1145/3385412.3386008
location: London, UK
numpages: '14'
pages: 519-532
publisher: Association for Computing Machinery
read: true
readings:
- 2021-07-05
series: PLDI 2020
title: 'CacheQuery: Learning replacement policies from hardware caches'
url: https://doi.org/10.1145/3385412.3386008
year: 2020
notes:
- hardware
- side channel
papers:
---

Uses Angluin-style learning to synthesize a model of hardware cache eviction policies.
Models are readable.
Evaluated on a simulator to test what policies it can learn and
also on x86 cores to learn L1, L2 and L3 policies and found two new eviction policies.

On the L3 cache that has adaptive policies (i.e., a follower policy is used to
select between multiple leader policies), it only learns

Built as a set of components, that solve different parts of the problem.

- POLCA is the learning algorithm.
  Built using the off-the-shelf "LearnLib" tool.
  The classic algorithm requires an equivalence test that is not available
  in hardware but can be approximated using m-complete test suites (that can
  detect differences between policies with up to m control states)
  and then further approximating to avoid an exponential blowup.

- MemBlockLang is a language for describing queries consisting of
  blocks to be profiled and blocks to be invalidated using clflush.

- CacheQuery's frontend is a python script that can run as an interactive
  REPL or in batch mode.
  This is sometimes (always?) run on a separate machine to reduce noise
  and(?) increase performance.

- CacheQuery's backend is a Linux Kernel Module that runs queries in
  a low-noise environment using performance/cycle counters, handling
  V-to-P translations, evicting caches above the one being profiled,
  turns off prefetching, hyper-threads, DVFS, other cores, collisions between
  instructions and data, etc.

- Explainable policies are created using syntax-guided synthesis to
  fill holes in templates for four separate operations: promote,
  evict, insert and normalize.
  The templates and the grammars used for synthesis limit the
  policies that can be learned (in particular, excluding states with
  global control state such as PLRU).

  Explainable policies are easier to compare against known policies
  to find new policies.

Runtimes on real hardware vary from 10s of seconds to several days.

{% include links.html %}
