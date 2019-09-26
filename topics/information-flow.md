# Information Flow

A distinction is often made before "explicit" information flow (e.g., "x = y;") and "implicit" information flow (e.g., "if y then x = 1;" which has an information flow from y to x even if y is False).  This distinction reflects a classic weakness of taint tracking approaches that dynamically tag values with metadata during an execution and, because they are based on a single execution, are unable to accurately track information flows in the paths that are not executed.

Backlog:

- Goguen and Meseguer; non-interference - fairly broad definition, often cited but, in practice, most people use specialised case (or later development by others)
- Goguen and Meseguer: [Unwinding and inference control](../papers/goguen:secpriv:1984.md)
- ?? And Schneider: Hyperproperties
- Denning: lattice (many later works drop transitivity from definition)
- Mantel: Preserving information flow properties under refinement
- Observational Determinism
- Rushby: non-interference


## Declassification

Declassification~\cite{MantelReinhard:WhatWhereDeclassify:2007}
Declassification dimensions~\cite{SabelfeldSands:DeclassificationDimensions:2009}
Robust declassification~\cite{ZdancewicMyers:RobustDeclassification:2001}
Myers~\cite{Myers+:EnforcingRobustDeclassification:2004}


## Cryptography

Backlog:

- Barthe: self-composition
- Almeida: verifying constant-time

## Operating Systems

Backlog:

- Nickel
- Asbestos
- HiStar
- Flask
- Flume
- seL4 non-interference proof

Flask~\cite{Spencer:1999:FSA:1251421.1251432}
Asbestos~\cite{Efstathopoulos:2005:LEP:1095810.1095813}
HiStar~\cite{Zeldovich:2006:MIF:1298455.1298481}
Flume~\cite{Krohn:2007:IFC:1294261.1294293}
Nickel~\cite{DBLP:conf/osdi/Sigurbjarnarson18}

## Languages

Backlog:

- Myers


## Hardware

Adding shadow logic to processors to precisely calculate whether each wire/flop is derived from untrusted values
[Complete information flow tracking from the gates up](../papers/tiwari:asplos:2009.md).
And an analysis of how it scales
[Theoretical analysis of gate-level information flow tracking](../papers/oberg:dac:2010.md).

Backlog:

- SecChisel
- Hyperflow
- Zhang: 
- [Secure autonomous cyber-physical systems through verifiable information flow control](../papers/liu:cpsspc:2018.md)
- Execution leases: a hardware-supported mechanism for enforcing strong non-interference, Micro, 2009


## Quantitative

[Foundations of Quantitative Information Flow](../papers/smith:fossacs:2009.md)

Backlog:

- Probabilistic / Non-deterministic 