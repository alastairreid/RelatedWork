---
ENTRYTYPE: inproceedings
added: 2019-10-12
authors:
- Haohui Mai
- Edgar Pek
- Hui Xue
- Samuel Talmadge King
- Parthasarathy Madhusudan
booktitle: ASPLOS '13 Proceedings of the eighteenth international conference on Architectural support for programming languages and operating systems
doi: 10.1145/2451116.2451148
layout: paper
number: '1'
organization: ACM
pages: 293-304
read: true
readings:
- 2019-10-21
title: Verifying security invariants in ExpressOS
volume: '41'
year: 2013
topics:
- os
- security
- verification
notes:
- abstract-interpretation
- dafny-verifier
- contract-based-development
papers:
- leino:lpair:2010
---

ExpressOS is a replacement single-threaded Android kernel written in C# running on top of L4/Fiasco.

This paper takes the interesting approach of only verifying security properties rather than full functional correctness and of building on top of untrusted file systems, etc. and relying on crypto/signing to provide confidentiality and integrity.

The verification work adds an impressively low 2.8% annotation overhead in the form of ghost state and ghost code and leverages code contracts (abstract interpretation) and [Dafny][leino:lpair:2010] (automated theorem proving) to prove properties about state machines, ownership, etc. that are reductions of the desired security invariants.

I was a little unclear about the interaction between Dafny and Code Contracts.
My best understanding is that Dafny is used to prove that methods satisfy their specification and then the specification is inserted at callsites where the abstract interpretation features of Code Contracts do the rest.
Presumably the way this works is that the abstract interpreter does its best to verify the code but, if that fails, it falls back on Dafny?

The paper notes a drawback of inserting ghost state and code: this part of the  specification ends up scattered across/interleaved with the code and is intimately tied to the code.
This raises the risk that this ghost code could contain mistakes.
They suggest that writing specs that are more independent from the code and more resilient to code changes but still enables automated theorem proving would be more robust and productive.

A number of experiments establish that the overhead of storing the additional metadata and signing/verifying/encrypting/decrypting the data is not too bad.
(The experiments are on a fairly low performance system with a slow disk – I wonder whether overhead would be larger or smaller on a modern SSD?)


{% include links.html %}
