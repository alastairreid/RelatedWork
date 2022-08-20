---
ENTRYTYPE: inproceedings
abstract: Paramount to the viability of a parallel architecture is the correct implementation of its memory consistency model (MCM). Although tools exist
  for verifying consistency models at several design levels, a problematic verification gap exists between checking an abstract microarchitectural specification
  of a consistency model and verifying that the actual processor RTL implements it correctly.This paper presents RTLCheck, a methodology and tool for narrowing
  the microarchitecture/RTL MCM verification gap. Given a set of microarchitectural axioms about MCM behavior, an RTL design, and user-provided mappings
  to assist in connecting the two, RTLCheck automatically generates the SystemVerilog Assertions (SVA) needed to verify that the implementation satisfies
  the microarchitectural specification for a given litmus test program. When combined with existing automated MCM verification tools, RTLCheck enables test-based
  full-stack MCM verification from high-level languages to RTL. We evaluate RTLCheck on a multicore version of the RISC-V V-scale processor, and discover
  a bug in its memory implementation. Once the bug is fixed, we verify that the multicore V-scale implementation satisfies sequential consistency across
  56 litmus tests. The JasperGold property verifier finds complete proofs for 89\% of our properties, and can find bounded proofs for the remaining properties.
added: 2022-08-20
address: New York, NY, USA
authors:
- Yatin A. Manerkar
- Daniel Lustig
- Margaret Martonosi
- Michael Pellauer
booktitle: Proceedings of the 50th Annual IEEE/ACM International Symposium on Microarchitecture
doi: 10.1145/3123939.3124536
isbn: '9781450349529'
keywords: SVA, automated verification, RTL, memory consistency models
layout: paper
link: https://doi.org/10.1145/3123939.3124536
location: Cambridge, Massachusetts
numpages: '14'
pages: 463-476
publisher: Association for Computing Machinery
read: false
readings: []
series: MICRO-50 '17
title: 'RTLcheck: Verifying the Memory Consistency of RTL Designs'
url: https://doi.org/10.1145/3123939.3124536
year: 2017
notes:
- uspec
- weak memory
- CPU verification
papers:
- hsiao:micro:2021
---
{% include links.html %}
