---
ENTRYTYPE: inproceedings
abstract: Linear type systems allow destructive operations such as object deallocation
  and imperative updates of functional data structures. These operations and others,
  such as the ability to reuse memory at different types, are essential in low-level
  typed languages. However, traditional linear type systems are too restrictive for
  use in low-level code where it is necessary to exploit pointer aliasing. We present
  a new typed language that allows functions to specify the shape of the store that
  they expect and to track the flow of pointers through a computation. Our type system
  is expressive enough to represent pointer aliasing and yet safely permit destructive
  operations.
added: 2020-01-07
address: Berlin, Heidelberg
authors:
- Frederick Smith
- David Walker
- Greg Morrisett
booktitle: Programming Languages and Systems
editor: Smolka, Gert
isbn: 978-3-540-46425-9
layout: paper
pages: 366-381
publisher: Springer Berlin Heidelberg
read: true
readings:
- 2020-01-08
title: Alias Types
year: 2000
topics:
- types
- verification
---

One of the difficult things about reasoning about programs that
modify pointer-based data structures is the possibility of
aliases.
If p and q alias each other then you need to recognize that writing
to "*p" will modify "*q".
Around the late 90s, there was a lot of work on how best to
reason about aliasing.
Nowadays, a lot of academic interest seems to have settled on using
separation logic and a lot of practical interest seems to have
settled on Rust's ownership types or C++11's smart pointers, etc.
But what makes this paper interesting to me is that it tackled
one of the outstanding problems in the
[TALx86 paper]({{ "papers/morrisett:wcsss:1999.md" | relative_url }}).
In particular, because they were interested in reasoning
about assembly code, they could not rely on
simplifications made in high-level languages such as

- In languages that follow RAII, objects are atomically
  initialized as they are allocated.
  But, in assembly language fields of an object are
  initialized one at a time and so it is crucial to be
  able to reason about whether a field has been initialized
  or not.
- In high level languages, you can declare as many local
  variables as you like and they are all logically distinct
  but in assembly language, there is a fixed set of registers
  that get reused and function activation records live on
  a stack where they overwrite previously used activation
  records.
- In high level languages, all local variables are equally
  accessible but in assembly language, registers are more
  accessible than variables on the stack and so you will
  copy variables from one local variable (on the stack)
  to another (in a register) all the time.
  This creates aliases and you have to be able to reason
  about them.
  
Their introduction concludes "Type systems for low-level languages
should represent sharing".

The type system they create is based on ideas from linear logic.
In particular, they augment the type system with aliasing constraints and then they impose linearity constraints to
enforce the connection with aliasing.


The flexibility of the type system is demonstrated by examples
through the paper and a detailed description of how to compile
a Pascal-like "display" mechanism.
(I think that) displays are interesting and challenging
because the display is an array of pointers to nested
stack frames so reasoning about a display requires a lot
of the machinery that they develop.

The paper includes a 21 page appendix in which they prove
type soundness of their system using a proof in the style
of Wright and Felleisen.