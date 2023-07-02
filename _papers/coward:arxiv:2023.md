---
ENTRYTYPE: misc
added: 2023-06-21
archiveprefix: arXiv
authors:
- Samuel Coward
- George A. Constantinides
- Theo Drane
eprint: '2303.01839'
layout: paper
primaryclass: cs.AR
read: true
readings:
- 2023-07-02
title: Automating constraint-aware datapath optimization using E-graphs
year: 2023
notes:
- egraphs
- Intel
papers:
---

Combines [egraphs], interval analysis and sub-domain equivalences to
generate efficient floating point datapath circuits.

[Egraphs] provide a lot of the power: they enable a circuit to be
transformed using rewrite rules and the most efficient of the many
possible resulting circuits to be extracted.

An essential extension of [Egraphs] is "sub-domain equivalences".
E-graphs capture equivalences between expressions for all values
of the input domain such as "x + y == y + x".
Sub-domain equivalences allow equivalences to be restricted to a subset of the
domain so that they can capture properties such as "abs(x) == x if x >= 0".
This extension to E-graphs allows them to exploit the additional information
that is available inside an if-statement and, in particular, to
take advantage of case-splits.

This is demonstrated on a half-precision floating point subtraction circuit.
Subtraction is interesting because of the possibility of catastrophic cancellation
leading to the "near-far" optimization from the '90s.
Half-precision is interesting because it has not been studied as thoroughly
as the more conventional single and double precision FP.

{% include links.html %}
