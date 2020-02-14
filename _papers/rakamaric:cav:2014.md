---
ENTRYTYPE: inproceedings
added: 2019-10-12
authors:
- Zvonimir Rakamarić
- Michael Emmi
booktitle: International Conference on Computer Aided Verification
doi: 10.1007/978-3-319-08867-9_7
layout: paper
organization: Springer
pages: 106-113
read: true
readings:
- 2019-10-08
title: 'SMACK: Decoupling source language details from verifier implementations'
year: 2014
topics:
- tools
- verification
---

SMACK translates LLVM bitcode files to the
[Boogie]({{ "papers/barnett:fmco:2005" | relative_url }})
Intermediate Verification Language (IVL)
allowing it to support any language that LLVM supports (mostly C/C++ in this
paper).

Smack implements one key optimization: using alias analysis to partition the
heap (and pointers into the heap) so that objects that could not be confused
are in separate sub-heaps.
