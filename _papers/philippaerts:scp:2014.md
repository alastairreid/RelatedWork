---
ENTRYTYPE: article
added: 2020-01-31
authors:
- Pieter Philippaerts
- Jan Tobias Mühlberg
- Willem Penninckx
- Jan Smans
- Bart Jacobs
- Frank Piessens
doi: 10.1016/j.scico.2013.01.006
issn: 0167-6423
journal: 'Science of Computer Programming '
layout: paper
month: '3'
number: '1'
pages: 77-97
publisher: North-Holland Pub. Co.
read: true
readings:
- 2020-02-12
title: 'Software verification with VeriFast: Industrial case studies'
url: https://lirias.kuleuven.be/95711
volume: '82'
year: 2014
topics:
- tools
- verification
notes:
- permission logic
- separation logic
- VeriFast verifier
papers:
- jacobs:nfm:2011
- penninckx:nfm:2012
- filliatre:fem:2004
- vogels:fmoods:2011
- cohen:cav:2010
---

This paper reports on four case studies using
[VeriFast][jacobs:nfm:2011]
to verify real code for an absence of safety violations
such as illegal memory accesses or data races.

The paper starts with a very nice overview of the features
of VeriFast and then describes the four case studies

- eID (Java)
  The Belgian Electronic Identity Card.
- PEP (C)
  Embedded Linux Network Management Software.
- USB BP (C)
  The Linux USB BP Keyboard Driver
  (brief description because it has been described
  [elsewhere][penninckx:nfm:2012])
- SECURECHANGE (Java)
  (brief description because it has been described elsewhere)

An interesting thing found in the SECURECHANGE study was that,
despite previously having been verified using [Why/Krakatoa/Caduceus][filliatre:fem:2004]
bugs were found.
They say "Clearly, the tool used earlier was not sound or was not
used in a sound way."

This kind of case study paper is really useful because it gives some
insight into how to tackle an unverified piece of code.

- Start by adding pre/post-conditions of true/true to all functions.
  (This will gradually flush out some more realistic conditions.
- Create specifications of all the libraries used.
  One technique used was to use "gcc -E" to make a header file
  for all the system library imports and delete everything that
  is not used.
- Delay handling threads by initially specifying that
  "pthread_create" immediately calls its function argument
  and runs it until it terminates.

This was also useful because they document the amount of
annotation required in each case.

| Program      |  Language | loc   |  annotations | overhead | #bugs |
|:------------ | :-------- | ----: | -----------: | -------: | ----: |
| eID          |  Java     | 1004  | 684          | 68%      | 38    |
| SECURECHANGE |  Java     |  251  | 205          | 80%      | some  |
| PEP          |  C        |  429  | 450          | 105%     | 41    |
| USB BP       |  C        |  329  | 822          | 250%     | ?     |

Note that they also did some work on
[annotation inference][vogels:fmoods:2011]
and I don't think all the data reflects those improvements.
In the related work section, they suggest that other tools
such as
[VCC][cohen:cav:2010]
would not need as much annotation but at the expense of
less predictable search time.

{% include links.html %}
