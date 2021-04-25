---
ENTRYTYPE: inproceedings
abstract: We present the design and implementation of p4v, a practical tool for verifying data planes described using the P4 programming language. The design
  of p4v is based on classic verification techniques but adds several key innovations including a novel mechanism for incorporating assumptions about the
  control plane and domain-specific optimizations which are needed to scale to large programs. We present case studies showing that p4v verifies important
  properties and finds bugs in real-world programs. We conduct experiments to quantify the scalability of p4v on a wide range of additional examples. We
  show that with just a few hundred lines of control-plane annotations, p4v is able to verify critical safety properties for switch.p4, a program that implements
  the functionality of on a modern data center switch, in under three minutes.
added: 2021-04-25
address: New York, NY, USA
authors:
- Jed Liu
- William Hallahan
- Cole Schlesinger
- Milad Sharif
- Jeongkeun Lee
- Robert Soulé
- Han Wang
- Călin Caşcaval
- Nick McKeown
- Nate Foster
booktitle: Proceedings of the 2018 Conference of the ACM Special Interest Group on Data Communication
doi: 10.1145/3230543.3230582
isbn: '9781450355674'
keywords: verification, P4, programmable data planes
layout: paper
link: https://doi.org/10.1145/3230543.3230582
location: Budapest, Hungary
numpages: '14'
pages: 490-503
publisher: Association for Computing Machinery
read: false
readings: []
series: SIGCOMM '18
title: 'p4v: Practical verification for programmable data planes'
url: https://doi.org/10.1145/3230543.3230582
year: 2018
notes:
papers:
---
{% include links.html %}
