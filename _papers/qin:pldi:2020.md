---
ENTRYTYPE: inproceedings
added: 2020-11-01
address: New York, NY, USA
authors:
- Boqin Qin
- Yilun Chen
- Zeming Yu
- Linhai Song
- Yiying Zhang
booktitle: Proceedings of the 41st ACM SIGPLAN Conference on Programming Language Design and Implementation
doi: 10.1145/3385412.3386036
isbn: '9781450376136'
keywords: Bug Study, Rust, Memory Bug, Concurrency Bug
layout: paper
link: https://doi.org/10.1145/3385412.3386036
location: London, UK
numpages: '17'
pages: 763-779
publisher: Association for Computing Machinery
read: true
readings:
- 2021-06-16
series: PLDI 2020
title: Understanding memory and thread safety practices and issues in real-world Rust programs
url: https://doi.org/10.1145/3385412.3386036
year: 2020
notes:
- Rust language
- Rust unsafe code
papers:
- astrauskas:oopsla:2020
- evans:icse:2020
---

A manual, empirical study of 850 uses of 'unsafe' in Rust and of 170 bugs (70 memory safety, 100 concurrency)
based on studies of Servo, Tock, Parity Ethereum, TikV, Redox and five libraries and with most (145) of the
bugs being in code after Rust 1.0 (2016).
*[I think that the choice has a bias towards system code so this may be a biased sample?]*
(Contrast  with the much larger, automated studies in [astrauskas:oopsla:2020] and [evans:icse:2020].)
Also describes a use-after-free checker and a double-lock checker for checking unsafe code.

They use the term 'interior unsafe' for a function that contains an unsafe block but that is not
annotated as unsafe.

In their analysis of bugs, they distinguish four categories based on the 'error propagation chain'
and whether it starts in safe or unsafe code and whether it ends in safe or unsafe code. e.g.,
if a safe function breaks an invariant which causes a later unsafe code block to perform an
out-of-bounds access, that is a "safe &rarr; unsafe" bug.

Findings:

- Most interior unsafe functions ensure safety through type invariants instead of by
  performing runtime checks.
  That is, by restricting how their arguments can be constructed so that they can
  ensure that their arguments satisfy the invariant.

- Uninitialized data can be a problem because assigning to that data will
  cause the previous contents to be dropped.

- Use after free ("unsafe &rarr; safe") can happen when safe code
  drops an object (because its lifetime ends)
  but unsafe code still accesses the object.

  > misunderstanding of lifetime [is] the main reason for most
  > use-after-free and many other types of memory-safety bugs.

- Deadlock (called "blocking bugs")
  are all caused by interior unsafe code.
  They are broken down by type of lock (mutex, condvar, etc.)
  and involve failing to acquire locks, inconsistent lock ordering problems,
  forgetting to unlock.

  **What makes locking issues especially hard is that it is hard to understand
  the boundaries of critical sections because 'unlock()' is implicitly called at the end
  of variable lifetimes.**
  They suggest tools could help highlight the range of lifetimes and critical sections
  and suggest that programmers explicitly use `mem::drop()` both to fix problems
  and to be explicit about the end of critical sections.

- Race conditions (called "non-blocking bugs")
  are mostly caused by 
  failure to protect shared resources
  or (rarely) message passing.

  The most common issue is passing raw pointers (since they lack lifetime
  information and ownership checks); followed by sharing results from OS syscalls
  or hardware resources; shared mutable global variables; and incorrectly
  providing adding Sync on a struct.

  They suggest careful review of code that implements Sync.


{% include links.html %}
