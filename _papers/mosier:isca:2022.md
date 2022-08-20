---
ENTRYTYPE: inproceedings
abstract: We propose leakage containment models (LCMs)--novel axiomatic security contracts which support formally reasoning about the security guarantees
  of programs when they run on particular microarchitectures. Our core contribution is an axiomatic vocabulary for formalizing LCMs, derived from the established
  axiomatic vocabulary for formalizing processor memory consistency models. Using this vocabulary, we formalize microarchitectural leakage--focusing on
  leakage through hardware memory systems--so that it can be automatically detected in programs and provide a taxonomy for classifying said leakage by severity.
  To illustrate the efficacy of LCMs, we first demonstrate that our leakage definition faithfully captures a sampling of (transient and non-transient) microarchitectural
  attacks from the literature. Second, we develop a static analysis tool based on LCMs which automatically identifies Spectre vulnerabilities in programs
  and scales to analyze real-world crypto-libraries.
added: 2022-08-20
address: New York, NY, USA
authors:
- Nicholas Mosier
- Hanna Lachnitt
- Hamed Nemati
- Caroline Trippel
booktitle: Proceedings of the 49th Annual International Symposium on Computer Architecture
doi: 10.1145/3470496.3527412
isbn: '9781450386104'
keywords: spectre, hardware-software contracts, hardware security, side-channel attacks, memory consistency models
layout: paper
link: https://doi.org/10.1145/3470496.3527412
location: New York, New York
numpages: '15'
pages: 72-86
publisher: Association for Computing Machinery
read: false
readings: []
series: ISCA '22
title: Axiomatic Hardware-Software Contracts for Security
url: https://doi.org/10.1145/3470496.3527412
year: 2022
notes:
- weak memory
- CPU verification
- ISA specification
- side-channel
- speculative execution
- uspec
papers:
---
{% include links.html %}
