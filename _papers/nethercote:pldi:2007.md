---
ENTRYTYPE: inproceedings
abstract: Dynamic binary instrumentation (DBI) frameworks make it easy to build dynamic binary analysis (DBA) tools such as checkers and profilers. Much
  of the focus on DBI frameworks has been on performance; little attention has been paid to their capabilities. As a result, we believe the potential of
  DBI has not been fully exploited.In this paper we describe Valgrind, a DBI framework designed for building heavyweight DBA tools. We focus on its unique
  support for shadow values-a powerful but previously little-studied and difficult-to-implement DBA technique, which requires a tool to shadow every register
  and memory value with another value that describes it. This support accounts for several crucial design features that distinguish Valgrind from other
  DBI frameworks. Because of these features, lightweight tools built with Valgrind run comparatively slowly, but Valgrind can be used to build more interesting,
  heavyweight tools that are difficult or impossible to build with other DBI frameworks such as Pin and DynamoRIO.
added: 2021-11-22
address: New York, NY, USA
authors:
- Nicholas Nethercote
- Julian Seward
booktitle: Proceedings of the 28th ACM SIGPLAN Conference on Programming Language Design and Implementation
doi: 10.1145/1250734.1250746
isbn: '9781595936332'
keywords: dynamic binary analysis, Memcheck, dynamic binary instrumentation, Valgrind, shadow values
layout: paper
link: https://doi.org/10.1145/1250734.1250746
location: San Diego, California, USA
numpages: '12'
pages: 89-100
publisher: Association for Computing Machinery
read: false
readings: []
series: PLDI '07
title: 'Valgrind: A framework for heavyweight dynamic binary instrumentation'
url: https://doi.org/10.1145/1250734.1250746
year: 2007
notes:
- binary instrumentation
- Valgrind tool
papers:
- shoshitaishvili:sp:2016
---
{% include links.html %}
