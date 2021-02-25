---
ENTRYTYPE: inproceedings
abstract: Concretization is an effective weapon in the armory of symbolic execution engines. However, concretization can lead to loss in coverage, path
  divergence, and generation of test-cases on which the intended bugs are not reproduced. In this paper, we propose an algorithm, Deferred Concretization,
  that uses a new category for values within symbolic execution (referred to as the symcrete values) to pend concretization till they are actually needed.
  Our tool, COLOSSUS, built around these ideas, was able to gain an average coverage improvement of 66.94\% and reduce divergence by more than 55\% relative
  to the state-of-the-art symbolic execution engine, KLEE. Moreover, we found that KLEE loses about 38.60\% of the states in the symbolic execution tree
  that COLOSSUS is able to recover, showing that COLOSSUS is capable of covering a much larger coverage space.
added: 2021-02-25
address: New York, NY, USA
authors:
- Awanish Pandey
- Phani Raj Goutham Kotcharlakota
- Subhajit Roy
booktitle: Proceedings of the 28th ACM SIGSOFT International Symposium on Software Testing and Analysis
doi: 10.1145/3293882.3330554
isbn: '9781450362245'
keywords: Fuzzing, Symbolic Execution, Software Testing
layout: paper
link: https://doi.org/10.1145/3293882.3330554
location: Beijing, China
numpages: '11'
pages: 228-238
publisher: Association for Computing Machinery
read: false
readings: []
series: ISSTA 2019
title: Deferred concretization in symbolic execution via fuzzing
url: https://doi.org/10.1145/3293882.3330554
year: 2019
notes:
- symbolic execution
- fuzz testing
- KLEE verifier
papers:
---
{% include links.html %}
