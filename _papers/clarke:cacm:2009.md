---
ENTRYTYPE: article
added: 2020-05-12
address: New York, NY, USA
authors:
- Edmund M. Clarke
- E. Allen Emerson
- Joseph Sifakis
doi: 10.1145/1592761.1592781
issn: 0001-0782
issue_date: November 2009
journal: Communications of the ACM
layout: paper
link: https://doi.org/10.1145/1592761.1592781
month: November
number: '11'
numpages: '11'
pages: 74-84
publisher: Association for Computing Machinery
read: true
readings:
- 2020-07-09
title: 'Model checking: Algorithmic verification and debugging'
url: https://doi.org/10.1145/1592761.1592781
volume: '52'
year: 2009
notes:
- survey
- model checking
- temporal logic
- bounded model checking
- symbolic model checking
- partial order reduction
- CEGAR
- abstract interpretation
- Turing Award
papers:
---

This [Turing Award] paper/talk is a great overview of [model checking:
definition,
[temporal logic],
what it is good for, challenges (mostly state-space explosion),
tricks (like [symbolic model checking], [bounded model checking], [partial order reduction] and [CEGAR]).

It also talks about the problems creating specifications.
As well as challenges understanding subtle details of [temporal logic],
there are challenges specifying extra-functional requirements for security
properties, reconfigurability properties, quality of service (e.g., jitter).

And it talks about problems verifying real world systems: mixed
hardware-software systems, using abstraction to scale (using hybrid
[model-checking]/[abstract-interpretation] methods and compositional reasoning)
and exploiting design-time architectural choices to improve verifiability.

{% include links.html %}
