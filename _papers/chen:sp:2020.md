---
ENTRYTYPE: inproceedings
added: 2021-06-03
authors:
- Yaohui Chen
- Peng Li
- Jun Xu
- Shengjian Guo
- Rundong Zhou
- Yulong Zhang
- Tao Wei
- Long Lu
booktitle: 2020 IEEE Symposium on Security and Privacy (SP)
doi: 10.1109/SP40000.2020.00002
layout: paper
number: ''
pages: 1580-1596
read: false
readings: []
title: 'SAVIOR: Towards bug-driven hybrid testing'
volume: ''
year: 2020
notes:
- fuzz testing
- hybrid testing
- concolic execution
- symbolic execution
- SAVIOR
- KLEE verifier
- AFL fuzzer
- QSYM
- Driller verifier
papers:
---

[SAVIOR] is a [hybrid testing] tool that prioritizes bug-finding over
coverage by using a pre-testing analysis that identifies code of interest
(i.e., potentially containing bugs) and prioritizes code paths leading to that
code.
It combines [KLEE][KLEE verifier] and [AFL fuzzer].

Each seed is scored according using a combination of this static information
and runtime information by counting how many distinct UBSan labels are reachable along
variants of the path that take unexplored branches weighted by the inverse of
how many attempts Savior has made to solve those branches.

> This scoring method is to ensure that SAVIOR always prioritizes seeds leading
> to more unverified bugs, while in the long run it would not trap into those with
> hard-to-solve branch conditions.

To handle function pointers, they use Andersen's points-to-analysis.

KLEE is somehow used as a  [concolic execution] tool -- I am not completely
clear how this works or whether it uses as modified version of KLEE.
They also add partial C++ support to KLEE.

Evaluation compares against [AFL fuzzer], AFLGo, TFuzz, Angora, [Driller verifier],
and [QSYM] using LAVA-M and some real-world libraries (libpcap, libtiff, binutils, libxml2,
libjpeg and jasper).

> On average, SAVIOR discovers vulnerabilities 43.4% faster than DRILLER
> and 44.3% faster than QSYM.

To gain further insight, they look at how quickly the different tools 
find UBSan labels in the code.


{% include links.html %}
