---
ENTRYTYPE: inproceedings
abstract: Modern C++ servers have memory footprints that vary widely over time, causing persistent heap fragmentation of up to 2x from long-lived objects
  allocated during peak memory usage. This fragmentation is exacerbated by the use of huge (2MB) pages, a requirement for high performance on large heap
  sizes. Reducing fragmentation automatically is challenging because C++ memory managers cannot move objects.This paper presents a new approach to huge
  page fragmentation. It combines modern machine learning techniques with a novel memory manager (LLAMA) that manages the heap based on object lifetimes
  and huge pages (divided into blocks and lines). A neural network-based language model predicts lifetime classes using symbolized calling contexts. The
  model learns context-sensitive per-allocation site lifetimes from previous runs, generalizes over different binary versions, and extrapolates from samples
  to unobserved calling contexts. Instead of size classes, LLAMA's heap is organized by lifetime classes that are dynamically adjusted based on observed
  behavior at a block granularity.LLAMA reduces memory fragmentation by up to 78\% while only using huge pages on several production servers. We address
  ML-specific questions such as tolerating mispredictions and amortizing expensive predictions across application execution. Although our results focus
  on memory allocation, the questions we identify apply to other system-level problems with strict latency and resource requirements where machine learning
  could be applied.
added: 2021-06-03
address: New York, NY, USA
authors:
- Martin Maas
- David G. Andersen
- Michael Isard
- Mohammad Mahdi Javanmard
- Kathryn S. McKinley
- Colin Raffel
booktitle: Proceedings of the Twenty-Fifth International Conference on Architectural Support for Programming Languages and Operating Systems
doi: 10.1145/3373376.3378525
isbn: '9781450371025'
keywords: memory management, profile-guided optimization, lstms, machine learning, lifetime prediction
layout: paper
link: https://doi.org/10.1145/3373376.3378525
location: Lausanne, Switzerland
numpages: '16'
pages: 541-556
publisher: Association for Computing Machinery
read: false
readings: []
series: ASPLOS '20
title: Learning-based memory allocation for C++ server workloads
url: https://doi.org/10.1145/3373376.3378525
year: 2020
notes:
papers:
---
{% include links.html %}
