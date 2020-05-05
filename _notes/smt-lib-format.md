---
layout: note
title: SMT-LIB format
website: http://smtlib.cs.uiowa.edu/
notes:
- Z3 solver
- SMT solver
- foreign function interface
---

The SMT-LIB format is the de facto standard for representing SMT
problems and so it allows a high degree of portability between
solvers in how problems are presented to solvers.

Standardization of the format was driven by the [SMT-COMP competition] that
uses the SMT-LIB standard in the competition rules.
This forces all SMT solvers that want to compete to, at least, implement
the SMT-LIB format.

The format is based on S-expressions to simplify machine parsing.
(I suspect that it also avoids endless arguing over syntax!)


## Extensions

The more actively developed solvers tend to implement extensions to
the standard.
Some of these are later added to the standard and new tracks are added to
the SMT-COMP competition.


## Associated SMT standards

todo: summarize standards for output of sat and unsat-core output.
(My experience is that there is much more variability here.)

## SMT-LIB language bindings

todo: summarize state of [FFI][foreign function interface] language bindings
(not as well developed, I think).
And mention the [Z3 solver] Python bindings.


## Alternative SMT interfaces

The main alternative is the [Z3 solver] Python binding/library that many use
for its convenience and to access Z3's other features.

The disadvantage of using alternative SMT interfaces is that they tend to be
less portable so you find yourself locked into a single solver.
The main disadvantage of which is that it makes it hard to try other
solvers to see whether they are faster.

[SMT-COMP competition]: https://smt-comp.github.io/

{% include links.html %}
