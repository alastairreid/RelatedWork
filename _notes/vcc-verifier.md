---
layout: note
title: VCC verifier
website: https://www.microsoft.com/en-us/research/project/vcc-a-verifier-for-concurrent-c/
---

VCC is a [auto-active program verifier] for concurrent C programs
based on "two-state invariants" that specify the legal state transitions.

VCC was developed by Microsoft Research and
was used for a (partial?) verification of Microsoft's Hyper-V hypervisor.

VCC is built using the [Boogie verifier] and [Z3].

[Auto-active program verifier]: {{ "notes/auto-active-verification" | relative_url }}
[Boogie verifier]: {{ "notes/boogie-verifier" | relative_url }}
[Z3]: {{ "notes/z3-solver" | relative_url }}
