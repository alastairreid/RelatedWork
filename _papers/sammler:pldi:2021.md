---
ENTRYTYPE: inproceedings
abstract: 'Given the central role that C continues to play in systems software, and the difficulty of writing safe and correct C code, it remains a grand
  challenge to develop effective formal methods for verifying C programs. In this paper, we propose a new approach to this problem: a type system we call
  RefinedC, which combines ownership types (for modular reasoning about shared state and concurrency) with refinement types (for encoding precise invariants
  on C data types and Hoare-style specifications for C functions). RefinedC is both automated (requiring minimal user intervention) and foundational (producing
  a proof of program correctness in Coq), while at the same time handling a range of low-level programming idioms such as pointer arithmetic. In particular,
  following the approach of RustBelt, the soundness of the RefinedC type system is justified semantically by interpretation into the Coq-based Iris framework
  for higher-order concurrent separation logic. However, the typing rules of RefinedC are also designed to be encodable in a new "separation logic programming"
  language we call Lithium. By restricting to a carefully chosen (yet expressive) fragment of separation logic, Lithium supports predictable, automatic,
  goal-directed proof search without backtracking. We demonstrate the effectiveness of RefinedC on a range of representative examples of C code.'
added: 2021-06-24
address: New York, NY, USA
authors:
- Michael Sammler
- Rodolphe Lepigre
- Robbert Krebbers
- Kayvan Memarian
- Derek Dreyer
- Deepak Garg
booktitle: Proceedings of the 42nd ACM SIGPLAN International Conference on Programming Language Design and Implementation
doi: 10.1145/3453483.3454036
isbn: '9781450383912'
keywords: proof automation, Iris, C programming language, refinement types, separation logic, ownership types, Coq
layout: paper
link: https://doi.org/10.1145/3453483.3454036
location: Virtual, Canada
numpages: '17'
pages: 158-174
publisher: Association for Computing Machinery
read: false
readings: []
series: PLDI 2021
title: 'RefinedC: Automating the foundational verification of C code with refined ownership types'
url: https://doi.org/10.1145/3453483.3454036
year: 2021
notes:
- coq theorem prover
- ownership types
- separation logic
- refinement types
papers:
---
{% include links.html %}
