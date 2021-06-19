---
ENTRYTYPE: article
added: 2021-06-19
authors:
- Joshua Yanovski
- Hoang-Hai Dang
- Ralf Jung
- Derek Dreyer
layout: paper
read: true
readings:
- 2021-06-19
title: 'GhostCell: Separating permissions from data in Rust'
link: https://plv.mpi-sws.org/rustbelt/ghostcell/paper.pdf
year: 2021
month: March
notes:
- Rust language
- ownership types
- regions
- Rust unsafe code
- RustBelt verifier
- Coq theorem prover
papers:
- beingessner:msc:2015
- fluet:jfp:2006
- jung:popl:2017
- jung:popl:2020
- clarke:oopsla:1998
---

This (currently unpublished) draft paper
shows how to use phantom types [fluet:jfp:2006]
together with [Rust][Rust language]'s
lifetime annotations
to capture the idea that a data structure 
should be seen as a single data structure
even though it is made up of multiple objects.
This gives a zero-overhead, safe mechanism to create
data structures with sharing and cycles
like a doubly linked list.

The use of lifetimes in this way was originally developed in
[beingessner:msc:2015] but is still somewhat unusual so they
prove that the GhostCell implementation is safe using [RustBelt][Rustbelt verifier].

The idea is based on the idea of branded types
and Haskell's `runST` function
and Beingessner's `BrandedVec` [beingessner:msc:2015].

> The key idea of `GhostCell` is to separate the permission to access a data structure from the data
> itself. As such, `GhostCell` introduces two types: `GhostToken<'id>` and `GhostCell<'id, T>`.
>
> * `GhostCell<'id, T>` describes data of type T that is marked with the brand 'id. When
>   this “cell” type is shared, the data it contains can only be accessed by whoever holds the
>   corresponding GhostToken<'id>.
>
> * `GhostToken<'id>` represents the permission to access all data in GhostCells marked with
>   the brand 'id.

The key operation that makes it all work is `GhostToken::new(k)`
that takes a continuation `k` of type `FnOnce(GhostToken<'new_id>) -> R`,
and runs `k` on a fresh, unique `GhostToken` (made unique by the `'new_id` brand).
This token gives permission to `borrow` or `borrow_mut` any GhostCells
with the same brand --- typically all the other objects in the data structure.
Using a continuation is a key part of restricting the `'new_id` brand
to the execution of the continuation.


{% include links.html %}
