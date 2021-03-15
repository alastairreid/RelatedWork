---
ENTRYTYPE: inproceedings
abstract: Symbolic execution is an effective technique for exploring paths in a program and reasoning about all possible values on those paths. However,
  the technique still struggles with code that uses complex heap data structures, in which a pointer is allowed to refer to more than one memory object.
  In such cases, symbolic execution typically forks execution into multiple states, one for each object to which the pointer could refer. In this paper,
  we propose a technique that avoids this expensive forking by using a segmented memory model. In this model, memory is split into segments, so that each
  symbolic pointer refers to objects in a single segment. The size of the segments are bound by a threshold, in order to avoid expensive constraints. This
  results in a memory model where forking due to symbolic pointer dereferences is significantly reduced, often completely. We evaluate our segmented memory
  model on a mix of whole program benchmarks (such as m4 and make) and library benchmarks (such as SQLite), and observe significant decreases in execution
  time and memory usage.
added: 2021-03-15
address: New York, NY, USA
authors:
- Timotej Kapus
- Cristian Cadar
booktitle: Proceedings of the 2019 27th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering
doi: 10.1145/3338906.3338936
isbn: '9781450355728'
keywords: Symbolic execution, memory models, pointer alias analysis, KLEE
layout: paper
link: https://doi.org/10.1145/3338906.3338936
location: Tallinn, Estonia
numpages: '11'
pages: 774-784
publisher: Association for Computing Machinery
read: false
readings: []
series: ESEC/FSE 2019
title: A segmented memory model for symbolic execution
url: https://doi.org/10.1145/3338906.3338936
year: 2019
notes:
- symbolic execution
- KLEE verifier
papers:
---
{% include links.html %}
