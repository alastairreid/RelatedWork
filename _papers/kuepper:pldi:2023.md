---
ENTRYTYPE: article
abstract: Most software domains rely on compilers to translate high-level code to multiple different machine languages, with performance not too much worse
  than what developers would have the patience to write directly in assembly language. However, cryptography has been an exception, where many performance-critical
  routines have been written directly in assembly (sometimes through metaprogramming layers). Some past work has shown how to do formal verification of
  that assembly, and other work has shown how to generate C code automatically along with formal proof, but with consequent performance penalties vs. the
  best- known assembly. We present CryptOpt, the first compilation pipeline that specializes high-level cryptographic functional programs into assembly
  code significantly faster than what GCC or Clang produce, with mechanized proof (in Coq) whose final theorem statement mentions little beyond the input
  functional program and the operational semantics of x86-64 assembly. On the optimization side, we apply randomized search through the space of assembly
  programs, with repeated automatic benchmarking on target CPUs. On the formal-verification side, we connect to the Fiat Cryptography framework (which translates
  functional programs into C-like IR code) and extend it with a new formally verified program-equivalence checker, incorporating a modest subset of known
  features of SMT solvers and symbolic-execution engines. The overall prototype is quite practical, e.g. producing new fastest-known implementations of
  finite-field arithmetic for both Curve25519 (part of the TLS standard) and the Bitcoin elliptic curve secp256k1 for the Intel 12𝑡ℎ and 13𝑡ℎ generations.
added: 2023-07-02
address: New York, NY, USA
articleno: '158'
authors:
- Joel Kuepper
- Andres Erbsen
- Jason Gross
- Owen Conoly
- Chuyue Sun
- Samuel Tian
- David Wu
- Adam Chlipala
- Chitchanok Chuengsatiansup
- Daniel Genkin
- Markus Wagner
- Yuval Yarom
doi: 10.1145/3591272
issue_date: June 2023
journal: Proc. ACM Program. Lang.
keywords: search-based software engineering, assembly, elliptic-curve cryptography
layout: paper
link: https://doi.org/10.1145/3591272
month: jun
number: PLDI
numpages: '25'
publisher: Association for Computing Machinery
read: false
readings: []
title: 'CryptOpt: Verified compilation with randomized program search for cryptographic primitives'
url: https://doi.org/10.1145/3591272
volume: '7'
year: 2023
notes:
- cryptography
- verification
papers:
---

Generates very fast crypto code using random mutation, hill-climbing and
verification of the final result.
To avoid finding a local maximum, they run with 100(?) random seeds,
perform 1000(?) optimization steps then pick the winner so far and
perform 100,000 more optimization steps.

Critically relies on being able to run with "typical input" so the random
mutation approach is mostly limited to applications like crypto where timing
does not vary with input value.

{% include links.html %}
