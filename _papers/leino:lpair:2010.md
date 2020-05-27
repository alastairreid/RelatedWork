---
ENTRYTYPE: inproceedings
added: 2019-10-12
authors:
- K. Rustan M. Leino
booktitle: International Conference on Logic for Programming Artificial Intelligence and Reasoning
doi: 10.1007/978-3-642-17511-4_20
layout: paper
organization: Springer
pages: 348-370
read: true
readings:
- 2020-03-03
title: 'Dafny: An automatic program verifier for functional correctness'
year: 2010
topics:
- tools
- verification
notes:
- auto-active verification
- Boogie verifier
- Dafny verifier
- Z3 solver
- SMT solver
papers:
- leino:tacas:2010
- demoura:tacas:2008
- tuerk:vstte:2010
- barnett:fmco:2005
---

Dafny is an [auto-active program verifier][auto-active verification]
for an imperative
language with functional and object oriented features
that uses
the 
[Boogie][leino:tacas:2010]
intermediate verification language
and the
[Z3][demoura:tacas:2008]
SMT solver
for automated proof.

This is one of the early papers about Dafny: before it could
actually execute the code it verifies.
(I am reminded of the Donald Knuth comment about a function that
it had been verified but not actually executed.)
It also describes 
the origins of Dafny as an exploration of dynamic frames
and some of the development of features driven
by features of the code they wanted to verify.

The main body of the paper is a description of the language
feature and how it is converted to Boogie – with some of the
author's characteristic asides about how the choices impact
verification and where the ideas were first explored.
(I really like this feature of Leino's papers.)

The big result in the paper is a verified version of
the Schorr-Waite algorithm in just 117 lines of
code, proof and comment.  Wow!
Also a nice summary of the development process.
The only thing not to like about this is the 19
loop invariants required.
(I wonder whether [loop specifications in the style of Tuerk][tuerk:vstte:2010]
would help at all?)
Also, the author admits that "deciphering the verifier's
error messages" is hard.
I wonder how much that improved in later versions
or with the development of the
[Boogie Verification Debugger][barnett:fmco:2005]?

{% include links.html %}
