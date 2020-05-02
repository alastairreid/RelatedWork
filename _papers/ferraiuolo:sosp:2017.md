---
ENTRYTYPE: inproceedings
added: 2019-10-12
authors:
- Andrew Ferraiuolo
- Andrew Baumann
- Chris Hawblitzel
- Bryan Parno
booktitle: Proceedings of the 26th Symposium on Operating Systems Principles
doi: 10.1145/3132747.3132782
layout: paper
organization: ACM
pages: 287-305
read: true
readings:
- 2019-11-06
title: 'Komodo: Using verification to disentangle secure-enclave hardware from software'
year: 2017
topics:
- os
- verification
notes:
- information-flow
---

Komodo implements functionality similar to SGX but is implemented in formally verified software on ARMv7 processors instead of being implemented in hardware and microcode.
The introduction makes a very convincing argument that this is the right way to deploy security extensions because
it can be updated much faster,
and the verification is transparent ("it replaces folklore with formal verification").
They verify both functional properties and security properties (non-interference).
(Komodo lacks the memory encryption features of SGX – that would benefit from having hardware support.
Komodo is also limited to a single processor at the moment.)



Komodo is a small, simple monitor running in Arm's TrustZone secure mode.
It supports about 12 secure monitor calls (SMC) allowing the OS to create an enclave, provide the enclave with memory, initialize the enclave and stop an enclave.
It also supports 7 supervisor calls (SVC) allowing the enclave to perform attestations, allocate more memory and exit.

The Komodo verification is largely performed in [Dafny]({{ "papers/leino:lpair:2010" | relative_url }}) and is based on:

- a (trusted) specification of a subset of ARMv7
- a (trusted) specification of Komodo's SMCs and SVCs
- a (trusted) specification of the allowed information flow

Although the proof is performed using Dafny, Dafny is (virtually) unused to write executable code.  Instead, Komodo is written in assembly code using Vale and the Vale tool generates proofs and ASTs that Dafny checks.

The paper describes subtleties around interrupts.
These are almost entirely disabled both to simplify the system and because the verification approach that is based on a linear control-flow model.
However, there is a one-instruction window at the start of a couple of exception handlers that is discussed at length.

Komodo as described here is a rewrite of an earlier prototype written in C and assembly (see [the Serval paper]({{ "papers/nelson:sosp:2019" | relative_url }})).
The current version in Vale took 2 person-years effort which should be compared with the effort required fir CertiKOS and seL.
The process of writing a specification and verifying the implementation revealed bugs in the original implementation.
They also ran into bugs associated with things omitted from their architecture specification such as the need for DSB/ISB barriers, cache issues and a bug in the code that dumped Vale assembly out as Arm assembly.

They report frustrating problems with the verification tools.
In particular, solver time increased exponentially with proof complexity and
they got no information from the tools to help them debug these issues.

[Note: I work with Andrew Ferraiuolo, the lead author on this paper.]
