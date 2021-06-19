---
ENTRYTYPE: inproceedings
abstract: Object-oriented programming languages allow inter-object aliasing. Although necessary to construct linked data structures and networks of interacting
  objects, aliasing is problematic in that an aggregate object's state can change via an alias to one of its components, without the aggregate being aware
  of any aliasing.Ownership types form a static type system that indicates object ownership. This provides a flexible mechanism to limit the visibility
  of object references and restrict access paths to objects, thus controlling a system's dynamic topology. The type system is shown to be sound, and the
  specific aliasing properties that a system's object graph satisfies are formulated and proven invariant for well-typed programs.
added: 2021-06-19
address: New York, NY, USA
authors:
- David G. Clarke
- John M. Potter
- James Noble
booktitle: Proceedings of the 13th ACM SIGPLAN Conference on Object-Oriented Programming, Systems, Languages, and Applications
doi: 10.1145/286936.286947
isbn: '1581130058'
keywords: containment, ownership, programming language design, representation exposure, sharing, alias protection
layout: paper
link: https://doi.org/10.1145/286936.286947
location: Vancouver, British Columbia, Canada
numpages: '17'
pages: 48-64
publisher: Association for Computing Machinery
read: false
readings: []
series: OOPSLA '98
title: Ownership types for flexible alias protection
url: https://doi.org/10.1145/286936.286947
year: 1998
notes:
- Rust language
- ownership types
- regions
papers:
---
{% include links.html %}
