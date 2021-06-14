---
ENTRYTYPE: inproceedings
added: 2021-03-15
address: Baltimore, MD
authors:
- Insu Yun
- Sangho Lee
- Meng Xu
- Yeongjin Jang
- Taesoo Kim
booktitle: Proceedings of the 27th USENIX Security Symposium (Security)
layout: paper
month: August
read: true
readings:
- 2021-06-13
title: 'QSYM: A practical concolic execution engine tailored for hybrid fuzzing'
year: 2018
notes:
- symbolic execution
- concolic execution
- DARPA CGC
- Driller verifier
- AFL fuzzer
- Fuzz testing
- Hybrid testing
- Dynamic binary translation
papers:
- poeplau:usenix:2020
---

QSYM significantly improves the performance of [concolic execution]
of binaries
to support [hybrid testing] (a form of [fuzz testing]).
The key ideas (based on a detailed examination of all the
usual design choices and their problems) are

1. Instead of tracking dependencies using taint-tracking at a basic
   block level, it tracks dependencies at the instruction level.

2. To relax the requirement of strict soundness because that is not so
   important in the context of hybrid fuzzing because the fuzzer
   will discard any incorrect solutions.

   They can skip compute-intensive code and crypto code.
   For this, they use an exponential back-off by only executing
   blocks that have been executed '2^N' times for some 'N'.
   This prevents very hot blocks from swamping the
   symbolic execution.
   (But then they relax that restriction a little using context-sensitivity
   and something else.)

   And they can significantly prune the number of constraints being
   solved for: only considering the constraints applying to the
   last branch in the execution path instead of all branches on the
   path.
   Again, this works fine with hybrid fuzzing: solving one more constraint
   lets the fuzzer make progress.

3. The performance improvements allow them to skip state snapshotting
   because re-execution is sufficiently fast.
   ([poeplau:usenix:2020] exploits the same observation.)
   This is especially important for hybrid fuzzing which has lower
   locality which reduces reuse of snapshots.
   Finally, it is not possible to snapshot any external state such
   as the filesystem anyway.

4. Avoid using an intermediate representation such as VEX
   or LLVM-IR because converting binary to IR and back to binary
   causes significant increase in the number of instructions
   and because IR-caching interferes with more important
   optimizations.

QSYM uses [dynamic binary translation] to identify the instructions
that need to be symbolically executed.

QSYM has a Python API that is used to control/extend execution.

QSYM found a bunch of new CVEs, the AFL+QSYM combo achieves significantly
higher coverage than AFL by itself, it does better than [Driller][Driller
verifier], and it is faster.

The whole paper has lots of references/discussion of both [symbolic execution]
tools and [fuzz testing] tools: really useful!

{% include links.html %}
