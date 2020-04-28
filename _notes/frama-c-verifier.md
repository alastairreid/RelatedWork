---
layout: note
title: Frama-C verifier
wiki: https://en.wikipedia.org/wiki/Frama-C
website: http://frama-c.com
papers:
- cuoq:sefm:2012
---

Frama-C (the Framework for Modular Analysis of C programs)
is a set of interoperable program analyzers for C programs.
It is structured as a plugin architecture supporting 
value analysis, deductive verification, weakest precondition
calculation, impact analysis and program slicing.
This is supported by a framework based on the CIL frontend to parse C code,
and some common analyses and libraries.

Frama-C also forms the basis of the [tis interpreter]
that executes C programs and detects [undefined behaviour].

Frama-C has commercial support from [TrustInSoft].

[TrustInSoft]: http://trust-in-soft.com/
[tis interpreter]: http://trust-in-soft.com/tis-interpreter
[undefined behaviour]: {{ "notes/undefined-behaviour" | relative_url }}
