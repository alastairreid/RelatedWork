---
ENTRYTYPE: inproceedings
abstract: SIMD extensions have gained widespread acceptance in modern microprocessors as a way to exploit data-level parallelism in general-purpose cores.
  Popular SIMD architectures (e.g., Intel SSE/AVX) have evolved by adding support for wider registers and datapaths, and advanced features like indexed
  memory accesses, per-lane predication and inter-lane instructions, at the cost of additional silicon area and design complexity.  This paper evaluates
  the performance impact of such advanced features on a set of workloads considered hard to vectorize for traditional SIMD architectures. Their sensitivity
  to the most relevant design parameters (e.g. register/datapath width and L1 data cache configuration) is quantified and discussed.  We developed an ARMv7
  NEON based ISA extension (ARGON), augmented a cycle accurate simulation framework for it, and derived a set of benchmarks from the Berkeley dwarfs. Our
  analyses demonstrate how ARGON can, depending on the structure of an algorithm, achieve speedups of 1.5x to 16x.
acceptance: '22'
added: 2019-06-01
affiliation: ARM Ltd and University of Southampton
ar_shortname: DATE 14
authors:
- Matthias Boettcher
- Bashir M. Al-Hashimi
- Mbou Eyole
- Giacomo Gabrielli
- Alastair Reid
booktitle: Design, Automation & Test in Europe Conference & Exhibition (DATE 2014)
day: 24-28
doi: 10.7873/DATE.2014.037
editor: Gerhard Fettweis and Wolfgang Nebel
layout: paper
location: Dresden, Germany
month: March
pages: 1-4
publisher: European Design and Automation Association
read: false
readings: []
title: 'Advanced SIMD: Extending the reach of contemporary SIMD architectures'
year: 2014
topics:
papers:
---

{% include links.html %}
