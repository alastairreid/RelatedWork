---
ENTRYTYPE: inproceedings
added: 2020-08-28
layout: paper
read: true
readings:
- 2020-08-27
url: http://www.cs.umd.edu/~pugh/SoftwareDefectWorkshop05/BugWorkshop05.pdf
title: Soundness and its role in bug detection systems
authors:
- Yichen Xie
- Mayur Naik
- Brian Hackett
- Alex Aiken
booktitle: Proceedings of BUGS 2005 (PLDI 2005 Workshop on the Evaluation of Software Defect Detection Tools)
location: Chicago, IL, USA
month: June
year: 2005
notes:
- under-approximation
papers:
- godefroid:bugs:2005
---

This one-page, position paper talks about three different, competing costs in
a tool: soundness (no false negatives); cost; and usability (which relates to
false positives).  They argue:

1. that unsound tools will usually appear before sound tools;
2. that sound tools will eventually appear;
3. that user-annotations will be used.

This paper is worth reading alongside [godefroid:bugs:2005] (from the same
workshop) that also discusses soundness but with a completely different
interpretation.

{% include links.html %}
