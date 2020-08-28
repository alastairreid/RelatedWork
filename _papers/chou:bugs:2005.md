---
ENTRYTYPE: inproceedings
added: 2020-08-28
layout: paper
read: true
readings:
- 2020-08-27
url: http://www.cs.umd.edu/~pugh/SoftwareDefectWorkshop05/BugWorkshop05.pdf
title: "False positives over time: A problem in deploying static analysis tools"
authors:
- Andy Chou
booktitle: Proceedings of BUGS 2005 (PLDI 2005 Workshop on the Evaluation of Software Defect Detection Tools)
location: Chicago, IL, USA
month: June
year: 2005
notes:
papers:
---

This one-page, position paper by one of the cofounders of Coverity
makes the interesting observation (that is obvious once it has been said)

> All source code analyzers generate false positives, or issues which are
> reported but are not really defects. False positives accumulate over time
> because developers fix real defects but tend to leave false positives in the
> source code.

Six mitigations are briefly sketched:

- annotations in the source code
- override analysis decisions
- change the source code
- stop using the tool or disable specific analyses
- rank errors based on utility, probability or whatever.  (This is what
  Coverity does)
- annotate false positives

Solutions based on changing source code are vulnerable to changes in the tool
rendering the changes obsolete because the tool no longer trips up on that
part of the code.

{% include links.html %}
