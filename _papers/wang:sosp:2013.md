---
ENTRYTYPE: inproceedings
abstract: 'This paper studies an emerging class of software bugs called optimization-unstable code: code that is unexpectedly discarded by compiler optimizations
  due to undefined behavior in the program. Unstable code is present in many systems, including the Linux kernel and the Postgres database. The consequences
  of unstable code range from incorrect functionality to missing security checks.To reason about unstable code, this paper proposes a novel model, which
  views unstable code in terms of optimizations that leverage undefined behavior. Using this model, we introduce a new static checker called Stack that
  precisely identifies unstable code. Applying Stack to widely used systems has uncovered 160 new bugs that have been confirmed and fixed by developers.'
added: 2021-06-15
address: New York, NY, USA
authors:
- Xi Wang
- Nickolai Zeldovich
- M. Frans Kaashoek
- Armando Solar-Lezama
booktitle: Proceedings of the Twenty-Fourth ACM Symposium on Operating Systems Principles
doi: 10.1145/2517349.2522728
isbn: '9781450323888'
layout: paper
link: https://doi.org/10.1145/2517349.2522728
location: Farminton, Pennsylvania
numpages: '16'
pages: 260-275
publisher: Association for Computing Machinery
read: false
readings: []
series: SOSP '13
title: 'Towards optimization-safe systems: Analyzing the impact of undefined behavior'
url: https://doi.org/10.1145/2517349.2522728
year: 2013
notes:
- undefined behaviour
papers:
---
{% include links.html %}
