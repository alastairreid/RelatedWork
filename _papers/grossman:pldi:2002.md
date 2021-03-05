---
ENTRYTYPE: inproceedings
abstract: Cyclone is a type-safe programming language derived from C. The primary design goal of Cyclone is to let programmers control data representation
  and memory management without sacrificing type-safety. In this paper, we focus on the region-based memory management of Cyclone and its static typing
  discipline. The design incorporates several advancements, including support for region subtyping and a coherent integration with stack allocation and
  a garbage collector. To support separate compilation, Cyclone requires programmers to write some explicit region annotations, but a combination of default
  annotations, local type inference, and a novel treatment of region effects reduces this burden. As a result, we integrate C idioms in a region-based framework.
  In our experience, porting legacy C to Cyclone has required altering about 8\% of the code; of the changes, only 6\% (of the 8\%) were region annotations.
added: 2021-03-05
address: New York, NY, USA
authors:
- Dan Grossman
- Greg Morrisett
- Trevor Jim
- Michael Hicks
- Yanling Wang
- James Cheney
booktitle: Proceedings of the ACM SIGPLAN 2002 Conference on Programming Language Design and Implementation
doi: 10.1145/512529.512563
isbn: '1581134630'
layout: paper
link: https://doi.org/10.1145/512529.512563
location: Berlin, Germany
numpages: '12'
pages: 282-293
publisher: Association for Computing Machinery
read: false
readings: []
series: PLDI '02
title: Region-based memory management in Cyclone
url: https://doi.org/10.1145/512529.512563
year: 2002
notes:
papers:
---
{% include links.html %}
