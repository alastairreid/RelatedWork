---
ENTRYTYPE: inproceedings
abstract: 'Previous work on the semantics of relaxed shared-memory concurrency has only considered the case in which each load reads the data of exactly
  one store. In practice, however, multiprocessors support mixed-size accesses, and these are used by systems software and (to some degree) exposed at the
  C/C++ language level. A semantic foundation for software, therefore, has to address them. We investigate the mixed-size behaviour of ARMv8 and IBM POWER
  architectures and implementations: by experiment, by developing semantic models, by testing the correspondence between these, and by discussion with ARM
  and IBM staff. This turns out to be surprisingly subtle, and on the way we have to revisit the fundamental concepts of coherence and sequential consistency,
  which change in this setting. In particular, we show that adding a memory barrier between each instruction does not restore sequential consistency. We
  go on to extend the C/C++11 model to support non-atomic mixed-size memory accesses. This is a necessary step towards semantics for real-world shared-memory
  concurrent code, beyond litmus tests.'
added: 2021-11-22
address: New York, NY, USA
authors:
- Shaked Flur
- Susmit Sarkar
- Christopher Pulte
- Kyndylan Nienhuis
- Luc Maranget
- Kathryn E. Gray
- Ali Sezgin
- Mark Batty
- Peter Sewell
booktitle: Proceedings of the 44th ACM SIGPLAN Symposium on Principles of Programming Languages
doi: 10.1145/3009837.3009839
isbn: '9781450346603'
keywords: ISA, Relaxed Memory Models, semantics, mixed-size
layout: paper
link: https://doi.org/10.1145/3009837.3009839
location: Paris, France
numpages: '14'
pages: 429-442
publisher: Association for Computing Machinery
read: false
readings: []
series: POPL 2017
title: 'Mixed-size concurrency: ARM, POWER, C/C++11, and SC'
url: https://doi.org/10.1145/3009837.3009839
year: 2017
notes:
- ISA specification
- instruction set architecture
- Arm architecture
- PowerPC architecture
papers:
---
{% include links.html %}
