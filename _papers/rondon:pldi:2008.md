---
ENTRYTYPE: inproceedings
abstract: We present Logically Qualified Data Types, abbreviated to Liquid Types, a system that combines Hindley-Milner type inference with Predicate Abstraction
  to automatically infer dependent types precise enough to prove a variety of safety properties. Liquid types allow programmers to reap many of the benefits
  of dependent types, namely static verification of critical properties and the elimination of expensive run-time checks, without the heavy price of manual
  annotation. We have implemented liquid type inference in DSOLVE, which takes as input an OCAML program and a set of logical qualifiers and infers dependent
  types for the expressions in the OCAML program. To demonstrate the utility of our approach, we describe experiments using DSOLVE to statically verify
  the safety of array accesses on a set of OCAML benchmarks that were previously annotated with dependent types as part of the DML project. We show that
  when used in conjunction with a fixed set of array bounds checking qualifiers, DSOLVE reduces the amount of manual annotation required for proving safety
  from 31\% of program text to under 1\%.
added: 2021-11-22
address: New York, NY, USA
authors:
- Patrick M. Rondon
- Ming Kawaguci
- Ranjit Jhala
booktitle: Proceedings of the 29th ACM SIGPLAN Conference on Programming Language Design and Implementation
doi: 10.1145/1375581.1375602
isbn: '9781595938602'
keywords: predicate abstraction, dependent types, type inference, hindley-milner
layout: paper
link: https://doi.org/10.1145/1375581.1375602
location: Tucson, AZ, USA
numpages: '11'
pages: 159-169
publisher: Association for Computing Machinery
read: false
readings: []
series: PLDI '08
title: Liquid types
url: https://doi.org/10.1145/1375581.1375602
year: 2008
notes:
- Dependent type
papers:
---
{% include links.html %}
