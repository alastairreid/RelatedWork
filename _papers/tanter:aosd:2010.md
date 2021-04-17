---
ENTRYTYPE: inproceedings
abstract: 'In aspect-oriented programming languages, advice evaluation is usually considered as part of the base program evaluation. This is also the case
  for certain pointcuts, such as if pointcuts in AspectJ, or simply all pointcuts in higher-order aspect languages like AspectScheme. While viewing aspects
  as part of base level computation clearly distinguishes AOP from reflection, it also comes at a price: because aspects observe base level computation,
  evaluating pointcuts and advice at the base level can trigger infinite regression. To avoid these pitfalls, aspect languages propose ad-hoc mechanisms,
  which increase the complexity for programmers while being insufficient in many cases. After shedding light on the many facets of the issue, this paper
  proposes to clarify the situation by introducing levels of execution in the programming language, thereby allowing aspects to observe and run at specific,
  possibly different, levels. We adopt a defensive default that avoids infinite regression in all cases, and give advanced programmers the means to override
  this default using level shifting operators. We formalize the semantics of our proposal, and provide an implementation. This work recognizes that different
  aspects differ in their intended nature, and shows that structuring execution contexts helps tame the power of aspects and metaprogramming.'
added: 2021-04-17
address: New York, NY, USA
authors:
- '{\''E}ric Tanter'
booktitle: Proceedings of the 9th International Conference on Aspect-Oriented Software Development
doi: 10.1145/1739230.1739236
isbn: '9781605589589'
keywords: meta-programming, execution level, scoping mechanism, aspect-oriented programming, infinite regression, conflation
layout: paper
link: https://doi.org/10.1145/1739230.1739236
location: Rennes and Saint-Malo, France
numpages: '12'
pages: 37-48
publisher: Association for Computing Machinery
read: false
readings: []
series: AOSD '10
title: Execution levels for aspect-oriented programming
url: https://doi.org/10.1145/1739230.1739236
year: 2010
notes:
papers:
---
{% include links.html %}
