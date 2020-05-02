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
notes:
- boogie-verifier
- intermediate-verification-language
- smack-verifier
- llvm-compiler
---

SMACK translates LLVM bitcode files to the [Boogie language]
(an [intermediate verification language])
allowing it to support any language that LLVM supports (mostly C/C++ in this
paper).

SMACK implements one key optimization: using alias analysis to partition the
heap (and pointers into the heap) so that objects that could not be confused
are in separate sub-heaps.

[intermediate verification language]: {{ "notes/intermediate-verification-language" | relative_url }}
[Boogie language]: {{ "notes/boogie-verifier" | relative_url }}

{% include links.html %}
