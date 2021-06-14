---
ENTRYTYPE: inproceedings
abstract: We investigate the use of coverage-guided fuzzing as a means of proving satisfiability of SMT formulas over finite variable domains, with specific
  application to floating-point constraints. We show how an SMT formula can be encoded as a program containing a location that is reachable if and only
  if the program's input corresponds to a satisfying assignment to the formula. A coverage-guided fuzzer can then be used to search for an input that reaches
  the location, yielding a satisfying assignment. We have implemented this idea in a tool, Just Fuzz-it Solver (JFS), and we present a large experimental
  evaluation showing that JFS is both competitive with and complementary to state-of-the-art SMT solvers with respect to solving floating-point constraints,
  and that the coverage-guided approach of JFS provides significant benefit over naive fuzzing in the floating-point domain. Applied in a portfolio manner,
  the JFS approach thus has the potential to complement traditional SMT solvers for program analysis tasks that involve reasoning about floating-point constraints.
added: 2021-06-14
address: New York, NY, USA
authors:
- Daniel Liew
- Cristian Cadar
- Alastair F. Donaldson
- J. Ryan Stinnett
booktitle: Proceedings of the 2019 27th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering
doi: 10.1145/3338906.3338921
isbn: '9781450355728'
keywords: Constraint solving, feedback-directed fuzzing
layout: paper
link: https://doi.org/10.1145/3338906.3338921
location: Tallinn, Estonia
numpages: '12'
pages: 521-532
publisher: Association for Computing Machinery
read: false
readings: []
series: ESEC/FSE 2019
title: 'Just fuzz it: Solving floating-point constraints using coverage-Guided fuzzing'
url: https://doi.org/10.1145/3338906.3338921
year: 2019
notes:
- fuzz testing
- SMT solver
papers:
---
{% include links.html %}
