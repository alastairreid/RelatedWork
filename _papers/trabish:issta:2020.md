---
ENTRYTYPE: inproceedings
abstract: 'Symbolic execution (SE) is a widely used program analysis technique. Existing SE engines model the memory space by associating memory objects
  with concrete addresses, where the representation of each allocated object is determined during its allocation. We present a novel addressing model where
  the underlying representation of an allocated object can be dynamically modified even after its allocation, by using symbolic addresses rather than concrete
  ones. We demonstrate the benefits of our model in two application scenarios: dynamic inter- and intra-object partitioning. In the former, we show how
  the recently proposed segmented memory model can be improved by dynamically merging several object representations into a single one, rather than doing
  that a-priori using static pointer analysis. In the latter, we show how the cost of solving array theory constraints can be reduced by splitting the representations
  of large objects into multiple smaller ones. Our preliminary results show that our approach can significantly improve the overall effectiveness of the
  symbolic exploration.'
added: 2021-06-14
address: New York, NY, USA
authors:
- David Trabish
- Noam Rinetzky
booktitle: Proceedings of the 29th ACM SIGSOFT International Symposium on Software Testing and Analysis
doi: 10.1145/3395363.3397363
isbn: '9781450380089'
keywords: Symbolic execution, Memory partitioning, Addressing model
layout: paper
link: https://doi.org/10.1145/3395363.3397363
location: Virtual Event, USA
numpages: '12'
pages: 51-62
publisher: Association for Computing Machinery
read: false
readings: []
series: ISSTA 2020
title: Relocatable addressing model for symbolic execution
url: https://doi.org/10.1145/3395363.3397363
year: 2020
notes:
- symbolic execution
papers:
---
{% include links.html %}
