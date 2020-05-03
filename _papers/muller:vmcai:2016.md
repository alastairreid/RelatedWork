---
ENTRYTYPE: inproceedings
abstract: 'The automation of verification techniques based on first-order logic specifications
  has benefitted greatly from verification infrastructures such as Boogie and Why.
  These offer an intermediate language that can express diverse language features
  and verification techniques, as well as back-end tools: in particular, verification
  condition generators.'
added: 2020-01-15
address: Berlin, Heidelberg
authors:
- Peter Müller
- Malte Schwerhoff
- Alexander J. Summers
booktitle: Verification, Model Checking, and Abstract Interpretation
editor: 'Jobstmann, Barbara and Leino, K. Rustan M.'
isbn: 978-3-662-49122-5
layout: paper
pages: 41-62
publisher: Springer Berlin Heidelberg
read: true
readings:
- 2020-02-11
title: 'Viper: A verification infrastructure for permission-based reasoning'
year: 2016
topics:
- tools
- verification
notes:
- permission logic
- Viper verifier
- intermediate verification language
- magic wand
- SMT solver
---

[Viper][Viper verifier] is like [Boogie]({{ "papers/barnett:fmco:2005" | relative_url }})
in that it is an [intermediate verification language] (IVL)
that can support multiple language frontends and also
multiple verification backends.
The most important difference is that Viper is based on a form of
[permission logic] that is well suited to reasoning about
heap based data structures.

The Viper language is an sequential, imperative, object-based
language with impure procedures (called "methods")
and pure functions and supporting loops and recursion.
Methods and functions have contracts consisting of
requires/ensures predicates and all reasoning
about method calls is based on instantiating the contract
at the call site.
Loops also have invariants (it is not clear whether they also
have variants to let you prove termination).

Methods serve two purposes: they can represent the code that
you want to reason about but they can also be used to
prove lemmas.
An example lemma in the paper is "concat" that relates
two parts of a linked list to the entire list.
I have seen the same trick being used in
[VeriFast]({{ "papers/jacobs:vstte:2010" | relative_url }})
but, since VeriFast is not an IVL, it keeps
C functions we are reasoning about separate from
lemma functions used to reason about them.

Predicates can describe the fields of an object that can be accessed
and [fractional permissions]({{ "papers/bornat:popl:2005" | relative_url }})
can be used to allow shared read-only access.

A relatively unusual feature of Viper is that it has first-class
support for [magic wand]s "——∗" (the implication operator from
separation logic).
There is a nice discussion of how using magic wands simplifies
reasoning about partial verisons of data structures and,
in their example, avoids the need to introduce recursive definitions
such as "concat" to combine parts of data structures.

Another unusual thing about Viper is that you can define
"domains" consisting of some uninterpreted functions plus some
axioms.
For example, arrays are defined in this way instead of being
built into Viper.
It seems that this approach lets them keep the Viper core
quite small and lean.

Finally, there is an evaluation and comparision with
[Chalice]({{ "papers/leino:fosad:2007" | relative_url }})
and
[Boogie]({{ "papers/barnett:fmco:2005" | relative_url }}).

{% include links.html %}
