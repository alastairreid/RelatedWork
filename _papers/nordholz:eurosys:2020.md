---
ENTRYTYPE: inproceedings
abstract: Hypervisor implementations such as XMHF, Nova, PROSPER, prplHypervisor, the various L4 descendants, as well as KVM and Xen offer mechanisms for
  dynamic startup and reconfiguration, including the allocation, delegation and destruction of objects and resources at runtime. Some use cases such as
  cloud computing depend on this dynamicity, yet its inclusion also renders the state space intractable to simulation-based verification tools. On the other
  hand, system architectures for embedded devices are often fixed in the number and properties of isolated tasks, therefore a much simpler, less dynamic
  hypervisor design would suffice. We close this design gap by presenting Phidias, a new hypervisor consisting of a minimal runtime codebase that is almost
  devoid of dynamicity, and a comprehensive compile-time configuration framework. We then leverage this lack of dynamic components to non-interactively
  verify the validity of certain invariants. Specifically, we verify hypervisor integrity by subjecting the compiled hypervisor binary to our own symbolic
  execution engine. Finally, we discuss our results, point out possible improvements, and hint at unexplored characteristics of a static hypervisor design.
added: 2021-11-05
address: New York, NY, USA
articleno: '6'
authors:
- Jan Nordholz
booktitle: Proceedings of the Fifteenth European Conference on Computer Systems
doi: 10.1145/3342195.3387516
isbn: '9781450368827'
keywords: SAT solving, symbolic execution, hypervisor, embedded
layout: paper
link: https://doi.org/10.1145/3342195.3387516
location: Heraklion, Greece
numpages: '16'
publisher: Association for Computing Machinery
read: false
readings: []
series: EuroSys '20
title: Design of a symbolically executable embedded hypervisor
url: https://doi.org/10.1145/3342195.3387516
year: 2020
notes:
- symbolic execution
- hypervisor
- ISA specification
papers:
---
{% include links.html %}
