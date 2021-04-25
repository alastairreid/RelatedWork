---
ENTRYTYPE: inproceedings
abstract: Previous shape analysis algorithms use a memory model where the heap is composed of discrete nodes that can be accessed only via access paths
  built from variables and field names, an assumption that is violated by pointer arithmetic. In this paper we show how this assumption can be removed,
  and pointer arithmetic embraced, by using an analysis based on separation logic. We describe an abstract domain whose elements are certain separation
  logic formulae, and an abstraction mechanism that automatically transits between a low-level RAM view of memory and a higher, fictional, view that abstracts
  from the representation of nodes and multiword linked-lists as certain configurations of the RAM. A widening operator is used to accelerate the analysis.
  We report experimental results obtained from running our analysis on a number of classic algorithms for dynamic memory management.
added: 2021-04-25
address: Berlin, Heidelberg
authors:
- Cristiano Calcagno
- Dino Distefano
- Peter W. O'Hearn
- Hongseok Yang
booktitle: Static Analysis
editor: Yi, Kwangkeun
isbn: 978-3-540-37758-0
layout: paper
pages: 182-203
publisher: Springer Berlin Heidelberg
read: false
readings: []
title: 'Beyond reachability: Shape abstraction in the presence of pointer arithmetic'
year: 2006
notes:
- separation logic
- abstract interpretation
papers:
---
{% include links.html %}
