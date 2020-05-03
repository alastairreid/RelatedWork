---
ENTRYTYPE: inproceedings
added: 2019-10-13
authors:
- Luke Nelson
- James Bornholt
- Ronghui Gu
- Andrew Baumann
- Emina Torlak
- Xi Wang
booktitle: Proceedings of the 27th ACM Symposium on Operating Systems Principles (SOSP)
doi: 10.1145/3341301.3359641
layout: paper
read: true
readings:
- 2019-10-15
title: Scaling symbolic evaluation for automated verification of systems code with Serval
year: 2019
topics:
- os
- security
- tools
- verification
notes:
- information-flow
- rosette-solver
- llvm-compiler
- riscv-architecture
- symbolic-evaluation
papers:
- nelson:sosp:2017
- sigurbjarnarson:osdi:2016
- sigurbjarnarson:osdi:2018
- demoura:tacas:2008
- torlak:pldi:2014
---

This paper continues the theme of "push-button automation" from the UNSAT group's earlier work on
[Hyperkernel][nelson:sosp:2017],
[Yggadrisil][sigurbjarnarson:osdi:2016]
and [Nickel][sigurbjarnarson:osdi:2018].
Like the earlier work, they are using the [Z3 SMT solver][demoura:tacas:2008] to verify systems code automatically 
and they are avoiding adding annotations ("auto-active verification") to help the verification 
by restricting the code they verify to "finite interfaces" so that all loops are bounded.
The big difference is that the earlier works wrote specifications in Python using the Z3Py library whereas this paper uses
[Rosette][torlak:pldi:2014]'s symbolic execution support.

They demonstrate the approach by porting Komodo and CertiKOS to RISC-V, rewriting the specs in Serval and reverifying their functional correctness and security properties on the binaries.  This process took an impressive 4 person-weeks each!
In addition, they created partial specifications of Linux BPF and the Keystone TEE and found bugs both in the artifacts they were verifying and in processors and other RISC-V specs.
(They also reveal that the CertiKOS verification excluded verification of the ELF loader.  Interesting omission.)

The basic idea in Serval is to write an interpreter for an instruction set (eg RISC-V, BPF, ...) and then lift this interpreter to create a symbolic execution engine (requires some annotations and performance tuning).  This symbolic execution engine generates SMT that is fed to Z3. Serval includes libraries for specifying non-interference and state-machine refinement.

Serval is impressively small: 4400 lines for Serval + RISC-V (subset) + x86-32 (subset) + LLVM (subset) + BPF.  That is tiny!

{% include links.html %}
