---
ENTRYTYPE: inproceedings
added: 2020-01-06
authors:
- Greg Morrisett
- Karl Crary
- Neal Glew
- Dan Grossman
- Richard Samuels
- Frederick Smith
- David Walker
- Stephanie Weirich
- Steve Zdancewic
booktitle: In Second Workshop on Compiler Support for System Software
layout: paper
pages: 25-35
read: true
readings:
- 2020-01-06
title: 'TALx86: A realistic typed assembly language'
year: 1999
topics:
- types
- verification
notes:
- x86-architecture
- instruction-set-architecture
- typed-assembly-language
- linear-logic
papers:
---

Typed assembly language is normal assembly language (x86 in this case) where any branch targets are labelled with the type of
all the registers.
The main purpose of the types is to make the assembly code type/memory
safe and so the focus is on distinguishing pointers from
non-pointers and distinguishing the size and type of what each
pointer points to.
This paper is one of the later papers in a series on typed assembly language and also related to the Cyclone language: a type/memory-safe C substitute.

To demonstrate that their type system is expressive enough, they describe 'Popcorn' - a small C-like language that they can compile to TALx86.
Compared with C, some major differences are that Popcorn

* includes memory allocation
* distinguishes between pointers that can be null and pointers that cannot be null
* provides tagged union types that resemble the algebraic data types found in functional languages
* supports parametric polymorphism

The essence of TALx86's type system is that you can give a code label a type like "{eax: B4, ebx: B4, ebp: {eax:B4}}" that says that eax and ebx are 4-byte values and ebp is a pointer to code that expects a 4-byte value in eax.
Building on top of that, they also have

* the type of a stack is a list of types like "sptr {eax:B4}::B4::B4::rho" which gives the type of the top three entries on the stack
* parametric polymorphism is used to express the idea that a function will work on any stack shape
  by letting us write
  "forall rho:Ts. {esp:sptr{eax:B4, esp:sptr B4::rho}::B4::rho"
* return addresses are treated as continuations - so there is no need for function types
* fields of structs have a "variance" u, r, w or rw to indicate whether it is uninitialized (really important!) or is readable/writable (in the absence of alias tracking in the type system, this can cause false positives)
* arrays are handled using singleton types like {5} to express
  the type that must have the value 5 and using existentials
  to associate the size of an array with the array.
  The neat thing about this is that the size information
  doesn't have to be in a pre-determined position in memory.
* support for the tagged union types from Popcorn
* they have various forms of inference, etc. to reduce the annotation burden


Although they come very close, they can't quite allow arbitrary assembly.

* memory allocation and array index checks are performed using macros
* memory deallocation is performed using conservative garbage collection.
* the Popcorn runtime is not written in TALx86

{% include links.html %}
