---
layout: topic
title: Information flow
---

Information flow checks are a form of security checks that track where
information is flowing from and to and under which circumstances.
It can be performed as a dynamic check on a single execution ("taint tracking")
or as a static analysis that typically compares results on two or more
executions.

A distinction is often made before "explicit" information flow (e.g., "x = y;")
and "implicit" information flow (e.g., "if y then x = 1;" which has an
information flow from y to x even if y is False).  This distinction reflects
a classic weakness of taint tracking approaches that dynamically tag values
with metadata during an execution and, because they are based on a single
execution, are unable to accurately track information flows in the paths that
are not executed.

## Declassification

Backlog:

- [Controlling the What and Where of Declassification in Language-Based Security]({% link _papers/mantel:pls:2007.md %})
- [Declassification: Dimensions and Principles]({% link _papers/sabelfield:jcs:2009.md %})
- [Robust declassification]({% link _papers/zdancewic:csfw:2001.md %})
- [Enforcing robust declassification]({% link _papers/myers:csfw:2004.md %})


## Cryptography

Backlog:

- [Secure information flow by self-composition]({% link _papers/barthe:mscs:2011.md %})
- [Verifying constant-time implementations]({% link _papers/almeida:security:2016.md %})

## Operating Systems

Backlog:

- [Nickel: A Framework for Design and Verification of Information Flow Control Systems]({% link _papers/sigurbjarnarson:osdi:2018.md %})
- [Labels and Event Processes in the Asbestos Operating System]({% link _papers/efstathopoulos:sosp:2005.md %})
- [Making Information Flow Explicit in HiStar]({% link _papers/zeldovich:osdi:2006.md %})
- [The Flask Security Architecture: System Support for Diverse Security Policies]({% link _papers/spencer:security:1999.md %})
- Flume: [Information Flow Control for Standard OS Abstractions]({% link _papers/krohn:sosp:2007.md %})
- [seL4: from general purpose to a proof of information flow enforcement]({% link _papers/murray:secpriv:2013.md %})


## Languages

Backlog:

- Myers


## Hardware

Adding shadow logic to processors to precisely calculate whether each wire/flop is derived from untrusted values
[Complete information flow tracking from the gates up]({% link _papers/tiwari:asplos:2009.md %}).
And an analysis of how it scales
[Theoretical analysis of gate-level information flow tracking]({% link _papers/oberg:dac:2010.md %}).

SecVerilog extends Verilog with information flow labels and checks: [A hardware design language for timing-sensitive information-flow security]({% link _papers/zhang:asplos:2015.md %})
A preliminary report on a similar extension to Chisel:
[SecChisel: Language and Tool for Practical and Scalable Security Verification of Security-Aware Hardware Architectures](_papers/deng:hasp:2019.md)

Backlog:

- [HyperFlow: A Processor Architecture for Nonmalleable, Timing-Safe Information-Flow Security]({% link _papers/ferraiuolo:ccs:2018.md %})
- [Execution leases: A hardware-supported mechanism for enforcing strong non-interference]({% link _papers/tiwari:isca:2009.md %})


## Systems

A self-driving robot vehicle that combines Jif, HyperFlow, etc. into an integrated system: [Secure autonomous cyber-physical systems through verifiable information flow control]({% link _papers/liu:cpsspc:2018.md %})

## Quantitative

[Foundations of Quantitative Information Flow]({% link _papers/smith:fossacs:2009.md %})

# Backlog of papers to read

- [Goguen and Meseguer: Security policies and security models]({% link _papers/goguen:secpriv:1982.md %}) - fairly broad definition, often cited but, in practice, most people use specialised case (or later development by others)
- [Hyperproperties]({% link _papers/clarkson:jcs:2010.md %})
- [A Lattice Model of Secure Information Flow]({% link _papers/denning:cacm:1976.md %}) (many later works drop transitivity from definition)
- [Preserving information flow properties under refinement]({% link _papers/mantel:sp:2001.md %})
[Observational determinism for concurrent program security]({% link _papers/zdancewic:csfw:2003.md %})
- Probabilistic / Non-deterministic 
