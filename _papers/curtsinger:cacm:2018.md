---
ENTRYTYPE: article
abstract: 'Improving performance is a central concern for software developers. To locate optimization opportunities, developers rely on software profilers.
  However, these profilers only report where programs spend their time: optimizing that code may have no impact on performance. Past profilers thus both
  waste developer time and make it difficult for them to uncover significant optimization opportunities.This paper introduces causal profiling. Unlike past
  profiling approaches, causal profiling indicates exactly where programmers should focus their optimization efforts, and quantifies their potential impact.
  Causal profiling works by running performance experiments during program execution. Each experiment calculates the impact of any potential optimization
  by virtually speeding up code: inserting pauses that slow down all other code running concurrently. The key insight is that this slowdown has the same
  relative effect as running that line faster, thus "virtually" speeding it up.We present Coz, a causal profiler, which we evaluate on a range of highly-tuned
  applications such as Memcached, SQLite, and the PARSEC benchmark suite. Coz identifies previously unknown optimization opportunities that are both significant
  and targeted. Guided by Coz, we improve the performance of Memcached by 9\%, SQLite by 25\%, and accelerate six PARSEC applications by as much as 68\%;
  in most cases, these optimizations involve modifying under 10 lines of code.'
added: 2021-06-14
address: New York, NY, USA
authors:
- Charlie Curtsinger
- Emery D. Berger
doi: 10.1145/3205911
issn: 0001-0782
issue_date: June 2018
journal: Communications of the ACM
layout: paper
link: https://doi.org/10.1145/3205911
month: May
number: '6'
numpages: '9'
pages: 91-99
publisher: Association for Computing Machinery
read: false
readings: []
title: 'Coz: Finding code that counts with causal profiling'
url: https://doi.org/10.1145/3205911
volume: '61'
year: 2018
notes:
papers:
---
{% include links.html %}
