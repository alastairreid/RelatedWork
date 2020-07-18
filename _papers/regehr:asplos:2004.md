---
ENTRYTYPE: inproceedings
abstract: 'Embedded software must meet conflicting requirements such as be- ing highly reliable, running on resource-constrained platforms, and being developed
  rapidly. Static program analysis can help meet all of these goals. People developing analyzers for embedded object code face a difficult problem: writing
  an abstract version of each instruction in the target architecture(s). This is currently done by hand, resulting in abstract operations that are both
  buggy and imprecise. We have developed Hoist: a novel system that solves these problems by automatically constructing abstract operations using a microprocessor
  (or simulator) as its own specification. With almost no input from a human, Hoist generates a collection of C functions that are ready to be linked into
  an abstract interpreter. We demonstrate that Hoist generates abstract operations that are correct, having been extensively tested, sufficiently fast,
  and substantially more precise than manually written abstract operations. Hoist is currently limited to eight-bit machines due to costs exponential in
  the word size of the target architecture. It is essential to be able to analyze software running on these small processors: they are important and ubiquitous,
  with many embedded and safety-critical systems being based on them.'
acceptance: '14'
added: 2019-06-01
affiliation: University of Utah
ar_shortname: ASPLOS 04
authors:
- John Regehr
- Alastair D. Reid
booktitle: Proceedings of the 11th International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS 2004)
day: 7-13
doi: 10.1145/1024393.1024410
editor: Shubu Mukherjee and Kathryn S. McKinley
layout: paper
location: Boston, MA, USA
month: October
pages: 133-143
publisher: ACM
read: false
readings: []
title: 'HOIST: a system for automatically deriving static analyzers for embedded systems'
year: 2004
notes:
- abstract interpretation
- ISA specification
- BDD
papers:
---

{% include links.html %}
