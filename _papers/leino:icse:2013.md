---
ENTRYTYPE: inproceedings
added: 2020-03-01
authors:
- K. Rustan M. Leino
booktitle: 2013 35th International Conference on Software Engineering (ICSE)
doi: 10.1109/ICSE.2013.6606754
issn: 1558-1225
keywords: program verification;specification languages;Dafny programs;specification
  langauge;program verifier;programming language;Arrays;Tutorials;Reactive power;Cognition;Security;Educational
  institutions;Computer languages
layout: paper
month: May
number: ''
pages: 1488-1490
read: true
readings:
- 2020-02-28
title: Developing verified programs with Dafny
volume: ''
year: 2013
topics:
- tools
- verification
notes:
- auto-active-verification
- boogie-verifier
- dafny-verifier
- ghost-code
- z3-solver
- smt-solver
---

[Dafny]({{ "papers/leino:lpair:2010" | relative_url }})
is both a language and a verification tool for creating verified
programs.
The language has features of object-oriented languages and functional
languages.
The verification support is based on contract-style verification.
This short, easy read seems to be the accompaniment for a tutorial
and discusses verification of six different functions that
demonstrates contracts and the specification notation,
loop invariants, immutable inductive datatypes, mutable datatypes,
use of pure functions in specifications, classes, ghost-fields,
invariants, and lemmas.
Proofs of lemmas are especially interesting because the lemmas
are just ghost methods and the body of those methods are
the proofs of the lemmas. e.g., to write an inductive proof,
one writes a recursive function using a case split to separate
the base case from the inductive step.

{% include links.html %}
