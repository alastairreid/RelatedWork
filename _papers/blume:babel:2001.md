---
ENTRYTYPE: article
abstract: We present a new foreign-function interface for SML/NJ. It is based on the idea of data-level interoperability-the ability of ML programs to inspect
  as well as manipulate C data structures directly. The core component of this work is an encoding of the almost2 complete C type system in ML types. The
  encoding makes extensive use of a "folklore" typing trick, taking advantage of ML's polymorphism, its type constructors, its abstraction mechanisms, and
  even functors. A small low-level component which deals with C struct and union declarations as well as program linkage is hidden from the programmer's
  eye by a simple program-generator tool that translates C declarations to corresponding ML glue code.
added: 2021-06-26
authors:
- Matthias Blume
doi: https://doi.org/10.1016/S1571-0661(05)80452-9
issn: 1571-0661
journal: Electronic Notes in Theoretical Computer Science
layout: paper
link: https://www.sciencedirect.com/science/article/pii/S1571066105804529
note: BABEL'01, First International Workshop on Multi-Language Infrastructure and Interoperability (Satellite Event of PLI 2001)
number: '1'
pages: 36-52
read: false
readings: []
title: 'No-longer-foreign: Teaching an ML compiler to speak C "natively"'
url: https://www.sciencedirect.com/science/article/pii/S1571066105804529
volume: '59'
year: 2001
notes:
- foreign function interface
- phantom types
papers:
---
{% include links.html %}
