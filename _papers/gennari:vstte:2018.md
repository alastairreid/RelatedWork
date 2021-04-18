---
ENTRYTYPE: inproceedings
abstract: Counterexamples--execution traces of the system that illustrate how an error state can be reached from the initial state--are essential for understanding
  verification failures. They are one of the most salient features of Model Checkers, which distinguish them from Abstract Interpretation and other Static
  Analysis techniques by providing a user with information on how to debug their system and/or the specification. While in Hardware and Protocol verification,
  the counterexamples can be replayed in the system, in Software Model Checking (SMC) counterexamples take the form of a textual or semi-structured report.
  This is problematic since it complicates the debugging process by preventing developers from using existing processes and tools such as debuggers, fault
  localization, and fault minimization.
added: 2021-04-17
address: Cham
authors:
- Jeffrey Gennari
- Arie Gurfinkel
- Temesghen Kahsai
- Jorge A. Navas
- Edward J. Schwartz
booktitle: Verified Software. Theories, Tools, and Experiments
editor: Piskac, Ruzica and Rümmer, Philipp
isbn: 978-3-030-03592-1
layout: paper
pages: 17-37
publisher: Springer International Publishing
read: true
readings:
- 2021-04-17
title: Executable counterexamples in software model checking
year: 2018
notes:
- SeaHorn verifier
- Test double
- SV competition
papers:
---

Argues that counterexamples from software model checking (SMC) should take the form of
executable mock environments that can be linked with the code under analysis (CUA).
These mock environments are a simple form of [test double] that implement each external
function with a function that returns a sequence of values to steer the CUA towards
failure.

One of the main problems in generating the counterexample is that the SMC may
have used simplification and optimization techniques that changed the code a lot.
They only need that they can extract the number of iterations of loops.
This allows loops to be unrolled so that the CFG is acyclic.
(i.e., it turns it into a BMC problem).
A "Directed Symbolic Execution" (DirSE) step transforms the counterexample on the
optimized code into a counterexample on the original program.
It starts by showing that the error is still reachable.
The overall approach is quite general but it is not necessary with BMC and
dynamic symbolic execution that can already generate counterexamples.

They evaluate their implementation in SeaHorn on the Linux Driver Verification
benchmarks from [SV-COMP][SV competition].  They can solve around half the
problems and generate counterexamples for almost all of them.  (Almost because
their SMC uses unbounded integers while their BMC uses bit-vectors so they get
a few mismatches.)

There seems to be a limitation in the handling of external functions that return pointers:
the pointers returned are often dereferenced further and this is not modeled well.
This problem seems to be more to do with using a simplistic model of external
functions than to do with their counterexample generation.

{% include links.html %}
