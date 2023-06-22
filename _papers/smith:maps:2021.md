---
ENTRYTYPE: inproceedings
abstract: Tensor kernels in machine learning (ML) often correspond to pure mathematical expressions, making term rewriting an attractive strategy for optimization
  and mapping to specialized hardware accelerators. However, existing ML intermediate representations (IRs) tend to either be pure but high-level, making
  low-level rewrites to hardware targets inexpressible, or low-level but impure, hampering the use of term rewriting altogether. This paper introduces Glenside,
  a pure IR whose core abstraction-the access pattern-enables low-level, layout-aware, hardware-centric program rewrites. We demonstrate how term rewriting
  in Glenside can be used to map program fragments to hardware accelerator invocations and automatically discover classic data layout transformations like
  im2col. Glenside establishes a new foundation for exploring further term rewriting techniques in optimizing low-level tensor programs.
added: 2023-06-21
address: New York, NY, USA
authors:
- Gus Henry Smith
- Andrew Liu
- Steven Lyubomirsky
- Scott Davidson
- Joseph McMahan
- Michael Taylor
- Luis Ceze
- Zachary Tatlock
booktitle: Proceedings of the 5th ACM SIGPLAN International Symposium on Machine Programming
doi: 10.1145/3460945.3464953
isbn: '9781450384674'
keywords: term rewriting, machine learning compilers
layout: paper
link: https://doi.org/10.1145/3460945.3464953
location: Virtual, Canada
numpages: '11'
pages: 21-31
publisher: Association for Computing Machinery
read: false
readings: []
series: MAPS 2021
title: Pure tensor program rewriting via access patterns (representation pearl)
url: https://doi.org/10.1145/3460945.3464953
year: 2021
notes:
- egraphs
papers:
---
{% include links.html %}
