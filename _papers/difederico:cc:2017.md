---
ENTRYTYPE: inproceedings
abstract: 'Static binary analysis is a key tool to assess the security of third-party binaries and legacy programs. Most forms of binary analysis rely on
  the availability of two key pieces of information: the program''s control-flow graph and function boundaries. However, current tools struggle to provide
  accurate and precise results, in particular when dealing with hand-written assembly functions and non-trivial control-flow transfer instructions, such
  as tail calls. In addition, most of the existing solutions are ad-hoc, rely on hand-coded heuristics, and are tied to a specific architecture. In this
  paper we highlight the challenges faced by an architecture agnostic static binary analysis framework to provide accurate information about a program''s
  CFG and function boundaries without employing debugging information or symbols. We propose a set of analyses to address predicate instructions, noreturn
  functions, tail calls, and context-dependent CFG. rev.ng, our binary analysis framework based on QEMU and LLVM, handles all the 17 architectures supported
  by QEMU and produces a compilable LLVM IR. We implement our described analyses on top of LLVM IR. In an extensive evaluation, we test our tool on binaries
  compiled for MIPS, ARM, and x86-64 using GCC and clang and compare them to the industry''s state of the art tool, IDA Pro, and two well-known academic
  tools, BAP/ByteWeight and angr. In all cases, the quality of the CFG and function boundaries produced by rev.ng is comparable to or improves over the
  alternatives.'
added: 2021-11-25
address: New York, NY, USA
authors:
- Alessandro Di Federico
- Mathias Payer
- Giovanni Agosta
booktitle: Proceedings of the 26th International Conference on Compiler Construction
doi: 10.1145/3033019.3033028
isbn: '9781450352338'
keywords: control-flow graph recovery, static binary analysis, function boundary detection
layout: paper
link: https://doi.org/10.1145/3033019.3033028
location: Austin, TX, USA
numpages: '11'
pages: 131-141
publisher: Association for Computing Machinery
read: false
readings: []
series: CC 2017
title: 'Rev.Ng: A unified binary analysis framework to recover CFGs and function boundaries'
url: https://doi.org/10.1145/3033019.3033028
year: 2017
notes:
- binary lifter
- binary analysis
- reverse engineering
- revng-tool
- QEMU
- TCG IR
- LLVM compiler
papers:
---
{% include links.html %}
