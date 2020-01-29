---
ENTRYTYPE: inproceedings
abstract: 'Case studies on formal software verification can be divided into two categories:
  while (i) unsound approaches may miss errors or report false-positive alarms due
  to coarse abstractions, (ii) sound approaches typically do not handle certain programming
  constructs like concurrency and/or suffer from scalability issues. This paper presents
  a case study on successfully verifying the Linux USB BP keyboard driver. Our verification
  approach is (a) sound, (b) takes into account dynamic memory allocation, complex
  API rules and concurrency, and (c) is applied on a real kernel driver which was
  not written with verification in mind. We employ VeriFast, a software verifier based
  on separation logic. Besides showing that it is possible to verify this device driver,
  we identify the parts where the verification went smoothly and the parts where the
  verification approach requires further research to be carried out.'
added: 2020-01-29
address: Berlin, Heidelberg
authors:
- Willem Penninckx
- Jan Tobias Mühlberg
- Jan Smans
- Bart Jacobs
- Frank Piessens
booktitle: NASA Formal Methods
editor: 'Goodloe, Alwyn E.
  and Person, Suzette'
isbn: 978-3-642-28891-3
layout: paper
pages: 210-215
publisher: Springer Berlin Heidelberg
read: false
readings: []
title: Sound formal verification of Linux's USB BP keyboard driver
year: 2012
topics:
- os
- verification
---
