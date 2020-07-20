---
doi: 10.1007/978-3-642-31424-7_32
ENTRYTYPE: inproceedings
abstract: Consider a sequential programming language with control flow constructs
  such as assignments, choice, loops, and procedure calls. We restrict the syntax
  of expressions in this language to one that can be efficiently decided by a satisfiability-modulo-theories
  solver. For such a language, we define the problem of deciding whether a program
  can reach a particular control location as the reachability-modulo-theories problem.
  This paper describes the architecture of Corral, a semi-algorithm for the reachability-modulo-theories
  problem. Corraluses novel algorithms for inlining procedures on demand (Stratified
  Inlining) and abstraction refinement (Hierarchical Refinement). The paper also presents
  an evaluation of Corralagainst other related tools. Corralconsistently outperforms
  its competitors on most benchmarks.
added: 2020-03-04
address: Berlin, Heidelberg
authors:
- Akash Lal
- Shaz Qadeer
- Shuvendu K. Lahiri
booktitle: Computer Aided Verification
editor: 'Madhusudan, P.
  and Seshia, Sanjit A.'
isbn: 978-3-642-31424-7
layout: paper
pages: 427-443
publisher: Springer Berlin Heidelberg
read: true
readings:
- 2020-02-03
title: A solver for reachability modulo theories
year: 2012
topics:
- tools
- verification
notes:
- Corral verifier
- bounded verification
papers:
---

This paper describes the Corral tool for finding bugs in device drivers using a variant of bounded model checking.
Like many bounded model checkers, they inline all functions and unroll all loops up to some bound – increasing the bound until some limit or until a bug is found.
What is interesting is that, instead of inlining all functions at once, they incrementally inline functions according to some heuristics.
They also use a CEGAR-like mechanism to control variable abstraction.

What I like about this paper is the discussion of several heuristics, improvements, tricks, etc.  that they use to get performance.  For example, when searching for the minimal number of variables in the abstraction, they could generate N different verification conditions VC and try each one.  Instead, they generate a single VC with additional Boolean variables to enable/disable use of each variable.  They then invoke the SMT solver N times on a single VC - potentially benefiting from anything that the solver learns that applies across multiple solutions efforts.



{% include links.html %}
