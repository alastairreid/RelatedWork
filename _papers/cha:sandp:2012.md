---
ENTRYTYPE: inproceedings
abstract: 'In this paper we present Mayhem, a new system for automatically finding exploitable bugs in binary (i.e., executable) programs. Every bug reported
  by Mayhem is accompanied by a working shell-spawning exploit. The working exploits ensure soundness and that each bug report is security-critical and
  actionable. Mayhem works on raw binary code without debugging information. To make exploit generation possible at the binary-level, Mayhem addresses two
  major technical challenges: actively managing execution paths without exhausting memory, and reasoning about symbolic memory indices, where a load or
  a store address depends on user input. To this end, we propose two novel techniques: 1) hybrid symbolic execution for combining online and offline (concolic)
  execution to maximize the benefits of both techniques, and 2) index-based memory modeling, a technique that allows Mayhem to efficiently reason about
  symbolic memory at the binary level. We used Mayhem to find and demonstrate 29 exploitable vulnerabilities in both Linux and Windows programs, 2 of which
  were previously undocumented.'
added: 2021-03-15
authors:
- Sang Kil Cha
- Thanassis Avgerinos
- Alexandre Rebert
- David Brumley
booktitle: 2012 IEEE Symposium on Security and Privacy
doi: 10.1109/SP.2012.31
issn: 2375-1207
keywords: binary codes;program debugging;Mayhem;binary programs;executable programs;working shell-spawning exploit;bug report;raw binary code;exploit generation;binary-level;active
  managing execution paths;symbolic memory indices;hybrid symbolic execution;online execution;offline execution;concolic execution;Linux programs;Windows
  programs;Concrete;Computer bugs;Engines;Servers;Binary codes;Switches;Memory management;hybrid execution;symbolic memory;index-based memory modeling;exploit
  generation
layout: paper
month: May
number: ''
pages: 380-394
read: false
readings: []
title: Unleashing Mayhem on binary code
volume: ''
year: 2012
notes:
- symbolic execution
- binary analysis
- automatic exploit generation
- Mayhem
papers:
---
{% include links.html %}
