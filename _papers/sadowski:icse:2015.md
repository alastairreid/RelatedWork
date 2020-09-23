---
ENTRYTYPE: inproceedings
added: 2020-09-10
authors:
- Caitlin Sadowski
- Jeffrey van Gogh
- Ciera Jaspan
- Emma Söderberg
- Collin Winter
booktitle: 2015 IEEE/ACM 37th IEEE International Conference on Software Engineering
doi: 10.1109/ICSE.2015.76
issn: 1558-1225
keywords: ecology;program diagnostics;software architecture;program analysis ecosystem;tricorder;static analysis tools;code readability;developer workflow;codebases;scalable
  architecture;Google;Google;Computer bugs;Buildings;Ecosystems;Java;Libraries;Usability;program analysis;static analysis
layout: paper
month: May
number: ''
pages: 598-608
read: true
readings:
- 2020-09-21
title: 'Tricorder: Building a program analysis ecosystem'
volume: '1'
year: 2015
notes:
- google
papers:
- potvin:cacm:2016
- chou:bugs:2005
- wright:icsm:2013
- sadowski:icse:2015
- sadowski:cacm:2018
---

This paper describes the experience of deploying a static analysis
infrastructure at Google.
This infrastructure ("Tricorder") had to support multiple languages,
tens of thousands of users, large code scale, etc.
Most importantly though, it had to be accepted by developers
if it was going to provide any benefit.

## Design

### False positives

The most important issue was probably the handling of the false-positive rate.
While a tool developer might have a technology-driven definition of false
positives; to a tool user

> a false positive report is any repont that they did not want to see.

Tricorder's user interface has a "NOT USEFUL" button for reporting false
positives and the false positive rate is continuously monitored.

It seems that the preferred form of report includes a suggested fix
that the engineer can automatically add to their change.
As well as being easier to do, the suggested fix can help explain the report
and puts a focus on actionable reports.
Of course, not all analyses can support this. For example, a tool that detects
missing documentation can hardly write the documentation for you.


### Enable user contributions

Given the scale and language diversity of the codebase/programmers, Tricorder
makes it easy for programmers to create their own static analyses.
The Tricorder team's contract with analysis developers is that they have to
keep the false positive rate sufficiently low.

> Our experience is that pride-in-work combined with the threat of disabling an
> analyzer makes the authors highly motivated to fix problems in their
> analyzers.

The Tricorder team helps them figure out what has gone wrong by establishing
feedback loops, etc.
Often the reason that a report is not useful is because of the way the report
is worded.


### Integration into code review

Tricorder is integrated into the code review system to take advantage of
engineers being in a change mindset during review and to take advantage of
the peer pressure of having their code and any reports visible to other
engineers.

Tools with a higher false positive rate are run nightly and their results
are surfaced during code browsing, etc.
These are to support a dedicated cleanup team who work on global code health.


### Customization

To avoid engineers in the same team seeing different reports, customization is
only supported on a per-project basis, not on a per-user basis.  This  puts
more pressure on the false positive rate and encourages a focus on high
priority issues.


## Evaluation

The evaluation is based on data gathered during use by instrumentation
in the tools.
They show things like the overall "not useful" click rate over time, drill down
into individual analyses, discuss spikes and trends.
They show the number of occurrences of some coding pattern over time as an
analyzer started reporting that as an anti-pattern.

## Recommendations

- Make data driven improvements
- Developers do not like false positives
- Empower users to contribute
- Workflow integration is key
- Code review is an excellent time to show analysis results
- Project customization, not user customization
- Big impact for relatively simple checks (the analyses they describe
  do not use control or data-flow information, pointer analysis, whole-program
  analysis, abstract interpretation, etc.
- Analysis tools should fix bugs, not just find them
- Analysis tools should be shardable (i.e., usable with map-reduce)

{% include links.html %}
