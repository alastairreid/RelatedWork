---
ENTRYTYPE: inproceedings
added: 2020-05-22
authors:
- Marcel Böhme
- Valentin Manes
- Sang-Kil Cha
booktitle: Proceedings of the 2020 28th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering
layout: paper
number: ''
pages: 11
read: true
readings:
- 2020-05-22
title: 'Boosting Fuzzer Efficiency: An Information Theoretic Perspective'
volume: ''
year: 2020
notes:
- fuzz testing
- entropy
papers:
---

Greybox fuzzers prioritise which seeds to explore in order to (hopefully)
maximise some metric such as coverage.
This paper proposes an information theoretic model (entropy) for evaluating the
effectiveness of each seed.
This forms the basis of an "entropy based power schedule" to assign more energy
to the seeds that elicit the most information.
The approach is inspired by "Active SLAM": an approach for autonomous robot
exploration of unknown terrain.

Some of the challenges they face are

- The theory best handles situations where each exploration learns zero
  or one facts at a time and needs normalization if a single exploration can
  discover multiple new things.
  (This deviates slightly from information theory?)

- When a new seed is introduced, we don't know its entropy so we should
  use an initial estimate that is too high (so that the seed gets scheduled)
  instead of too low (causing us never to schedule the seed which prevents
  us from learning the entropy).

- A few facts are superabundant (I think this is basically the first few
  branches in the program or maybe frequently called functions like printf?)
  and so whichever seed first runs will be credited
  with learning facts that any other seed could have found as easily.
  This is handled by introducing a "global abundance threshold": any facts
  that are more abundant than the threshold are ignored when calculating
  entropy.

The ideas in this paper were tried in Google's LibFuzzer and the small changes
(350 lines) are being merged into LibFuzzer.
The evaluation has four clearly stated research questions that are evaluated
on a large body of fuzzing benchmarks.

{% include links.html %}
