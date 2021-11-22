---
ENTRYTYPE: article
abstract: 'ARM has a relaxed memory model, previously specified in informal prose for ARMv7 and ARMv8. Over time, and partly due to work building formal
  semantics for ARM concurrency, it has become clear that some of the complexity of the model is not justified by the potential benefits. In particular,
  the model was originally non-multicopy-atomic: writes could become visible to some other threads before becoming visible to all - but this has not been
  exploited in production implementations, the corresponding potential hardware optimisations are thought to have insufficient benefits in the ARM context,
  and it gives rise to subtle complications when combined with other ARMv8 features. The ARMv8 architecture has therefore been revised: it now has a multicopy-atomic
  model. It has also been simplified in other respects, including more straightforward notions of dependency, and the architecture now includes a formal
  concurrency model. In this paper we detail these changes and discuss their motivation. We define two formal concurrency models: an operational one, simplifying
  the Flowing model of Flur et al., and the axiomatic model of the revised ARMv8 specification. The models were developed by an academic group and by ARM
  staff, respectively, and this extended collaboration partly motivated the above changes. We prove the equivalence of the two models. The operational model
  is integrated into an executable exploration tool with new web interface, demonstrated by exhaustively checking the possible behaviours of a loop-unrolled
  version of a Linux kernel lock implementation, a previously known bug due to unprevented speculation, and a fixed version.'
added: 2021-11-22
address: New York, NY, USA
articleno: '19'
authors:
- Christopher Pulte
- Shaked Flur
- Will Deacon
- Jon French
- Susmit Sarkar
- Peter Sewell
doi: 10.1145/3158107
issue_date: January 2018
journal: Proc. ACM Program. Lang.
keywords: Semantics, Operational, Relaxed Memory Models, Axiomatic
layout: paper
link: https://doi.org/10.1145/3158107
month: dec
number: POPL
numpages: '29'
publisher: Association for Computing Machinery
read: false
readings: []
title: 'Simplifying ARM concurrency: Multicopy-atomic axiomatic and operational models for ARMv8'
url: https://doi.org/10.1145/3158107
volume: '2'
year: 2017
notes:
- Arm architecture
- weak memory
- ISA specification
papers:
---
{% include links.html %}
