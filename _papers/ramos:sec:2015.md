---
ENTRYTYPE: inproceedings
abstract: Software bugs are a well-known source of security vulnerabilities. One technique for finding bugs, symbolic execution, considers all possible
  inputs to a program but suffers from scalability limitations. This paper uses a variant, under-constrained symbolic execution, that improves scalability
  by directly checking individual functions, rather than whole programs. We present UC-KLEE, a novel, scalable framework for checking C/C++ systems code,
  along with two use cases. First, we use UC-KLEE to check whether patches introduce crashes. We check over 800 patches from BIND and OpenSSL and find 12
  bugs, including two OpenSSL denial-of-service vulnerabilities. We also verify (with caveats) that 115 patches do not introduce crashes. Second, we use
  UC-KLEE as a generalized checking framework and implement checkers to find memory leaks, uninitialized data, and unsafe user input. We evaluate the checkers
  on over 20,000 functions from BIND, OpenSSL, and the Linux kernel, find 67 bugs, and verify that hundreds of functions are leak free and that thousands
  of functions do not access uninitialized data.
added: 2021-04-17
address: USA
authors:
- David A. Ramos
- Dawson Engler
booktitle: Proceedings of the 24th USENIX Conference on Security Symposium
isbn: '9781931971232'
layout: paper
location: Washington, D.C.
numpages: '16'
pages: 49-64
publisher: USENIX Association
read: true
readings:
- 2021-04-18
series: SEC'15
title: 'Under-constrained symbolic execution: Correctness checking for real code'
year: 2015
notes:
- KLEE verifier
- symbolic execution
- lazy initialization
papers:
- ramos:cav:2011
- engler:issta:2007
- khurshid:tacas:2003
- xie:popl:2005
- calcagno:popl:2009
- goodman:ndss:2018
- cui:asplos:2013
---

Avoids the path explosion of application level symbolic execution by analyzing functions in isolation
checking for crashes and also using three checkers for memory leaks, uninitialized data and unsanitized use of user input.
Applying to BIND, OpenSSL and Linux kernel, they find 67 new bugs.
They also apply this to patches from BIND and OpenSSL and find 12 bugs and verify (with caveats) 115 patches.
(On the others, they do not exhaust all execution paths but achieve high coverage.)

This is based on an extension to the [KLEE verifier] used to test for equivalence ([ramos:cav:2011]).
Use of under-constrained checking can lead to false positives that can be (lazily) suppressed
by adding preconditions which they suggest is orders of magnitude less work than eagerly providing a full spec for each function.
Their approach depends on "lazy initialization" of symbolic inputs (including complex, pointer-rich data structures)
([khurshid:tacas:2003], [xie:popl:2005]) --- possibly similar to "biabduction" ([calcagno:popl:2009]).
The basic idea is that pointers start "unbound" and the shape of the object they point to (if any) is gradually
filled in as fields of the object are accessed.
They place a bound on the maximum number of allocations.
The symbolic objects constructed are assumed to have no aliasing or cyclic data structures (they are trees, not DAGs).
(The approach does not work for function pointers.)

To check patches, they exclude patches that add fields (their lazy initialization implementation cannot handle that).
They look for patches that introduce new failures: inputs that cause failures that the original function did not fail on.
In effect, they are assuming that the new function has the same precondition as the original and they are reporting
cases where the precondition is stronger.
They automatically generate a test harness based on the type of the function under test and they call the patched version P'
before the unpatched version P to help path pruning.
(There is something slightly weird in the harness: according to the description, failures in P' are caught and the
same inputs are then run on P --- but it is not clear how.)
There is also a pruning technique that conservatively discards code that is the same in P and P', code that cannot lead to an
exception, etc. (I probably need to read [ramos:cav:2011] for more detail on this.)

In addition, they checked for paths through functions that *must fail* if that path is executed. i.e., that could not
be eliminated by any non-vacuous precondition.

The evaluation has lots of detail on the number of paths explored, etc.

False positives were caused by:

- missing data structure invariants (e.g., that a binary tree is sorted)
- state machine invariants (and possibly how that relates to other parts of the state?)
- API invariants (e.g., that an argument must be null)
- relationships between function arguments (e.g., that one argument is the length of another argument)

False positives can be filtered by data structure invariants and function call annotations (preconditions).
Function call annotations are specified separately from the code being tested.
They have some convenience macros. (See [goodman:ndss:2018] for other convenience functions/macros like "pumping".)

- INVARIANT(c) adds a path constraint and kills path if infeasible
- EXPECT(c) adds a path constraint only if it does not make the path infeasible (otherwise ignore)
- IMPLIES(a, b) -- implication
- HOLDS(a) -- true if a must hold (this and MAY_HOLD relate to controlling path explosion)
- MAY_HOLD(a) -- true if a may hold
- SINK(e) -- evaluate e (compiler may not optimize away)
- VALID_POINTER(p) -- true if p is a valid pointer
- OBJECT_SIZE(p) -- size of object pointed to by p, kills path if p is invalid

They also suppress (or rank?) reports using automated heuristics

- must-fail. will fail if this path is executed no matter what (non-vacuous) precondition
  is added to this function
- belief-fail. e.g., if a function checks if a pointer is null and then dereferences this
  pointer that it knows must be null. (But if F calls G, the beliefs of G do not propagate
  back to F.) That is, the belief set is the set of constraints added within the current
  function or inherited from its caller.
- concrete-fail. an assertion failure or memory error
  depends only on non-symbolic conditions/pointers.

Concrete-fail and belief fail were the most effective.
Only 8-20% of belief fails were true bugs but these heuristics
reduced the number of cases that had to be manually examined to a feasible level
by reducing the number of false positives by 98%.

A large fraction of belief fails that were still false positives was due to paths
reading past the end of an input buffer. e.g., strlen could easily read past the end
because there was no precondition saying that strings were null-terminated.

## Generalized checking

"Generalized checking" refers to adding instrumentation and checks into the LLVM
being verified. This is like what you might do for concrete execution with valgrind or Pin or, for
symbolic execution with the KLEE-based Woodpecker tool ([cui:asplos:2013]).
They used this to implement three checkers

- A memory leak checker
- An uninitialized data checker.
  This has to be limited to uninitialized data used in branches or as memory addresses
  because memcpy (for example) often copies uninitialized data.
- User input checker.
  Uses shadow memory to tracks whether values are untrusted data (e.g., marked by
  calling "copy_from_user", or subjected to endianness transformation (ntohs, ntohl, etc.)
  and tracks whether the constraints *potentially* sanitize the value.
  (This was designed after the fact to catch Heartbleed.)

When analyzing functions in Linux, they link with other functions in the same module or vmalloc.h but
treat anything else as external.

The leak checker was most effective.

## Implementation

Two ways to do lazy initialization where you don't know the size of an object.
(1) Provide a form of backtracking: checkpoint the state on allocation; rewind on error;
replay the same path that triggered the error.
(2) Use symbolically size objects.
Using symbolically sized objects was implemented later -- sounds like they should have
just implemented that early (although the checkpointing idea may be useful for other things?)

Error reporting is hard because heap allocated objects are hard to describe.
They generate a "path summary" = the path followed plus the path constraints added
at each condition along the path.

Miscellaneous optimizations

- Control path explosion by adding symbolic if-then-else constructs.
- Many rules to simplify symbolic expressions.
- "Lazy constraints" that defer expensive constraints until checking that a detected
  error is on a feasible path.
- Function pointers need to be resolved by user input.

*[This was a long summary but there was a lot more in this paper -- worth reading
and chasing down the papers it cites if you are into this line of work.]*

{% include links.html %}
