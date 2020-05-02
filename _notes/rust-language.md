---
layout: note
title: Rust language
wiki: https://en.wikipedia.org/wiki/Rust_(programming_language)
papers:
- astrauskas:oopsla:2019
- baranowski:atva:2018
- jung:popl:2017
- jung:popl:2020
- levy:apsys:2017
- toman:ase:2015
notes:
- ownership types
- Prusti verifier
- SMACK verifier
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

{% include links.html %}
