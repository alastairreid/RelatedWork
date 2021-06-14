---
ENTRYTYPE: inproceedings
abstract: When symbolic execution is used to analyse real-world applications, it often consumes all available memory in a relatively short amount of time,
  sometimes making it impossible to analyse an application for an extended period. In this paper, we present a technique that can record an ongoing symbolic
  execution analysis to disk and selectively restore paths of interest later, making it possible to run symbolic execution indefinitely. To be successful,
  our approach addresses several essential research challenges related to detecting divergences on re-execution, storing long-running executions efficiently,
  changing search heuristics during re-execution, and providing a global view of the stored execution. Our extensive evaluation of 93 Linux applications
  shows that our approach is practical, enabling these applications to run for days while continuing to explore new execution paths.
added: 2021-06-14
address: New York, NY, USA
authors:
- Frank Busse
- Martin Nowack
- Cristian Cadar
booktitle: Proceedings of the 29th ACM SIGSOFT International Symposium on Software Testing and Analysis
doi: 10.1145/3395363.3397360
isbn: '9781450380089'
keywords: memoization, KLEE, symbolic execution
layout: paper
link: https://doi.org/10.1145/3395363.3397360
location: Virtual Event, USA
numpages: '12'
pages: 63-74
publisher: Association for Computing Machinery
read: false
readings: []
series: ISSTA 2020
title: Running symbolic execution forever
url: https://doi.org/10.1145/3395363.3397360
year: 2020
notes:
- symbolic execution
- KLEE verifier
papers:
---
{% include links.html %}
