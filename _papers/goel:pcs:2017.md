---
ENTRYTYPE: inbook
abstract: Construction of a formal model of a computing system is a necessary practice in formal verification. The results of formal analysis can only be
  valued to the same degree as the model itself. Model development is error-prone, not only due to the complexity of the system being modeled, but also
  because it involves addressing disparate requirements. For example, a formal model should be defined using simple constructs to enable efficient reasoning
  but it should also be optimized to offer fast concrete simulations. Models of large computing systems are themselves large software systems and must be
  subject to rigorous validation. We describe our formal, executable model of the x86 instruction-set architecture; we use our model to reason about x86
  machine-code programs. Validation of our x86 ISA model is done by co-simulating it regularly against a physical x86 machine. We present design decisions
  made during model development to optimize both validation and verification, i.e., efficiency of both simulation and reasoning. Our engineering process
  provides insight into the development of a software verification and model animation framework from the points of view of accuracy, efficiency, scalability,
  maintainability, and usability.
added: 2019-07-01
address: Cham
authors:
- Shilpi Goel
- Warren A. Hunt Jr.
- Matt Kaufmann
booktitle: Provably Correct Systems
doi: 10.1007/978-3-319-48628-4_8
isbn: 978-3-319-48628-4
layout: paper
pages: 173-209
publisher: Springer International Publishing
read: false
readings: []
title: Engineering a formal, executable x86 ISA simulator for software verification
year: 2017
topics:
notes:
- x86 architecture
- instruction set architecture
- ISA specification
- ACL2 theorem prover
papers:
---

{% include links.html %}
