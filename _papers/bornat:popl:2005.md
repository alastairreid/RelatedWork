---
ENTRYTYPE: inproceedings
added: 2020-02-05
address: New York, NY, USA
authors:
- Richard Bornat
- Cristiano Calcagno
- Peter O'Hearn
- Matthew Parkinson
booktitle: Proceedings of the 32nd ACM SIGPLAN-SIGACT Symposium on Principles of Programming
  Languages
doi: 10.1145/1040305.1040327
isbn: 158113830X
keywords: permissions, logic, concurrency, separation
layout: paper
location: Long Beach, California, USA
numpages: '12'
pages: 259-270
publisher: Association for Computing Machinery
read: true
readings:
- 2020-02-07
series: POPL '05
title: Permission accounting in separation logic
url: https://doi.org/10.1145/1040305.1040327
year: 2005
topics:
- verification
---

Separation logic is about tracking ownership of objects
and, usually, this means full ownership: you either own
an object and can do anything you want with it or
you have no access at all.
This paper is about sharing ownership as in the reader-writer
pattern where an object can be shared between several readers
or ownership can be given to a single writer.

The paper explores two ways of doing this:

1. Using fractional permissions where ownership can be split
   into several parts and can be recombined later.
   (This seems to be best for recursive functions?)

2. Using counting permissions where the number of readers is
   tracked.

The main technical trick used in adding this to the logic is to
change from modelling the heap as a map from addresses to values
but, instead, as a map from addresses to pairs of values and
permissions and permissions are either a fraction or a count.

Besides the technical content, the writing style of the author
stands out. Beyond the innocent sounding fact that it is written
in the first person, the style is very hard to describe – you
need to read it for yourself.
