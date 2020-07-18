---
ENTRYTYPE: inproceedings
abstract: 'Knit is a new component specification and linking language. It was initially designed for low-level systems software, which requires especially
  flexible components with especially well-defined interfaces. For example, threads and virtual memory are typically implemented by components within the
  system, instead of being supplied by some execution environment. Consequently, components used to construct the system must expose interactions with threads
  and memory. The component composition tool must then check the resulting system for correctness, and weave the components together to achieve reasonable
  performance.  Component composition with Knit thus acts like aspect weaving: component interfaces determine the ``join points'''' for weaving, while components
  (some of which may be automatically generated) implement aspects. Knit is not limited to the construction of low-level software, and to the degree that
  a set of components exposes fine-grained relationships, Knit provides the benefits of aspect-oriented programming within its component model.'
added: 2019-06-01
affiliation: University of Utah
ar_shortname: ASPSE 01
authors:
- Eric Eide
- Alastair D. Reid
- Matthew Flatt
- Jay Lepreau
booktitle: Workshop on Advanced Separation of Concerns in Software Engineering
layout: paper
location: Toronto, Ontario, Canada
month: May
read: false
readings: []
title: 'Aspect weaving as component knitting: Separating concerns with Knit'
year: 2001
notes:
- operating systems
- Domain Specific Language
papers:
- reid:osdi:2000
---

{% include links.html %}
