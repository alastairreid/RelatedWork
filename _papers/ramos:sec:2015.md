---
ENTRYTYPE: inproceedings
abstract: Software bugs are a well-known source of security vulnerabilities. One technique for finding bugs, symbolic execution, considers all possible
  inputs to a program but suffers from scalability limitations. This paper uses a variant, under-constrained symbolic execution, that improves scalability
  by directly checking individual functions, rather than whole programs. We present UC-KLEE, a novel, scalable framework for checking C/C++ systems code,
  along with two use cases. First, we use UC-KLEE to check whether patches introduce crashes. We check over 800 patches from BIND and OpenSSL and find 12
  bugs, including two OpenSSL denial-of-service vulnerabilities. We also verify (with caveats) that 115 patches do not introduce crashes. Second, we use
  UC-KLEE as a generalized checking framework and implement checkers to find memory leaks, uninitialized data, and unsafe user input. We evaluate the checkers
  on over 20,000 functions from BIND, OpenSSL, and the Linux kernel, find 67 bugs, and verify that hundreds of functions are leak free and that thousands
  of functions do not access uninitialized data.
added: 2021-04-17
address: USA
authors:
- David A. Ramos
- Dawson Engler
booktitle: Proceedings of the 24th USENIX Conference on Security Symposium
isbn: '9781931971232'
layout: paper
location: Washington, D.C.
numpages: '16'
pages: 49-64
publisher: USENIX Association
read: false
readings: []
series: SEC'15
title: 'Under-constrained symbolic execution: Correctness checking for real code'
year: 2015
notes:
- KLEE verifier
papers:
---
{% include links.html %}
