---
ENTRYTYPE: inproceedings
abstract: 'We describe the transformation of XVision, a large library of C++ code for real-time vision processing, into FVision (pronounced ``fission''''),
  a fully-featured domain-specific language embedded in Haskell. The resulting prototype system substantiates the claims of increased modularity, effective
  code reuse, and rapid prototyping that characterize the DSL approach to system design. It also illustrates the need for judicious interface design: relegating
  computationally expensive tasks to XVision (pre-existing C++ components), and leaving modular compositional tasks to FVision (Haskell). At the same time,
  our experience demonstrates how Haskell''s advanced language features (specifically parametric polymorphism, lazy evaluation, higher order functions and
  automatic storage reclamation) permit a rapid DSL design that is itself highly modular and easily modified. Overall, the resulting hybrid system exceeded
  our expectations: visual tracking programs continue to spend most of their time executing low level image-processing code, while Haskell''s advanced features
  allow us to quickly develop and test small prototype systems within a matter of a few days and to develop realistic applications within a few weeks.'
acceptance: '19'
added: 2019-06-01
affiliation: Yale University
ar_shortname: ICSE 99
authors:
- Alastair D. Reid
- John Peterson
- Gregory D. Hager
- Paul Hudak
booktitle: Proceedings of the 1999 International Conference on Software Engineering (ICSE '99)
day: 16-22
doi: 10.1109/icse.1999.841038
editor: Barry W. Boehm and David Garlan and Jeff Kramer
layout: paper
location: Los Angeles, CA, USA
month: May
pages: 484-493
publisher: ACM
read: false
readings: []
title: 'Prototyping real-time vision systems: An experiment in DSL design'
year: 1999
notes:
- Haskell language
- Functional Reactive Programming
- Domain Specific Language
papers:
---

{% include links.html %}
