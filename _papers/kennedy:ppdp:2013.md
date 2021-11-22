---
ENTRYTYPE: inproceedings
abstract: 'We describe a Coq formalization of a subset of the x86 architecture. One emphasis of the model is brevity: using dependent types, type classes
  and notation we give the x86 semantics a makeover that counters its reputation for baroqueness. We model bits, bytes, and memory concretely using functions
  that can be computed inside Coq itself; concrete representations are mapped across to mathematical objects in the SSReflect library (naturals, and integers
  modulo 2n) to prove theorems. Finally, we use notation to support conventional assembly code syntax inside Coq, including lexically-scoped labels. Ordinary
  Coq definitions serve as a powerful "macro" feature for everything from simple conditionals and loops to stack-allocated local variables and procedures
  with parameters. Assembly code can be assembled within Coq, producing a sequence of hex bytes. The assembler enjoys a correctness theorem relating machine
  code in memory to a separation-logic formula suitable for program verification.'
added: 2021-11-22
address: New York, NY, USA
authors:
- Andrew Kennedy
- Nick Benton
- Jonas B. Jensen
- Pierre-Evariste Dagand
booktitle: Proceedings of the 15th Symposium on Principles and Practice of Declarative Programming
doi: 10.1145/2505879.2505897
isbn: '9781450321549'
keywords: Coq, dependent types, assembly code
layout: paper
link: https://doi.org/10.1145/2505879.2505897
location: Madrid, Spain
numpages: '12'
pages: 13-24
publisher: Association for Computing Machinery
read: false
readings: []
series: PPDP '13
title: 'Coq: The world''s best macro assembler?'
url: https://doi.org/10.1145/2505879.2505897
year: 2013
notes:
- Coq theorem prover
- ISA specification
- Separation Logic
papers:
- jensen:popl:2013
---
{% include links.html %}
