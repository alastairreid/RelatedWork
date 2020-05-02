---
ENTRYTYPE: article
abstract: We present a trace semantics for a language of parallel programs which share
  access to mutable data. We introduce a resource-sensitive logic for partial correctness,
  based on a recent proposal of O'Hearn, adapting separation logic to the concurrent
  setting. The logic allows proofs of parallel programs in which "ownership" of critical
  data, such as the right to access, update or deallocate a pointer, is transferred
  dynamically between concurrent processes. We prove soundness of the logic, using
  a novel "local" interpretation of traces which allows accurate reasoning about ownership.
  We show that every provable program is race-free.
added: 2020-02-05
authors:
- Stephen Brookes
doi: https://doi.org/10.1016/j.tcs.2006.12.034
issn: 0304-3975
journal: Theoretical Computer Science
keywords: Concurrency, Pointers, Race condition, Semantics, Logic
layout: paper
note: Festschrift for John C. Reynolds's 70th birthday
number: '1'
pages: 227 - 270
read: false
readings: []
title: A semantics for concurrent separation logic
url: http://www.sciencedirect.com/science/article/pii/S0304397506009248
volume: '375'
year: 2007
topics:
- verification
notes:
- permission-logic
---
