---
ENTRYTYPE: article
abstract: This paper describes a memory management discipline for programs that perform dynamic memory allocation and de-allocation. At runtime, all values
  are put intoregions. The store consists of a stack of regions. All points of region allocation and de-allocation are inferred automatically, using a type
  and effect based program analysis. The scheme does not assume the presence of a garbage collector. The scheme was first presented in 1994 (M. Tofte and
  J.-P. Talpin,in"Proceedings of the 21st ACM SIGPLAN SIGACT Symposium on Principles of Programming Languages," pp. 188 201); subsequently, it has been
  tested in The ML Kit with Regions, a region-based, garbage-collection free implementation of the Standard ML Core language, which includes recursive datatypes,
  higher-order functions and updatable references L. Birkedal, M. Tofte, and M. Vejlstrup, (1996),in"Proceedings of the 23 rd ACM SIGPLAN SIGACT Symposium
  on Principles of Programming Languages," pp. 171 183. This paper defines a region-based dynamic semantics for a skeletal programming language extracted
  from Standard ML. We present the inference system which specifies where regions can be allocated and de-allocated and a detailed proof that the system
  is sound with respect to a standard semantics. We conclude by giving some advice on how to write programs that run well on a stack of regions, based on
  practical experience with the ML Kit.
added: 2021-03-05
address: USA
authors:
- Mads Tofte
- Jean-Pierre Talpin
doi: 10.1006/inco.1996.2613
issn: 0890-5401
issue_date: Feb. 1, 1997
journal: Inf. Comput.
layout: paper
link: https://doi.org/10.1006/inco.1996.2613
month: February
number: '2'
numpages: '68'
pages: 109-176
publisher: Academic Press, Inc.
read: false
readings: []
title: Region-based memory management
url: https://doi.org/10.1006/inco.1996.2613
volume: '132'
year: 1997
notes:
papers:
---
{% include links.html %}
