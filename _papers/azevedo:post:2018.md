---
ENTRYTYPE: inproceedings
abstract: 'We give a rigorous characterization of what it means for a programming language to be memory safe, capturing the intuition that memory safety
  supports local reasoning about state. We formalize this principle in two ways. First, we show how a small memory-safe language validates a noninterference
  property: a program can neither affect nor be affected by unreachable parts of the state. Second, we extend separation logic, a proof system for heap-manipulating
  programs, with a ``memory-safe variant'''' of its frame rule. The new rule is stronger because it applies even when parts of the program are buggy or
  malicious, but also weaker because it demands a stricter form of separation between parts of the program state. We also consider a number of pragmatically
  motivated variations on memory safety and the reasoning principles they support. As an application of our characterization, we evaluate the security of
  a previously proposed dynamic monitor for memory safety of heap-allocated data.'
added: 2021-04-17
address: Cham
authors:
- Arthur Azevedo de Amorim
- Cătălin Hrițcu
- Benjamin C. Pierce
booktitle: Principles of Security and Trust
editor: Bauer, Lujo and Küsters, Ralf
isbn: 978-3-319-89722-6
layout: paper
pages: 79-105
publisher: Springer International Publishing
read: false
readings: []
title: The meaning of memory safety
year: 2018
notes:
- memory safety
- separation logic
papers:
---
{% include links.html %}
