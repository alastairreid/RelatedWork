---
ENTRYTYPE: inproceedings
abstract: This paper describes the design of an implementation of the Transmission Control Protocol using an extension of the Standard ML (SML) language.
  SML supports higher-order functions, modularity, and type-safe module composition. We find that by using SML we can achieve good structure and good performance
  simultaneously. Good structure includes a modular decomposition of the protocol stack and of the TCP implementation, a control structure that imposes
  a total ordering on all events and processes them synchronously, and a test structure that allows component testing to catch problems before system integration.
  Strategies that help achieve good performance include using fast algorithms, using language constructs that make it easy to stage function evaluation,
  and language implementation features such as compacting garbage collection.
added: 2023-02-21
address: New York, NY, USA
authors:
- Edoardo Biagioni
booktitle: Proceedings of the Conference on Communications Architectures, Protocols and Applications
doi: 10.1145/190314.190318
isbn: 0897916824
layout: paper
link: https://doi.org/10.1145/190314.190318
location: London, United Kingdom
numpages: '10'
pages: 36-45
publisher: Association for Computing Machinery
read: true
readings:
- 1998-01-01
series: SIGCOMM '94
title: A structured TCP in Standard ML
url: https://doi.org/10.1145/190314.190318
year: 1994
notes:
- operating systems
- module system
- networks
papers:
---
{% include links.html %}
