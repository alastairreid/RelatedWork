---
ENTRYTYPE: inproceedings
added: 2019-10-12
authors:
- Mike Barnett
- Bor-Yuh Evan Chang
- Robert DeLine
- Bart Jacobs
- K. Rustan M. Leino
booktitle: International Symposium on Formal Methods for Components and Objects
doi: 10.1007/11804192_17
layout: paper
organization: Springer
pages: 364-387
read: true
readings:
- 2019-10-21
title: 'Boogie: A modular reusable verifier for object-oriented programs'
year: 2005
topics:
- tools
- verification
notes:
- Boogie verifier
- Z3 solver
- intermediate verification language
- verification condition generator
- spec-sharp-project
- modular verification
- contract driven development
- SMACK verifier
- Corral verifier
- abstract interpretation
papers:
- rakamaric:cav:2014
- cohen:cav:2010
- leinenbach:fm:2009
- barnett:cassis:2004
- filliatre:fem:2004
---

Boogie factors verification of [Spec#][barnett:cassis:2004] programs into
- Generating the Intermediate Verification Language BoogiePL by encoding language semantics, using abstract interpretation and introducing ghost state.
- Verifying BoogiePL by generating Verification Conditions and proving them using "Simplify" (with plans of switch to "Zap").
This combination simplifies and separates the two tasks and allows use of abstract interpretation (good at calculating fixpoints) and theorem proving (good at handling quantification).

BoogiePL is a simple imperative language with fresh (unconstrained) variables, assume, assert, requires, ensures, function calls, heap and non-deterministic goto but no structured control.

A strength and a weakness is that functions calls are always verified by inserting the requires/ensures from the function spec not using the function definition itself. (The weakness is that this requires the creation of specs for every function.)

This builds on the authors' previous work on ESC Modula3/Java.
Simple loop invariants (especially those associated with object allocation/lifetime) are inferred to reduce need for trivial invariants.

The paper notes that separation of generation from proof is not always ideal because it leads to some duplication of reasoning support and it makes loop invariant generation harder.

Similar work is [Caduceus and its IVL "Why"][filliatre:fem:2004].
Used by
[SMACK][rakamaric:cav:2014]
[Hyper-V][cohen:cav:2010]
[VCC][leinenbach:fm:2009]
and others.

{% include links.html %}
