---
ENTRYTYPE: inproceedings
added: 2021-03-14
authors:
- Sebastian Poeplau
- Aurélien Francillon
booktitle: 29th USENIX Security Symposium (USENIX Security 20)
isbn: 978-1-939133-17-5
layout: paper
link: https://www.usenix.org/conference/usenixsecurity20/presentation/poeplau
month: August
pages: 181-198
publisher: USENIX Association
read: true
readings:
- 2021-06-13
title: "Symbolic execution with SymCC: Don't interpret, compile!"
url: https://www.usenix.org/conference/usenixsecurity20/presentation/poeplau
year: 2020
notes:
- symbolic execution
- concolic execution
- LLVM compiler
- KLEE verifier
- CUTE verifier
- DART verifier
- EXE verifier
- QSYM verifier
- SymCC
- angr verifier
- S2E verifier
- Mayhem
- SMT solver
- Z3 solver
- DARPA CGC
papers:
- yun:usenix:2018
- poeplau:acsac:2019
---

SymCC is an [LLVM][LLVM compiler]-based [symbolic execution] tool that
focuses on performance by compiling the LLVM bitcode instead of interpreting
it (as is done by tools like [KLEE][KLEE verifier]).
The result is an average speedup (relative to KLEE) of 12 and up to 3 orders of magnitude
and a consequent improvement in coverage and bug discovery.

Use of compilation is justified by the analysis in [[yun:usenix:2018]] that (concrete) execution is
a major bottleneck in symbolic execution.
(The effect is similar to how the early tools [DART][DART verifier], [CUTE][CUTE
verifier] and [EXE][EXE verifier] worked except that they operated by
instrumenting C source code.)

The tool uses concolic execution: using concrete inputs, it executes as normal
but constructs a symbolic path condition as a side-effect of execution;
when execution completes, the path condition can be modified and then
solved by an [SMT solver] to generate additional concrete inputs.

Unlike non-concolic tools such as [KLEE][KLEE verifier], [angr][angr verifier]
and [Mayhem], [SYMCC] does not store multiple symbolic states and use
backtracking, copy-on-write, etc. to avoid re-exploration of earlier execution:
the argument is that this is only necessary because re-execution is too slow.

The compilation process inserts symbolic calculations alongside the concrete
calculations.  To reduce overhead, compile time checks test for constants (not
sure if this really means concrete values?) and generates runtime checks for
constants.
The instrumentation process is written as an LLVM pass that can be dynamically loaded
into the [LLVM compiler].

The symbolic library API can use either the [Z3 solver] or the [QSYM] symbolic
backend to take advantage of its dependency tracking and back-off strategies
for hot code paths.

Evaluation used the [DARPA CGC] and compared against [QSYM] and [KLEE][KLEE
verifier] and considers (concrete) execution time, concolic execution time (with
KLEE configure/modified to use [concolic execution] and
coverage of test cases.
On concrete execution, SymCC is 2-3x slower than native and around 30x faster than QSYM and KLEE.
On concolic execution, SymCC is about 10x faster than QSYM and KLEE.
On coverage, SymCC found more paths on 46 programs and less paths on 10 programs within
the available time (compared with KLEE) and, compared with QSYM, more on 47, the same on 29 and less on 40.
Part, but not all, of the performance difference is due to shifting
initialization time from runtime to compile time.

Also tested a combination of AFL with SymCC (and comparing with AFL+QSYM)
using the fuzzer to generate seeds and the concolic engine to generate
variants of the seeds.
The SymCC combination was significantly better.

{% include links.html %}
