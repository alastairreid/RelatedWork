---
ENTRYTYPE: inproceedings
abstract: 'Binary lifting and recompilation allow a wide range of install-time program transformations, such as security hardening, deobfuscation, and reoptimization.
  Existing binary lifting tools are based on static disassembly and thus have to rely on heuristics to disassemble binaries.In this paper, we present BinRec,
  a new approach to heuristic-free binary recompilation which lifts dynamic traces of a binary to a compiler-level intermediate representation (IR) and
  lowers the IR back to a "recovered" binary. This enables BinRec to apply rich program transformations, such as compiler-based optimization passes, on
  top of the recovered representation. We identify and address a number of challenges in binary lifting, including unique challenges posed by our dynamic
  approach. In contrast to existing frameworks, our dynamic frontend can accurately disassemble and lift binaries without heuristics, and we can successfully
  recover obfuscated code and all SPEC INT 2006 benchmarks including C++ applications. We evaluate BinRec in three application domains: i) binary reoptimization,
  ii) deobfuscation (by recovering partial program semantics from virtualization-obfuscated code), and iii) binary hardening (by applying existing compiler-level
  passes such as AddressSanitizer and SafeStack on binary code).'
added: 2021-11-25
address: New York, NY, USA
articleno: '36'
authors:
- Anil Altinay
- Joseph Nash
- Taddeus Kroes
- Prabhu Rajasekaran
- Dixin Zhou
- Adrian Dabrowski
- David Gens
- Yeoul Na
- Stijn Volckaert
- Cristiano Giuffrida
- Herbert Bos
- Michael Franz
booktitle: Proceedings of the Fifteenth European Conference on Computer Systems
doi: 10.1145/3342195.3387550
isbn: '9781450368827'
layout: paper
link: https://doi.org/10.1145/3342195.3387550
location: Heraklion, Greece
numpages: '16'
publisher: Association for Computing Machinery
read: false
readings: []
series: EuroSys '20
title: 'BinRec: Dynamic binary lifting and recompilation'
url: https://doi.org/10.1145/3342195.3387550
year: 2020
notes:
- binary lifter
- LLVM compiler
- binary analysis
- QEMU
- KLEE verifier
papers:
---
{% include links.html %}
