---
ENTRYTYPE: article
added: 2023-12-02
authors:
- Nicholas Mosier
- Hamed Nemati
- John C. Mitchell
- Caroline Trippel
bibsource: dblp computer science bibliography, https://dblp.org
biburl: https://dblp.org/rec/journals/corr/abs-2309-05174.bib
doi: 10.48550/ARXIV.2309.05174
eprint: '2309.05174'
eprinttype: arXiv
journal: CoRR
layout: paper
link: https://doi.org/10.48550/arXiv.2309.05174
read: true
readings:
- 2023-12-01
timestamp: Fri, 15 Sep 2023 12:26:52 +0200
title: 'Serberus: Protecting Cryptographic Code from Spectres at Compile-Time'
url: https://doi.org/10.48550/arXiv.2309.05174
volume: abs/2309.05174
year: 2023
notes:
- leakage contracts
- side-channel
- speculative execution
papers:
---

Serberus is a mitigation against [speculative execution] attacks
implemented as an extension of LLVM.
It relies on the use of Intel Architecture CET features to
constrain speculative branches.


{% include links.html %}
