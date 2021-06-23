---
ENTRYTYPE: inproceedings
abstract: 'Programs expecting structured inputs often consist of both a syntactic analysis stage, which parses raw input, and a semantic analysis stage,
  which conducts checks on the parsed input and executes the core logic of the program. Generator-based testing tools in the lineage of QuickCheck are a
  promising way to generate random syntactically valid test inputs for these programs. We present Zest, a technique which automatically guides QuickCheck-like
  random input generators to better explore the semantic analysis stage of test programs. Zest converts random-input generators into deterministic parametric
  input generators. We present the key insight that mutations in the untyped parameter domain map to structural mutations in the input domain. Zest leverages
  program feedback in the form of code coverage and input validity to perform feedback-directed parameter search. We evaluate Zest against AFL and QuickCheck
  on five Java programs: Maven, Ant, BCEL, Closure, and Rhino. Zest covers 1.03x-2.81x as many branches within the benchmarks'' semantic analysis stages
  as baseline techniques. Further, we find 10 new bugs in the semantic analysis stages of these benchmarks. Zest is the most effective technique in finding
  these bugs reliably and quickly, requiring at most 10 minutes on average to find each bug.'
added: 2021-06-22
address: New York, NY, USA
authors:
- Rohan Padhye
- Caroline Lemieux
- Koushik Sen
- Mike Papadakis
- Yves Le Traon
booktitle: Proceedings of the 28th ACM SIGSOFT International Symposium on Software Testing and Analysis
doi: 10.1145/3293882.3330576
isbn: '9781450362245'
keywords: random testing, property-based testing, Structure-aware fuzzing
layout: paper
link: https://doi.org/10.1145/3293882.3330576
location: Beijing, China
numpages: '12'
pages: 329-340
publisher: Association for Computing Machinery
read: false
readings: []
series: ISSTA 2019
title: Semantic fuzzing with Zest
url: https://doi.org/10.1145/3293882.3330576
year: 2019
notes:
- Fuzz testing
papers:
---
{% include links.html %}
