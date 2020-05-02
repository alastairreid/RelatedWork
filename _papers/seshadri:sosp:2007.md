---
ENTRYTYPE: inproceedings
added: 2019-11-02
authors:
- Arvind Seshadri
- Mark Luk
- Ning Qu
- Adrian Perrig
booktitle: SOSP
doi: 10.1145/1323293.1294294
layout: paper
number: '6'
organization: ACM
pages: 335-350
read: true
readings:
- 2019-11-03
title: 'SecVisor: A tiny hypervisor to provide lifetime kernel code integrity for
  commodity OSes'
volume: '41'
year: 2007
topics:
- os
- security
---

SecVisor is a hypervisor that virtualizes physical RAM, the MMU and the IO-MMU
in order to protect the kernel executable code from modification.
It uses the AMD architectural support for hypervisors to provide most of the
protection and switches memory protection on every entry/exit from kernel.
And it requires small changes to parts of Linux that normally load/modify the
kernel executable: boot  and module load/unload.

Although it is a hypervisor, only one virtual machine is supported – this keeps
SecVisor small.
Small kernel, lots of great detail about implementation, option to rely more on
software (for use on older hardware that lacks virtualization support) and good
benchmarking.

Limitations:
- It seems that this paper came out more or less simultaneously with ROP/JOP attacks
  and, by itself, this work does not protect against these attacks since they do
  not modify the kernel code – they just repurpose it.

- This is a uniprocessor hypervisor – discussion of MP support sounds plausible
  (although I worry about how switching protection on entry/exit could work?)

- Self-modifying code is a major issue.  The easy case is code that patches
  itself against known bugs.

See [later paper by Franklin, et al.]({{"papers/franklin:cmu:2008"|relative_url}})
that describes security issues in design, use of formal verification to model
design, fixes and performance impact.

{% include links.html %}
