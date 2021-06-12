---
ENTRYTYPE: article
added: 2020-05-12
address: New York, NY, USA
articleno: '50'
authors:
- Roberto Baldoni
- Emilio Coppa
- Daniele Cono D'elia
- Camil Demetrescu
- Irene Finocchi
doi: 10.1145/3182657
issn: 0360-0300
issue_date: July 2018
journal: ACM Computing Surveys
keywords: static analysis, software testing, Symbolic execution, concolic execution
layout: paper
link: https://doi.org/10.1145/3182657
month: May
number: '3'
numpages: '39'
publisher: Association for Computing Machinery
read: true
readings:
- 2020-06-25
title: A survey of symbolic execution techniques
url: https://doi.org/10.1145/3182657
volume: '51'
year: 2018
notes:
- symbolic execution
- KLEE verifier
- interpolation
- survey
papers:
---

This [survey] reinforces my impression that [symbolic execution] is
a beautifully simple idea that, like most beautifully simple ideas, requires
a lot of optimizations to make it scale.
As the structure of the paper shows, most of the survey is concerned with the optimizations.

- Introduction
    - Challenges in Symbolic Execution
    - Related Work
    - Organization of the Article
- Symbolic Execution Engines
    - Mixing Symbolic and Concrete Execution
        - Dynamic Symbolic Execution
        - Selective Symbolic Execution
    - Path Selection

      Can use depth-first, breadth-first, random, buggy-path-first
      or other schedules such as prioritizing symbolic memory accesses.
      (Depth and breadth-first lend themselves to particular optimizations.)

    - Caching
    - Symbolic Backward Execution
    - Design Principles of Symbolic Executors

      Principles include: "ensuring progress", avoiding "work repetition" and
      "analysis reuse".

      "Online" executors explore multiple paths in one run;
      "offline" executors explore one path and then stop;
      "hybrid" executors such as MAYHEM do both.

- Memory model
    - Fully Symbolic Memory
    - Address Concretization
    - Theory of Arrays
    - Partial Memory Modeling
    - Complex Objects
    - Lazy Initialization
        - Verifying Client Code Only
- Interaction with the environment
        - System Environment
        - Application Environment
- Path explosion
    - Pruning Unrealizable Paths

      Path constraints can be "eagerly" evaluated,
      or "lazily" evaluated.

    - Function and Loop Summarization
        - Function Summaries
        - Loop Summaries
    - Path Subsumption and Equivalence
        - Interpolation
        - Subsumption with Interpolation
        - Unbounded Loops
        - Subsumption with Abstraction
        - Path Partitioning
    - Under-constrained Symbolic Execution

      To avoid false positives when a function is evaluated in isolation,
      under-constrained variables (e.g., symbolic inputs) to the function are marked and
      errors based on under-constrained variables are suppressed.

    - Exploiting Preconditions and Input Features
    - Controlled Loop Exploration
    - Dynamic symbolic execution
    - State Merging
        - Tradeoffs: to Merge or Not to Merge?
        - Merging Heuristics
        - Dynamic State Merging
    - Leveraging Program Analysis and Optimization Techniques
        - Program Slicing
        - Taint Analysis
        - Fuzzing
        - Branch Predication
        - Type Checking
        - Compiler Optimizations
- Constraint solving
    - Optimization Techniques
        - Constraint Reduction
        - Reuse of Constraint Solutions
    - Unburdening the Constraint Solver
        - Reuse of Constraint Solutions
    - Other Optimizations in Symbolic Executors
    - Reducing the Symbolic Executor's Pressure on Constraint Solvers
        - Lazy Constraints
        - Concretization
        - Handling Problematic Constraints
- Further Directions
    - Separation Logic
    - Invariants
    - Function Summaries
    - Program Analysis and Optimization
    - Symbolic Computation
- Conclusions


{% include links.html %}
