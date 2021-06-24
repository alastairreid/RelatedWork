---
layout: note
title: Symbolic execution
wiki: https://en.wikipedia.org/wiki/Symbolic_execution
notes:
- bounded model checking
- fuzz testing
- separation logic
- symbolic evaluation
- symbolic execution
- DART verifier
- KLEE verifier
- SAGE verifier
- Smallfoot verifier
- VeriFast verifier
papers:
- nelson:sosp:2019
- bornholt:oopsla:2018
- baldoni:compsurv:2018
- avgerinos:icse:2014
- kuznetsov:pldi:2012
- siddiqui:oopsla:2012
- avgerinos:cacm:2014
---

**Terminology update:**
There are multiple, consistent but conflicting uses of the term "symbolic execution"
and "symbolic evaluation". These terms are used by different groups of people in
different ways so, if you use these terms without qualification, you are likely
to cause misunderstandings. Much better to use precise terms like DSE, concolic execution,
bounded model checking, etc. which seem to have much more agreement about what they mean.

*Old attempt to find a consistently used terminology follows -- use at your peril.*

Following the terminology in section 3.1 of
[bornholt:oopsla:2018], [symbolic execution] is a form of
[symbolic evaluation] where a single path is followed at a time.

Following a single path has the advantage that states do not need to be merged
at join points and so many calculations involve concrete values and so can be
evaluated directly and efficiently.  The price paid for this advantage is that
there can be an exponential number of paths.

See also [bounded model checking] and [symbolic evaluation].
and see [kuznetsov:pldi:2012] for a unifying framework that
describes the symbolic evaluation design space/spectrum in terms of
how loop/recursion are handled, whether/how branches are tested for
feasibility, whether/how states from different paths are merged and
compositionality.


Types of symbolic execution include

- (Pure) symbolic execution enumerates paths, collects path conditions
  along those paths and then checks which path conditions are satisfiable.
  (Checking path conditions can be done eagerly to prune infeasible paths
  early.)

  I think this is mostly used in [separation logic] checkers such as
  the [Smallfoot verifier] and the [VeriFast verifier].

- Dynamic Symbolic Execution (DSE) mixes concrete and symbolic execution
  benefiting from the efficiency and decidability of concrete execution and the
  need to use concrete values when interacting with the program environment
  (libraries, OS, etc.) and from the stronger guarantees of symbolic execution.

  - "Offline" DSE (aka "concolic execution") relies on concrete execution
    to drive symbolic execution using an instrumented interpreter/
    simulator/... to build symbolic representations while executing
    with concrete values.

    Used in the [DART verifier].

  - "Online" DSE (aka "Execution Generated Testing" (EGT))
    mixes concrete and symbolic execution
    by using concrete execution whenever the inputs to an operation
    are concrete and using symbolic execution if any inputs are symbolic.

    Used in the [KLEE verifier].

- Static Symbolic Execution (SSE) avoids path explosion by generating
  a symbolic formula representing all paths through a piece of code.
  It does this by merging formulae at join points in a pre-execution pass.

  This approach has significant overlap with [bounded model checking]
  and the term is mostly used in the context of hybrid approaches
  such as [avgerinos:icse:2014].

- Selective Symbolic Execution (SSE)
  interleaves concrete and symbolic execution with a focus on
  performing symbolic execution as much of the code you
  care about as possible.

  (I think this may be a special case of DSE?)

- Forward symbolic execution constructs paths in normal program order.
  *[I have seen references to backward symbolic execution but I
  don't think I have seen backward symbolic execution being used
  for software verification.]*

*[todo: it is probably less useful to have a tree-shaped taxonomy of this topic
than to have a list of design choices that define an N-dimensional taxonomy
where most dimensions include "yes", "no" and "hybrid" on their axis.  This
would better capture how thoroughly the symbolic execution design space has
been explored.]*

In part because of the exponential path explosion of pure symbolic execution,
it is rarely feasible to check all paths so there has been a lot of work on
scheduling algorithms that try to maximize coverage, to cover some part of the
code (e.g., code that is part of a recent commit), to execute enough iterations
to overflow a buffer ([avgerinos:cacm:2014]), etc.  These scheduling algorithms make [state merging]
harder (but see [kuznetsov:pldi:2012]), make ranged analysis harder
([siddiqui:oopsla:2012]), and probably other impacts too.

(Note that even if you could explore all paths, you still can't guarantee to find
all bugs because things like external calls and syscalls require concretization
and therefore lose completeness.)

{% include links.html %}
