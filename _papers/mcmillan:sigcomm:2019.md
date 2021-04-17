---
ENTRYTYPE: inproceedings
abstract: QUIC is a new Internet secure transport protocol currently in the process of IETF standardization. It is intended as a replacement for the TLS/TCP
  stack and will be the basis of HTTP/3, the next official version of the hypertext transfer protocol. As a result, it is likely, in the near future, to
  carry a substantial fraction of traffic on the Internet. We describe our experience applying a methodology of compositional specification-based testing
  to QUIC. We develop a formal specification of the wire protocol, and use this specification to generate automated randomized testers for implementations
  of QUIC. The testers effectively take one role of the QUIC protocol, interacting with the other role to generate full protocol executions, and verifying
  that the implementations conform to the formal specification. This form of testing generates significantly more diverse stimuli and stronger correctness
  criteria than interoperability testing, the primary method used to date to validate QUIC and its implementations. As a result, numerous implementation
  errors have been found. These include some vulnerabilities at the protocol and implementation levels, such as an off-path denial of service scenario and
  an information leak similar to the "heartbleed" vulnerability in OpenSSL.
added: 2021-04-17
address: New York, NY, USA
authors:
- Kenneth L. McMillan
- Lenore D. Zuck
booktitle: Proceedings of the ACM Special Interest Group on Data Communication
doi: 10.1145/3341302.3342087
isbn: '9781450359566'
layout: paper
link: https://doi.org/10.1145/3341302.3342087
location: Beijing, China
numpages: '14'
pages: 227-240
publisher: Association for Computing Machinery
read: false
readings: []
series: SIGCOMM '19
title: Formal specification and testing of QUIC
url: https://doi.org/10.1145/3341302.3342087
year: 2019
notes:
papers:
---
{% include links.html %}
