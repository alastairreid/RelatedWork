---
ENTRYTYPE: inproceedings
added: 2020-01-28
authors:
- J. C. Reynolds
booktitle: Proceedings 17th Annual IEEE Symposium on Logic in Computer Science
doi: 10.1109/LICS.2002.1029817
issn: 1043-6871
keywords: formal logic;computational complexity;data structures;separation logic;shared
  mutable data structures;Hoare logic;reasoning;low-level imperative programs;imperative
  programming language;heap;program logic;address arithmetic;recursive procedures;Data
  structures;Computer science;Programmable logic arrays;Reflection;Logic programming;Computer
  languages;Logic arrays;Arithmetic;Artificial intelligence;Bibliographies
layout: paper
month: July
number: ''
pages: 55-74
read: true
readings:
- 2020-02-04
title: 'Separation logic: a logic for shared mutable data structures'
volume: ''
year: 2002
topics:
- verification
notes:
- separation-logic
- permission-logic
---

Separation logic is an extension of Hoare logic for reasoning about
programs that use pointers.
In particular, it copes well with aliasing (by providing
a compact way of saying that a set of pointers do not alias)
and a "frame rule" that lets you reason locally about a piece of
code without getting bogged down in the surrounding context.
This paper introduces separation logic,
illustrates its use to verify
 a number of list, tree and dag algorithms
 [this is one of the real strengths of this paper]
and discusses a lot of the work by the author and others
on developing, defining, using and extending 
the different forms of separation logic that existed at the
time (2002).

{% include links.html %}
