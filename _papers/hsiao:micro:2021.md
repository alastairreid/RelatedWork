---
ENTRYTYPE: inproceedings
abstract: Modern hardware complexity makes it challenging to determine if a given microarchitecture adheres to a particular memory consistency model (MCM).
  This observation inspired the Check tools, which formally check that a specific microarchitecture correctly implements an MCM with respect to a suite
  of litmus test programs. Unfortunately, despite their effectiveness and efficiency, the Check tools must be supplied a microarchitecture in the guise
  of a manually constructed axiomatic specification, called a \mu spec model. To facilitate MCM verification-and enable the Check tools to consume processor
  RTL directly-we introduce a methodology and associated tool, rtl2\mu spec, for automatically synthesizing \mu spec models from processor designs written
  in Verilog or SystemVerilog, with the help of modest user-provided design metadata. As a case study, we use rtl2\mu spec to facilitate the Check-based
  verification of the four-core RISC-V V-scale (multi-V-scale) processor's MCM implementation. We show that rtl2\mu spec can synthesize a complete, and
  proven correct by construction, \mu spec model from the SystemVerilog design of the multi-V-scale processor in 6.84 minutes. Subsequent Check-based MCM
  verification of the synthesized \mu spec model takes less than one second per litmus test.
added: 2021-11-05
address: New York, NY, USA
authors:
- Yao Hsiao
- Dominic P. Mulligan
- Nikos Nikoleris
- Gustavo Petri
- Caroline Trippel
booktitle: 'MICRO-54: 54th Annual IEEE/ACM International Symposium on Microarchitecture'
doi: 10.1145/3466752.3480087
isbn: '9781450385572'
keywords: verification, shared memory, memory consistency, concurrency
layout: paper
link: https://doi.org/10.1145/3466752.3480087
location: Virtual Event, Greece
numpages: '16'
pages: 679-694
publisher: Association for Computing Machinery
read: true
readings:
- 2022-08-20
series: MICRO '21
title: Synthesizing formal models of hardware from RTL for efficient verification of memory model implementations
url: https://doi.org/10.1145/3466752.3480087
year: 2021
notes:
- ISA specification
- weak memory
- CPU verification
- uspec
papers:
- manerkar:micro:2017
---

RTL2uspec fills a gap in the [uspec] methodology by automatically lifting RTL into [uspec] models.
It works by producing an initial overapproximation of the dependencies and then refining that using
a bounded model checker (jasper gold) to check that all the dependencies are valid.

Input is the RTL of a processor plus some manual labelling with the PC that applies to various stages.
The netlist for the RTL is transformed to a graph with registers as nodes and combinational logic
collapsed into the edges; nodes are numbered by shortest distance from I-fetch.
For each instruction, extract a sub-graph based on which nodes are potentially written to by
that instruction - this is the execution path of that instruction.
(Limitation: only really works for processors that have a single execution path for each instruction
which rules out use of store buffers, caches, bypass logic, etc.)

The resulting overapproximation is a bit like the result of a taint analysis - it says that there
might be a data dependency but does not guarantee that there is.
This is refined by instantiating some SVA templates that check
each edge in the graph and that each node is reachable.

The nice thing about this approach is that it is a very local analysis: mostly just
analysing combinational logic. So it scales really well.
The evaluation compares against RTLCheck [manerkar:micro:2017]
(which tried to verify the RTL directly against the uspec spec)
on a simple RISC-V core (that does not have store buffers, caches, etc.).
The approach of first lifting the spec scales much better.
They also found a bug in the processor's handling of undefined instructions.


{% include links.html %}
