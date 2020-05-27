---
ENTRYTYPE: inproceedings
abstract: 'Interrupt handling is a tricky business in lazy functional languages: we have to make sure that thunks that are being evaluated can be halted
  and later restarted if and when they are required. This is a particular problem for implementations which use black-holing. Black-Holing deliberately
  makes it impossible to revert such thunks to their original state to avoid a serious space leak. Interactive Haskell implementations such as Hugs and
  hbi catch interrupts and avoid the problem by omitting or disabling black-holing. Batch mode Haskell implementations such as HBC and the Glasgow Haskell
  Compiler (GHC) avoid this problem by disabling black-holing or by providing no way to catch interrupts. This paper describes a modification to GHC''s
  abstract machine (the Spineless Tagless G-Machine) which simultaneously supports both interrupts and black-holing.'
added: 2019-06-01
affiliation: Yale University
ar_shortname: IFL 98
authors:
- Alastair D. Reid
booktitle: Implementation of Functional Languages, 10th International Workshop (IFL'98) Selected Papers
day: 9-11
doi: 10.1007/3-540-48515-5_12
editor: Kevin Hammond and Antony J. T. Davie and Chris Clack
layout: paper
location: London, UK
month: September
pages: 186-199
publisher: Springer
read: false
readings: []
series: Lecture Notes in Computer Science
title: 'Putting the spine back in the Spineless Tagless G-Machine: An implementation of resumable black-holes'
volume: '1595'
year: 1998
topics:
notes:
- Haskell language
papers:
---

{% include links.html %}
