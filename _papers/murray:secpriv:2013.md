---
ENTRYTYPE: inproceedings
added: 2019-10-06
authors:
- Toby Murray
- Daniel Matichuk
- Matthew Brassil
- Peter Gammie
- Timothy Bourke
- Sean Seefried
- Corey Lewis
- Xin Gao
- Gerwin Klein
booktitle: 2013 IEEE Symposium on Security and Privacy
doi: 10.1109/SP.2013.35
layout: paper
organization: IEEE
pages: 415-429
read: true
readings:
- 2020-02-07
title: 'seL4: from general purpose to a proof of information flow enforcement'
year: 2013
topics:
- security
- os
notes:
- information-flow
papers:
- klein:sosp:2009
- costanzo:pldi:2016
---

Most operating systems do two things:
they isolate processes from each other;
and
they allow some limited communication between processes.
There have been multiple attempts over more
than 30 years to prove
that an operating system actually achieves these goals;
this is the first really convincing such proof.
The proof is about the seL4 microkernel that had
already been
[formally verified][klein:sosp:2009]
as implementing its formal specification.
The paper takes us step by step through the proof
as well as being very clear about the assumptions and gaps
in the verification and the effort required for the verification.

Besides the proof, the paper focusses on three tricky areas:

1. Information flow through the scheduler.
   To avoid information flow, they took the common step of replacing
   the scheduler with a simple static round-robin scheduler between
   partitions.
   They then had to prove that this was sufficient to eliminate
   information flow.

2. Directional communication between processes.
   They need to show that there is no back-channel that allows
   bidirectional information flow.

3. What is the formal security specification?
   Given a set of processes, communication channels between them,
   etc. how do we formally state what can and cannot happen?
   There are many subtleties here that the paper walk us through.
   (But reference [36] promises to have even more detail.)

The paper ends with a lengthy discussion of the strength of the
proof.
There is little concern about the proof since it is machine-checked
and it is based on the actual C code rather than a hand-written
model of the C code.
(Around the same time, the group was also working on translation validation
to show that the C code matched the compiled binary.)
They acknowledge gaps around their model of the hardware.
The most significant issue, of course, is around covert
channels – a problem that we the field has no good solutions
for at present.

They also discuss ways in which they changed the design of seL4,
surprising information leaks they discovered and which parts
of the proof were hardest to complete.

This paper should be compared with the later work
on [verifying information flow properties of the mCertiKOS separation kernel][costanzo:pldi:2016].
The big difference between the two is that this paper proves
results in the presence of communication between different
processes while the mCertiKOS paper proves results about
a system in which inter-process communication has been
disabled.

{% include links.html %}
