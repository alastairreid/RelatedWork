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

- [Controlling the What and Where of Declassification in Language-Based Security]({{ "papers/mantel:pls:2007" | relative_url }})
- [Declassification: Dimensions and Principles]({{ "papers/sabelfield:jcs:2009" | relative_url }})
- [Robust declassification]({{ "papers/zdancewic:csfw:2001" | relative_url }})
- [Enforcing robust declassification]({{ "papers/myers:csfw:2004" | relative_url }})


## Cryptography

Backlog:

- [Verifying constant-time implementations]({{ "papers/almeida:security:2016" | relative_url }})

## Operating Systems

Backlog:

- [Nickel: A Framework for Design and Verification of Information Flow Control Systems]({{ "papers/sigurbjarnarson:osdi:2018" | relative_url }})
- [Labels and Event Processes in the Asbestos Operating System]({{ "papers/efstathopoulos:sosp:2005" | relative_url }})
- [Making Information Flow Explicit in HiStar]({{ "papers/zeldovich:osdi:2006" | relative_url }})
- [The Flask Security Architecture: System Support for Diverse Security Policies]({{ "papers/spencer:security:1999" | relative_url }})
- Flume: [Information Flow Control for Standard OS Abstractions]({{ "papers/krohn:sosp:2007" | relative_url }})
- [seL4: from general purpose to a proof of information flow enforcement]({{ "papers/murray:secpriv:2013" | relative_url }})


## Languages

### Type-based information flow checking

Backlog:

- Myers


### Self-composition

- [Secure information flow by self-composition]({{ "papers/barthe:csfw:2004" | relative_url }})


## Hardware

Adding shadow logic to processors to precisely calculate whether each wire/flop is derived from untrusted values
[Complete information flow tracking from the gates up]({{ "papers/tiwari:asplos:2009" | relative_url }}).
And an analysis of how it scales
[Theoretical analysis of gate-level information flow tracking]({{ "papers/oberg:dac:2010" | relative_url }}).

SecVerilog extends Verilog with information flow labels and checks: [A hardware design language for timing-sensitive information-flow security]({{ "papers/zhang:asplos:2015" | relative_url }})
A preliminary report on a similar extension to Chisel:
[SecChisel: Language and Tool for Practical and Scalable Security Verification of Security-Aware Hardware Architectures]({{ "papers/deng:hasp:2019" | relative_url }})

Backlog:

- [HyperFlow: A Processor Architecture for Nonmalleable, Timing-Safe Information-Flow Security]({{ "papers/ferraiuolo:ccs:2018" | relative_url }})
- [Execution leases: A hardware-supported mechanism for enforcing strong non-interference]({{ "papers/tiwari:isca:2009" | relative_url }})


## Systems

A self-driving robot vehicle that combines Jif, HyperFlow, etc. into an integrated system: [Secure autonomous cyber-physical systems through verifiable information flow control]({{ "papers/liu:cpsspc:2018" | relative_url }})

## Quantitative

[Foundations of Quantitative Information Flow]({{ "papers/smith:fossacs:2009" | relative_url }})

# Backlog of papers to read

- [Goguen and Meseguer: Security policies and security models]({{ "papers/goguen:secpriv:1982" | relative_url }}) - fairly broad definition, often cited but, in practice, most people use specialised case (or later development by others)
- [Hyperproperties]({{ "papers/clarkson:jcs:2010" | relative_url }})
- [A Lattice Model of Secure Information Flow]({{ "papers/denning:cacm:1976" | relative_url }}) (many later works drop transitivity from definition)
- [Preserving information flow properties under refinement]({{ "papers/mantel:sp:2001" | relative_url }})
[Observational determinism for concurrent program security]({{ "papers/zdancewic:csfw:2003" | relative_url }})
- Probabilistic / Non-deterministic 
