---
ENTRYTYPE: article
abstract: 'Conventional computer engineering relies on test-and-debug development processes, with the behavior of common interfaces described (at best)
  with prose specification documents. But prose specifications cannot be used in test-and-debug development in any automated way, and prose is a poor medium
  for expressing complex (and loose) specifications.The TCP/IP protocols and Sockets API are a good example of this: they play a vital role in modern communication
  and computation, and interoperability between implementations is essential. But what exactly they are is surprisingly obscure: their original development
  focused on "rough consensus and running code," augmented by prose RFC specifications that do not precisely define what it means for an implementation
  to be correct. Ultimately, the actual standard is the de facto one of the common implementations, including, for example, the 15&nbsp;000 to 20&nbsp;000
  lines of the BSD implementation-optimized and multithreaded C code, time dependent, with asynchronous event handlers, intertwined with the operating system,
  and security critical.This article reports on work done in the Netsem project to develop lightweight mathematically rigorous techniques that can be applied
  to such systems: to specify their behavior precisely (but loosely enough to permit the required implementation variation) and to test whether these specifications
  and the implementations correspond with specifications that are executable as test oracles. We developed post hoc specifications of TCP, UDP, and the
  Sockets API, both of the service that they provide to applications (in terms of TCP bidirectional stream connections) and of the internal operation of
  the protocol (in terms of TCP segments and UDP datagrams), together with a testable abstraction function relating the two. These specifications are rigorous,
  detailed, readable, with broad coverage, and rather accurate. Working within a general-purpose proof assistant (HOL4), we developed language idioms (within
  higher-order logic) in which to write the specifications: operational semantics with nondeterminism, time, system calls, monadic relational programming,
  and so forth. We followed an experimental semantics approach, validating the specifications against several thousand traces captured from three implementations
  (FreeBSD, Linux, and WinXP). Many differences between these were identified, as were a number of bugs. Validation was done using a special-purpose symbolic
  model checker programmed above HOL4.Having demonstrated that our logic-based engineering techniques suffice for handling real-world protocols, we argue
  that similar techniques could be applied to future critical software infrastructure at design time, leading to cleaner designs and (via specification-based
  testing) more robust and predictable implementations. In cases where specification looseness can be controlled, this should be possible with lightweight
  techniques, without the need for a general-purpose proof assistant, at relatively little cost.'
added: 2021-11-05
address: New York, NY, USA
articleno: '1'
authors:
- Steve Bishop
- Matthew Fairbairn
- Hannes Mehnert
- Michael Norrish
- Tom Ridge
- Peter Sewell
- Michael Smith
- Keith Wansbrough
doi: 10.1145/3243650
issn: 0004-5411
issue_date: January 2019
journal: J. ACM
keywords: specification, Rigorous engineering, network protocols
layout: paper
link: https://doi.org/10.1145/3243650
month: December
number: '1'
numpages: '77'
publisher: Association for Computing Machinery
read: false
readings: []
title: 'Engineering with logic: Rigorous test-oracle specification and validation for TCP/IP and the sockets API'
url: https://doi.org/10.1145/3243650
volume: '66'
year: 2018
notes:
- ISA specification
papers:
---
{% include links.html %}
