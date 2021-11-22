---
ENTRYTYPE: inproceedings
abstract: This paper presents an approach to construct a verified virtual protoyping framework of embedded software. The machine code executed on a simulated
  target architecture can be proven to provide the same results as the real hardware, and the proof is verified with a theorem prover. The method consists
  in proving each instruction of the instruction set independently, by proving that the execution of the C code simulating an instruction yields an identical
  result to that obtained by a formal executable model of the processor architecture. This formal model itself is obtained through an automated translation
  process from the architecture specifications. Each independent proof draws a number of lemmas from a generic lemma library and also uses the automation
  of inversion tactics in the theorem prover. The paper presents the proof of the ARM architecture version 6 Instruction Set Simulator of the SimSoC open
  source simulator, with all of the proofs being verified by the Coq proof assistant, using automated tactics to reduce manual proof development.
added: 2021-11-22
address: Cham
authors:
- Vania Joloboff
- Jean-François Monin
- Xiaomu Shi
booktitle: 'Dependable Software Engineering: Theories, Tools, and Applications'
editor: Li, Xuandong and Liu, Zhiming and Yi, Wang
isbn: 978-3-319-25942-0
layout: paper
pages: 105-119
publisher: Springer International Publishing
read: false
readings: []
title: Towards verified faithful simulation
year: 2015
notes:
- ISA specification
- Arm architecture
papers:
---
{% include links.html %}
