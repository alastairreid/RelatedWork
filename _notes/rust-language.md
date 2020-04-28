---
layout: note
title: Rust language
wiki: https://en.wikipedia.org/wiki/Rust_(programming_language)
---

Rust is a systems programming language that differs from C
in that it aims for high performance without sacrificing memory safety.
It achieves this using an unusual [ownership type system] that
largely eliminates aliasing problems and simplifies the creation
of concurrent programs.

Verifiers for Rust include
[Prusti verifier],
[SMACK verifier]

## Papers about Rust

{% include paperlist.html %}

[ownership type system]: {{ "notes/ownership-types" | relative_url }}
[Prusti verifier]: {{ "notes/prusti-verifier" | relative_url }}
[SMACK verifier]: {{ "notes/smack-verifier" | relative_url }}
[Rust research]: {{ "topics/rust" | relative_url }}
[jung:popl:2020]: {{ "papers/jung:popl:2020" | relative_url }}
[astrauskas:oopsla:2019]: {{ "papers/astrauskas:oopsla:2019" | relative_url }}
[baranowski:atva:2018]: {{ "papers/baranowski:atva:2018" | relative_url }}
[jung:popl:2017]: {{ "papers/jung:popl:2017" | relative_url }}
[levy:apsys:2017]: {{ "papers/levy:apsys:2017" | relative_url }}
[toman:ase:2015]: {{ "papers/toman:ase:2015" | relative_url }}
