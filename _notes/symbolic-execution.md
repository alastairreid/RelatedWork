---
layout: note
title: Symbolic execution
wiki: https://en.wikipedia.org/wiki/Symbolic_execution
notes:
- bounded model checking
- symbolic evaluation
- symbolic execution
papers:
- nelson:sosp:2019
- bornholt:oopsla:2018
- baldoni:compsurv:2018
---

Following the terminology in section 3.1 of 
[bornholt:oopsla:2018], [symbolic execution] is a form of
[symbolic evaluation] where a single path is followed at a time.

Following a single path has the advantage that states do not need to be merged
at join points and so many calculations involve concrete values and so can be
evaluated directly and efficiently.  The price paid for this advantage is that
there can be an exponential number of paths.

See also [bounded model checking] and [symbolic evaluation].

Types of symbolic execution include

- "Concolic execution" mixes concrete and symbolic execution benefiting
  from the efficiency and decidability of concrete execution and
  the need to use concrete values when interacting with the program
  environment (libraries, OS, etc.)
  and from the stronger guarantees of symbolic execution.
  (See <https://en.wikipedia.org/wiki/Concolic_testing>)

  - Dynamic Symbolic Execution (DSE) relies on concrete execution
    to drive symbolic execution using an instrumented interpreter/
    simulator/... to build symbolic representations while executing
    with concrete values.

  - Selective Symbolic Execution (SSE)
    interleaves concrete and symbolic execution with a focus on
    performing symbolic execution as much of the code you
    care about as possible.

{% include links.html %}
