---
ENTRYTYPE: inproceedings
added: 2019-10-06
address: Berkeley, CA, USA
authors:
- Ray Spencer
- Stephen Smalley
- Peter Loscocco
- Mike Hibler
- David Andersen
- Jay Lepreau
booktitle: Proceedings of the 8th Conference on USENIX Security Symposium
layout: paper
location: Washington, D.C.
numpages: '1'
pages: 11-11
publisher: USENIX Association
read: true
readings:
- 2019-10-06
series: SSYM'99
title: 'The Flask security architecture: System support for diverse security policies'
year: 1999
topics:
- information-flow
- os
---

This paper by some of my former colleagues in the [Flux group at the University of Utah](https://www.flux.utah.edu) describes the Flask microkernel-based operating system.
Like its successor SE-Linux, Flask adds fine-grained protection checks into the operating system and separates mechanism from policy by making decisions in a separate policy module that is free to implement whatever policy you want.  That is, you are not stuck with whatever Linux or Windows or ... provides by default.

The paper emphasises the importance of being able to control the propagation of a permission once it has been granted and of being able to revoke a permission (including aborting any in-flight operations that depend on the permission).  These are key differences from capability systems.

The design is implemented in the Fluke micro kernel but they emphasise that it is broadly applicable. (Part of their mechanism allows for delegation to allow a server to act on behalf of several different clients using the permissions of those clients.  It is not clear to me whether that would be as easy in a monolithic kernel.)
For performance reasons, they cache permissions.

The gap in the story is that creating policies and ensuring that the set of checks you implement implements your desired policy is quite hard.  This gap was tackled in a succession of other OSes such as
[Asbestos]({{ "papers/efstathopoulos:sosp:2005" | relative_url }}),
[HiStar]({{ "papers/zeldovich:osdi:2006" | relative_url }}) 
and
[Flume]({{ "papers/krohn:sosp:2007" | relative_url }}).

_Personal note: I joined the Flux group as Flask was being completed.  I think part of the plan was that I would work on creating a policy language for Flask.  Alas, I had no idea how to tackle this problem so I worked on component-based operating systems instead._
