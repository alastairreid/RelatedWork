---
ENTRYTYPE: inproceedings
abstract: Verification of modern microprocessors is a complex task that requires a substantial allocation of resources. Despite significant progress in
  formal verification, the goal of complete verification of an industrial design has not been achieved. In this paper, we describe a current contribution
  of formal methods to the validation of modern x86 microprocessors at Centaur Technology. We focus on proving correctness of instruction implementations,
  which includes the decoding of an instruction, its translation into a sequence of micro-operations, any subsequent execution of traps to microcode ROM,
  and the implementation of these micro-operations in execution units. All these tasks are performed within one verification framework, which includes a
  theorem prover, a verified symbolic simulator, and SAT solvers. We describe the work of defining the needed formal models for both the architecture and
  micro-architecture in this framework, as well as tools for decomposing the requisite properties into smaller lemmas which can be automatically checked.
  We additionally cover the advantages and limitations of our approach. To our knowledge, there are no similar results in the verification of implementations
  of an x86 microprocessor.
added: 2021-11-05
address: New York, NY, USA
authors:
- Shilpi Goel
- Anna Slobodova
- Rob Sumners
- Sol Swords
booktitle: Proceedings of the 9th ACM SIGPLAN International Conference on Certified Programs and Proofs
doi: 10.1145/3372885.3373811
isbn: '9781450370974'
keywords: formal verification, hardware verification, microcode verification, x86 ISA, ACL2
layout: paper
link: https://doi.org/10.1145/3372885.3373811
location: New Orleans, LA, USA
numpages: '14'
pages: 47-60
publisher: Association for Computing Machinery
read: false
readings: []
series: CPP 2020
title: Verifying x86 instruction implementations
url: https://doi.org/10.1145/3372885.3373811
year: 2020
notes:
- hardware
- CPU verification
- ISA specification
papers:
---
{% include links.html %}
