Title: Complete information flow tracking from the gates up
Author: Mohit Tiwari, Hassan Wassel, Bita Mazloom, Shashidhar Mysore, Frederic Chong, Timothy Sherwood
Venue: ASPLOS
Year: 2009

Builds on ideas also described in [Theoretical analysis of gate-level information flow tracking](oberg:dac:2010.md) of adding "shadow circuits" that calculate whether each wire/flop in a processor depends on some initial set of untrusted values.
This paper describes a processor with automatically added shadow circuits.  The main problem is that conventional branching/looping means that if the PC becomes untrusted then all other state becomes untrusted in the next few cycles and if a pointer becomes untrusted, then all memory becomes untrusted after the next write through that pointer.  They solve this by, instead, providing predication, fixed iteration count loops and only allowing loop counters as address offsets.
The processor is 5 stages but is not pipelined.  They compare with NIOS-II and are 70% more gates (but not quite an apples-for-apples comparison).
The related work section covers previous hardware based security tracking features quite thoroughly because they claim to be the first processor of their type.