---
ENTRYTYPE: inproceedings
abstract: Swarm testing is a novel and inexpensive way to improve the diversity of test cases generated during random testing. Increased diversity leads
  to improved coverage and fault detection. In swarm testing, the usual practice of potentially including all features in every test case is abandoned.
  Rather, a large "swarm" of randomly generated configurations, each of which omits some features, is used, with configurations receiving equal resources.
  We have identified two mechanisms by which feature omission leads to better exploration of a system's state space. First, some features actively prevent
  the system from executing interesting behaviors; e.g., "pop" calls may prevent a stack data structure from executing a bug in its overflow detection logic.
  Second, even when there is no active suppression of behaviors, test features compete for space in each test, limiting the depth to which logic driven
  by features can be explored. Experimental results show that swarm testing increases coverage and can improve fault detection dramatically; for example,
  in a week of testing it found 42\% more distinct ways to crash a collection of C compilers than did the heavily hand-tuned default configuration of a
  random tester.
added: 2021-02-26
address: New York, NY, USA
authors:
- Alex Groce
- Chaoqiang Zhang
- Eric Eide
- Yang Chen
- John Regehr
booktitle: Proceedings of the 2012 International Symposium on Software Testing and Analysis
doi: 10.1145/2338965.2336763
isbn: '9781450314541'
layout: paper
link: https://doi.org/10.1145/2338965.2336763
location: Minneapolis, MN, USA
numpages: '11'
pages: 78-88
publisher: Association for Computing Machinery
read: false
readings: []
series: ISSTA 2012
title: Swarm testing
url: https://doi.org/10.1145/2338965.2336763
year: 2012
notes:
- swarm verification
papers:
- holzmann:ieeetse:2011
---

{% include links.html %}