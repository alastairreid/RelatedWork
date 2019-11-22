---
ENTRYTYPE: inproceedings
added: 2019-11-10
address: Austin, TX
authors:
- Amit Vasudevan
- Sagar Chaki
- Petros Maniatis
- Limin Jia
- Anupam Datta
booktitle: 25th USENIX Security Symposium (USENIX Security 16)
isbn: 978-1-931971-32-4
layout: paper
month: August
pages: 87-104
publisher: USENIX Association
read: true
readings:
- 2019-11-22
title: 'überSpark: Enforcing Verifiable Object Abstractions for Automated Compositional Security Analysis of a Hypervisor'
url: https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/vasudevan
year: 2016
topics:
- os
- verification
---

Verifies properties of a concurrent micro-hypervisor uXMHF using Frama-C with some custom plugins and using CompCert to compile.
Assembly language and a hardware model are accomodated by invoking via function calls and providing a C equivalent function that accesses shadow C variables that model changes in hardware state.
Interestingly, the hypervisor also allows unverified plugins - but all unverified plugins are run in a sandbox (and incur higher overhead).

The core of the idea is to structure the hypervisor as a set of singleton objects
and prove isolation properties, etc. about each object.
(I am unclear how/if a singleton object differs from a module!)

Verification is of security invariants (not full functional correctness).
Invariants cover memory separation, control flow integrity and information flow.
Verification is automatic but depends on annotation.
The annotation burden is around 110% though it is not clear what fraction of that is really a specification burden.

The related work section in this paper is really good – covering both work in unverified OSes and verified OSes.

Also, the detail on the proof structure and the invariants is unusually good.
(And the corresponding tech report apparently has even more detail!)


