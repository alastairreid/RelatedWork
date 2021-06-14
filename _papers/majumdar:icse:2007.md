---
ENTRYTYPE: inproceedings
abstract: We present hybrid concolic testing, an algorithm that interleaves random testing with concolic execution to obtain both a deep and a wide exploration
  of program state space. Our algorithm generates test inputs automatically by interleaving random testing until saturation with bounded exhaustive symbolic
  exploration of program points. It thus combines the ability of random search to reach deep program states quickly together with the ability of concolic
  testing to explore states in a neighborhood exhaustively. We have implemented our algorithm on top of CUTE and applied it to obtain better branch coverage
  for an editor implementation (VIM 5.7, 150K lines of code) as well as a data structure implementation in C. Our experiments suggest that hybrid concolic
  testing can handle large programs and provide, for the same testing budget, almost 4\texttimes  the branch coverage than random testing and almost 2\texttimes  that
  of concolic testing.
added: 2021-06-14
address: USA
authors:
- Rupak Majumdar
- Koushik Sen
booktitle: Proceedings of the 29th International Conference on Software Engineering
doi: 10.1109/ICSE.2007.41
isbn: 0769528287
keywords: concolic testing., directed random testing
layout: paper
link: https://doi.org/10.1109/ICSE.2007.41
numpages: '11'
pages: 416-426
publisher: IEEE Computer Society
read: false
readings: []
series: ICSE '07
title: Hybrid concolic testing
url: https://doi.org/10.1109/ICSE.2007.41
year: 2007
notes:
- concolic execution
- symbolic execution
- hybrid testing
papers:
---
{% include links.html %}
