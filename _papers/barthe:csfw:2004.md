---
ENTRYTYPE: inproceedings
added: 2019-10-13
authors:
- Gilles Barthe
- Pedro R. D'Argenio
- Tamara  Rezk
booktitle: '17th IEEE Computer Security Foundations Workshop, (CSFW-17 2004)'
doi: 10.1109/CSFW.2004.17
layout: paper
pages: 100-114
read: true
readings:
- 2019-10-11
title: Secure information flow by self-composition
year: 2004
notes:
- information-flow
- self-composition
papers:
---

This paper is a counter to the popular type-based approaches to information flow control.  They point out that type-based approaches are sound but not complete and fail on things like "output := secret; output := 0;".  Their solution is a more semantic approach that is based more closely on the basic definitions of non-interference and is sound and complete (but, unlike type-based approaches, is often undecidable and not obviously compositional).

"Self-composition" consists of proving 2-safety properties of a program "P" by reasoning about the program "P; P'" where "P'" is a copy of P with all variables renamed from x to x'.
(They make explicit the assumption that renaming a variable, adding a new variable, etc. does not affect the meaning — note that this may not be true if your program or language is not memory-safe.)

This approach can be used to enable Hoare-logic reasoning about pointer free programs, separation logic reasoning about programs with pointers, and model checking about non-deterministic programs.  (Other papers seem to have used similar definitions — the distinguishing feature of this paper seems to be the generality of their approach.)

Good paper for citation/discussion of related work.

{% include links.html %}
