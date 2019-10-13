---
ENTRYTYPE: inproceedings
authors:
- José Bacelar Almeida
- Manuel Barbosa
- Gilles Barthe
- François Dupressoir
- Michael Emmi
booktitle: 25th USENIX Security Symposium (USENIX Security 16)
layout: paper
pages: 53-70
read: true
readings:
- 2019-09-14
title: Verifying constant-time implementations
topics:
- information-flow
---

Tool for verifying constant time behaviour of C code based on self-composition preprocessing then using SMACK and Boogie.
Parameterized by whether leakage is just PC divergence or also memory access divergence.
Correctness of a reduced/simplified version of analysis is proved in Coq and full algorithm "should not present any additional difficulty".
Demonstrated on a very broad range of crypto code, fixed-time fixed-point code.
Key idea is to reduce security property (2-safety) to 1-safety property using a product construction exploiting the requirement that, if the code is constant time then there should be no PC divergence between the two runs.
A key strength is the ability to be output insensitive: it is ok to leak information that will be leaked anyway.  E.g., if the size is part of the intended output, then it is ok for runtime to depend on size even though size may depend on the secret input.  This distinguishes it from approaches that use some form of tainting of inputs.
