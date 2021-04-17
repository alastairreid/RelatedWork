---
ENTRYTYPE: inproceedings
abstract: 'We give a rigorous characterization of what it means for a programming language to be memory safe, capturing the intuition that memory safety
  supports local reasoning about state. We formalize this principle in two ways. First, we show how a small memory-safe language validates a noninterference
  property: a program can neither affect nor be affected by unreachable parts of the state. Second, we extend separation logic, a proof system for heap-manipulating
  programs, with a ``memory-safe variant'''' of its frame rule. The new rule is stronger because it applies even when parts of the program are buggy or
  malicious, but also weaker because it demands a stricter form of separation between parts of the program state. We also consider a number of pragmatically
  motivated variations on memory safety and the reasoning principles they support. As an application of our characterization, we evaluate the security of
  a previously proposed dynamic monitor for memory safety of heap-allocated data.'
added: 2021-04-17
address: Cham
authors:
- Arthur Azevedo de Amorim
- Cătălin Hrițcu
- Benjamin C. Pierce
booktitle: Principles of Security and Trust
editor: Bauer, Lujo and Küsters, Ralf
isbn: 978-3-319-89722-6
layout: paper
pages: 79-105
publisher: Springer International Publishing
read: true
readings:
- 2021-04-17
title: The meaning of memory safety
year: 2018
notes:
- memory safety
- separation logic
- non-interference
- Coq theorem prover
- Rust language
- Cyclone language
papers:
---

Aims to define [memory safety] in terms of reasoning principles it enables instead of the errors that memory unsafety manifests.
The key idea is the [separation logic] notion of a function's "footprint" -- whether specified by a separation logic predicate
or by reachability (from free variables / arguments).

Discussed in the context of a simple imperative language that includes local
variables, heap objects, conditionals, loops and pointer arithmetic but whose
semantics uses some form of fat pointer so that the underlying object can
always be recovered. Also assumes underlying objects cannot be distinguished
and that memory is unbounded.

Initial set of theorems

1. Adding more memory doesn't affect result of terminating program.
2. Allocating objects in a different order doesn't affet result.
3. Adding more memory doesn't make non-terminating programs terminate.
4. Adding more memory doesn't make erroneous programs non-erroneous.

Corollary (non-interference): Inaccessible memory neither interferes with nor
is interfered with by a command.
Note that this captures both *integrity* and *secrecy*; they hint at connections between secrecy and relational program logics.

An initial attempt (theorem 5) at a frame rule following from theorems 1 and 3 is not very
useful because it only works for non-erroneous commands -- an overly restrictive requirement.

A revised attempt (theorem 6) uses a relaxed Hoare-style contract that allows
errors and replaces the 'separating conjunction' "p * r" with the 'isolating
conjunction' "p |> r" where none of the object *identifiers* in the state
described by p overlap with the objects in the state described by r. (The
difference is the addition of the word "identifiers").  Use of the isolating
conjunction ensures that the fragment satisfying 'r' is reachable from the rest
of the state.

In a realistic language, various parts of these guarantees are lost

- memory is finite - breaking integrity by allowing the outcome to depend
  on available free memory
- time is observable - breaking secrecy and integrity
- pointer values may be partly observable (e.g., can be ordered)
- memory can be allocated without initialization (perhaps restricted to
  having a non-pointer type) - breaking secrecy
- dangling pointers, double-free, etc. - breaking integrity
- pointer spoofing - e.g., Javascript allows all globals to be
  accessed via a string with its name: effectively allowing pointer spoofing.

The reason about a heap-safety monitor for machine-code.

Everything is formalized in [Coq theorem prover].

The related work points to other formalizations, languages such as garbage
collected languages, [Cyclone language] and [Rust language] that relax one or
more of the assumptions, etc.

{% include links.html %}
