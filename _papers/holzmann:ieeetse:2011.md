---
ENTRYTYPE: article
abstract: The range of verification problems that can be solved with logic model checking tools has increased significantly in the last few decades. This
  increase in capability is based on algorithmic advances and new theoretical insights, but it has also benefitted from the steady increase in processing
  speeds and main memory sizes on standard computers. The steady increase in processing speeds, though, ended when chip-makers started redirecting their
  efforts to the development of multicore systems. For the near-term future, we can anticipate the appearance of systems with large numbers of CPU cores,
  but without matching increases in clock-speeds. We will describe a model checking strategy that can allow us to leverage this trend and that allows us
  to tackle significantly larger problem sizes than before.
added: 2021-02-26
authors:
- Gerard J. Holzmann
- Rajeev Joshi
- Alex Groce
doi: 10.1109/TSE.2010.110
issn: 0098-5589
issue_date: November 2011
journal: IEEE Trans. Softw. Eng.
keywords: distributed algorithms, software verification., logic model checking, Software engineering tools and techniques
layout: paper
link: https://doi.org/10.1109/TSE.2010.110
month: November
number: '6'
numpages: '13'
pages: 845-857
publisher: IEEE Press
read: true
readings:
- 2021-02-27
title: Swarm verification techniques
url: https://doi.org/10.1109/TSE.2010.110
volume: '37'
year: 2011
notes:
- verifier performance
- verification performance
- swarm verification
- model checking
papers:
- goodman:ndss:2018
- groce:issta:2012
---

Swarm verification uses parallelism and (most importantly) *diversity* to hunt
for violations using model checkers. The goal is to find violations within some
limited time budget, not to prove absence of violations using an exhaustive
search.

Using SPIN, they run a large number of small jobs (number*size chosen to fit in
physical RAM) and create diversity by

- varying hash polynomials
- varying the number of hashes (in a Bloom filter??)
- varying random seeds for process scheduling decisions
- varying random seeds for transition selection within processes

The result is dramatically better at achieving coverage or at finding known
problems in a synthetic example.

The benefits come from a mixture of greater search velocity in the early stages
of the search and from avoiding the need to coordinate runs and largely
avoiding repeated work in separate runs.

There is no need for a parallelized algorithm or to run on an SMP machine
because there is no need to coordinate runs if they are sufficiently
independent that they are not repeating (much) work.
(I think it can also be combined with parallel algorithms if you want.)

The `swarm` tool uses just a few parameters to generate a verification script
to control all the separate runs.  For example, SPIN has a predictable memory
consumption over time so, given a time limit it calculates the maximum memory
needed per process and, from that and the physical memory, the number of
processes to run.  This makes it easy to apply `swarm` without needing to
understand SPIN or swarm in detail.


{% include links.html %}
