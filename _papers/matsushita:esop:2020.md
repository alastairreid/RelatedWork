---
doi: 10.1007/978-3-030-44914-8_18
ENTRYTYPE: inproceedings
abstract: Reduction to the satisfiablility problem for constrained Horn clauses (CHCs) is a widely studied approach to automated program verification. The
  current CHC-based methods for pointer-manipulating programs, however, are not very scalable. This paper proposes a novel translation of pointer-manipulating
  Rust programs into CHCs, which clears away pointers and heaps by leveraging ownership. We formalize the translation for a simplified core of Rust and
  prove its correctness. We have implemented a prototype verifier for a subset of Rust and confirmed the effectiveness of our method.
added: 2020-05-05
address: Cham
authors:
- Yusuke Matsushita
- Takeshi Tsukada
- Naoki Kobayashi
booktitle: Programming Languages and Systems
editor: Müller, Peter
isbn: 978-3-030-44914-8
layout: paper
pages: 484-514
publisher: Springer International Publishing
read: true
readings:
- 2020-05-06
title: 'RustHorn: CHC-based verification for Rust programs'
year: 2020
notes:
- Rust language
- MIR
papers:
- gurfinkel:cav:2015
- astrauskas:oopsla:2019
- baranowski:atva:2018
- ullrich:msc:2016
---

Verifies Rust programs by converting basic blocks in the [MIR] representation
of the code into Constrained Horn Clauses (CHCs) that
are then verified using Horn clause support in Z3 or HoIce.

The conversion reminds me of [Electrolysis][ullrich:msc:2016]
(that translates Rust to Lean functions)
while the use of Horn clauses reminds me of [SeaHorn][gurfinkel:cav:2015]
(that translates LLVM IR to Horn clauses).

The implementation is [here](https://github.com/hopv/rust-horn).

{% include links.html %}
