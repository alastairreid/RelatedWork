---
ENTRYTYPE: inproceedings
abstract: In spite of decades of research in bug detection tools, there is a surprising dearth of ground-truth corpora that can be used to evaluate the
  efficacy of such tools. Recently, systems such as LAVA and EvilCoder have been proposed to automatically inject bugs into software to quickly generate
  large bug corpora, but the bugs created so far differ from naturally occurring bugs in a number of ways. In this work, we propose a new automated bug
  injection system, Apocalypse, that uses formal techniques-symbolic execution, constraint-based program synthesis and model counting-to automatically inject
  fair (can potentially be discovered by current bug-detection tools), deep (requiring a long sequence of dependencies to be satisfied to fire), uncorrelated
  (each bug behaving independent of others), reproducible (a trigger input being available) and rare (can be triggered by only a few program inputs) bugs
  in large software code bases. In our evaluation, we inject bugs into thirty Coreutils programs as well as the TCAS test suite. We find that bugs synthesized
  by Apocalypse are highly realistic under a variety of metrics, that they do not favor a particular bug-finding strategy (unlike bugs produced by LAVA),
  and that they are more difficult to find than manually injected bugs, requiring up around 240\texttimes  more tests to discover with a state-of-the-art
  symbolic execution tool.
added: 2021-06-14
address: New York, NY, USA
authors:
- Subhajit Roy
- Awanish Pandey
- Brendan Dolan-Gavitt
- Yu Hu
booktitle: Proceedings of the 2018 26th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering
doi: 10.1145/3236024.3236084
isbn: '9781450355735'
keywords: Symbolic Execution, Program Synthesis, Constraint-based Synthesis, Bug Injection
layout: paper
link: https://doi.org/10.1145/3236024.3236084
location: Lake Buena Vista, FL, USA
numpages: '11'
pages: 224-234
publisher: Association for Computing Machinery
read: false
readings: []
series: ESEC/FSE 2018
title: 'Bug synthesis: Challenging bug-finding tools with deep faults'
url: https://doi.org/10.1145/3236024.3236084
year: 2018
notes:
- symbolic execution
papers:
---
{% include links.html %}
