---
ENTRYTYPE: inproceedings
abstract: This paper introduces memoized symbolic execution (Memoise), a new approach for more efficient application of forward symbolic execution, which
  is a well-studied technique for systematic exploration of program behaviors based on bounded execution paths. Our key insight is that application of symbolic
  execution often requires several successive runs of the technique on largely similar underlying problems, e.g., running it once to check a program to
  find a bug, fixing the bug, and running it again to check the modified program. Memoise introduces a trie-based data structure that stores the key elements
  of a run of symbolic execution. Maintenance of the trie during successive runs allows re-use of previously computed results of symbolic execution without
  the need for re-computing them as is traditionally done. Experiments using our prototype implementation of Memoise show the benefits it holds in various
  standard scenarios of using symbolic execution, e.g., with iterative deepening of exploration depth, to perform regression analysis, or to enhance coverage
  using heuristics.
added: 2021-06-14
address: New York, NY, USA
authors:
- Guowei Yang
- Corina S. Păsăreanu
- Sarfraz Khurshid
booktitle: Proceedings of the 2012 International Symposium on Software Testing and Analysis
doi: 10.1145/2338965.2336771
isbn: '9781450314541'
layout: paper
link: https://doi.org/10.1145/2338965.2336771
location: Minneapolis, MN, USA
numpages: '11'
pages: 144-154
publisher: Association for Computing Machinery
read: false
readings: []
series: ISSTA 2012
title: Memoized symbolic execution
url: https://doi.org/10.1145/2338965.2336771
year: 2012
notes:
- symbolic execution
papers:
---
{% include links.html %}
