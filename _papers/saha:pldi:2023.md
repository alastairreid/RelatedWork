---
ENTRYTYPE: article
abstract: 'Information leaks are a significant problem in modern software systems. In recent years, information theoretic concepts, such as Shannon entropy,
  have been applied to quantifying information leaks in programs. One recent approach is to use symbolic execution together with model counting constraints
  solvers in order to quantify information leakage. There are at least two reasons for unsoundness in quantifying information leakage using this approach:
  1) Symbolic execution may not be able to explore all execution paths, 2) Model counting constraints solvers may not be able to provide an exact count.
  We present a sound symbolic quantitative information flow analysis that bounds the information leakage both for the cases where the program behavior is
  not fully explored and the model counting constraint solver is unable to provide a precise model count but provides an upper and a lower bound. We implemented
  our approach as an extension to KLEE for computing sound bounds for information leakage in C programs.'
added: 2023-07-02
address: New York, NY, USA
articleno: '167'
authors:
- Seemanta Saha
- Surendra Ghentiyala
- Shihua Lu
- Lucas Bang
- Tevfik Bultan
doi: 10.1145/3591281
issue_date: June 2023
journal: Proc. ACM Program. Lang.
keywords: Model Counting, Quantitative Program Analysis, Symbolic Quantitative Information Flow Analysis, Optimization, Information Leakage
layout: paper
link: https://doi.org/10.1145/3591281
month: jun
number: PLDI
numpages: '22'
publisher: Association for Computing Machinery
read: false
readings: []
title: Obtaining information leakage bounds via approximate model counting
url: https://doi.org/10.1145/3591281
volume: '7'
year: 2023
notes:
- information flow
- model counting
- security
papers:
---
{% include links.html %}
