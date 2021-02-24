---
ENTRYTYPE: inproceedings
abstract: Symbolic execution has proven to be a practical technique for building automated test case generation and bug finding tools. Nevertheless, due
  to state explosion, these tools still struggle to achieve scalability. Given a program, one way to reduce the number of states that the tools need to
  explore is to merge states obtained on different paths. Alas, doing so increases the size of symbolic path conditions (thereby stressing the underlying
  constraint solver) and interferes with optimizations of the exploration process (also referred to as search strategies). The net effect is that state
  merging may actually lower performance rather than increase it.We present a way to automatically choose when and how to merge states such that the performance
  of symbolic execution is significantly increased. First, we present query count estimation, a method for statically estimating the impact that each symbolic
  variable has on solver queries that follow a potential merge point; states are then merged only when doing so promises to be advantageous. Second, we
  present dynamic state merging, a technique for merging states that interacts favorably with search strategies in automated test case generation and bug
  finding tools.Experiments on the 96 GNU Coreutils show that our approach consistently achieves several orders of magnitude speedup over previously published
  results. Our code and experimental data are publicly available at http://cloud9.epfl.ch.
added: 2021-02-24
address: New York, NY, USA
authors:
- Volodymyr Kuznetsov
- Johannes Kinder
- Stefan Bucur
- George Candea
booktitle: Proceedings of the 33rd ACM SIGPLAN Conference on Programming Language Design and Implementation
doi: 10.1145/2254064.2254088
isbn: '9781450312059'
keywords: state merging, bounded software model checking, testing, symbolic execution, verification
layout: paper
link: https://doi.org/10.1145/2254064.2254088
location: Beijing, China
numpages: '12'
pages: 193-204
publisher: Association for Computing Machinery
read: false
readings: []
series: PLDI '12
title: Efficient state merging in symbolic execution
url: https://doi.org/10.1145/2254064.2254088
year: 2012
notes:
- symbolic execution
- KLEE verifier
papers:
---
{% include links.html %}
