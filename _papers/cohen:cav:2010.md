---
ENTRYTYPE: inproceedings
authors:
- Ernie Cohen
- "Micha\u0142 Moskal"
- Wolfram Schulte
- Stephan Tobies
booktitle: International Conference on Computer Aided Verification
layout: paper
organization: Springer
pages: 480-494
read: true
title: Local verification of global invariants in concurrent programs
year: 2010
topics:
- verification
- os
---

Describes how VCC was used to verify Hyper-V Hypervisor and PikeOS RTOS.
Key idea is “two-state invariants” which are basically specs of parts of the transition relation.  Required to be reflexive to allow a stuttering-style verification.  Overall name for the technique is “Locally Checked Invariants” (LCI).
Unlike alternatives like Concurrent Separation Logic, this is built out of some simple primitives with a small amount of syntactic sugar so that it can be very explicit about object lifetime, object ownership, which fields are protected by each lock, etc.
Annotations can introduce ghost state and ghost code to modify that state - this allows them to keep things first-order.
Significant annotation burden: 1 line of annotation per line of code.  This seems to be partly the cost of flexibility / building everything out of primitives and partly the complexity of the relationships being described.  I suspect that more sugar and some annotation inference would make a big difference.
They allude to some performance issues that are fixed by changing how the invariants, etc are written.  With 1/3 of the 100kloc annotated, it takes around 16 CPU hours to verify the properties - but this is very parallel. 
Limitation: seems to assume SC or DRF.
