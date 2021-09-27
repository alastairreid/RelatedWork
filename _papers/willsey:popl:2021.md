---
ENTRYTYPE: article
abstract: An e-graph efficiently represents a congruence relation over many expressions. Although they were originally developed in the late 1970s for use
  in automated theorem provers, a more recent technique known as equality saturation repurposes e-graphs to implement state-of-the-art, rewrite-driven compiler
  optimizations and program synthesizers. However, e-graphs remain unspecialized for this newer use case. Equality saturation workloads exhibit distinct
  characteristics and often require ad-hoc e-graph extensions to incorporate transformations beyond purely syntactic rewrites. This work contributes two
  techniques that make e-graphs fast and extensible, specializing them to equality saturation. A new amortized invariant restoration technique called rebuilding
  takes advantage of equality saturation's distinct workload, providing asymptotic speedups over current techniques in practice. A general mechanism called
  e-class analyses integrates domain-specific analyses into the e-graph, reducing the need for ad hoc manipulation. We implemented these techniques in a
  new open-source library called egg. Our case studies on three previously published applications of equality saturation highlight how egg's performance
  and flexibility enable state-of-the-art results across diverse domains.
added: 2021-09-22
address: New York, NY, USA
articleno: '23'
authors:
- Max Willsey
- Chandrakana Nandi
- Yisu Remy Wang
- Oliver Flatt
- Zachary Tatlock
- Pavel Panchekha
doi: 10.1145/3434304
issue_date: January 2021
journal: Proc. ACM Program. Lang.
keywords: e-graphs, equality saturation
layout: paper
link: https://doi.org/10.1145/3434304
month: January
number: POPL
numpages: '29'
publisher: Association for Computing Machinery
read: false
readings: []
title: 'Egg: Fast and extensible equality saturation'
url: https://doi.org/10.1145/3434304
volume: '5'
year: 2021
notes:
- equality saturation
papers:
---
{% include links.html %}
