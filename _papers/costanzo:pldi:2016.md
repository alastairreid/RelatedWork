---
ENTRYTYPE: inproceedings
acmid: '2908100'
added: 2019-11-10
address: New York, NY, USA
authors:
- David Costanzo
- Zhong Shao
- Ronghui Gu
booktitle: Proceedings of the 37th ACM SIGPLAN Conference on Programming Language
  Design and Implementation
doi: 10.1145/2908080.2908100
isbn: 978-1-4503-4261-2
keywords: Certified OS Kernels, Information Flow Control, Program Verification, Security Policy Specification, Security-Preserving Simulation
layout: paper
location: Santa Barbara, CA, USA
numpages: '17'
pages: 648-664
publisher: ACM
read: true
readings:
- 2020-01-02
series: PLDI'16
title: End-to-end verification of information-flow security for C and assembly programs
url: http://doi.acm.org/10.1145/2908080.2908100
year: 2016
topics:
- os
- security
- verification
notes:
- information-flow
---

Information-flow control tackles two of the classic Confidentiality-Integrity-Availability (CIA) aspects of security.
This paper presents a framework that applies IFC to the mCertiKOS microkernel in order to prove confidentiality properties.
The proof consists of Coq proofs about individual system calls and a general framework relating lower-level "unwinding conditions" to the overall security properties.
The proof covers both C and x86 assembly code in mCertiKOS and includes reasoning about page tables.

For those familiar with the mCertiKOS work, one of the remarkable things about this paper is the size of the proofs.
While the refinement proofs (described [elsewhere]({{ "papers/gu:osdi:2016" | relative_url }})) are over 200K lines of proof, the security proofs in this paper are just over 6K lines of proof.
I think that the reason that they are so small comes from two things.

1.  mCertiKOS is deterministic and is isomorphic to its
    specification.
    This means that they only/mostly need to prove that
    the specification satisfies their security specification.
    This allows them to leverage their existing, voluminous
    refinement proofs that the implementation satisfies
    the functional specification.

2. The proof is limited to a restricted subset of mCertiKOS that 
   omits inter-processor communication.
   Omitting IPC eliminates a lot of information flow which makes
   it simpler to state and prove the security properties.
   But omitting IPC also eliminates a lot of the useful behaviour
   of an operating system leaving you with little more than
   time-sharing.
   
The framework used is a variant of Sabelfield and Sand's PER model
and fits into the classic pattern of "non-interference" proofs.
The framework used is more general than is required for the proof
about mCertiKOS that seems to be based on a static labelling of
each component of the state as being part of one process or another.
This static labelling seems to cause some difficulty as shared
pieces of state such as machine registers need to change labels
on every context switch.

{% include links.html %}
