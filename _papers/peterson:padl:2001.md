---
ENTRYTYPE: inproceedings
abstract: 'Functional programming languages are not generally associated with computationally intensive tasks such as computer vision. We show that a declarative
  programming language like Haskell is effective for describing complex visual tracking systems. We have taken an existing C++ library for computer vision,
  called XVision, and used it to build FVision (pronounced ``fission''''), a library of Haskell types and functions that provides a high-level interface
  to the lower-level XVision code. Using functional abstractions, users of FVision can build and test new visual tracking systems rapidly and reliably.
  The use of Haskell does not degrade system performance: computations are dominated by low-level calculations expressed in C++ while the Haskell ``glue
  code'''' has a negligible impact on performance.  FVision is built using functional reactive programming (FRP) to express interaction in a purely functional
  manner. The resulting system demonstrates the viability of mixed-language programming: visual tracking programs continue to spend most of their time executing
  low-level image-processing code, while Haskell''s advanced features allow us to develop and test systems quickly and with confidence. In this paper, we
  demonstrate the use of Haskell and FRP to express many basic abstractions of visual tracking.'
added: 2019-06-01
affiliation: Yale University
ar_shortname: PADL 01
authors:
- John Peterson
- Paul Hudak
- Alastair Reid
- Gregory D. Hager
booktitle: Practical Aspects of Declarative Languages, Third International Symposium (PADL 2001)
day: 11-12
doi: 10.1007/3-540-45241-9_21
editor: I. V. Ramakrishnan
layout: paper
location: Las Vegas, Nevada, USA
month: March
pages: 304-321
publisher: Springer
read: false
readings: []
series: Lecture Notes in Computer Science
title: 'FVision: A declarative language for visual tracking'
volume: '1990'
year: 2001
topics:
notes:
- haskell-language
papers:
---

{% include links.html %}
