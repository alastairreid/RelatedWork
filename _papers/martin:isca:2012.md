---
ENTRYTYPE: article
abstract: 'Over the past two decades, several microarchitectural side channels have been exploited to create sophisticated security attacks. Solutions to
  this problem have mainly focused on fixing the source of leaks either by limiting the flow of information through the side channel by modifying hardware,
  or by refactoring vulnerable software to protect sensitive data from leaking. These solutions are reactive and not preventative: while the modifications
  may protect against a single attack, they do nothing to prevent future side channel attacks that exploit other microarchitectural side channels or exploit
  the same side channel in a novel way.In this paper we present a general mitigation strategy that focuses on the infrastructure used to measure side channel
  leaks rather than the source of leaks, and thus applies to all known and unknown microarchitectural side channel leaks. Our approach is to limit the fidelity
  of fine grain timekeeping and performance counters, making it difficult for an attacker to distinguish between different microarchitectural events, thus
  thwarting attacks. We demonstrate the strength of our proposed security modifications, and validate that our changes do not break existing software. Our
  proposed changes require minor - or in some cases, no - hardware modifications and do not result in any substantial performance degradation, yet offer
  the most comprehensive protection against microarchitectural side channels to date.'
added: 2021-09-22
address: New York, NY, USA
authors:
- Robert Martin
- John Demme
- Simha Sethumadhavan
doi: 10.1145/2366231.2337173
issn: 0163-5964
issue_date: June 2012
journal: SIGARCH Comput. Archit. News
layout: paper
link: https://doi.org/10.1145/2366231.2337173
month: June
number: '3'
numpages: '12'
pages: 118-129
publisher: Association for Computing Machinery
read: false
readings: []
title: 'TimeWarp: Rethinking timekeeping and performance monitoring mechanisms to mitigate side-channel attacks'
url: https://doi.org/10.1145/2366231.2337173
volume: '40'
year: 2012
notes:
- side channel
papers:
---
{% include links.html %}
