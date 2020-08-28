---
ENTRYTYPE: inproceedings
added: 2020-08-28
layout: paper
read: true
readings:
- 2020-08-27
url: https://patricegodefroid.github.io/public_psfiles/bugs2005.pdf
url2: http://www.cs.umd.edu/~pugh/SoftwareDefectWorkshop05/BugWorkshop05.pdf
authors:
- Patrice Godefroid
title: The soundness of bugs is what matters (position statement)
booktitle: Proceedings of BUGS 2005 (PLDI 2005 Workshop on the Evaluation of Software Defect Detection Tools)
location: Chicago, IL, USA
month: June
year: 2005
notes:
- symbolic execution
- under-approximation
papers:
- xie:bugs:2005
---

This one-page, position paper is "written in a provocative style for
entertainment purposes" but, nevertheless, makes some very good points.  The
main argument is that the goal of most verification research is defect
detection and that they should therefore focus on finding "sound bugs" (bugs
that can actually occur) and avoid "unsound bugs" (false alarms).  This is why
(despite its limitations) testing remains so important: testing finds sound
bugs.  The solution is to switch from "may analysis" (over-approximation) to
"must analysis" ([under-approximation]).

This paper is worth reading alongside [xie:bugs:2005] (from the same workshop)
that uses "soundness" in the more conventional sense of showing absence of any
bugs of a certain class.

{% include links.html %}
