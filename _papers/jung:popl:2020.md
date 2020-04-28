---
ENTRYTYPE: article
added: 2020-01-28
address: New York, NY, USA
articleno: Article 41
authors:
- Ralf Jung
- Hoang-Hai Dang
- Jeehoon Kang
- Derek Dreyer
doi: 10.1145/3371109
issue_date: January 2020
journal: Proc. ACM Program. Lang.
keywords: program transformation, Rust, operational semantics, alias analysis
layout: paper
month: December
number: POPL
numpages: '32'
publisher: Association for Computing Machinery
read: true
readings:
- 2020-01-19
title: 'Stacked borrows: An aliasing model for Rust'
url: https://doi.org/10.1145/3371109
volume: '4'
year: 2019
topics:
- rust-language
notes:
- rust-language
- mir-interpreter
- undefined-behaviour
- mir
- rust-unsafe-code
- coq-theorem-prover
---

As in [the Rustbelt paper]({{ "papers/jung:popl:2017" | relative_url }}),
the topic of this paper is the soundness of Rust code that
is marked "unsafe" because it needs to do something that
cannot be expressed within the restrictions of Rust's type
system but that the programmer (hopefully) considers to be
ok.
In particular, this paper defines what the "unsafe" code
is and (crucially) is not allowed to do based on what
they want Rust types to mean.

There is no "right answer" in this sort of paper – you can't
prove that you have the right design.
But what they can do is
- Describe how their choice handles particular tricky cases
- Demonstrate that their choice matches people's expectations on some specific cases.
  (They go further and prove two desirable compiler transformations
  are valid under their semantics.)
- Measure the impact of the semantics on existing code to
  get a sense of whether their model fits with how most
  people in the community think.
  (In the architecture-independent part of the standard
  libraries, they found only six violations of their rules.)
- Persuade the community that any changes required by their
  semantics are acceptable.
  (All six violations have now been fixed.)
  
The major tool that they used for this work is 
"Miri" – an interpreter for Rust that tries to catch
all (most?) undefined behaviour.
They extended this interpreter with 
their semantics to let them experiment with different
variations.
This was clearly key to finding the sweet spot of
a restrictive semantics that lets you prove things
but that fits programmer's existing model of Rust.

The model itself is based on two changes to the semantics

- Tagging pointers so that it is possible to distinguish
  two pointers to the same object.
  (Surprisingly, it did not seem to be necessary to track
  provenance: how a pointer was generated.)
- For each object in memory, maintaining a stack of the
  pointers that are allowed to access it (and in what way).
  A stack of pointers is used to model nested borrowing.
  
The obvious piece of future work is to extend RustBelt
([jung:popl:2017]) with this model.

[jung:popl:2017]: {{ "papers/jung:popl:2017" | relative_url }}
