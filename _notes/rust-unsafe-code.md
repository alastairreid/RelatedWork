---
layout: note
title: Rust unsafe code
website: https://doc.rust-lang.org/nomicon/
papers:
- jung:popl:2020
- wang:sosp:2013
- astrauskas:oopsla:2020
- qin:pldi:2020
- evans:icse:2020
notes:
- Rust language
- undefined behaviour
---

todo: Add some words around the following useful links

- <https://rust-lang.github.io/unsafe-code-guidelines/>
- <https://doc.rust-lang.org/nomicon/>

Blog posts about unsafe

- Ralf Jung [The scope of unsafe](https://www.ralfj.de/blog/2016/01/09/the-scope-of-unsafe.html)

  This post makes the point that unsafe code often depends on invariants holding
  and that adding safe code that breaks the invariants can make code incorrect.

  > There used to be claims on the interwebs that “if a Rust program crashes,
  > the bug must be in some unsafe block”. (And there probably still are.) Even
  > academic researchers working on Rust got this wrong, arguing that in order
  > to detect bugs in data structures like Vec it suffices to check functions
  > involving unsafe code.

- Niko Matsakis
  - [Unsafe abstractions](http://smallcultfollowing.com/babysteps/blog/2016/05/23/unsafe-abstractions/)
  - [The 'Tootsie Pop' model for unsafe code](http://smallcultfollowing.com/babysteps/blog/2016/05/27/the-tootsie-pop-model-for-unsafe-code/)

    This post makes the point that you need to look at which data structure fields are accessible to
    understand whether your unsafe code is safe because even unsafe code could
    break your code's invariants. For that reason, the unsafe boundary is closer
    to the module boundary (assuming the fields are not public).

- Alex Ozdemir
  - [Unsafe in Rust: Syntactic Patterns](https://cs.stanford.edu/~aozdemir/blog/unsafe-rust-syntax/)

    An early automated empirical analysis of thousands of Rust crates looking at how 'unsafe' is used
    in Rust code.
    See [astrauskas:oopsla:2020], [qin:pldi:2020] and [evans:icse:2020] for more recent analyses
    that dig into this from various perspectives.

  - [Unsafe in Rust: The Abstraction Safety Contract and Public Escape](https://cs.stanford.edu/~aozdemir/blog/unsafe-rust-escape/)

    A "public escape" occurs when a safety condition escapes through a safe public interface so that
    that interface cannot uphold the "Abstraction Safety Contract" (ASC).

    Proposes a backwards analysis to calculate the safety condition (precondition?) of a public, safe
    function and check that the condition always holds.


{% include links.html %}
