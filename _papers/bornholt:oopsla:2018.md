---
ENTRYTYPE: article
added: 2020-04-30
address: New York, NY, USA
articleno: Article 149
authors:
- James Bornholt
- Emina Torlak
doi: 10.1145/3276519
issue_date: October 2018
journal: Proc. ACM Program. Lang.
keywords: solver-aided programming, symbolic execution, profiling
layout: paper
link: https://doi.org/10.1145/3276519
month: October
number: OOPSLA
numpages: '26'
publisher: Association for Computing Machinery
read: true
readings:
- 2021-02-10
title: Finding code that explodes under symbolic evaluation
url: https://doi.org/10.1145/3276519
volume: '2'
year: 2018
topics:
notes:
- symbolic evaluation
- symbolic execution
- bounded model checking
- Rosette solver
- case splitting
- state merging
papers:
- galea:arxiv:2018
- torlak:pldi:2014
---

Like [galea:arxiv:2018] (which is also worth a read), this paper looks at how
to find verification bottlenecks in symbolic evaluation.  They propose a
symbolic profiling approach that works for any symbolic evaluator (symbolic
executor, BMC or hybrids) and, using a simple but effective metric to rank hotspots,
is effective at highlighting the root cause of the problem.


Symbolic profiling (SymPro)

- Two resources: symbolic heap and symbolic evaluation graph
  - Heap = constants, terms, etc. (with hash-consing used to avoid duplicates)
  - Graph = paths and any merge points (DAG) from evaluation strategy
  - Track evolution: where are values created, accessed, sent to solver; how are paths merged at ctrl-flow joins.
  - Rank procedure calls by metrics about evolution
- Model is general (to any forward symbolic evaluator: symbolic execution, BMC and hybrids), explainable (independent of internal details) and actionable (finds root causes)
- Key insight: "effective symbolic evaluation involves maximizing (opportunities for) concrete evaluation while minimizing path explosion".
- Challenge: naïve time-profiling highlights the wrong part of the code: the consumption of symbolic terms, not the construction.
  (This reminds me of profiling lazy evaluation in Haskell.) 


List of antipatterns in solver-aided code

- Algorithmic
- Representation
  - Irregular data structures that cause divergence in control flow. (IIRC,
    Rosette groups data structures by shape (they call it “type”) and merges
    flows that have the same shape.)
- Concreteness
  - Failure leads to large evaluation graphs with many infeasible paths.
  - Introducing [case splits][case splitting] can concretize symbolic values.
    Eg “if x == 0 { … 0 … } elsif x == 1 { … 1 … } else { … x … }” makes x
    concrete in the first two branches (and maybe the third option is an error
    case?) (Rosette’s for/all form does this (section 5.1))


Profiling

  - Considered input-sensitive profiling [Coppa et al., 2012] but correlation between input size and performance is often poor for symbolic evaluation: inaccurate and noisy.
  - Considered path-based profiling [Kuznetsov et al., 2012]: rank functions based on number of infeasible paths explored and size of path conditions. But infeasible paths are not always the problem and measuring feasibility is expensive (uses solver); and does not work for BMC.
  - These lead them to heap + graph model (above).
    - Symbolic profiler interface (I have transliterated the interface into pseudo-Rust).
      - mkTerm(Vec<term>) -> term
      - step(state, Vec<guarded_exprs>) -> Vec<state>
      - merge(srcloc, Vec<state>) -> state
      - solve(srcloc, expr) -> bool

Visualization

- Flamegraph: time vs. call stack colour-coded by a score
- Score computed from five statistics
  - wall-clock time; #terms created; #unused terms; union size (sum of out-degrees); merge cases (sum of in-degrees). (See figure 3.)
  - Calculation of overall score: normalize the five statistics to range 0.0 .. 1.0; sum results
  - Experiment with machine-learning ranking scheme had high recall but poor precision (many false positives) - so manual scheme is default.


Extensive empirical evaluation
- Ferrite crash-safe file system
- Cosette SQL query system
- Neutrons (radiotherapy system)
- Also Bonsai (checks soundness of type systems), Quivela (verifies security of crypto protocols), Fluidics (synthesizes microfluidics protocols), RTR (Refinement typechecker for Ruby).
- Evaluates which of the metrics are most reliable in ranking bottlenecks.
- User study: time taken to identify performance issue: 4 benchmarks, with/without SymPro. (A bit small for statistical significance
- Implemented on both Rosette and Jalangi. Tried on red-black tree, calculator parser and BDD.
  - Highlights idea of using SymPro to develop efficient formal models of libraries and frameworks. (Because optimizing for reasoning and optimizing for concrete execution can require conflicting changes.)


{% include links.html %}
