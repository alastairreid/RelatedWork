---
ENTRYTYPE: article
abstract: Although largely driven by economies of scale, the development of the modern cloud also enables increased security. Large data centers provide
  aggregate availability, reliability, and security assurances. The operational cost of ensuring that operating systems, databases, and other services have
  secure configurations can be amortized among all tenants, allowing the cloud provider to employ experts who are responsible for security; this is often
  unfeasible for smaller businesses, where the role of systems administrator is often conflated with many others.
added: 2021-07-05
address: New York, NY, USA
authors:
- Mark Russinovich
- Manuel Costa
- Cédric Fournet
- David Chisnall
- Antoine Delignat-Lavaud
- Sylvan Clebsch
- Kapil Vaswani
- Vikas Bhatia
doi: 10.1145/3454122.3456125
issn: 1542-7730
issue_date: January-February 2021
journal: Queue
layout: paper
link: https://doi.org/10.1145/3454122.3456125
month: February
number: '1'
numpages: '28'
pages: 49-76
publisher: Association for Computing Machinery
read: true
readings:
- 2021-07-05
title: 'Toward confidential cloud computing: Extending hardware-enforced cryptographic protection to data while in use'
url: https://doi.org/10.1145/3454122.3456125
volume: '19'
year: 2021
notes:
papers:
---

Talks about the use of reduced TCB, encryption at rest and in storage, etc.
to increase confidentiality in datacenters and (?) transparency.
Relates to the Confidential Computing Consortium (10+ companies from H/W,
cloud and OS vendors).

Mechanisms: TEEs, hardware root of trust, TPMs, attestation, Arm TrustZone or Intel SGX or AMD SEV,
Secure nested paging (SNP), Intel's TDX, accelerators and GPUs, blind hypervisors,

Applications include:
confidential AI (e.g., for medical diagnostics),
confidential databases and analytics (protecting confidential databases),
confidential multiparty collaboration (pooling multiple data sources without federated learning, etc.),
confidential ledgers (providing tamper resistance, auditability, verifiability and confidentiality)
[something about Byzantine fault tolerance],

Foundational services that these platforms must provide include:
key management and attestation (enabling policies about what machines run the service),
and
code transparency.

{% include links.html %}
