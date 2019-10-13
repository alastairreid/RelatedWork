---
ENTRYTYPE: article
authors:
- Gilles Barthe
- Pedro R. D'Argenio
- Tamara  Rezk
doi: 10.1017/S0960129511000193
journal: Mathematical Structures in Computer Science
layout: paper
number: '6'
pages: 1207-1252
publisher: Cambridge University Press
read: true
title: Secure information flow by self-composition
volume: '21'
year: 2011
topics:
- information-flow
readings:
- 2019-10-11
---

_Todo: I think I read a conference paper but the publication data above is for a journal._

This paper is a counter to the popular type-based approaches to information flow control.  They point out that type-based approaches are sound but not complete and fail on things like "output := secret; output := 0;".  Their solution is a more semantic approach that is based more closely on the basic definitions of non-interference and is sound and complete (but, unlike type-based approaches, is often undecidable and not obviously compositional).

"Self-composition" consists of proving 2-safety properties of a program "P" by reasoning about the program "P; P'" where "P'" is a copy of P with all variables renamed from x to x'.
(They make explicit the assumption that renaming a variable, adding a new variable, etc. does not affect the meaning - note that this may not be true if your program or language is not memory-safe.)

This approach can be used to enable Hoare-logic reasoning about pointer free programs, separation logic reasoning about programs with pointers, and model checking about non-deterministic programs.  (Other papers seem to have used similar definitions - the distinguishing feature of this paper seems to be the generality of their approach.)

Good paper for citation/discussion of related work.
