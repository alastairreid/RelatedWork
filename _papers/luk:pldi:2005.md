---
ENTRYTYPE: inproceedings
abstract: 'Robust and powerful software instrumentation tools are essential for program analysis tasks such as profiling, performance evaluation, and bug
  detection. To meet this need, we have developed a new instrumentation system called Pin. Our goals are to provide easy-to-use, portable, transparent,
  and efficient instrumentation. Instrumentation tools (called Pintools) are written in C/C++ using Pin''s rich API. Pin follows the model of ATOM, allowing
  the tool writer to analyze an application at the instruction level without the need for detailed knowledge of the underlying instruction set. The API
  is designed to be architecture independent whenever possible, making Pintools source compatible across different architectures. However, a Pintool can
  access architecture-specific details when necessary. Instrumentation with Pin is mostly transparent as the application and Pintool observe the application''s
  original, uninstrumented behavior. Pin uses dynamic compilation to instrument executables while they are running. For efficiency, Pin uses several techniques,
  including inlining, register re-allocation, liveness analysis, and instruction scheduling to optimize instrumentation. This fully automated approach delivers
  significantly better instrumentation performance than similar tools. For example, Pin is 3.3x faster than Valgrind and 2x faster than DynamoRIO for basic-block
  counting. To illustrate Pin''s versatility, we describe two Pintools in daily use to analyze production software. Pin is publicly available for Linux
  platforms on four architectures: IA32 (32-bit x86), EM64T (64-bit x86), Itanium\textregistered , and ARM. In the ten months since Pin 2 was released in
  July 2004, there have been over 3000 downloads from its website.'
added: 2021-11-25
address: New York, NY, USA
authors:
- Chi-Keung Luk
- Robert Cohn
- Robert Muth
- Harish Patil
- Artur Klauser
- Geoff Lowney
- Steven Wallace
- Vijay Janapa Reddi
- Kim Hazelwood
booktitle: Proceedings of the 2005 ACM SIGPLAN Conference on Programming Language Design and Implementation
doi: 10.1145/1065010.1065034
isbn: '1595930566'
keywords: program analysis tools, instrumentation, dynamic compilation
layout: paper
link: https://doi.org/10.1145/1065010.1065034
location: Chicago, IL, USA
numpages: '11'
pages: 190-200
publisher: Association for Computing Machinery
read: false
readings: []
series: PLDI '05
title: 'Pin: Building customized program analysis tools with dynamic instrumentation'
url: https://doi.org/10.1145/1065010.1065034
year: 2005
notes:
- pin tool
- binary instrumentation
papers:
---
{% include links.html %}
