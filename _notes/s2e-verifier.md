---
layout: note
title: S2E verifier
notes:
- symbolic execution
- KLEE verifier
papers:
- chipounov:hotdep:2009
- chipounov:asplos:2011
- chipounov:tcs:2012
---

The S2E verifier is an implementation of the idea of "selective
symbolic execution" described in [chipounov:hotdep:2009].

The tool can analyze application code, complex GUI
libraries, kernel code, device drivers, and even hardware devices.
This allows it to analyze Windows kernel code.
It does this by alternating between concrete execution (using QEMU) and
[symbolic execution] (using the [KLEE verifier]).

{% include links.html %}
