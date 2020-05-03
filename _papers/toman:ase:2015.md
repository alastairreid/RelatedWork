---
ENTRYTYPE: inproceedings
added: 2020-01-10
authors:
- J. Toman
- S. Pernsteiner
- Emina Torlak
booktitle: 2015 30th IEEE/ACM International Conference on Automated Software Engineering (ASE)
doi: 10.1109/ASE.2015.77
keywords: data structures;formal verification;program compilers;program debugging;program
  diagnostics;program testing;software libraries;CRUST;Rust;static analysis;compiler;pointer
  aliasing invariants;data structure implementations;memory safety violations;exhaustive
  test generation;bounded model checking;unsafe library code;memory safety bugs;Arrays;Libraries;Safety;Computer
  bugs;Indexes;Standards;SMT-based verification;test generation;memory safety
layout: paper
month: November
number: ''
pages: 75-80
read: true
readings:
- 2020-01-14
title: 'Crust: A bounded verifier for Rust'
volume: ''
year: 2015
topics:
- tools
- verification
notes:
- rust-language
- bounded-verification
- cbmc-verifier
- rust-unsafe-code
- undefined-behaviour
papers:
- jung:popl:2017
---

One of the key strengths and weaknesses of Rust is the ability to extend its
typesystem with libraries that do not follow Rust's typesystem (i.e., they are
"unsafe") but that (we hope) do not break the Rust semantics that Rust's
typesystem is meant to enforce.
This paper describes a bounded model checking approach to verifying these
libraries for the kinds of error that violate Rust's typesystem.
The tool is demonstrated on three libraries and is able to detect
bugs in old versions of the libraries.

Their approach has three phases:

1. Exhaustive generation of sequences of calls to the library up to some
   size bound where sequences include all possible levels of sharing in order
   to test all forms of aliasing.
   The sequences of calls are followed by assertions to check for aliasing
   in the results of the call sequences that would contravene the Rust
   semantics.

2. Translation of the Rust code to C using a custom backend for the rustc Rust
   compiler.

3. Uses the CBMC bounded model checker for C to verify the translated code.

(They point out that the last two steps could be replaced by using a bounded
model checker such as LLBMC that would verify the LLVM IR code generated
inside the rustc compiler.)

It is useful to compare this with the
[Rustbelt paper][jung:popl:2017].
The Crust approach in this paper uses bounded model checking to automatically
and thoroughly
verify the code for certain classes of problem up to some bound
while the Rustbelt paper uses the Coq interactive theorem prover to manually verify
similar libraries that have been manually transcribed into
a similar language they call "lamda-rust".

I really like this work but it has a few limitations that are worth mentioning.
The focus is on detecting aliasing issues and does not appear to detect
concurrency issues or similar.
The aliasing detection is based on comparing pointers returned by library API
calls but it is not clear whether could be other forms of aliasing that
break the Rust semantics but do not show up as aliasing between
externally revealed pointers.
The Rust-to-C translation cannot handle closures or dynamic dispatch.
If the generated sequence generates a panic, this is ignored instead of
being reported as a failure – this feels like a missed opportunity.


{% include links.html %}
