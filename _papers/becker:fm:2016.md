---
ENTRYTYPE: inproceedings
added: 2019-11-21
authors:
- Hanno Becker
- Juan Manuel Crespo
- Jacek Galowicz
- Ulrich Hensel
- Yoichi Hirai
- César Kunz
- Keiko Nakata
- Jorge Luis Sacchini
- Hendrik Tews
- Thomas Tuerk
booktitle: International Symposium on Formal Methods
doi: 10.1007/978-3-319-48989-6_5
layout: paper
organization: Springer
pages: 69-84
read: true
readings:
- 2019-11-19
title: Combining mechanized proofs and model-based testing in the formal analysis
  of a hypervisor
year: 2016
topics:
- os
- security
- verification
---

Describes formal verification in Coq of a model of the commercial NOVA micro-hypervisor.
NOVA is a hypervisor in the L4 family that supports DMA access (protected
by IOMMU).
Very extensive testing is used to compare the model against the actual
implementation using over 12 million conformance tests.

The main properties proved are security properties: authority confinement, memory confinement.
To support this, they prove invariants:
a consistency invariant,
no dangling-pointers, 
semaphore consistency relating thread state to semaphore state,
...

This process found around 2 dozen bugs in the hypervisor source code.
Half were found during code review as part of the model construction process.
Half were found while debugging the model against the implementation.
In addition, they found roughly as many bugs in their model.
_It is not clear whether the construction of proofs found any bugs so I wonder
if N-version programming would have most of the same benefit (assuming that
the second version is written in an expressive high-level language)._

Not mentioned in the paper is that the project was cancelled due to a change in company plans.
Unusually, the affiliation on the paper says that the authors' employers wish to remain anonymous.
