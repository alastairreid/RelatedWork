---
ENTRYTYPE: inproceedings
abstract: 'We present the design and implementation of Vigor, a software stack and toolchain for building and running software network middleboxes that
  are guaranteed to be correct, while preserving competitive performance and developer productivity. Developers write the core of the middlebox--the network
  function (NF)--in C, on top of a standard packet-processing framework, putting persistent state in data structures from Vigor''s library; the Vigor toolchain
  then automatically verifies that the resulting software stack correctly implements a specification, which is written in Python.Vigor has three key features:
  network function developers need no verification expertise, and the verification process does not require their assistance (push-button verification);
  the entire software stack is verified, down to the hardware (full-stack verification); and verification can be done in a pay-as-you-go manner, i.e., instead
  of investing upfront a lot of time in writing and verifying a complete specification, one can specify one-off properties in a few lines of Python and
  verify them without concern for the rest.We developed five representative NFs--a NAT, a Maglev load balancer, a MAC-learning bridge, a firewall, and a
  traffic policer--and verified with Vigor that they satisfy standards-derived specifications, are memory-safe, and do not crash or hang. We show that they
  provide competitive performance.The Vigor framework is available at http://vigor.epfl.ch.'
added: 2021-05-05
address: New York, NY, USA
authors:
- Arseniy Zaostrovnykh
- Solal Pirelli
- Rishabh Iyer
- Matteo Rizzo
- Luis Pedrosa
- Katerina Argyraki
- George Candea
booktitle: Proceedings of the 27th ACM Symposium on Operating Systems Principles
doi: 10.1145/3341301.3359647
isbn: '9781450368735'
layout: paper
link: https://doi.org/10.1145/3341301.3359647
location: Huntsville, Ontario, Canada
numpages: '16'
pages: 275-290
publisher: Association for Computing Machinery
read: false
readings: []
series: SOSP '19
title: Verifying software network functions with no verification expertise
url: https://doi.org/10.1145/3341301.3359647
year: 2019
notes:
- symbolic execution
papers:
---
{% include links.html %}
