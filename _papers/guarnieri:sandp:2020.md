---
ENTRYTYPE: inproceedings
added: 2021-07-05
address: Los Alamitos, CA, USA
authors:
- Marco Guarnieri
- Boris Köpf
- José F. Morales
- Jan Reineke
- Andrés Sánchez
booktitle: 2020 IEEE Symposium on Security and Privacy (SP)
doi: 10.1109/SP40000.2020.00011
issn: ''
keywords: semantics;security;microarchitecture;registers;standards;syntactics;optimization
layout: paper
link: https://doi.ieeecomputersociety.org/10.1109/SP40000.2020.00011
month: may
pages: 1-19
publisher: IEEE Computer Society
read: true
readings:
- 2021-07-05
title: 'Spectector: Principled detection of speculative information flows'
url: https://doi.ieeecomputersociety.org/10.1109/SP40000.2020.00011
volume: ''
year: 2020
notes:
- hardware
- non-interference
- side-channel
- speculative execution
- symbolic execution
- concolic execution
- SMT solver
papers:
---

Proposes 'speculative [non-interference]' (SNI) as a semantic notion of security
against [side-channel] attacks and the use of [symbolic execution] ([concolic execution])
to detect leaks due to [speculative execution] or prove their absence.
(More precisely, SNI characterizes "disclosure gadgets".)

It is enough to compare an execution that correctly predicts every branch
with an execution that mispredicts every branch so their symbolic
execution tool generates two SMT formulae representing traces
of k instructions deep down each path.
The two microarchitectural states are compared for differences in the
PC and memory locations on the assumption that these are sufficient.

They can use prediction oracles that model branching history (to model
history-based branch predictors).

The implementation uses a frontend that converts x86 to a small IR (uASM),
a core engine ([concolic execution] for the IR that watches for
control-flow leaks and memory leaks) and an [SMT solver] backend (Z3).

They evaluate the implementation on C compilers that contain SPECTRE mitigations
on a set of SPECTRE implementations and find some unmitigated leaks.

To evaluate the ability of the approach to scale,
they also evaluate on the Xen codebase using approximations for unimplemented
instructions.
The cost of performing SNI on paths is broadly the same as the cost of
generating the paths using concolic execution (sometimes faster, sometimes slower).


{% include links.html %}
