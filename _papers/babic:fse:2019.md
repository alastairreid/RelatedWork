---
ENTRYTYPE: inproceedings
added: 2020-09-07
address: New York, NY, USA
authors:
- Domagoj Babić
- Stefan Bucur
- Yaohui Chen
- Franjo Ivančić
- Tim King
- Markus Kusano
- Caroline Lemieux
- László Szekeres
- Wei Wang
booktitle: Proceedings of the 2019 27th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering
doi: 10.1145/3338906.3340456
isbn: '9781450355728'
keywords: code synthesis, testing, program slicing, fuzz testing, software security, fuzzing, automated test generation
layout: paper
link: https://doi.org/10.1145/3338906.3340456
location: Tallinn, Estonia
numpages: '11'
pages: 975-985
publisher: Association for Computing Machinery
read: true
readings:
- 2020-09-07
series: ESEC/FSE 2019
title: 'FUDGE: Fuzz driver generation at scale'
url: https://doi.org/10.1145/3338906.3340456
year: 2019
notes:
- fuzz testing
- test generation
papers:
---

Addresses the problem of generating fuzzing test harnesses for libraries by
automatically generating harnesses based on example uses in existing clients.
The goal is to increase the productivity of users and
it is expected that a human will examine the generated harnesses for legality,
etc. before they are used to report bugs.

The approach has three stages: slicing, synthesis and evaluation.

- Slicing analyzes functions and extracts code related to the library under test
  using the ClangMR frontend hook.

- Synthesis turns slices into runnable code.
  Results of calls to other libraries are replaced with placeholders and
  several candidate test harnesses are generated with different combinations
  of concrete and fuzzable values.

- Evaluation weeds out candidates that fail within a time bound since they
  are considered low-value.
  The remainder are passed to users who can rank them, observe increase in
  coverage, modify them (e.g., to choose better variable names and other
  readability improvements), etc.

This tooling is embedded in a flow that

- uses heuristics to try to identify APIs
  worth fuzzing (e.g., it looks for names like "parse", "load",
  "open", ...).

- ranks APIs by number of uses within Google's internal codebase

- presents generated harnesses as "code findings" next to the code
  that they test.

The paper reports several case studies with open-source (non-Google) code
and they report several lessons learned.

1. Choosing a suitable fuzz target (still) requires a human.

2. API call sites present good locality.
   (This allows the use of an intraprocedural analysis most of the time.)

3. Analyzing C++ is challenging due to a long tail of language features.

4. Randomized algorithms have a good cost-value tradeoff for program synthesis.

5. Program synthesis artifacts can be presented as code findings to developers.

A lot of the previous tools in this space were for Java.

{% include links.html %}
