---
ENTRYTYPE: inproceedings
abstract: 'An important correctness criterion for software running on embedded microcontrollers is stack safety: a guarantee that the call stack does not
  overflow. We address two aspects of the problem of creating stack-safe embedded software that also makes efficient use of memory: statically bounding
  worst-case stack depth, and automatically reducing stack memory requirements. Our first contribution is a method for statically guaranteeing stack safety
  by performing whole-program analysis, using an approach based on context-sensitive abstract interpretation of machine code. Abstract interpretation permits
  our analysis to accurately model when interrupts are enabled and disabled, which is essential for accurately bounding the stack depth of typical embedded
  systems. We have implemented a stack analysis tool that targets Atmel AVR microcontrollers, and tested it on embedded applications compiled from up to
  30,000 lines of C. We experimentally validate the accuracy of the tool, which runs in a few seconds on the largest programs that we tested. The second
  contribution of this paper is a novel framework for automatically reducing stack memory requirements. We show that goal-directed global function inlining
  can be used to reduce the stack memory requirements of component-based embedded software, on average, to 40\% of the requirement of a system compiled
  without inlining, and to 68\% of the requirement of a system compiled with aggressive whole-program inlining that is not directed towards reducing stack
  usage.'
added: 2019-06-01
affiliation: University of Utah
ar_shortname: EMSOFT 03
authors:
- John Regehr
- Alastair Reid
- Kirk Webb
booktitle: Embedded Software, Third International Conference (EMSOFT 2003)
day: 13-15
doi: 10.1007/978-3-540-45212-6_20
editor: Rajeev Alur and Insup Lee
layout: paper
location: Philadelphia, PA, USA
month: October
pages: 306-322
publisher: Springer
read: false
readings: []
series: Lecture Notes in Computer Science
title: Eliminating stack overflow by abstract interpretation
volume: '2855'
year: 2003
notes:
- abstract interpretation
- ISA specification
papers:
---

{% include links.html %}
