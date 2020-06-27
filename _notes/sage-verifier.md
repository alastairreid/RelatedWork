---
layout: note
title: SAGE verifier
notes:
- symbolic execution
- fuzz testing
papers:
---

SAGE is a [symbolic execution] tool used for whitebox [fuzz testing]
developed at Microsoft.
It is based on the "concolic" or "offline" variant of
"dynamic symbolic execution" and operates at the binary level
by symbolically executing x86 instructions.

SAGE schedules paths to optimize code coverage based on the likelihood of
a path to discover new, unexecuted instructions.

{% include links.html %}
