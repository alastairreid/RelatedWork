---
ENTRYTYPE: inproceedings
abstract: Systems code must obey many rules, such as "opened files must be closed." One approach to verifying rules is static analysis, but this technique
  cannot infer precise runtime effects of code, often emitting many false positives. An alternative is symbolic execution, a technique that verifies program
  paths over all inputs up to a bounded size. However, when applied to verify rules, existing symbolic execution systems often blindly explore many redundant
  program paths while missing relevant ones that may contain bugs.Our key insight is that only a small portion of paths are relevant to rules, and the rest
  (majority) of paths are irrelevant and do not need to be verified. Based on this insight, we create WOODPECKER, a new symbolic execution system for effectively
  checking rules on systems programs. It provides a set of builtin checkers for common rules, and an interface for users to easily check new rules. It directs
  symbolic execution toward the program paths relevant to a checked rule, and soundly prunes redundant paths, exponentially speeding up symbolic execution.
  It is designed to be heuristic-agnostic, enabling users to leverage existing powerful search heuristics.Evaluation on 136 systems programs totaling 545K
  lines of code, including some of the most widely used programs, shows that, with a time limit of typically just one hour for each verification run, WOODPECKER
  effectively verifies 28.7\% of the program and rule combinations over bounded input, whereas an existing symbolic execution system KLEE verifies only
  8.5\%. For the remaining combinations, WOODPECKER verifies 4.6 times as many relevant paths as KLEE. With a longer time limit, WOODPECKER verifies much
  more paths than KLEE, e.g., 17 times as many with a fourhour limit. WOODPECKER detects 113 rule violations, including 10 serious data loss errors with
  2 most serious ones already confirmed by the corresponding developers.
added: 2021-04-18
address: New York, NY, USA
authors:
- Heming Cui
- Gang Hu
- Jingyue Wu
- Junfeng Yang
booktitle: Proceedings of the Eighteenth International Conference on Architectural Support for Programming Languages and Operating Systems
doi: 10.1145/2451116.2451152
isbn: '9781450318709'
keywords: verification, path slicing, systems rules, error detection, symbolic execution
layout: paper
link: https://doi.org/10.1145/2451116.2451152
location: Houston, Texas, USA
numpages: '14'
pages: 329-342
publisher: Association for Computing Machinery
read: false
readings: []
series: ASPLOS '13
title: Verifying systems rules using rule-directed symbolic execution
url: https://doi.org/10.1145/2451116.2451152
year: 2013
notes:
- KLEE verifier
- symbolic execution
papers:
- ramos:sec:2015
---
{% include links.html %}
