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
read: true
readings:
- 2020-01-29
title: Sound formal verification of Linux's USB BP keyboard driver
year: 2012
topics:
- os
- permission-logic
- tools
- verification
notes:
- permission-logic
- separation-logic
- concurrent-separation-logic
- verifast-verifier
---

This paper reports on verification of a simple Linux USB
keyboard driver using
[VeriFast](https://github.com/verifast/verifast).
Except, of course, Linux drivers are not simple:
they have asynchronous callbacks, dynamically allocated
memory, synchronization and interact with complex
Linux driver APIs including USB, input and spinlocks.
This work found bugs in the driver and the fixes have been
accepted by the maintainer.

The properties verified include freedom of data races,
freedom of illegal memory accesses and correct API
usage.
(Though, as they point out themselves, the API spec could have
bugs.)

The driver is 426 lines long, of which there are 329 lines of
non-blank, non-comment code.
To this, they add 769 lines of reusable API specifications
and 53 lines of annotation (or maybe it is 822 lines – it
is not clear whether the 822 lines of annotations includes the 769 lines of spec
or not).
Verification takes about 1 second.

They report that some of the concurrency patterns
involved in LED handling was tricky to verify and
required the introduction of "ghost counters".
They also had to reason about permissions passed between
callbacks.



