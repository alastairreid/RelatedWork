---
ENTRYTYPE: inproceedings
added: 2021-06-14
address: Los Alamitos, CA, USA
authors:
- Shih-Wei Li
- Xupeng Li
- Ronghui Gu
- Jason Nieh
- John Zhuang Hui
booktitle: 2021 2021 IEEE Symposium on Security and Privacy (SP)
doi: 10.1109/SP40001.2021.00049
issn: 2375-1207
keywords: ''
layout: paper
link: https://doi.ieeecomputersociety.org/10.1109/SP40001.2021.00049
month: may
pages: 839-856
publisher: IEEE Computer Society
read: false
readings: []
title: A secure and formally verified Linux KVM hypervisor
url: https://doi.ieeecomputersociety.org/10.1109/SP40001.2021.00049
volume: ''
year: 2021
notes:
- operating systems
- annotation burden
- Coq theorem prover
papers:
- nelson:sosp:2017
- costanzo:pldi:2016
- gu:osdi:2016
---

Dramatically reduces the cost of verifying the security of large codebases by:
refactoring into a small "microkernel"-like piece of code that is tightly specified and verified
using the [Coq theorem prover];
and
proving that the microkernel provides sufficient isolation that
the remaining pieces of the original codebase cannot break certain security properties.
Specifically, they tackle the multiprocessor Linux KVM hypervisor.
They use hardware mechanisms (Arm-v8 Virtualization Extensions (Arm VE)) and the System MMU (cf. IO MMU in x86 architecture)
to provide the isolation.
The bulk of KVM features run as EL1 virtual machines while their verified code runs in EL2.
(This is what Arm VE is for.)
Their threat model assumes that VMs do not deliberately reveal their private data and compromised VMs leaking
data are considered out of scope.
The system is assumed to be initially benign. *[I think this means that the boot process is not verified.]*
Overhead is reported to be modest.


Their small core "KCore" is 3800 lines of code plus a separately verified crypto library.
The specifications and proof are 32.7Kloc.
The verification took two person-years. *[Does this time include or exclude the implementation and specification effort?]*

Like CertiKOS ([costanzo:pldi:2016], [gu:osdi:2016]) KCore is structured as a number (34) of small layers
and they prove both functional correctness and non-interference properties (i.e., confidentiality and integrity)
even for multiprocessor deployments that have shared page tables.
Declassification is handled using "data oracles" that act as proxies for intentionally released data.

Most/all of the layers are "security preserving": any information flow is captured by the specification
so that refinement preserves security.

Interestingly, most of the bugs were found while proving non-interference: suggesting a weakness of
relying on functional correctness proof to find bugs. *[Is this due to common-mode failure or
a side effect of a single small team both specifying and implementing the system?]*





*[One of the things that is not clear to me is the completeness and accuracy of their specification
of the Arm ISA architecture and, in particular, the semantics associated with page tables,
weak memory accesses, concurrent accesses by software and hardware page table walks, etc.
There are dragons here.]*







{% include links.html %}
