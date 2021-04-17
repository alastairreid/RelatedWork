---
ENTRYTYPE: inproceedings
abstract: The main reason for the standardization of network protocols, like QUIC, is to ensure interoperability between implementations, which poses a
  challenging task. Manual tests are currently used to test the different existing implementations for interoperability, but given the complex nature of
  network protocols, it is hard to cover all possible edge cases.State-of-the-art automated software testing techniques, such as Symbolic Execution (SymEx),
  have proven themselves capable of analyzing complex real-world software and finding hard to detect bugs. We present a SymEx-based method for finding interoperability
  issues in QUIC implementations, and explore its merit in a case study that analyzes the interoperability of picoquic and QUANT.We find that, while SymEx
  is able to analyze deep interactions between different implementations and uncovers several bugs, in order to enable efficient interoperability testing,
  implementations need to provide additional information about their current protocol state.
added: 2021-04-17
address: New York, NY, USA
authors:
- Felix Rath
- Daniel Schemmel
- Klaus Wehrle
booktitle: Proceedings of the Workshop on the Evolution, Performance, and Interoperability of QUIC
doi: 10.1145/3284850.3284853
isbn: '9781450360821'
keywords: QUIC, Symbolic Execution, Interoperability Testing
layout: paper
link: https://doi.org/10.1145/3284850.3284853
location: Heraklion, Greece
numpages: '7'
pages: 15-21
publisher: Association for Computing Machinery
read: false
readings: []
series: EPIQ'18
title: Interoperability-guided testing of QUIC implementations using symbolic execution
url: https://doi.org/10.1145/3284850.3284853
year: 2018
notes:
- QUIC protocol
- symbolic execution
papers:
- mcmillan:sigcomm:2019
---
{% include links.html %}
