---
ENTRYTYPE: inproceedings
abstract: 'Garbage collection yields numerous software engineering benefits, but its quantitative impact on performance remains elusive. One can compare
  the cost of conservative garbage collection to explicit memory management in C/C++ programs by linking in an appropriate collector. This kind of direct
  comparison is not possible for languages designed for garbage collection (e.g., Java), because programs in these languages naturally do not contain calls
  to free. Thus, the actual gap between the time and space performance of explicit memory management and precise, copying garbage collection remains unknown.We
  introduce a novel experimental methodology that lets us quantify the performance of precise garbage collection versus explicit memory management. Our
  system allows us to treat unaltered Java programs as if they used explicit memory management by relying on oracles to insert calls to free. These oracles
  are generated from profile information gathered in earlier application runs. By executing inside an architecturally-detailed simulator, this "oracular"
  memory manager eliminates the effects of consulting an oracle while measuring the costs of calling malloc and free. We evaluate two different oracles:
  a liveness-based oracle that aggressively frees objects immediately after their last use, and a reachability-based oracle that conservatively frees objects
  just after they are last reachable. These oracles span the range of possible placement of explicit deallocation calls.We compare explicit memory management
  to both copying and non-copying garbage collectors across a range of benchmarks using the oracular memory manager, and present real (non-simulated) runs
  that lend further validity to our results. These results quantify the time-space tradeoff of garbage collection: with five times as much memory, an Appel-style
  generational collector with a non-copying mature space matches the performance of reachability-based explicit memory management. With only three times
  as much memory, the collector runs on average 17\% slower than explicit memory management. However, with only twice as much memory, garbage collection
  degrades performance by nearly 70\%. When physical memory is scarce, paging causes garbage collection to run an order of magnitude slower than explicit
  memory management.'
added: 2021-04-17
address: New York, NY, USA
authors:
- Matthew Hertz
- Emery D. Berger
booktitle: Proceedings of the 20th Annual ACM SIGPLAN Conference on Object-Oriented Programming, Systems, Languages, and Applications
doi: 10.1145/1094811.1094836
isbn: '1595930310'
keywords: explicit memory management, garbage collection, oracular memory management, performance analysis, paging, throughput, time-space tradeoff
layout: paper
link: https://doi.org/10.1145/1094811.1094836
location: San Diego, CA, USA
numpages: '14'
pages: 313-326
publisher: Association for Computing Machinery
read: false
readings: []
series: OOPSLA '05
title: Quantifying the performance of garbage collection vs. explicit memory management
url: https://doi.org/10.1145/1094811.1094836
year: 2005
notes:
- memory management
- garbage collection
papers:
---
{% include links.html %}
