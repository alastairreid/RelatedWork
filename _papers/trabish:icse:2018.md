---
ENTRYTYPE: inproceedings
abstract: Symbolic execution is a powerful program analysis technique that systematically explores multiple program paths. However, despite important technical
  advances, symbolic execution often struggles to reach deep parts of the code due to the well-known path explosion problem and constraint solving limitations.In
  this paper, we propose chopped symbolic execution, a novel form of symbolic execution that allows users to specify uninteresting parts of the code to
  exclude during the analysis, thus only targeting the exploration to paths of importance. However, the excluded parts are not summarily ignored, as this
  may lead to both false positives and false negatives. Instead, they are executed lazily, when their effect may be observable by code under analysis. Chopped
  symbolic execution leverages various on-demand static analyses at runtime to automatically exclude code fragments while resolving their side effects,
  thus avoiding expensive manual annotations and imprecision.Our preliminary results show that the approach can effectively improve the effectiveness of
  symbolic execution in several different scenarios, including failure reproduction and test suite augmentation.
added: 2021-02-24
address: New York, NY, USA
authors:
- David Trabish
- Andrea Mattavelli
- Noam Rinetzky
- Cristian Cadar
booktitle: Proceedings of the 40th International Conference on Software Engineering
doi: 10.1145/3180155.3180251
isbn: '9781450356381'
keywords: symbolic execution, static analysis, program slicing
layout: paper
link: https://doi.org/10.1145/3180155.3180251
location: Gothenburg, Sweden
numpages: '11'
pages: 350-360
publisher: Association for Computing Machinery
read: true
readings:
- 2021-02-25
series: ICSE '18
title: Chopped symbolic execution
url: https://doi.org/10.1145/3180155.3180251
year: 2018
notes:
- symbolic execution
- KLEE verifier
- case splitting
papers:
---

This adds a form of lazy evaluation to symbolic execution: deferring execution
of code until the analysis actually needs it.

Chopped symbolic execution uses

- A static pointer analysis to identify potential dependencies of the symbolic
  state on the deferred code so that the code can be executed when it is
  actually needed. (Whole program, flow/context-insensitive, field-sensitive
  points-to analysis.)
- A snapshot of the state just before the deferred code
- Accesses to dependencies trigger execution of the deferred code
- A list of "guiding constraints": constraints added to the path condition since
  after the deferred code. These are added to filter out invalid executions.
- Static program slicing of the deferred code is used to limit execution
  to instructions that write to the dependencies.
  (The 'static' slicing appears to take place just before the deferred code
  is symbolically executed.)
- A recovery cache avoids some need to execute the deferred code multiple times.
  (I think there is some tension between this and slicing?)

*[This seems to have all the elements one would expect in lazy evaluation:
capturing the closure, creating thunks, using updates to avoid executing thunks
multiple times.]*


Notes

- Deferring execution interferes with the search heuristics so deferred code can
  be scheduled with some low probability.
- There is a limitation involving symbolic addresses caused by the need to be
  able to watch for accesses to dependencies.
- Implemented as an extension to the [KLEE verifier].
- Requires user to identify functions to be skipped.
- Evaluation
  - All comparisons are with an unmodified KLEE, not other approaches:
    goal is to understand impact on symbolic execution.
  - GNU libtasn1 (ASN.1 parsing library) with a focus on four CVEs.
    - Improvements are dramatic 10x or more.
    - The methodology for choosing what functions to skip seems to depend on
      knowing something about the CVEs???
  - Testsuite augmentation for BC, LibYAML, GNU oSIP.
    - Goal is to improve on KLEE.
    - Skip any functions whose descendents have adequate coverage.
    - Decent improvement in coverage (up to double).


{% include links.html %}
