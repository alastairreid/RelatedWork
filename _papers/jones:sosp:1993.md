---
ENTRYTYPE: inproceedings
abstract: 'Many contemporary operating systems utilize a system call interface between the operating system and its clients. Increasing numbers of systems
  are providing low-level mechanisms for intercepting and handling system calls in user code. Nonetheless, they typically provide no higher-level tools
  or abstractions for effectively utilizing these mechanisms. Using them has typically required reimplementation of a substantial portion of the system
  interface from scratch, making the use of such facilities unwieldy at best.This paper presents a toolkit that substantially increases the ease of interposing
  user code between clients and instances of the system interface by allowing such code to be written in terms of the high-level objects provided by this
  interface, rather than in terms of the intercepted system calls themselves. This toolkit helps enable new interposition agents to be written, many of
  which would not otherwise have been attempted.This toolkit has also been used to construct several agents including: system call tracing tools, file reference
  tracing tools, and customizable filesystem views. Examples of other agents that could be built include: protected environments for running untrusted binaries,
  logical devices implemented entirely in user space, transparent data compression and/or encryption agents, transactional software environments, and emulators
  for other operating system environments.'
added: 2023-02-21
authors:
- Mike Jones
booktitle: SOSP '93 Proceedings of the fourteenth ACM symposium on Operating systems principles
edition: SOSP \textquotesingle 93 Proceedings of the fourteenth ACM symposium on Operating systems principles
layout: paper
link: https://www.microsoft.com/en-us/research/publication/interposition-agents-transparently-interposing-user-code-system-interface/
month: December
publisher: ACM
read: true
readings:
- 1998-01-01
title: 'Interposition agents: transparently interposing user code at the system interface'
url: https://www.microsoft.com/en-us/research/publication/interposition-agents-transparently-interposing-user-code-system-interface/
year: 1993
notes:
- operating systems
- module system
papers:
---
{% include links.html %}
