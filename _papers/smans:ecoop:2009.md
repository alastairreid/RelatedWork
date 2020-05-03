---
ENTRYTYPE: inproceedings
abstract: The dynamic frames approach has proven to be a powerful formalism for specifying
  and verifying object-oriented programs. However, it requires writing and checking
  many frame annotations. In this paper, we propose a variant of the dynamic frames
  approach that eliminates the need to explicitly write and check frame annotations.
  Reminiscent of separation logic's frame rule, programmers write access assertions
  inside pre- and postconditions instead of writing frame annotations. From the precondition,
  one can then infer an upper bound on the set of locations writable or readable by
  the corresponding method. We implemented our approach in a tool, and used it to
  automatically verify several challenging programs, including subject-observer, iterator
  and linked list.
added: 2020-02-14
address: Berlin, Heidelberg
authors:
- Jan Smans
- Bart Jacobs
- Frank Piessens
booktitle: ECOOP 2009 -- Object-Oriented Programming
editor: Drossopoulou, Sophia
isbn: 978-3-642-03013-0
layout: paper
pages: 148-172
publisher: Springer Berlin Heidelberg
read: true
readings:
- 2020-02-14
title: 'Implicit dynamic frames: Combining dynamic frames and separation logic'
year: 2009
topics:
- tools
- verification
notes:
- permission-logic
- separation-logic
- implicit-dynamic-frames
papers:
- ohearn:cacm:2019
- jacobs:nfm:2011
---

Permission logics are Hoare-style logics for reasoning about heap allocated
data structures and whether a piece of code has permission to access a given
part of the structure.  Their particular strength is the ability to reason
about the lack of aliases – drawing on ideas from linear logic.  The best known
permission logic is
[separation logic][ohearn:cacm:2019];
another permission logic is dynamic frames.  This paper
tackles the problem that dynamic frames have a high annotation overhead because
of the need to define and manipulate “frame annotations” for each method.
Their solution is to infer the frame information directly from the access
assertions in the pre/post-conditions of functions.

A large part of what makes this more concise is that, in a tool like [VeriFast][jacobs:nfm:2011],
I have to write access predicates and (pure) expresssions separately.  For
example, given a pointer “p” to a pair with fields “lo” and “hi”, I might write
a predicate

p->lo ↦ ?l &∗& p->hi ↦ ?h &∗& l ≤ h

To say that I have access to the lo field and its value is “l” and I have
access to the hi field and its value is “h” and “l ≤ h”.  But, this seems
a bit verbose compared with

p->lo ≤ p->hi

Which, just by mentioning “p->lo” and “p->hi” implies that they are accessible.

The ideas in this paper were implemented in the “VeriCool” tool for verifying
concurrent object-oriented languages.


{% include links.html %}
