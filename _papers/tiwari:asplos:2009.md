---
ENTRYTYPE: inproceedings
authors:
- Mohit Tiwari
- Hassan MG Wassel
- Bita Mazloom
- Shashidhar Mysore
- Frederic T Chong
- Timothy Sherwood
booktitle: ACM Sigplan Notices
doi: 10.1145/1508244.1508258
layout: paper
number: '3'
organization: ACM
pages: 109-120
read: true
readings:
- 2019-10-6
title: Complete information flow tracking from the gates up
volume: '44'
year: 2009
topics:
- hardware
- information-flow
---

Builds on ideas also described in [Theoretical analysis of gate-level information flow tracking](oberg:dac:2010.md) of adding "shadow circuits" that calculate whether each wire/flop in a processor depends on some initial set of untrusted values.

This paper describes a processor with automatically added shadow circuits.  The main problem is that conventional branching/looping means that if the PC becomes untrusted then all other state becomes untrusted in the next few cycles and if a pointer becomes untrusted, then all memory becomes untrusted after the next write through that pointer.  They solve this by, instead, providing predication, fixed iteration count loops and only allowing loop counters as address offsets.

The processor is 5 stages but is not pipelined.  They compare with NIOS-II and are 70% more gates (but not quite an apples-for-apples comparison).

The related work section covers previous hardware based security tracking features quite thoroughly because they claim to be the first processor of their type.
