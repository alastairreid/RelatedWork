---
ENTRYTYPE: article
abstract: A record data type can be extended by addition of more fields. The extended type is a subtype of the original, in that any value of the extended
  type can be regarded as a value of the original type by ignoring the additional fields. This results in a type hierarchy.Milner [3] has proposed a polymorphic
  type system. With the Milner approach, the type of a function may contain type variables. This also results in a type hierarchy.In a language with a polymorphic
  type system, if it is anticipated that a record type will need to be extended, then the record type can be defined to have a dummy extension field. In
  the parent type, the extension field will have null contents of type void. The type of the extension field can differ with different subtypes.The approach
  can be extended to allow a type to be subtype of two or more parent types.To a limited extent, this approach can be used in Ada and other languages with
  generic program units.
added: 2021-06-26
address: New York, NY, USA
authors:
- F. Warren Burton
doi: 10.1145/77606.214515
issn: 0164-0925
issue_date: Jan. 1990
journal: ACM Trans. Program. Lang. Syst.
layout: paper
link: https://doi.org/10.1145/77606.214515
month: January
number: '1'
numpages: '4'
pages: 135-138
publisher: Association for Computing Machinery
read: false
readings: []
title: Type extension through polymorphism
url: https://doi.org/10.1145/77606.214515
volume: '12'
year: 1990
notes:
- phantom types
papers:
---
{% include links.html %}
