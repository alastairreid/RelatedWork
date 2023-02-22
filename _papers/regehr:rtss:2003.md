---
ENTRYTYPE: inproceedings
abstract: 'We have developed a new way to look at real-time and embedded software: as a collection of execution environments created by a hierarchy of schedulers.
  Common schedulers include those that run interrupts, bottom-half handlers, threads, and events. We have created algorithms for deriving response times,
  scheduling overheads, and blocking terms for tasks in systems containing multiple execution environments. We have also created task scheduler logic, a
  formalism that permits checking systems for race conditions and other errors. Concurrency analysis of low-level software is challenging because there
  are typically several kinds of locks, such as thread mutexes and disabling interrupts, and groups of cooperating tasks may need to acquire some, all,
  or none of the available types of locks to create correct software. Our high level goal is to create systems that are evolvable: they are easier to modify
  in response to changing requirements than are systems created using traditional techniques. We have applied our approach to two case studies in evolving
  software for networked sensor nodes.'
added: 2019-06-01
affiliation: University of Utah
ar_shortname: RTSS 03
authors:
- John Regehr
- Alastair D. Reid
- Kirk Webb
- Michael A. Parker
- Jay Lepreau
booktitle: Proceedings of the 24th IEEE Real-Time Systems Symposium (RTSS 2003)
day: 3-5
doi: 10.1109/REAL.2003.1253251
layout: paper
location: Cancun, Mexico
month: December
pages: 25-36
publisher: IEEE Computer Society
read: false
readings: []
title: Evolving real-time systems using hierarchical scheduling and concurrency analysis
year: 2003
topics:
notes:
- networks
- operating systems
papers:
---

{% include links.html %}
