---
ENTRYTYPE: article
added: 2020-01-10
address: New York, NY, USA
articleno: Article 66
authors:
- Ralf Jung
- Jacques-Henri Jourdan
- Robbert Krebbers
- Derek Dreyer
doi: 10.1145/3158154
issue_date: December 2017
journal: Proc. ACM Program. Lang.
keywords: logical relations, concurrency, type systems, Rust, separation logic
layout: paper
month: December
number: POPL
numpages: '34'
publisher: Association for Computing Machinery
read: true
readings:
- 2020-01-10
title: 'RustBelt: Securing the foundations of the Rust programming language'
url: https://doi.org/10.1145/3158154
volume: '2'
year: 2017
topics:
- rust
- types
- verification
---

Rust aims to archive the holy grail of a language that gives low-control over resource management and safe high-level abstractions.
It does this using a type system that restricts programs to eliminate unsafe programming practices coupled with a practice of extending that type system with libraries that are observably safe but that internally use “unsafe” operations.
This paper provides a framework for proving that these libraries do not break the safety guarantees of the standard type system.
Along the way, the paper gives a nice insight into the way that the community as a whole has been developing.

This paper departs from standard practice over the last 20 or so years of using syntactic techniques to prove results about the type system.
They argue that these syntactic techniques are closed-world methods but Rust’s extensible type system requires an open-world approach.
So they revert to the older practice of proving type soundness semantically.
This is done in the Iris framework building on “step-indexed” logical relations for scalability.

After a tour of the key concepts in Rust’s ownership type system, they present lambda-rust which is at a level simile are to Rust’s Mid-level Intermediate Representations (MIR) and is (roughly) a continuation passing lambda calculus extended with lifetimes.


For a more detailed summary, I recommend [the morning
paper](https://blog.acolyer.org/2018/01/18/rustbelt-securing-the-foundations-of-the-rust-programming-language/).

