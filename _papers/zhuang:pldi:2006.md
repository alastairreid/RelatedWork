---
ENTRYTYPE: inproceedings
abstract: Calling context profiles are used in many inter-procedural code optimizations and in overall program understanding. Unfortunately, the collection
  of profile information is highly intrusive due to the high frequency of method calls in most applications. Previously proposed calling-context profiling
  mechanisms consequently suffer from either low accuracy, high overhead, or both. We have developed a new approach for building the calling context tree
  at runtime, called adaptive bursting. By selectively inhibiting redundant profiling, this approach dramatically reduces overhead while preserving profile
  accuracy. We first demonstrate the drawbacks of previously proposed calling context profiling mechanisms. We show that a low-overhead solution using sampled
  stack-walking alone is less than 50\% accurate, based on degree of overlap with a complete calling-context tree. We also show that a static bursting approach
  collects a highly accurate profile, but causes an unacceptable application slowdown. Our adaptive solution achieves 85\% degree of overlap and provides
  an 88\% hot-edge coverage when using a 0.1 hot-edge threshold, while dramatically reducing overhead compared to the static bursting approach.
added: 2021-06-03
address: New York, NY, USA
authors:
- Xiaotong Zhuang
- Mauricio J. Serrano
- Harold W. Cain
- Jong-Deok Choi
booktitle: Proceedings of the 27th ACM SIGPLAN Conference on Programming Language Design and Implementation
doi: 10.1145/1133981.1134012
isbn: '1595933204'
keywords: adaptive, profiling, java virtual machine, calling context, calling context tree, call graph
layout: paper
link: https://doi.org/10.1145/1133981.1134012
location: Ottawa, Ontario, Canada
numpages: '9'
pages: 263-271
publisher: Association for Computing Machinery
read: false
readings: []
series: PLDI '06
title: Accurate, efficient, and adaptive calling context profiling
url: https://doi.org/10.1145/1133981.1134012
year: 2006
notes:
papers:
---
{% include links.html %}
