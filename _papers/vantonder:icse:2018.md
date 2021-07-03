---
ENTRYTYPE: inproceedings
abstract: 'Static analysis tools have demonstrated effectiveness at finding bugs in real world code. Such tools are increasingly widely adopted to improve
  software quality in practice. Automated Program Repair (APR) has the potential to further cut down on the cost of improving software quality. However,
  there is a disconnect between these effective bug-finding tools and APR. Recent advances in APR rely on test cases, making them inapplicable to newly
  discovered bugs or bugs difficult to test for deterministically (like memory leaks). Additionally, the quality of patches generated to satisfy a test
  suite is a key challenge. We address these challenges by adapting advances in practical static analysis and verification techniques to enable a new technique
  that finds and then accurately fixes real bugs without test cases. We present a new automated program repair technique using Separation Logic. At a high-level,
  our technique reasons over semantic effects of existing program fragments to fix faults related to general pointer safety properties: resource leaks,
  memory leaks, and null dereferences. The procedure automatically translates identified fragments into source-level patches, and verifies patch correctness
  with respect to reported faults. In this work we conduct the largest study of automatically fixing undiscovered bugs in real-world code to date. We demonstrate
  our approach by correctly fixing 55 bugs, including 11 previously undiscovered bugs, in 11 real-world projects.'
added: 2021-06-28
address: New York, NY, USA
authors:
- Rijnard van Tonder
- Claire Le Goues
booktitle: Proceedings of the 40th International Conference on Software Engineering
doi: 10.1145/3180155.3180250
isbn: '9781450356381'
keywords: separation logic, automated program repair
layout: paper
link: https://doi.org/10.1145/3180155.3180250
location: Gothenburg, Sweden
numpages: '12'
pages: 151-162
publisher: Association for Computing Machinery
read: false
readings: []
series: ICSE '18
title: Static automated program repair for heap properties
url: https://doi.org/10.1145/3180155.3180250
year: 2018
notes:
papers:
---
{% include links.html %}
