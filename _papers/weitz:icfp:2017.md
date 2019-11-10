---
ENTRYTYPE: inproceedings
added: 2019-10-18
address: Oxford, UK
authors:
- Konstantin Weitz
- Steven Lyubomirsky
- Stefan Heule
- Emina Torlak
- Michael D. Ernst
- Zachary Tatlock
booktitle: 'ICFP 2017: Proceedings of the 22nd ACM SIGPLAN International Conference on Functional Programming'
doi: 10.1145/3110269
layout: paper
month: September
pages: 25:1-25:28
read: true
readings:
- 2019-10-17
title: 'SpaceSearch: A library for building and verifying solver-aided tools'
year: 2017
topics:
- verification
---

Coq embedding of Rosette solver aided language inspired by smten.

Factors proof into two parts
with SpaceSearch ADT as the interface between the two.
- Coq proof (interactive) - can use induction, coinduction, higher order, etc.
- Rosette proof (automatic) - limited to first order.

Demonstrated by
- verifying RockSalt against STOKE
- verifying Bagpipe

Found bugs in both.
