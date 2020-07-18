---
ENTRYTYPE: article
added: 2020-05-12
address: New York, NY, USA
articleno: '21'
authors:
- Ranjit Jhala
- Rupak Majumdar
doi: 10.1145/1592434.1592438
issn: 0360-0300
issue_date: October 2009
journal: ACM Computing Surveys
keywords: abstraction, counterexample-guided refinement, liveness, safety, enumerative and symbolic model checking, Software model checking
layout: paper
link: https://doi.org/10.1145/1592434.1592438
month: October
number: '4'
numpages: '54'
publisher: Association for Computing Machinery
read: true
readings:
- 2020-07-16
title: Software model checking
url: https://doi.org/10.1145/1592434.1592438
volume: '41'
year: 2009
notes:
- survey
- model checking
- bounded model checking
- partial order reduction
- symbolic evaluation
- symbolic execution
- symbolic model checking
- reachability
- separation logic
- alias analysis
- shape analysis
- temporal logic
- buchi automaton
- kripke structure
- BDD
- CEGAR
- BLAST verifier
- CBMC verifier
- KLEE verifier
papers:
---

This 2009 [survey] of software [model checking] covers a lot of
ground from the roots in hardware model checking through to its
application to software.
A number of the key algorithms are described in pseudocode.

The sections give a good sense of what is covered

- Introduction
- Preliminary definitions
  - Simple programs
  - Properties
  - Organization
- Concrete enumerative model checking

  (For small, finite state spaces)
  - Stateful search

    Forward and backward algorithms,
    [Partial order reduction],
    compositional techniques,
    assume-guarantee
  - Systematic execution exploration

    Test amplification
  - Stateless search
  - Execution-based tools

    VeriSoft, JavaPathFinder, Cmc, MaceMC
- Concrete symbolic model checking
  - The region data structure

    SymbolicReachability algorithm,
    [reachability]
  - Example: propositional logic

    [BDD]s
  - Example: first order logic with interpreted theories
  - [Bounded model checking]

    [symbolic execution]
  - Invariants and invariant synthesis

    abstraction techniques for invariant synthesis,
    k-induction,
    template-based synthesis
- Model checking and abstraction

  [reachability],
  - Abstract reachability analysis

    Finite height domains;
    infinite height domains and widening operators
  - Example: polyhedral domains
  - Example: predicate abstraction

    SLAM verifier,
    [BLAST verifier],
    cartesian predicate abstraction
  - Example: control abstraction

    sequential programs,
    concurrent programs
  - Combined abstractions

    > Gulwani and Tiwari shows a general framework for
    > combining abstract interpretations for different
    > theories, analogous to the manner in which decision
    > procedures for different theories are combined.

- Abstraction refinement

  [CEGAR]
  - Counterexamples and refinement
    - Counterexamples
    - Trace formulas
    - Syntax-based refinement
    - Interpolation-based refinement
    - Relative completeness
    - Refining multiple paths
    - Refining other domains
  - Abstraction-refinement-based model checkers
    - SLAM verifier and BEBOP
    - [BLAST verifier] and lazy refinement
    - Magic and concurrent, message-passing C programs
    - F-Soft
    - IMPACT
    - ARMC
- Procedural abstraction
  - Programs with procedures
  - InterProcedural reachability

    memoization
    - Graph-based algorithms
    - Symbolic algorithms
    - Abstraction
    - Top-down vs. Bottom-up
    - Saturn
    - Houdini
  - Concurrency and recursion
- Heap data structures
  - [Alias analysis]
  - [Shape analysis]
  - [Separation logic]
  - Reachability predicates
  - Quantified loop invariants
- Liveness and termination
  - Finite state

    [Büchi automaton][buchi automaton],
    LTL [temporal logic],
    pushdown systems
  - Infinite state

    Program termination,
    fairness conditions
  - Nontermination
- Model checking and software quality
  - Model checking and testing

    underapproximation
    - Test generation by [symbolic evaluation]
  - Model checking and type systems
    - Typestates
    - Dependent types
    - Hybrid type checking
- Conclusion

{% include links.html %}
