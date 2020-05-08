---
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
read: false
readings: []
title: 'RustHorn: CHC-Based Verification for Rust Programs'
year: 2020
notes:
- Rust language
papers:
- gurfinkel:cav:2015
- astrauskas:oopsla:2019
- baranowski:atva:2018
---
{% include links.html %}
