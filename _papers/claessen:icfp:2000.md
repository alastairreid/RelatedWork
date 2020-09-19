---
ENTRYTYPE: inproceedings
added: 2020-09-07
address: New York, NY, USA
authors:
- Koen Claessen
- John Hughes
booktitle: Proceedings of the Fifth ACM SIGPLAN International Conference on Functional Programming
doi: 10.1145/351240.351266
isbn: '1581132026'
layout: paper
link: https://doi.org/10.1145/351240.351266
numpages: '12'
pages: 268-279
publisher: Association for Computing Machinery
read: true
readings:
- 2020-09-13
series: ICFP '00
title: 'QuickCheck: A lightweight tool for random testing of Haskell programs'
url: https://doi.org/10.1145/351240.351266
year: 2000
notes:
- property-based testing
- fuzz testing
- unit tests
papers:
- becker:fm:2016
---

QuickCheck takes a test-based approach to formal verification.
You write universally-quantified properties and QuickCheck uses
random testing ([fuzz testing]) to check whether the property holds.
QuickCheck was originally written for Haskell but various people have
since implemented it for around 40 different languages.

It is based on a lightweight DSL (the original was around 300 lines – most of
which is included in an appendix).

A bunch of cool things in the paper

- 'classify' labels inputs satisfying some condition so that
  you can count different categories of test input.

- 'collect' generates histograms of input values.
  (This and 'collect' is reminiscent of similar functionality that
  later appeared in System-Verilog.)

- parts of the DSL for creating test-data generators

  - 'forAll' is used to invoke custom test-data generators.
    (They remark that it is important to know the desired
    distribution of test-cases in order to create (select?) a
    good test-data generator.)

  - 'oneof' is used to combine generators

  - 'frequency' is used to combine generators with different weights

  - 'sized' is used to control the size of values generated

  - the typeclass 'Arbitrary' is used to select a test-data generator
    based on type.

  - the typeclass 'Coarbitrary' is used to generate random functions.
    It is roughly equivalent to generating a hash from the inputs and
    using that as to modify the random seed to generate the outputs.

    Key to making this work is that '>>' splits seeds instead of serializing
    them.

- structured inputs (e.g., substitution maps) can't just be random: you have
  to design a generator that has the right data distribution to generate
  values that are not just legal but are likely to hit important cases.

- When they tried QuickCheck on Lava, they were able to also check properties
  with a first-order solver but it was still worth using QuickCheck because
  it would quickly find counterexamples a lot of the time and because
  the ability to create random functions allows QuickCheck to test
  higher-order properties.

- An important part of QuickCheck is that it is easy to use which means
  that it is much more likely to be used.

- The errors detected are roughly equally in the test-data generators, the
  specifications and the program.
  (This reminds me of what [becker:fm:2016] reports.)

- To help write specifications, they are developing a library of finite set
  theory.

- There is no measurement of *test coverage* because they want QuickCheck
  to be lightweight and easy to use with any Haskell compiler.

Something that I had not remembered correctly about this paper was shrinking.
Shrinking (simplifying test-data values) is a key part of QuickCheck
but it is mentioned almost as an afterthought as an idea suggested by
Andy Gill and with little detail on the best ways to shrink values.

{% include links.html %}
