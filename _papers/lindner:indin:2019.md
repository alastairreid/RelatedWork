---
ENTRYTYPE: inproceedings
added: 2020-05-08
authors:
- Marcus Lindner
- Nils Fitinghoff
- Johan Eriksson
- Per Lindgren
booktitle: 'Proceedings : 2019 IEEE 17th International Conference on Industrial Informatics (INDIN)'
doi: 10.1109/INDIN41052.2019.8972014
institution: Luleå University of Technology, Computer Science
layout: paper
note: ISBN för värdpublikation: 978-1-7281-2927-3, 978-1-7281-2928-0
pages: 432-439
read: true
readings:
- 2020-05-12
series: IEEE International Conference on Industrial Informatics (INDIN)
title: 'Verification of safety functions implemented in Rust: A symbolic execution based approach'
year: 2019
notes:
- Rust language
- symbolic execution
- extended static checking
- KLEE verifier
papers:
- lindner:indin:2018
---

This paper looks at how to use the [KLEE verifier] to verify
code implementing a state machine written in Rust
based on their earlier work ([lindner:indin:2018]).
The challenge here is that KLEE is a [symbolic execution]
tool and does not guarantee to explore all paths through
the code to a sufficient depth to guarantee soundness.
Their solution lies in constructing an appropriate
verification harness.

{% include links.html %}
