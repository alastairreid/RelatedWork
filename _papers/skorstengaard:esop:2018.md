---
doi: 10.1007/978-3-319-89884-1_17
ENTRYTYPE: inproceedings
abstract: Capability machines provide security guarantees at machine level which makes
  them an interesting target for secure compilation schemes that provably enforce
  properties such as control-flow correctness and encapsulation of local state. We
  provide a formalization of a representative capability machine with local capabilities
  and study a novel calling convention. We provide a logical relation that semantically
  captures the guarantees provided by the hardware (a form of capability safety) and
  use it to prove control-flow correctness and encapsulation of local state. The logical
  relation is not specific to our calling convention and can be used to reason about
  arbitrary programs.
added: 2020-03-01
address: Cham
authors:
- Lau Skorstengaard
- Dominique Devriese
- Lars Birkedal
booktitle: Programming Languages and Systems
editor: Ahmed, Amal
isbn: 978-3-319-89884-1
layout: paper
pages: 475-501
publisher: Springer International Publishing
read: true
readings:
- 2020-02-27
title: Reasoning about a machine with local capabilities
year: 2018
topics:
- hardware
- verification
notes:
- CHERI architecture
- capabilities
papers:
- skorstengaard:popl:2019
---

This paper is concerned with reasoning about software running
on a capability machine such as CHERI and, in particular,
proving that the calling convention ensures proper
nesting of function calls no matter how buggy or malicious
the function you're calling may be.
It enforces that, if a function returns,
it can only return to the return address it was given,
with the stack pointer it was given and that it cannot
use some other address or stack pointer or even
re-use values from some earlier invocation of the
function.

The threat model is that neither the caller nor the
callee completely trust each other not to be malicious.
This requires that the caller and callee respect a new
calling convention where the caller is responsible
for creating a suitably restricted environment from
which to call the callee and the callee is responsible
for cleaning up their state before returning to the
callee.

The key to implementing this is a new restricted form
of capability that can only exist in registers or
on the stack (or, more accurately, regions of the
memory that have permission to store these capabilities).

The paper explains and motivates the calling convention
and then describes proofs that the calling convention
achieves the intended goals.
It assumes one new hardware primitive that it requires
to be efficient: clearing a contiguous region of the stack
to prevent capabilities held by a function from leaking
into other functions that happen to share the stack.

{% include links.html %}
