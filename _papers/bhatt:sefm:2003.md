---
ENTRYTYPE: inproceedings
abstract: The architectural reference model, a critical tool in microprocessor validation, serves as a gold standard against which a microprocessor is compared.
  As all validation is performed using it, the reference model must be timely, extensible beyond the original specification, customizable for specific usage
  models, and, most importantly, functionally flawless. Ideally, we would like a specification-based design flow that transforms the published English language
  specifications into compilable code that is directly incorporated into the reference model without loss of information or accuracy. At Intel, we have
  developed and implemented such a flow to create the Itanium Processor Family's (IPF) reference model, which is used to validate all IPF processors. In
  this paper, we describe the benefits and limitations of this process and discuss the practical implications of specification-based design.
added: 2021-12-02
authors:
- Rahul Bhatt
- Dave LaFollette
- Arjun Kapur
booktitle: First International Conference onSoftware Engineering and Formal Methods, 2003.Proceedings.
doi: 10.1109/SEFM.2003.1236217
issn: ''
keywords: ''
layout: paper
month: Sep.
number: ''
pages: 156-162
read: true
readings:
- 2021-12-20
title: The fallacy of spec-based design
volume: ''
year: 2003
notes:
- ISA specification
- Intel
- Itanium architecture
papers:
- reid:fmcad:2016
---

Describes a process similar to the later [reid:fmcad:2016] of using the official [ISA specification] of
a processor directly as a reference model for processor validation as well as for documentation.
This was developed during the design of [Intel]'s [Itanium architecture] and then maintained
as the architecture evolved. The architecture specification was subject to a strict review
policy.

The language was "C-like" (I think this means a subset of C) and covered the instruction behaviour.
Non-instruction behaviour such as page table walks was handled by function calls to code provided by the simulator.
(In comparision, the Arm specification described in [reid:fmcad:2016] includes non-instruction behaviour.)
The complete tool (excluding supporting libraries like disassembly, instruction decode and FP) is 475,000 lines
and the generated code (from the spec) is 40,000 lines of that. The remainder models load address tables, register
stacks, bus and memory;  adds a machine-code debugger (breakpoints, etc.), and other UI; adds the IA-32
simulator (around 100,000 lines), etc.
It appears that all function calls in the specification are to simulator code so instruction specs get a bit cluttered
due to not having an abstraction mechanism.

When used for processor validation, the generated code is modified (subclassed) to model the implementation specific behaviour
including any undefined behaviour.
Optional behaviour in the spec such as writing FP values to uncached memory is not included in the spec so that is
handled the same way.

It seems that the transformation from the C-like code to executable code for use in the simulator
performs  no significant translation/transformation leading to problems such as name clashes between
names used in the spec and names used elsewhere in the simulation tool.
These are dealt with by manually modifying the generated code which leads to problems when
the specification is changed and the code has to be regenerated.

The paper identifies reasons for these shortcomings

- An expectation that the architecture would evolve by (only) adding new instructions
  lead to a flow where manual modification of generated code seemed reasonable.

- The style of the specification and the relatively shallow optimization
  lead to performance problems in the simulator.
  *[I suspect that this was also because the instructions and the supporting functions
  are written in different languages - preventing optimization across the boundary.](

- Specifying only instruction behaviour made for difficult debug experience
  since different debugging tools were needed for debugging instructions
  and for everything else.

- Supporting implementation defined and undefined behaviour is easy but
  it is done by writing code in C/C++ instead of the spec language which
  diminishes the value of the spec.
  *[I suspect that the need to be able to mix the two languages in this way
  makes it harder to add optimizations during the translation process.]*

- Support for other uses such as test generation, performance modelling,
  checkers, etc. was provided by adding a (necessarily) stable callback API
  around calls from the instructions into the hand-written parts of
  the simulator. For example, test generators needed to rewind and
  replay instructions.
  It seems that this grew significantly in time.
  *[I would regard this as a partial success: all these different uses
  indicate that the spec was valuable.]*

Overall, the paper reports that there were some benefits but they are
disappointed with the cost and that there was not more benefit.

*[I believe that most of the issues were due to the approach they
took. e.g., a shallow transformation process from spec to simulator,
limiting the spec to only the instruction behaviour, using a process
that included manual modification of machine-generated code, having
just one execution model in mind during development and not
anticipating the multiple uses of the spec and supporting their
needs (e.g., callbacks) in their simulator generation tool.]*

{% include links.html %}
