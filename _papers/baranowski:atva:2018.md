---
doi: 10.1007/978-3-030-01090-4_32
ENTRYTYPE: inproceedings
abstract:
  Rust is an emerging systems programming language with guaranteed
  memory safety and modern language features that has been extensively adopted to
  build safety-critical software. However, there is currently a lack of automated
  software verifiers for Rust. In this work, we present our experience extending
  the SMACK verifier to enable its usage on Rust programs. We evaluate SMACK on
  a set of Rust programs to demonstrate a wide spectrum of language features it
  supports.
added: 2020-01-10
address: Cham
authors:
- Marek S. Baranowski
- Shaobo He
- Zvonimir Rakamarić
booktitle: Automated Technology for Verification and Analysis
editor: 'Lahiri, Shuvendu K. and Wang, Chao'
isbn: 978-3-030-01090-4
layout: paper
pages: 528-535
publisher: Springer International Publishing
read: true
readings:
- 2020-01-16
title: Verifying Rust programs with SMACK
year: 2018
topics:
- tools
- verification
notes:
- Boogie verifier
- Corral verifier
- intermediate verification language
- Rust language
- Rust unsafe code
- SMACK verifier
- LLVM compiler
papers:
- rakamaric:cav:2014
- barnett:fmco:2005
- lal:fse:2014
- demoura:tacas:2008
---

The Rust programming language promises a balance between safety
and control that makes it an interesting target for
formal verification work.
Unfortunately, some of the earliest verification tools supporting
Rust are not maintained.
[SMACK][rakamaric:cav:2014]
is an LLVM-based verification toolchain that translates LLVM IR
into verification conditions.
In principle, it should be able to cope with any language that
can be translated to LLVM IR but every language has its quirks
and this paper describes additional features and analyses required
to support the Rust language well.
An interesting aspect of basing this on LLVM is that
it allows verification of programs that combine Rust and C
(or any other language that LLVM supports).

This toolchain uses rustc to convert Rust code to LLVM IR;
SMACK converts LLVM IR code
into [Boogie][barnett:fmco:2005]
[intermediate verification language]
and then into [Corral][lal:fse:2014]
and the [Z3 SMT solver][demoura:tacas:2008]
In this paper, this is used for bounded verification: unrolling loops and recursion up to some bound.



Some of the problems they solved in this paper are:

- detecting arithmetic overflow
- adding new macros 'assume' and 'assert'
- use of "i1" to represent booleans (instead of "i8" in C)
- better support for structures (which are used far more 
  extensively in idiomatic C code)
- rustc optimizations such as combining two 32-bit loads into
  a single 64-bit load
- rustc specific intrinsics such as "llvm.expect" that are
  used in Rust to provide branch hints
- creating models of standard libraries that replace Rust's
  highly optimized libraries with libraries more suited for
  verification
  
To drive development, they created some microbenchmarks
and to judge the quality of their implementation, they
verified three small (80–140 loc) real world applications.
(They had to slightly simplify all three applications
to simplify verification.)
In the process, they found a bug in one of the applications
and they realized that an overflow panic in one of the
other applications corresponded to a bug in a C implementation
of the same application.

Future work includes

- modelling more of the standard library
- checking unsafe pointer usage in Rust - especially those
  from external functions
- concurrency

{% include links.html %}
