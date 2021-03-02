---
ENTRYTYPE: inproceedings
abstract: 'One of the advantages of temporal-logic model-checking tools is their ability to accompany a negative answer to the correctness query by a counterexample
  to the satisfaction of the specification in the system. On the other hand, when the answer to the correctness query is positive, most model-checking tools
  provide no additional information. In the last few years there has been growing awareness to the importance of suspecting the system or the specification
  of containing an error also in the case model checking succeeds. The main justification of such suspects are possible errors in the modeling of the system
  or of the specification. The goal of sanity checks is to detect such errors by further automatic reasoning. Two leading sanity checks are vacuity and
  coverage. In vacuity, the goal is to detect cases where the system satisfies the specification in some unintended trivial way. In coverage, the goal is
  to increase the exhaustiveness of the specification by detecting components of the system that do not play a role in verification process. For both checks,
  the challenge is to define vacuity and coverage formally, develop algorithms for detecting vacuous satisfaction and low coverage, and suggest methods
  for returning to the user helpful information. We survey existing work on vacuity and coverage and argue that, in many aspects, the two checks are essentially
  the same: both are based on repeating the verification process on some mutant input. In vacuity, mutations are in the specifications, whereas in coverage,
  mutations are in the system. This observation enables us to adopt work done in the context of vacuity to coverage, and vise versa.'
added: 2021-02-20
address: Berlin, Heidelberg
authors:
- Orna Kupferman
booktitle: CONCUR 2006 - Concurrency Theory
editor: Baier, Christel and Hermanns, Holger
isbn: 978-3-540-37377-3
layout: paper
pages: 37-51
publisher: Springer Berlin Heidelberg
read: true
readings:
- 2021-02-20
title: Sanity checks in formal verification
year: 2006
notes:
- Model checking
- Temporal logic
- Mutation testing
papers:
---

Writing specifications is hard. It is especially hard to write
specifications that don't leave things out (underconstrain)
or say too much (overconstrain).
This paper deals with two particular problems and argues that
they can be tackled with the same analysis

- Vacuity: accidentally specifying a property that says nothing
  because the precondition is unsatisfiable.

- Completeness: accidentally leaving out some important property.

Recognizing that they are related allows cross-fertilization
of ideas between two separate groups of researchers.

Both vacuity and coverage are defined in terms of semantic notions of
mutation of subformulae (vacuity) or states. That is,
if changing the value of the subformula/state makes no difference
to whether a formula is satisfied, then either the formula is
vacuous or the state is not covered. (Definitions 2 and 4.)

These can then be generalized to changing the value all the time (structural),
exactly once (node) and N times (tree). (The tree/node terminology comes from
the definition in terms of a Kripke structure.)

For both coverage and vacuity, it can be useful to produce witnesses that show
how [mutant implementations][mutation testing] (slightly modified versions of the implementation)
would fail to satisfy the formula.

> A witness is interesting if it satisfies the specification non-vacuously.

and

> In the context of coverage, however, we return to the user a family of
> counterexamples – one for each sub-specification that is no longer
> satisfied in the system with c mutated.

Generating coverage counterexamples is done by introducing two new variables for
each subformula to decide whether to invert the subformula and to track how
many times it has been inverted before.  (This is for hardware model checking
where all signals are booleans.)

Generating vacuity counterexamples is done by introducing a new variable to select
which subformula to invert and then solving for the choice that makes no difference.

The paper is written from the context of model checking, temporal logic and
hardware verification but may be more general than that.


{% include links.html %}
