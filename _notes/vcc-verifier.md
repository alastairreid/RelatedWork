---
layout: note
title: VCC verifier
logo: https://www.microsoft.com/en-us/research/uploads/prod/2016/02/vcc-vcc-150x139.png
website: https://www.microsoft.com/en-us/research/project/vcc-a-verifier-for-concurrent-c/
notes:
- Boogie verifier
- Z3 solver
- auto-active verification
---

VCC is a [auto-active program verifier][auto-active verification] for concurrent C programs
based on "two-state invariants" that specify the legal state transitions.

VCC was developed by Microsoft Research and
was used for a (partial?) verification of Microsoft's Hyper-V hypervisor.

VCC is built using the [Boogie verifier] and [Z3 solver].

{% include links.html %}
