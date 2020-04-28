---
layout: note
title: MIR
---

Mir is the [Rust language]'s
mid-level intermediate representation.

It has an interpreter [miri] that attempts to check many
kinds of [undefined behaviour] that is partly described
in [jung:popl:2020].


[Rust language]: {{ "notes/rust-language" | relative_url }}
[Miri]: {{ "notes/mir-interpreter" | relative-url }}
[jung:popl:2020]: {{ "papers/jung:popl:2020" | relative_url }}
[undefined behaviour]: {{ "notes/undefined-behaviour" | relative_url }}
