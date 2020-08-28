---
ENTRYTYPE: inproceedings
added: 2020-08-28
layout: paper
read: true
readings:
- 2020-08-27
url: http://www.cs.umd.edu/~pugh/SoftwareDefectWorkshop05/BugWorkshop05.pdf
title: Issues in deploying software defect detection tools
authors:
- David R. Cok
booktitle: Proceedings of BUGS 2005 (PLDI 2005 Workshop on the Evaluation of Software Defect Detection Tools)
location: Chicago, IL, USA
month: June
year: 2005
notes:
- under-approximation
papers:
---

This one-page, position paper talks about what makes a bug-finding tool useful
and usable in an industrial setting.
The [slides](https://www.cs.umd.edu/~pugh/BugWorkshop05/presentations/3-adoptation/Cok-BUGS05.pdf) are worth reading since they say things not present in the paper.

Usefulness is affected by three things

- Accuracy.
  In the [slides](https://www.cs.umd.edu/~pugh/BugWorkshop05/presentations/3-adoptation/Cok-BUGS05.pdf)
  the conventional true/false positive/negative metrics are recast as follows

  - TP/(TP+FN) = recall = sensitivity = Pr(detect the bug | there is a bug)
  - TP/(TP+FP) = precision = predictive value positive = Pr(real bug| detected bug)
  - TN/(TN+FP) = specificity = Pr(no detection | no bug)
  - FN/(FN+TN) = predictive value negative = Pr(no bug| no detection)

- Handling the bulk of the important defect areas for a user
- Time and space performance consistent with the benefit provided

Usability has several components

- Out-of-the-box experience
- Resource investment profile
- Perspicuity

Finally, there is a need for confidence that the tool will continue to exist
and be supported.

{% include links.html %}
