---
ENTRYTYPE: inproceedings
abstract: COASTAL is a program analysis tool for Java programs. It combines concolic execution and fuzz testing in a framework with built-in concurrency,
  allowing the two approaches to cooperate naturally.
added: 2020-08-11
address: Cham
authors:
- Willem Visser
- Jaco Geldenhuys
booktitle: Tools and Algorithms for the Construction and Analysis of Systems
doi: 10.1007/978-3-030-45237-7_23
editor: Biere, Armin and Parker, David
isbn: 978-3-030-45237-7
layout: paper
pages: 373-377
publisher: Springer International Publishing
read: true
readings:
- 2020-08-11
title: 'COASTAL: Combining concolic and fuzzing for Java (competition contribution)'
year: 2020
notes:
- fuzz testing
- symbolic execution
- SV competition
- test generation
papers:
---

This is a nice short, readable description of Coastal which

- maintains two work queues (one for [fuzz testing]
  and one for [symbolic execution])
- uses "strategies" to generate new queue entries from the results of the
  fuzzing and symex engines
- uses "observers" to track assertions, coverage, prune paths, display
  information in a GUI

Coastal was still under development when it was entered in [SV competition].


{% include links.html %}
