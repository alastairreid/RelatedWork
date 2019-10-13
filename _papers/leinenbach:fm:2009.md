---
ENTRYTYPE: inproceedings
layout: paper
read: true
authors:
- Dirk Leinenbach
- Thomas Santen
booktitle: International Symposium on Formal Methods
doi: 10.1007/978-3-642-05089-3_51
layout: paper
organization: Springer
pages: 806-809
title: Verifying the Microsoft Hyper-V hypervisor with VCC
year: 2009
topics:
- information-flow
---

This short (3.5 page) paper gives a brief overview of Hyper-V verification.  Hyper-V is a high performance commercial hypervisor not written with verification in mind.  It is 100kloc of C plus 5kloc x86-64 assembly, uses lock free data structures, simulates 2-stage page translation.  Verification makes heavy use of “two-state invariants” and “claims”.
Useful as an overview but need to read other papers to get any detail.
