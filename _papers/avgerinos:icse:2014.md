---
ENTRYTYPE: inproceedings
added: 2020-07-08
address: New York, NY, USA
authors:
- Thanassis Avgerinos
- Alexandre Rebert
- Sang Kil Cha
- David Brumley
booktitle: Proceedings of the 36th International Conference on Software Engineering
doi: 10.1145/2568225.2568293
isbn: '9781450327565'
keywords: Verification, Symbolic Execution, Veritesting
layout: paper
link: https://doi.org/10.1145/2568225.2568293
location: Hyderabad, India
numpages: '12'
pages: 1083-1094
publisher: Association for Computing Machinery
read: true
readings:
- 08-07-2020
series: ICSE 2014
title: Enhancing symbolic execution with veritesting
url: https://doi.org/10.1145/2568225.2568293
year: 2014
notes:
- symbolic execution
- BAP tool
- PIN tool
- Z3 solver
papers:
---

This paper attacks the path explosion problem of [symbolic execution] by using
a hybrid of dynamic symbolic execution (DSE) and static symbolic execution
(SSE) that they call "veritesting".  Their tool "MergePoint" starts with
concolic execution (a form of DSE) from some seed but opportunistically
switches to SSE whenever the paths ahead contain straightforward code that SSE
can cope with.  They find that the additional cost due to having larger, more
complex SMT queries is compensated for by the exponentially smaller number of
paths

The tool is based on converting x86 machine code to CFGs (using the Binary
Analysis Platform (BAP)), introducing transition points where execution
should switch from SSE back to DSE and merging paths that do not include
transitions.
This is built on top of the Mayhem symbolic execution tool, the [BAP tool],
the [PIN tool] and the [Z3 solver] and they are able to turn SSE on or off
allowing a very clear measurement of the benefit of their hybrid mode.

The evaluation is a particularly impressive demonstration of their ability
to scale: they take all binaries from Debian
(that do not access hardcoded file paths) and symbolically execute them all.
They measure several coverage-related
metrics and report a large number of bugs.  In fact, their tool scales so well
that the bottleneck becomes bug reporting: finding who to report the bugs to,
writing the bug report, etc.  Within the timelimit they use, SSE does not cover
every single line or find every single bug found without SSE but SSE covers
more code and finds more bugs.

They also analyze coreutils (the traditional benchmark for symbolic execution
tools) and, despite this suite having been analyzed many times before, they are
able to find a new family of bugs.

An interesting new statistic reported in this paper is the (estimated) cost of
bug discovery: $0.28 per bug on Amazon's EC2 instances.  This metric is
imperfect because costs will change over time, and because crash triage is an
approximate and inconsistent technique. But, it is probably one of the key
metrics that would be used to decide when and for how long to use a tool like
this.


{% include links.html %}
