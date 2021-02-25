---
ENTRYTYPE: inproceedings
acmid: '2594340'
added: 2019-11-16
address: New York, NY, USA
authors:
- Emina Torlak
- Rastislav Bodik
booktitle: Proceedings of the 35th ACM SIGPLAN Conference on Programming Language Design and Implementation
doi: 10.1145/2594291.2594340
isbn: 978-1-4503-2784-8
keywords: solver-aided languages, symbolic virtual machine
layout: paper
location: Edinburgh, United Kingdom
numpages: '12'
pages: 530-541
publisher: ACM
read: true
readings:
- 2019-11-16
series: PLDI'14
title: A lightweight symbolic virtual machine for solver-aided host languages
url: http://doi.acm.org/10.1145/2594291.2594340
year: 2014
topics:
- tools
- verification
notes:
- Rosette solver
- symbolic evaluation
- symbolic execution
- bounded model checking
- state merging
- case splitting
papers:
- nelson:sosp:2019
---

Rosette is a Racket DSL for implementing Solver-aided Domain Specific
Languages (SDSLs): tools based on solvers that support
angelic execution, debugging, verifying properties and
synthesis.
A key feature of Rosette is "symbolic reflection" – that allows
Racket code to be symbolically evaluated (in addition to being
executable in the normal way).

Rosette lies somewhere between [symbolic execution] (that enumerates
all paths and solves constraints along each path)
and [bounded model checking].
Like [bounded model checking], Rosette depends on finitizing the
program being reasoned about but it differs in that the
program may be "self-finitizing": instead of simply unrolling loops
to some limit, any constant parts of the input/program, are used
to determine how much to unroll loops.
Indeed, a key insight seems to be that SDSL's have a significant
amount of concrete evaluation in loops/recursion.

Rosette also differs from [bounded model-checking] in how it merges symbolic
values: for each shape of the values, a separate symbolic value is constructed.

Rosette is demonstrated/evaluated on an OpenCL synthesis task, an XPath
synthesis task and an information flow verification task.

This forms the basis of a number of other projects including
[Serval][nelson:sosp:2019].

There are a number of optimizations to make Rosette perform well:
type-driven [state merging] (using the shape of data structures to determine which states to merge);
[case-splitting] using the `for/all` construct.
More broadly, Rosette introduced "symbolic reflection": an API for inspecting
and manipulating symbolic values, the term cache, etc. to enable efficient
implementation.

{% include links.html %}
