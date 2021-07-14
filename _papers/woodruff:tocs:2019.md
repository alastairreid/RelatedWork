---
ENTRYTYPE: article
abstract: We present CHERI Concentrate, a new fat-pointer compression scheme applied to CHERI, the most developed capability-pointer system at present.
  Capability fat pointers are a primary candidate to enforce fine-grained and non-bypassable security properties in future computer systems, although increased
  pointer size can severely affect performance. Thus, several proposals for capability compression have been suggested elsewhere that do not support legacy
  instruction sets, ignore features critical to the existing software base, and also introduce design inefficiencies to RISC-style processor pipelines.
  CHERI Concentrate improves on the state-of-the-art region-encoding efficiency, solves important pipeline problems, and eases semantic restrictions of
  compressed encoding, allowing it to protect a full legacy software stack. We present the first quantitative analysis of compiled capability code, which
  we use to guide the design of the encoding format. We analyze and extend logic from the open-source CHERI prototype processor design on FPGA to demonstrate
  encoding efficiency, minimize delay of pointer arithmetic, and eliminate additional load-to-use delay. To verify correctness of our proposed high-performance
  logic, we present a HOL4 machine-checked proof of the decode and pointer-modify operations. Finally, we measure a 50 to 75 percent reduction in L2 misses
  for many compiled C-language benchmarks running under a commodity operating system using compressed 128-bit and 64-bit formats, demonstrating both compatibility
  with and increased performance over the uncompressed, 256-bit format.
added: 2021-07-14
authors:
- Jonathan Woodruff
- Alexandre Joannou
- Hongyan Xia
- Anthony Fox
- Robert M. Norton
- David Chisnall
- Brooks Davis
- Khilan Gudka
- Nathaniel W. Filardo
- A. Theodore Markettos
- Michael Roe
- Peter G. Neumann
- Robert N. M. Watson
- Simon W. Moore
doi: 10.1109/TC.2019.2914037
issn: 1557-9956
journal: IEEE Transactions on Computers
keywords: ''
layout: paper
month: Oct
number: '10'
pages: 1455-1469
read: true
readings:
- 2021-07-14
title: 'CHERI concentrate: Practical compressed capabilities'
volume: '68'
year: 2019
notes:
- CHERI architecture
- capabilities
papers:
- woodruff:isca:2014
---

The core of the [CHERI architecture] is a form of "fat pointer" ([capabilities])
that captures the value of a pointer, lower and upper bounds on what addresses
can be dereferenced at offsets from that pointer, permission flags and
type flags.
The original architecture design had 1+256-bit fat pointers; this paper slims
this down to 1+128-bits.
(The `1+` part is because an unforgeable tag bit is added to prevent spoofing
of capabilities.)

The paper reviews alternative approaches to creating low-fat pointers
and walks through a series of limitations and optimizations.
The final design has the following features.

- Uses tricks from floating point representations like the leading-one omission in normalized FP values
  and the split into a mantissa and exponent.

- Allows out-of-bounds pointers where the pointer points outside the low-high boundary
  (but will have an offset added to them before the pointer is dereferenced).

  The representable region is at least twice the size of the dereferencable region.

- An efficient approximate representability check is performed during (fat)
  pointer arithmetic operations to check that the new pointer value is safely
  within the representable region.  An approximate check is performed to avoid
  making pointer arithmetic too slow,

  (They check that this does not impact timing on their FPGA implementation of
  CHERI.)


{% include links.html %}
