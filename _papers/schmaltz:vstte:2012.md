---
doi: 10.1007/978-3-642-27705-4_3
ENTRYTYPE: inproceedings
abstract: Pervasive formal verification of operating systems and hypervisors is, due to their safety-critical aspects, a highly relevant area of research.
  Many implementations consist of both assembler and C functions. Formal verification of their correctness must consider the correct interaction of code
  written in these languages, which is, in practice, ensured by using matching application binary interfaces (ABIs). Also, these programs must be able to
  interact with hardware. We present an integrated operational small-step semantics model of intermediate-language C and Macro-Assembler code execution
  for pervasive operating systems and hypervisor verification. Our semantics is based on a compiler calling convention that defines callee- and caller-save
  registers. We sketch a theory connecting this semantic layer with an ISA-model executing the compiled code for use in a pervasive verification context.
  This forms a basis for soundness proofs of tools used in the VerisoftXT project and is a crucial step towards arguing formal correctness of execution
  of the verified code on a gate-level hardware model.
added: 2019-07-02
address: Berlin, Heidelberg
authors:
- Sabine Schmaltz
- Andrey Shadrin
booktitle: 'Verified Software: Theories, Tools, Experiments'
editor: Joshi, Rajeev and Müller, Peter and Podelski, Andreas
isbn: 978-3-642-27705-4
layout: paper
pages: 18-33
publisher: Springer Berlin Heidelberg
read: false
readings: []
title: Integrated semantics of intermediate-language C and macro-assembler for pervasive formal verification of operating systems and hypervisors from VerisoftXT
year: 2012
notes:
- ISA specification
- hypervisor
- operating systems
---
{% include links.html %}
