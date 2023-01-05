---
ENTRYTYPE: inproceedings
added: 2023-01-05
authors:
- Dapeng Gao
- Tom Melham
booktitle: Proceedings of the 21st Conference on Formal Methods in Computer-Aided Design -- FMCAD 2021
doi: 10.34727/2021/isbn.978-3-85448-046-4_10
editor: Ruzica Piskac and Michael W.~Whalen
layout: paper
link: http://www.cs.ox.ac.uk/tom.melham/pub/Gao-2021-EFVG.pdf
month: October
pages: 24-33
publisher: TUI Wien Academic Press
read: true
readings:
- 2023-01-05
title: End-to-End Formal Verification of a RISC-V Processor Extended with Capability Pointers
url: http://www.cs.ox.ac.uk/tom.melham/pub/Gao-2021-EFVG.pdf
volume: '2'
year: 2021
notes:
- CHERI architecture
- RISCV architecture
- ISA specification
- CPU verification
- SAIL language
- JasperGold
- BlueSpec
- SystemVerilog Assertions
- Symbolic QED
papers:
- reid:cav:2016
---

Describes verification of [CHERI-Flute] implementation of the [CHERI architecture] for the [RISCV architecture]
against the [SAIL language] [ISA specification] of the architecture.

They verified four classes of end-to-end correctness properties finding several
previously unknown bugs in combinational logic in the process.

1. Correct execution of all 80+ CHERI instructions (but not the existing RISC-V instructions).
2. Liveness properties for the entire processor.
3. Unrepresentable capabilities are never created by the processor.
   (A capability is unrepresentable if it is not exactly representable by a compressed capability.)
4.

All verification code is available as open source.
The proof is structured as lemmas about microarchitectural invariants that are used in the end to end proofs.
Proofs are performed using the [JasperGold] bounded model checker on the SystemVerilog code produced
by the [BlueSpec] compiler.
Properties to be checked are written in [SystemVerilog Assertions] (SVA) - around 100 properties in total.

They verify that if the processor successfully executes an instruction (without reporting
a security violation) then the spec says that this is correct and, conversely, that if
the spec says that a failure should be detected/reported then a failure is detected/reported.
(This does not check that the processor always succeeds when it should or that it reports the
correct security violation.)

Instructions are split into three classes that require different sets of (safety) properties:

1. Register only CHERI instructions - checked by examining the writeback stage state.
2. Branching CHERI instructions - separately checking the (CHERI-derived) guard conditions,
   saving the return address (for branch-and-link instructions), and checking the
   new PC.
3. Memory CHERI instructions - check that the memory request was not reordered
   wrt previous requests, that a memory exception did not occur,
   that any loaded capabilities are decompressed and stored correctly,
   the value read is passed down the pipeline correctly.

Liveness properties are challenging for several reasons (getting bounded proofs,
whether the events are timely, and correctness of the external components through which the
CPU communicates with the external world).
To get bounded proofs, they turn the liveness property "X eventually happens" into the safety
property "X happens with N cycles" (for some fixed N). (N is 9 for this 5 stage processor
assuming memory responds within 2 cycles.)

Some properties have to be decomposed to get push-button verification.

- To show pipeline properties, they first prove properties about early
  stages of the pipeline and use the resulting lemmas
  to prove properties about later stages of the pipeline.
  (The detailed description in section VI.A. is worth
  studying in detail.)

- Microarchitectural invariants were developed using
  [JasperGold]'s "State Space Tunnelling" feature which
  generates a trace of length k that violates the invariant
  and then manually adding the necessary property.
  This is used with gradually increasing k to gradually
  discover the invariant.

They briefly describe 9 bugs that were found in the course
of this verification effort.
Some are due to misunderstanding the spec or changes in
the spec after processor implementation.
The fix for one of the bugs found still had a bug in it
and the authors submitted their own fix (that they
had proved was correct).
For 2 of the bugs, it was unclear whether the bug was
in the spec or in the implementation.
Most, if not all, of the bugs found were 'single-instruction bugs'
that occur deterministically and require comparison against
a formal spec or similar reference (as opposed to 'self-consistency
bugs' of the kind found by [Symbolic QED]).

Although the project compares against the SAIL specification,
they had to manually convert the SAIL to SystemVerilog
(unlike, [reid:cav:2016] which automatically converts
their formal spec to SV).

{% include links.html %}
