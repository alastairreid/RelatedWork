---
layout: note
title: Cactus plot / Survival plot
wiki: https://en.wikipedia.org/wiki/Survival_function
notes:
- SV competition
---

A cactus plot or "survival plot" is used to summarize the performance
of an automated verification tool
in verification tool competitions such as [SMT-COMP] and [SV-COMP 2020].
The graph plots how many problems can be solved in a given time.

(I think that a "cactus plot" is the transpose of the "survival plot".)

A [paper about the use of cactus plots in competitions](http://www.sc-square.org/CSA/workshop2-papers/RP3-FinalVersion.pdf).

Here is an example from [SV-COMP 2020].

![cactus plot for SV-COMP overflow verification results](https://sv-comp.sosy-lab.org/2020/results/results-verified/quantilePlot-NoOverflows.svg)


[SMT-COMP]: https://smt-comp.github.io/
[SV-COMP 2020]: https://sv-comp.sosy-lab.org/2020/
{% include links.html %}
