---
ENTRYTYPE: TECHREPORT
added: 2019-11-02
authors:
- Jason Franklin
- Arvind Seshadri
- Ning Qu
- Sagar Chaki
- Anupam Datta
layout: paper
institution: CMU
number: CMU-CyLab-08-008
read: true
readings:
- 2019-11-04
title: 'Attacking, repairing, and verifying SecVisor: A retrospective on the security of a hypervisor'
year: 2008
topics:
- os
- security
- verification
---

Uses the Murphi model checker to formalize the combined software and hardware security features in the [SecVisor]({{ "papers/seshadri:sosp:2007" | relative_url }}) hypervisor developed by some of the authors the year before.
Interestingly, the adversary is modelled as an explicit piece of code that tries to write to everywhere that it should not.
They were able to discover two bugs involving mapping physical pages that contain unapproved code and creating aliases in the virtual address space.

Some lessons that they highlight are the importance of

- a clear, explicit specification of the adversary model
- an explicit statement of the top-level security requirements
- a clean separation between these requirements and the mechanisms used to achieve them  (This separation was not as clear in the original paper.)

Notes:

- this paper verifies a manually constructed abstraction of the software - possible errors could occur due to both the manual process and the degree of abstraction required
- it appears that Murphi does not produce minimal counterexamples
- Murphi is an explicit state model checker and therefore requires significant abstraction and, even then, runs into severe scaling issues.  They were only able to verify with three or four memory pages, four pages was over 100 times slower, five pages exceeded available resources.
