---
ENTRYTYPE: inproceedings
added: 2019-10-13
authors:
- Bart Jacobs
- Jan Smans
- Pieter Philippaerts
- Frédéric Vogels
- Willem Penninckx
- Frank Piessens
booktitle: NASA Formal Methods Symposium
doi: 10.1007/978-3-642-20398-5_4
layout: paper
organization: Springer
pages: 41-55
read: true
readings:
- 2020-02-09
title: 'VeriFast: A powerful, sound, predictable, fast verifier for C and Java'
year: 2011
topics:
- tools
- verification
notes:
- permission logic
- separation logic
- fractional permissions
- permission accounting
- VeriFast verifier
- ghost code
- SMT solver
- auto-active verification
papers:
- bornat:popl:2005
- jacobs:vstte:2010
- philippaerts:scp:2014
---

VeriFast is an auto-active verification tool for C and Java based on separation
logic and SMT solvers.
This paper is a nice overview of the state of the project in 2011 when they had

- a symbolic execution based checker with a nice UI
- support for both C and Java
- support for
  [permission accounting][bornat:popl:2005]
  based on fractional permissions and an encoding of counting permissions
- support for
  [writing (recursive) lemma functions][jacobs:vstte:2010]
  to prove inductive properties
- and they were starting on some
  [industrial case studies][philippaerts:scp:2014]


{% include links.html %}
