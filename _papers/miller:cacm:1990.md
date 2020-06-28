---
ENTRYTYPE: article
added: 2020-06-23
address: New York, NY, USA
authors:
- Barton P. Miller
- Louis Fredriksen
- Bryan So
doi: 10.1145/96267.96279
issn: 0001-0782
issue_date: Dec. 1990
journal: Communications of the ACM
layout: paper
link: https://doi.org/10.1145/96267.96279
month: December
number: '12'
numpages: '13'
pages: 32-44
publisher: Association for Computing Machinery
read: true
readings:
- 2020-06-28
title: An empirical study of the reliability of UNIX utilities
url: https://doi.org/10.1145/96267.96279
volume: '33'
year: 1990
notes:
- fuzz testing
papers:
---

This is the paper that started the field of [fuzz testing], coined
the name, and tells the origin story.

> On a  dark and stormy night one of the  authors was logged on to his
> workstation on a dial-up line from home and the rain had affected the phone
> lines; there were frequent spurious characters on the line.  The author had to
> race to see if he could type a sensible sequence of characters before the noise
> scrambled the command. This line noise was not surprising; but we were
> surprised that these spurious characters were causing programs to crash.

They went on to test almost 90 Unix utilities on seven versions of Unix
using by piping random characters into them and found that 24% of them
failed.

The programs failed for a range of reasons that is depressingly familiar
30 years later

- buffer overflow errors
- dereferencing null and invalid pointers
- not checking return codes
- not using bounds with fscanf
- invoking vulnerable programs as subprocesses
- using user-input as the first argument to printf
- bugs in error handling code
- assuming 'char' is unsigned
- race conditinos with signal handlers

As one would expect, the biggest source was buffer overflows, pointer
dereferences and input errors (e.g., fscanf).

The paper also makes recommendations, suggests that the way Unix was developed
and the fact that it is easier to work round a bug than to report it makes
these bugs common.
They report that their "jigs" (fuzzing harnesses) are available for others to
try using.

Although they compare with traditional testing, they make a surprising number
of references to formal verification such as

> ... our simple testing technique has discovered a wealth of errors and is
> likely to be more commonly used (at least in the near term) than more formal
> procedures.


{% include links.html %}
