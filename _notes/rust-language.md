---
layout: note
title: Rust language
logo: https://www.rust-lang.org/static/images/rust-logo-blk.svg
webpage: https://www.rust-lang.org
wiki: https://en.wikipedia.org/wiki/Rust_(programming_language)
papers:
- anderson:icse:2016
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
It achieves this using an unusual [ownership type system][ownership types] that
largely eliminates aliasing problems and simplifies the creation
of concurrent programs.

Verifiers for Rust include
[Prusti verifier],
[SMACK verifier]

An incredibly early description of Rust is [here](http://venge.net/graydon/talks/intro-talk-2.pdf)
but many aspects of the language have changed since 2010.

{% include links.html %}
