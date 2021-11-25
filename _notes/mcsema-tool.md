---
layout: note
notes:
- remill library
- LLVM compiler
- ISA specification
- binary lifter
- binary analysis
- reverse engineering
papers:
- dasgupta:pldi:2020
title: McSema binary lifter
url: https://github.com/lifting-bits/mcsema
logo: https://raw.githubusercontent.com/lifting-bits/mcsema/master/docs/images/mcsema_logo.png
---

McSema is an executable lifter.
It translates ("lifts") executable binaries from native machine code to LLVM bitcode.
It uses the [Remill library] for disassembly and binary lifting of individual instructions.
It uses IDAPro for control-flow graph (CFG) recovery.

[Slides](https://recon.cx/2014/slides/McSema.pdf)

{% include links.html %}
