---
ENTRYTYPE: inproceedings
abstract: Operating system (OS) kernels achieve isolation between user-level processes using multi-level page tables and translation lookaside buffers (TLBs).
  Controlling the TLB correctly is a fundamental security property--yet all large-scale formal OS verification projects leave correct functionality of the
  TLB as an assumption. We present a logic for reasoning about low-level programs in the presence of TLB address translation. We extract invariants and
  necessary conditions for correct TLB operation that mirror the informal reasoning of OS engineers. Our program logic reduces to a standard logic for user-level
  reasoning, reduces to side-condition checks for kernel-level reasoning, and can handle typical OS kernel tasks such as context switching and page table
  manipulations.
added: 2021-11-22
address: Cham
authors:
- Hira Taqdees Syeda
- Gerwin Klein
booktitle: Interactive Theorem Proving
editor: Avigad, Jeremy and Mahboubi, Assia
isbn: 978-3-319-94821-8
layout: paper
pages: 542-559
publisher: Springer International Publishing
read: false
readings: []
title: Program verification in the presence of cached address translation
year: 2018
notes:
- Operating systems
- ISA specification
papers:
---
{% include links.html %}
