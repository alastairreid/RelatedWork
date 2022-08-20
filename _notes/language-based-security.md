---
layout: note
title: Language based security
notes:
- information flow
- non-interference
- security
- microarchitecture
- side-channel
- speculative execution
papers:
- guarnieri:sandp:2020
- cauligi:sandp:2022
---

An approach to defining security problems based on techniques from
the programming language community including defining a formal operational
semantics, leakage models based on that semantics and policies.

[cauligi:sandp:2022] follows the approach in [guarnieri:sandp:2020] of defining

- An execution model - a formal operational semantics

  - ⟦ ⟧<sup>seq</sup> (sequential execution),
  - ⟦ ⟧<sup>pht</sup> (conditional branch prediction),
  - ⟦ ⟧<sup>pht-stl</sup> (branch prediction),
  - ⟦ ⟧<sup>pbrs</sup> (branch prediction),


- A leakage observation model
  that defines what information is visible to attackers.

  This adds traces to the execution model

  - ⟦ ⟧<sub>ct</sub> adds traces of control flow and memory addresses
  - ⟦ ⟧<sub>mem</sub>
  - ⟦ ⟧<sub>arch</sub> adds traces of all register values (or, equivalently, values loaded from memory and their addresses)

    [cauligi:sandp:2022] labels subsets of architecture state as follows

    - P: path
    - B: speculation rollbacks
    - M: memory addresses
    - C: cache lines / cache state
    - L: values loaded from memory
    - R: values in registers
    - S: branch predictor state
    - T: timer

  Leakage models form a partial order: some models leak strictly more than others.

  ⟦ ⟧<sub>arch</sub> is useful for reasoning about software isolation.

- Contracts are based on pairs of execution models and leakage models.
  For example the contract
  ⟦⟧<span class="supsub"><span>seq</span><span>ct</span></span>
  which has been heavily used in the crypto community
  is based on secrets not influencing branches and secrets
  not influencing addresses.

- Policies π are defined by equivalence relations ≃<sub>π</sub>
  over states that compares public values in the states.

  For example, a policy may be based on a range of memory addresses
  that can be observed or some bits of the addresses (those that influence
  what cache line is accessed).

A program satisfies non-interference if, for any two π-equivalent initial states,
an attacker cannot distinguish the two resulting leakage traces.

{% include links.html %}
