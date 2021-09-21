---
ENTRYTYPE: inproceedings
added: 2021-09-21
authors:
- Zacharias Hadjilambrou
- Shidhartha Das
- Paul N Whatmough
- David Bull
- Yiannakis Sazeides
booktitle: 2019 IEEE International Symposium on Performance Analysis of Systems and Software (ISPASS)
doi: 10.1109/ISPASS.2019.00009
layout: paper
number: ''
pages: 1-10
read: true
readings:
- 2021-09-21
title: 'GeST: An automatic framework for generating CPU stress-tests'
volume: ''
year: 2019
notes:
- power virus
- resonant frequency
- Arm architecture
- x86 architecture
- hardware faults
- genetic algorithm
papers:
---

Digital electronics is a myth: the underlying analog nature of
digital electronics is revealed by overclocking, voltage droops,
resonance and a host of other effects.
Designers (and users) find it useful to stress-test CPUs
using [power viruses][power virus] that try to create
high IPC load, thermal load, voltage noise, etc.
at the resonant frequency of the chips power delivery network (PDN).
(Matching the PDN's 1st order resonance frequency maximizes the
CPU voltage droops and overshoots.)

The paper cites around 10 other papers about these various forms of virus.
Early power viruses were hand-written, then created using [genetic algorithms][genetic algorithm],
some use simulators to evaluate different sequences, some use real hardware,
some use measurements like IPC as proxies for power or temperature,
and various work focused on different kinds of virus (power, voltage noise).

GeST is an open source, easy to use framework that uses genetic algorithms
to generate a range of different viruses using whatever measurement
you want to use in the feedback mechanism, using whatever fitness function you want,
and supporting whatever assembly language you want to use.

GeST is demonstrated for both Arm and AMD processors to create IPC, power,
thermal and voltage noise viruses and the differences between the solutions
for the different feedback mechanisms are discussed.

{% include links.html %}
