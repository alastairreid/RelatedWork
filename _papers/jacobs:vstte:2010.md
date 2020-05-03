---
ENTRYTYPE: inproceedings
added: 2020-01-29
authors:
- Bart Jacobs
- Jan Smans
- Frank Piessens
booktitle: VSTTE workshop on Tools and Experiments
layout: paper
read: true
readings:
- 2020-01-29
title: 'VeriFast: Imperative programs as proofs'
year: 2010
topics:
- tools
- verification
notes:
- permission logic
- separation logic
- fractional permissions
- permission accounting
- VeriFast verifier
- ghost code
- SMT solver
- auto-active verification
papers:
- reynolds:lics:2002
---

[VeriFast](https://github.com/verifast/verifast)
is a symbolic evaluator based on
[Separation Logic][reynolds:lics:2002]
[(wikipedia)](https://en.wikipedia.org/wiki/Separation_logic)
for verifying C and Java code.
Specifications can use inductive datatypes,
primitive recursive functions and abstract predicates.
As the name suggests, a key feature is performance
though the abstract also mentions predictability.

Proof in VeriFast relies on symbolic evaluation (using an SMT solver)
but can be assisted by lemmas that are written as imperative
functions.
I think the essence of this is that if you can prove correctness of
a terminating lemma function with contract "requires P; ensures Q;",
then "P —∗ Q".
(Where "—∗" (pronounced "magic wand") is "separating
implication" from separation logic.)
These lemma functions are allowed to be recursive so it is possible to
write inductive proofs.

{% include links.html %}
