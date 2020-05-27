---
ENTRYTYPE: inproceedings
abstract: 'Despite 20+ years of research on processor verification, it remains hard to use formal verification techniques in commercial processor development.  There
  are two significant factors: scaling issues and return on investment.  The scaling issues include the size of modern processor specifications, the size/complexity
  of processor designs, the size of design/verification teams and the (non)availability of enough formal verification experts.  The return on investment
  issues include the need to start catching bugs early in development, the need to continue catching bugs throughout development, and the need to be able
  to reuse verification IP, tools and techniques across a wide range of design styles.  This paper describes how ARM has overcome these issues in our Instruction
  Set Architecture Formal Verification framework ``ISA-Formal.'''' This is an end-to-end framework to detect bugs in the datapath, pipeline control and
  forwarding/stall logic of processors.  A key part of making the approach scale is use of a mechanical translation of ARM''s Architecture Reference Manuals
  to Verilog allowing the use of commercial model-checkers.  ISA-Formal has proven especially effective at finding micro-architecture specific bugs involving
  complex sequences of instructions.  An essential feature of our work is that it is able to scale all the way from simple 3-stage microcontrollers, through
  superscalar in-order processors up to out-of-order processors.  We have applied this method to 8 different ARM processors spanning all stages of development
  up to release.  In all processors, this has found bugs that would have been hard for conventional simulation-based verification to find and ISA-Formal
  is now a key part of ARM''s formal verification strategy.  To the best of our knowledge, this is the most broadly applicable formal verification technique
  for verifying processor pipeline control in mainstream commercial use.'
acceptance: '28'
added: 2019-06-01
affiliation: ARM Ltd
ar_shortname: CAV 16
authors:
- Alastair D. Reid
- Rick Chen
- Anastasios Deligiannis
- David Gilday
- David Hoyes
- Will Keen
- Ashan Pathirane
- Erin Shepherd
- Peter Vrabel
- Ali Zaidi
booktitle: Proceedings of the 2016 International Conference on Computer Aided Verification (CAV'16)
doi: 10.1007/978-3-319-41540-6_3
editor: S. Chaudhuri and A. Farzan
isbn: 978-3-319-41539-0
journal: CAV 2016, Part II, Lecture Notes in Computer Science
layout: paper
location: Toronto, Canada
month: July
number: '9780'
pages: 42-58
publisher: Springer Verlag
read: false
readings: []
series: Lecture Notes in Computer Science
title: End-to-end verification of ARM processors with ISA-formal
volume: '9780'
year: 2016
topics:
notes:
- Arm architecture
- ISA specification
- instruction set architecture
- bounded model checking
- dependent type
- ASL
papers:
---
{% include links.html %}
