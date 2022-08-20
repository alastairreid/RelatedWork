---
ENTRYTYPE: inproceedings
abstract: The recent Spectre attacks have demonstrated the fundamental insecurity of current computer microarchitecture. The attacks use features like pipelining,
  out-of-order and speculation to extract arbitrary information about the memory contents of a process. A comprehensive formal microarchitectural model
  capable of representing the forms of out-of-order and speculative behavior that can meaningfully be implemented in a high performance pipelined architecture
  has not yet emerged. Such a model would be very useful, as it would allow the existence and non-existence of vulnerabilities, and soundness of countermeasures
  to be formally established. This paper presents such a model targeting single core processors. The model is intentionally very general and provides an
  infrastructure to define models of real CPUs. It incorporates microarchitectural features that underpin all known Spectre vulnerabilities. We use the
  model to elucidate the security of existing and new vulnerabilities, as well as to formally analyze the effectiveness of proposed countermeasures. Specifically,
  we discover three new (potential) vulnerabilities, including a new variant of Spectre v4, a vulnerability on speculative fetching, and a vulnerability
  on out-of-order execution, and analyze the effectiveness of existing countermeasures including constant time and serializing instructions.
added: 2021-04-17
address: New York, NY, USA
authors:
- Roberto Guanciale
- Musard Balliu
- Mads Dam
booktitle: Proceedings of the 2020 ACM SIGSAC Conference on Computer and Communications Security
doi: 10.1145/3372297.3417246
isbn: '9781450370899'
keywords: countermeasures, out-of-order, speculation, vulnerabilities, microarchitecture, verification, formal models
layout: paper
link: https://doi.org/10.1145/3372297.3417246
location: Virtual Event, USA
numpages: '17'
pages: 1853-1869
publisher: Association for Computing Machinery
read: false
readings: []
series: CCS '20
title: 'InSpectre: Breaking and fixing microarchitectural vulnerabilities by formal analysis'
url: https://doi.org/10.1145/3372297.3417246
year: 2020
notes:
- side channel
- microarchitecture
- speculative execution
papers:
---
{% include links.html %}
