---
ENTRYTYPE: inproceedings
added: 2020-08-28
layout: paper
read: true
readings:
- 2020-08-27
url: http://www.cs.umd.edu/~pugh/SoftwareDefectWorkshop05/BugWorkshop05.pdf
title: Locating defects is uncertain
authors:
- Andreas Zeller
booktitle: Proceedings of BUGS 2005 (PLDI 2005 Workshop on the Evaluation of Software Defect Detection Tools)
location: Chicago, IL, USA
month: June
year: 2005
notes:
- bug localization
papers:
---

This one-page, position paper talks about bug localization.
Failures are seen as the symptom of a chain of infection that
starts with some initial cause/infection.

The problem of localization consists of splitting the code into
parts that are responsible for the bug and parts that are not.
The interesting observation is that

> to precisely locate the defect, we need a specification [of each part that is
> considered] that is precise enough to tell us where to correct it.

and this leads to the conclusion that

> programmers do not "locate" defects; they design fixes along with the
> implicit specification of what should be going on at this location—and the
> location that is changed is defined as the defect in hindsight.

Tools that try to locate bugs will be imprecise for several reasons so they
should estimate the probablity of each location they suggest and list locations
in order of decreasing probability.

{% include links.html %}
