---
ENTRYTYPE: article
abstract: 'Symbolic execution is a powerful technique for analyzing  program behavior, finding bugs, and generating tests, but  suffers from severely limited
  scalability: the largest  programs that can be symbolically executed today are on the  order of thousands of lines of code. To ensure feasibility  of
  symbolic execution, even small programs must curtail  their interactions with libraries, the operating system,  and hardware devices. This paper introduces
  selective  symbolic execution, a technique for creating the illusion  of full-system symbolic execution, while symbolically  running only the code that
  is of interest to the developer.  We describe a prototype that can symbolically execute  arbitrary portions of a full system, including  applications,
  libraries, operating system, and device  drivers. It seamlessly transitions back and forth between  symbolic and concrete execution, while transparently  converting
  system state from symbolic to concrete and back.  Our technique makes symbolic execution practical for large  software that runs in real environments,
  without requiring  explicit modeling of these environments.'
added: 2020-06-28
authors:
- Vitaly Chipounov
- Vlad Georgescu
- Cristian Zamfir
- George Candea
journal: Proceedings of the 5th Workshop on Hot Topics in System Dependability (HotDep)
layout: paper
link: http://infoscience.epfl.ch/record/139393
read: true
readings:
- 2020-06-28
title: Selective Symbolic Execution
url: http://infoscience.epfl.ch/record/139393
year: 2009
notes:
- symbolic execution
- KLEE verifier
- S2E verifier
papers:
---

The [S2E verifier] can analyze application code, complex GUI
libraries, kernel code, device drivers, and even hardware devices.
It does this by alternating between concrete execution (using QEMU) and
[symbolic execution] (using the [KLEE verifier]).
Switching modes makes it more flexible but it also makes it more efficient
because (slower) symbolic execution can be restricted to the code
of most interest which might be a library, a recently changed code path,
etc.

The big trick is switching from concrete execution to symbolic execution.

The evaluation is fairly sparse but they say they are able to analyze
device drivers in Windows with only a 1.7x slowdown relative to unmodified
QEMU.

{% include links.html %}
