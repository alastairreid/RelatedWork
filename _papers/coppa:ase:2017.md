---
ENTRYTYPE: inproceedings
abstract: Symbolic execution is a popular program analysis technique that allows seeking for bugs by reasoning over multiple alternative execution states
  at once. As the number of states to explore may grow exponentially, a symbolic executor may quickly run out of space. For instance, a memory access to
  a symbolic address may potentially reference the entire address space, leading to a combinatorial explosion of the possible resulting execution states.
  To cope with this issue, state-of-the-art executors concretize symbolic addresses that span memory intervals larger than some threshold. Unfortunately,
  this could result in missing interesting execution states, e.g., where a bug arises. In this paper we introduce MEMSIGHT, a new approach to symbolic memory
  that reduces the need for concretization, hence offering the opportunity for broader state explorations and more precise pointer reasoning. Rather than
  mapping address instances to data as previous tools do, our technique maps symbolic address expressions to data, maintaining the possible alternative
  states resulting from the memory referenced by a symbolic address in a compact, implicit form. A preliminary experimental investigation on prominent benchmarks
  from the DARPA Cyber Grand Challenge shows that MemSight enables the exploration of states unreachable by previous techniques.
added: 2021-03-18
authors:
- Emilio Coppa
- Daniele Cono D'Elia
- Camil Demetrescu
booktitle: 2017 32nd IEEE/ACM International Conference on Automated Software Engineering (ASE)
doi: 10.1109/ASE.2017.8115671
issn: ''
keywords: program debugging;program diagnostics;program testing;program verification;symbolic execution;symbolic executor;memory access;span memory intervals;symbolic
  memory;address instances;bugs;address space;execution states;program analysis technique;pointer reasoning;symbolic address expressions;Concrete;Weapons;Cognition;Indexes;Merging;Load
  modeling;Computer bugs
layout: paper
month: Oct
number: ''
pages: 613-618
read: true
readings:
- 2021-03-18
title: Rethinking pointer reasoning in symbolic execution
volume: ''
year: 2017
notes:
- symbolic execution
- angr verifier
- symbolic memory
papers:
- avgerinos:icse:2014
- cha:sandp:2012
- trtik:atva:2014
- stephens:ndss:2016
- david:issta:2016
---

Symbolic addresses (and array indices) are a problem for symbolic execution
that could lead to a large explosion in SMT terms due to the need to add
an 'ite' expression for every potentially aliasing write.
Many symbolic execution tools deal with this by selectively concretizing
addresses used for reads, for writes or for both -- leading to lower coverage
of the program (i.e., unsound results).

This paper proposes an efficient structure for tracking writes to symbolic addresses
that does not limit their range (as in [angr][angr verifier]) and can
support state merging (as in Veritesting [avgerinos:icse:2014]).

The base implementation represents memory as a set of tuples (e, v, t, delta)
representing a store to address e of value v
at time t under condition delta.
(e, v and delta are all symbolic, t is concrete virtual time).

- Stores add (e,v,t,true) and increment virtual time.
- Loads construct an ite expression starting with the oldest stores.
- Merges conjoin deltas and increment virtual time to the max of the two paths.

They apply many optimizations to make this scale.

- The ite-construction during a load can be terminated if an exact match
  is found.

- Range calculations are used to limit the number of stores
  considered during a load.

- Multiple stores to the same address can be garbage collected.

- A trick for uninitialized memory involving negative virtual time.

- The memory is organized as bytes and multi-byte accesses are
  split/joined as required.

- An interval tree is used to efficiently find stored intervals
  that overlap with a read/write.

- The interval tree is paged to support efficient copy-on-write
  operations and each tuple is contained in exactly one page.
  Page size is determined empirically.

- Writes to concrete addresses (the majority af accesses) are
  stored in a separate structure that maps concrete addresses
  to a pair of a symbolic value and a timestamp.
  (This is a paged hashmap to support efficient copy-on-write.)

This was implemented as a plugin to [angr][angr verifier] (which already had a modular
structure).

This was evaluated on the Cromulence (CROMU) group from the Cyber Grand Challenge
by comparing with three different configurations of angr:
fully concrete, symbolic within bounded address ranges (default angr) and
fully symbolic but without all the tricks mentioned above.
They run for 2 hours with 32GB RAM in what sounds like a breadth-first exploration.
They are interested in how many paths are discarded due to concretization (in the standard angr)
and whether tools timeout due to excessive size of symbolic expressions.

Results show that

- the more symbolic the treatment of addresses the more paths found
- their optimizations avoid timeouts

They suggest a number of ways to improve it in the future using ideas
from MAYHEM [cha:sandp:2012] and others.

{% include links.html %}
