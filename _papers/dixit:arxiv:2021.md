---
ENTRYTYPE: article
added: 2021-09-15
authors:
- Harish Dattatraya Dixit
- Sneha Pendharkar
- Matt Beadon
- Chris Mason
- Tejasvi Chakravarthy
- Bharath Muthiah
- Sriram Sankar
bibsource: dblp computer science bibliography, https://dblp.org
biburl: https://dblp.org/rec/journals/corr/abs-2102-11245.bib
eprint: '2102.11245'
eprinttype: arXiv
journal: CoRR
layout: paper
link: https://arxiv.org/abs/2102.11245
read: true
readings:
- 2021-09-15
timestamp: Wed, 24 Feb 2021 15:42:45 +0100
title: Silent data corruptions at scale
url: https://arxiv.org/abs/2102.11245
volume: abs/2102.11245
year: 2021
notes:
- Hardware faults
papers:
- hochschild:hotos:2021
---

This paper explores the same problem as [hochschild:hotos:2021]: CPUs that
silently give incorrect results without any detection or correction mechanism (like, for example,
ECC on SRAM/DRAM).
Unlike radiation-induced failures that are transient, they are interested in more consistent
and higher frequency failures that they observe in datacenters due to timing errors, manufacturing
variation, degradation and end-of-life wearout and associated with increased transistor density
and wider datapaths.

They do a detailed case study of debugging one failure on one particular core on one chip.
In a distributed filesystem, they found that the
Scala power function was returning zero for non-zero input (for double-precision floats)

    pow(1.1, 53) = 0

but

    pow(1.1, 52) = 142

But, debugging JITed languages like Scala is non-trivial (can't just use gdb).
And minimizing binary code takes care.
Eventually, they reduce 146K to 60 lines of assembly and find both positive and
negative exponents that fail including the following examples.

    1.1 ^ 3 = 0 (should be 1)
    1.1 ^ 107 = 32809 (should be 26854)
    1.1 ^ -3 = 1 (should be 0)











{% include links.html %}
