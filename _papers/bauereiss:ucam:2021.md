---
ENTRYTYPE: techreport
abstract: 'Memory safety bugs continue to be a major source of security vulnerabilities in our critical infrastructure. The CHERI project has proposed extending
  conventional architectures with hardware-supported capabilities to enable fine-grained memory protection and scalable compartmentalisation, allowing historically
  memory-unsafe C and C++ to be adapted to deterministically mitigate large classes of vulnerabilities, while requiring only minor changes to existing system
  software sources. Arm is currently designing and building Morello, a CHERI-enabled prototype architecture, processor, SoC, and board, extending the high-performance
  Neoverse N1, to enable industrial evaluation of CHERI and pave the way for potential mass-market adoption. However, for such a major new security-oriented
  architecture feature, it is important to establish high confidence that it does provide the protections it intends to, and that cannot be done with conventional
  engineering techniques.  In this paper we put the Morello architecture on a solid mathematical footing from the outset. We define the fundamental security
  property that Morello aims to provide, reachable capability monotonicity, and prove that the architecture definition satisfies it. This proof is mechanised
  in Isabelle/HOL, and applies to a translation of the official Arm Morello specification into Isabelle. The main challenge is handling the complexity and
  scale of a production architecture: 62,000 lines of specification, translated to 210,000 lines of Isabelle. We do so by factoring the proof via a narrow
  abstraction capturing the essential properties of instruction execution in an arbitrary CHERI ISA, expressed above a monadic intra-instruction semantics.
  We also develop a model-based test generator, which generates instruction-sequence tests that give good specification coverage, used in early testing
  of the Morello implementation and in Morello QEMU development. We also use Arm''s internal test suite to validate our internal model.  This gives us machine-checked
  mathematical proofs of whole-ISA security properties of a full-scale industry architecture, at design-time. To the best of our knowledge, this is the
  first demonstration that that is feasible, and it significantly increases confidence in Morello.'
added: 2021-09-22
authors:
- Thomas Bauereiss
- Brian Campbell
- Thomas Sewell
- Alasdair Armstrong
- Lawrence Esswood
- Ian Stark
- Graeme Barnes
- Robert N. M. Watson
- Peter Sewell
doi: 10.48456/tr-959
institution: University of Cambridge, Computer Laboratory
issn: 1476-2986
layout: paper
link: https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-959.pdf
month: September
number: UCAM-CL-TR-959
read: false
readings: []
title: Verified security for the Morello capability-enhanced prototype Arm architecture
url: https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-959.pdf
year: 2021
notes:
- ISA specification
- CHERI architecture
papers:
---
{% include links.html %}
