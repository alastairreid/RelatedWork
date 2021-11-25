---
ENTRYTYPE: inproceedings
abstract: Concurrent systems software is widely-used, complex, and error-prone, posing a significant security risk. We introduce VRM, a new framework that
  makes it possible for the first time to verify concurrent systems software, such as operating systems and hypervisors, on Arm relaxed memory hardware.
  VRM defines a set of synchronization and memory access conditions such that a program that satisfies these conditions can be mostly verified on a sequentially
  consistent hardware model and the proofs will automatically hold on relaxed memory hardware. VRM can be used to verify concurrent kernel code that is
  not data race free, including code responsible for managing shared page tables in the presence of relaxed MMU hardware. Using VRM, we verify the security
  guarantees of a retrofitted implementation of the Linux KVM hypervisor on Arm. For multiple versions of KVM, we prove KVM's security properties on a sequentially
  consistent model, then prove that KVM satisfies VRM's required program conditions such that its security proofs hold on Arm relaxed memory hardware. Our
  experimental results show that the retrofit and VRM conditions do not adversely affect the scalability of verified KVM, as it performs similar to unmodified
  KVM when concurrently running many multiprocessor virtual machines with real application workloads on Arm multiprocessor server hardware. Our work is
  the first machine-checked proof for concurrent systems software on Arm relaxed memory hardware.
added: 2021-11-22
address: New York, NY, USA
authors:
- Runzhou Tao
- Jianan Yao
- Xupeng Li
- Shih-Wei Li
- Jason Nieh
- Ronghui Gu
booktitle: Proceedings of the ACM SIGOPS 28th Symposium on Operating Systems Principles
doi: 10.1145/3477132.3483560
isbn: '9781450387095'
keywords: hypervisors, KVM, Arm, systems verification, Formal methods, relaxed memory
layout: paper
link: https://doi.org/10.1145/3477132.3483560
location: Virtual Event, Germany
numpages: '16'
pages: 866-881
publisher: Association for Computing Machinery
read: false
readings: []
series: SOSP '21
title: Formal verification of a multiprocessor hypervisor on Arm relaxed memory hardware
url: https://doi.org/10.1145/3477132.3483560
year: 2021
notes:
- weak memory
- Arm architecture
- Operating systems
- ISA specification
papers:
---
{% include links.html %}
