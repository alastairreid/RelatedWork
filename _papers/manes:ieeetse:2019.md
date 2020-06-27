---
ENTRYTYPE: article
added: 2020-05-22
authors:
- Valentin J.M. Manès
- HyungSeok Han
- Choongwoo Han
- Sang-Kil Cha
- Manuel Egele
- Edward J. Schwartz
- Maverick Woo
doi: 10.1109/TSE.2019.2946563
journal: IEEE Transactions on Software Engineering
layout: paper
number: ''
pages: 21
read: true
readings:
- 2020-06-27
title: 'The art, science, and engineering of fuzzing: A survey'
volume: ''
year: 2019
notes:
- fuzz testing
- symbolic execution
- survey
papers:
---

This large (21 pages, 240 references) survey of [fuzz testing]
proposes a taxonomy and standardized terminology.
They use a "model fuzzer" throughout the survey to motivate/explain
fuzzer design choices.

The survey covers all fuzzing papers from 2008–2019 in 7 conferences
(CCS, S&P, NDSS, USEC, FSE, ASE and ICSE) plus additional relevant
papers.

Their terminology:

- Program Under Test (PUT)
- Fuzzing = testing with a large number of unexpected inputs
  to find security bugs
- Fuzz campaign
- Seed pool (called a corpus by AFL)
- Taint analysis = determining dependency of branches on parts of input
- Crash triage = grouping bugs.
  Can use coverage, execution counts, stack hashing, etc.
- Instrumentation – used to detect bugs and to measure coverage/etc.
  (Note: dynamic instrumentation needed for dynamic libraries, etc.)
- In-memory fuzzing is fuzzing part of the program repeatedly
  without respawning the process.
  Can lead to unrepeatable reports or false reports.
  (cf. "online" or "execution generated testing (EGT)" in [symbolic execution]).
- Seed trimming reduces the size of seeds



Their model fuzzer starts as

    Preprocess(fuzz_config)
    while t_elapsed <= t_limit:
        config = Schedule(fuzz_config, t_elapsed, t_limit)
        test_cases = InputGen(config)
        new_bugs, exec_infos = InputEval(config, test_cases, oracle)
        all_bugs = all_bugs + new_bugs
        fuzz_config = ConfigUpdate(fuzz_config, config, exec_infos)
        if !Continue(fuzz_config): break

This model allows them to classify around 100 fuzzers according to the design choices
they make in each of the functions:

- Misc:
  feedback gathering granularity (black/grey/white),
  open sourced,
  requires source code for PUT
- Preprocess: 
  supports in-memory fuzzing,
  constructs model,
  performs program analysis
- Schedule:
  performs seed scheduling
- InputGen:
  mutation,
  model-based,
  constraint-based,
  taint analysis
- InputEval:
  crash triage by stack hash,
  crash triage by coverage
- ConfigUpdate:
  evolutionaly seed pool update,
  model update,
  seed pool culling

The following sections follow the structure of the paper
(and of the paper's model fuzzer).

## Preprocess

## Scheduling

The "Fuzz Configuration Scheduling (FCS) Problem":

> Fundamentally, every scheduling algorithm confronts the same _exploration_
> vs. _exploitation_ conflict – time can either be spent on gathering more
> accurate information on each configuration to inform future decisions
> (explore), or on fuzzing the configurations that are currently believed to
> lead to more favorable outcomes (exploit).

The main choices are black/grey/white-box.
There is a table that organizes fuzzers by date and by genealogical
connections and breaks them down into

- black-box (subdivided into network, file and kernel)
- grey-box (subdivided into concurrency, file and kernel)
- white-box

Models of black-box mutational fuzzing include Bernoulli trials,
"Weighted Coupon Collector's Problem with Unknown Weights" (WCCP/UW),
"Multi-armed bandit" (MAB).
Grey-box fuzzers often use "evolutionary algorithms" (EA), may prioritize
configurations that have been used least (which encourages cycling
through configurations), use a power schedule.

## Input generation

Inputs can be generated

- according to a model: "generation-based fuzzers" or "model-based fuzzers"
  - grammar-based
  - inferring grammars from examples, source code, etc. during Preprocess
  - inferring grammars from instrumentation during ConfigUpdate
- by mutation of a seed: "mutation-based fuzzers"
  - bit-flipping
  - arithmetic mutation
  - block-based mutation
  - dictionary-based mutation

## Input evaluation

Oracles include

- instrumentation such as address/memory/UB/thread sanitizers, control-flow integrity, etc.
- detecting known insecurity vulnerability
- differential testing

Seed trimming is reducing the size of a crashing test case.
Test case minimization is reducing the size of a crashing test case
using the bug oracle. (This distinction is not clear to me.)

## Configuration updating

- Evolutionary algorithms update the seed pool and update the fitness function
- Updating the minset of testcases according to some coverage metric by
  culling weaker testcases



{% include links.html %}
