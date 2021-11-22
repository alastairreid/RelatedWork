---
ENTRYTYPE: inproceedings
abstract: 'Despite years of work on retargetable compilers, creating a good, reliable back end for an optimizing compiler still entails a lot of hard work.
  Moreover, a critical component of the back end--the instruction selector--must be written by a person who is expert in both the compiler''s intermediate
  code and the target machine''s instruction set. By generating the instruction selector from declarative machine descriptions we have (a) made it unnecessary
  for one person to be both a compiler expert and a machine expert, and (b) made creating an optimizing back end easier than ever before.Our achievement
  rests on two new results. First, finding a mapping from intermediate code to machine code is an undecidable problem. Second, using heuristic search, we
  can find mappings for machines of practical interest in at most a few minutes of CPU time. Our most significant new idea is that heuristic search should
  be controlled by algebraic laws. Laws are used not only to show when a sequence of instructions implements part of an intermediate code, but also to limit
  the search: we drop a sequence of instructions not when it gets too long or when it computes too complicated a result, but when too much reasoning will
  be required to show that the result computed might be useful.'
added: 2021-11-22
address: New York, NY, USA
authors:
- João Dias
- Norman Ramsey
booktitle: Proceedings of the 37th Annual ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages
doi: 10.1145/1706299.1706346
isbn: '9781605584799'
keywords: declarative machine descriptions, instruction selection, retargetable compilers
layout: paper
link: https://doi.org/10.1145/1706299.1706346
location: Madrid, Spain
numpages: '14'
pages: 403-416
publisher: Association for Computing Machinery
read: false
readings: []
series: POPL '10
title: Automatically generating instruction selectors using declarative machine descriptions
url: https://doi.org/10.1145/1706299.1706346
year: 2010
notes:
- ISA specification
- SLED
papers:
---
{% include links.html %}
