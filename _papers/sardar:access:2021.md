---
ENTRYTYPE: article
abstract: In August 2020, Intel asked the research community for feedback on the newly offered architecture extensions, called Intel Trust Domain Extensions
  (TDX), which give more control to Trust Domains (TDs) over processor resources. One of the key features of these extensions is the remote attestation
  mechanism, which provides a unified report verification mechanism for TDX and its predecessor Software Guard Extensions (SGX). Based on our experience
  and intuition, we respond to the request for feedback by formally specifying the attestation mechanism in the TDX using ProVerif's specification language.
  Although the TDX technology seems very promising, the process of formal specification reveals a number of subtle discrepancies in Intel's specifications
  that could potentially lead to design and implementation flaws. After resolving these discrepancies, we also present fully automated proofs that our specification
  of TD attestation preserves the confidentiality of the secret and authentication of the report by considering the state-of-the-art Dolev-Yao adversary
  in the symbolic model using ProVerif. We have submitted the draft to Intel, and Intel is in the process of making the changes.
added: 2021-07-09
authors:
- Muhammad Usama Sardar
- Saidgani Musaev
- Christof Fetzer
doi: 10.1109/ACCESS.2021.3087421
issn: 2169-3536
journal: IEEE Access
keywords: ''
layout: paper
month: ''
number: ''
pages: 83067-83079
read: false
readings: []
title: Demystifying attestation in Intel Trust Domain Extensions via formal verification
volume: '9'
year: 2021
notes:
papers:
---
{% include links.html %}
