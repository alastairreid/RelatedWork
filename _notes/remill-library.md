---
layout: note
notes:
- McSema tool
- XED tool
- LLVM compiler
- ISA specification
- binary lifter
- x86 architecture
- Arm architecture
papers:
- dasgupta:pldi:2020
logo: https://github.com/lifting-bits/remill/raw/master/docs/images/remill_logo.png
url: https://github.com/lifting-bits/remill
title: Remill binary lifting library
---

Remill is a static binary translator that translates machine code instructions
into [LLVM][LLVM compiler] bitcode. It translates AArch64 (64-bit ARMv8), SPARC32 (SPARCv8),
SPARC64 (SPARCv9), x86 and amd64 machine code (including AVX and AVX512) into
LLVM bitcode. AArch32 (32-bit ARMv8 / ARMv7) support is underway.

Uses [XED tool] for disassembly on [x86 architecture].

{% include links.html %}
