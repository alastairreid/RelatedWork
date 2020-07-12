---
ENTRYTYPE: inbook
abstract: Vx86 is the first static analyzer for sequential Intel x86 assembler code using automated deductive verification. It proves the correctness of
  assembler code against function contracts, which are expressed in terms of pre-, post-, and frame conditions using first-order predicates. Vx86 takes
  the annotated assembler code, translates it into C code simulating the processor, and then uses an existing C verifier to either prove the correctness
  of the assembler program or find errors in it. First experiments on applying Vx86 on the Windows Hypervisor code base are encouraging. Vx86 verified the
  Windows Hypervisor's memory safety, arithmetic safety, call safety and interrupt safety.
added: 2019-07-02
address: Berlin, Heidelberg
authors:
- Stefan Maus
- Michał Moskal
- Wolfram Schulte
booktitle: 'Algebraic Methodology and Software Technology: 12th International Conference, AMAST 2008 Urbana, IL, USA, July 28-31, 2008 Proceedings'
doi: 10.1007/978-3-540-79980-1_22
isbn: 978-3-540-79980-1
layout: paper
pages: 284-298
publisher: Springer
read: false
readings: []
title: 'Vx86: x86 Assembler Simulated in C Powered by Automated Theorem Proving'
year: 2008
notes:
---
