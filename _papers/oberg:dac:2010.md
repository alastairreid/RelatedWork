---
ENTRYTYPE: inproceedings
added: 2019-10-06
authors:
- Jason Oberg
- Wei Hu
- Ali Irturk
- Mohit Tiwari
- Timothy Sherwood
- Ryan Kastner
booktitle: Proceedings of the 47th Design Automation Conference
doi: 10.1145/1837274.1837337
layout: paper
organization: ACM
pages: 244-247
read: true
readings:
- 2019-10-06
title: Theoretical analysis of gate level information flow tracking
year: 2010
notes:
- hardware
- information flow
papers:
---

GLIFT (Gate Level Information Flow Tracking) calculates a precise "taint" bit for every signal indicating whether the signal depends on some input signals.  GLIFT is added by calculating taint for each primitive gate type (and, or, XOR, not) with an assumption of linearity.  This paper looks at how the number of midterms grows with circuit complexity for 1-8 bit adder, multiplier, comparator, shifter and multiplexer.  All costs are exponential and quite high.

Questions: Can linearity assumption be justified?  Is number of midterms the right metric?

{% include links.html %}
