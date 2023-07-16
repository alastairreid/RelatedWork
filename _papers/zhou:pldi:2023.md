---
ENTRYTYPE: article
abstract: Test input generators are an important part of property-based testing (PBT) frameworks. Because PBT is intended to test deep semantic and structural
  properties of a program, the outputs produced by these generators can be complex data structures, constrained to satisfy properties the developer believes
  is most relevant to testing the function of interest. An important feature expected of these generators is that they be capable of producing all acceptable
  elements that satisfy the function's input type and generator-provided constraints. However, it is not readily apparent how we might validate whether
  a particular generator's output satisfies this coverage requirement. Typically, developers must rely on manual inspection and post-mortem analysis of
  test runs to determine if the generator is providing sufficient coverage; these approaches are error-prone and difficult to scale as generators become
  more complex. To address this important concern, we present a new refinement type-based verification procedure for validating the coverage provided by
  input test generators, based on a novel interpretation of types that embeds "must-style" underapproximate reasoning principles as a fundamental part of
  the type system. The types associated with expressions now capture the set of values guaranteed to be produced by the expression, rather than the typical
  formulation that uses types to represent the set of values an expression may produce. Beyond formalizing the notion of coverage types in the context of
  a rich core language with higher-order procedures and inductive datatypes, we also present a detailed evaluation study to justify the utility of our ideas.
added: 2023-07-02
address: New York, NY, USA
articleno: '157'
authors:
- Zhe Zhou
- Ashish Mishra
- Benjamin Delaware
- Suresh Jagannathan
doi: 10.1145/3591271
issue_date: June 2023
journal: Proc. ACM Program. Lang.
keywords: underapproximate reasoning, refinement types, property-based testing
layout: paper
link: https://doi.org/10.1145/3591271
month: jun
number: PLDI
numpages: '24'
publisher: Association for Computing Machinery
read: false
readings: []
title: 'Covering all the bases: Type-based verification of test input generators'
url: https://doi.org/10.1145/3591271
volume: '7'
year: 2023
notes:
- incorrectness logic
- under-approximation
- over-approximation
papers:
- ohearn:popl:2019
---

Most type systems are based on the style of [over-approximate][over-approximation]
or "may-style" reasoning found in Hoare logic and are used to show that something _does not_ happen.
This paper develops an alternative type system based on the [under-approximate][under-approximation]
or "must-style" reasoning found in [incorrectness logic] in order to show that
something _does_ happen.

This type system is used to show that a random test generator is theoretically able to
generate all possible values of an abstract data type.

One minor point to note (I'm not sure if the paper mentions this) is that, if you
are using an ADT to represent abstract syntax trees, then you usually don't want to
generate ASTs that represent illegal programs (e.g., containing type errors
or references to undeclared variables).

{% include links.html %}

