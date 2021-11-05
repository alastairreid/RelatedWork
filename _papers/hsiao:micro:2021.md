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
read: false
readings: []
series: MICRO '21
title: Synthesizing formal models of hardware from RTL for efficient verification of memory model implementations
url: https://doi.org/10.1145/3466752.3480087
year: 2021
notes:
- ISA specification
papers:
---
{% include links.html %}
