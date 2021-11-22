---
layout: note
title: CHERI architecture
logo: https://www.cl.cam.ac.uk/research/security/ctsrd/cheri/
notes:
- capabilities
- instruction set architecture
papers:
- skorstengaard:esop:2018
- skorstengaard:popl:2019
- nienhuis:secpriv:2020
- woodruff:isca:2014
- watson:sandp:2015
---

CHERI is an [instruction set architecture] based on providing hardware
support for [capabilities].
In particular, CHERI separates protection checks from virtual memory.

The basic CHERI design in [woodruff:isca:2014] tackled spatial safety but left
a hole wrt temporal safety. That is, capabilities could be used to protect
a region of memory but there was no way to revoke a capability.
This was addressed in later papers.

{% include links.html %}
