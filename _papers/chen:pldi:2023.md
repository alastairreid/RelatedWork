---
ENTRYTYPE: article
abstract: We introduce a new paradigm for analysing and finding bugs in quantum circuits. In our approach, the problem is given by a\hspace{0.33em}‍triple
  P C Q and the question is whether, given a set P of quantum states on the input of a circuit C, the set of quantum states on the output is equal to (or
  included in) a set Q. While this is not suitable to specify, e.g., functional correctness of a quantum circuit, it is sufficient to detect many bugs in
  quantum circuits. We propose a technique based on tree automata to compactly represent sets of quantum states and develop transformers to implement the
  semantics of quantum gates over this representation. Our technique computes with an algebraic representation of quantum states, avoiding the inaccuracy
  of working with floating-point numbers. We implemented the proposed approach in a prototype tool and evaluated its performance against various benchmarks
  from the literature. The evaluation shows that our approach is quite scalable, e.g., we managed to verify a large circuit with 40 qubits and 141,527 gates,
  or catch bugs injected into a circuit with 320 qubits and 1,758 gates, where all tools we compared with failed. In addition, our work establishes a connection
  between quantum program verification and automata, opening new possibilities to exploit the richness of automata theory and automata-based verification
  in the world of quantum computing.
added: 2023-07-02
address: New York, NY, USA
articleno: '156'
authors:
- Yu-Fang Chen
- Kai-Min Chung
- Ond{\v r}ej Lengál
- Jyun-Ao Lin
- Wei-Lun Tsai
- Di-De Yen
doi: 10.1145/3591270
issue_date: June 2023
journal: Proc. ACM Program. Lang.
keywords: quantum circuits, tree automata, verification
layout: paper
link: https://doi.org/10.1145/3591270
month: jun
number: PLDI
numpages: '26'
publisher: Association for Computing Machinery
read: false
readings: []
title: An automata-based framework for verification and bug hunting in quantum circuits
url: https://doi.org/10.1145/3591270
volume: '7'
year: 2023
notes:
- verification
- quantum computing
papers:
---

A bug-finding technique for quantum circuits that scales well
and that avoids the more conventional floating point.

Idea is to model a vector of quantum bits as a weighted decision tree
where the bits in the vector select the path through the tree.
Quantum operators can be viewed as transformations on the tree
(e.g., rotations, etc.)

Properties are written using Hoare-like notation "{P} c {Q}"

{% include links.html %}
