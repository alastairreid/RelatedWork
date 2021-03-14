---
ENTRYTYPE: article
abstract: Satisfiability modulo theories (SMT) solving has become a critical part of many static analyses, including symbolic execution, refinement type
  checking, and model checking. We propose Formulog, a domain-specific language that makes it possible to write a range of SMT-based static analyses in
  a way that is both close to their formal specifications and amenable to high-level optimizations and efficient evaluation.  Formulog extends the logic
  programming language Datalog with a first-order functional language and mechanisms for representing and reasoning about SMT formulas; a novel type system
  supports the construction of expressive formulas, while ensuring that neither normal evaluation nor SMT solving goes wrong. Our case studies demonstrate
  that a range of SMT-based analyses can naturally and concisely be encoded in Formulog, and that - thanks to this encoding - high-level Datalog-style optimizations
  can be automatically and advantageously applied to these analyses.
added: 2021-03-14
address: New York, NY, USA
articleno: '141'
authors:
- Aaron Bembenek
- Michael Greenberg
- Stephen Chong
doi: 10.1145/3428209
issue_date: November 2020
journal: Proc. ACM Program. Lang.
keywords: Datalog, SMT solving
layout: paper
link: https://doi.org/10.1145/3428209
month: November
number: OOPSLA
numpages: '31'
publisher: Association for Computing Machinery
read: false
readings: []
title: 'Formulog: Datalog for SMT-based static analysis'
url: https://doi.org/10.1145/3428209
volume: '4'
year: 2020
notes:
papers:
---
{% include links.html %}
