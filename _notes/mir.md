---
layout: note
title: MIR
papers:
- jung:popl:2020
notes:
- Rust language
- MIR interpreter
- undefined behaviour
---

MIR is the [Rust language]'s
mid-level intermediate representation.

It has an interpreter [miri][MIR interpreter] that attempts to check many
kinds of [undefined behaviour] that is partly described
in [jung:popl:2020].

{% include links.html %}
