---
ENTRYTYPE: article
abstract: 'Coverage-guided fuzz testing has gained prominence as a highly effective method of finding security vulnerabilities such as buffer overflows
  in programs that parse binary data. Recently, researchers have introduced various specializations to the coverage-guided fuzzing algorithm for different
  domain-specific testing goals, such as finding performance bottlenecks, generating valid inputs, handling magic-byte comparisons, etc. Each such solution
  can require non-trivial implementation effort and produces a distinct variant of a fuzzing tool. We observe that many of these domain-specific solutions
  follow a common solution pattern. In this paper, we present FuzzFactory, a framework for developing domain-specific fuzzing applications without requiring
  changes to mutation and search heuristics. FuzzFactory allows users to specify the collection of dynamic domain-specific feedback during test execution,
  as well as how such feedback should be aggregated. FuzzFactory uses this information to selectively save intermediate inputs, called waypoints, to augment
  coverage-guided fuzzing. Such waypoints always make progress towards domain-specific multi-dimensional objectives. We instantiate six domain-specific
  fuzzing applications using FuzzFactory: three re-implementations of prior work and three novel solutions, and evaluate their effectiveness on benchmarks
  from Google''s fuzzer test suite. We also show how multiple domains can be composed to perform better than the sum of their parts. For example, we combine
  domain-specific feedback about strict equality comparisons and dynamic memory allocations, to enable the automatic generation of LZ4 bombs and PNG bombs.'
added: 2021-06-22
address: New York, NY, USA
articleno: '174'
authors:
- Rohan Padhye
- Caroline Lemieux
- Koushik Sen
- Laurent Simon
- Hayawardh Vijayakumar
doi: 10.1145/3360600
issue_date: October 2019
journal: Proc. ACM Program. Lang.
keywords: domain-specific fuzzing, frameworks, fuzz testing, waypoints
layout: paper
link: https://doi.org/10.1145/3360600
month: October
number: OOPSLA
numpages: '29'
publisher: Association for Computing Machinery
read: false
readings: []
title: 'FuzzFactory: Domain-specific fuzzing with waypoints'
url: https://doi.org/10.1145/3360600
volume: '3'
year: 2019
notes:
- fuzz testing
papers:
---
{% include links.html %}
