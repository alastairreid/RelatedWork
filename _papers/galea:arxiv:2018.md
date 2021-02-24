---
ENTRYTYPE: misc
added: 2021-02-10
archiveprefix: arXiv
authors:
- John Galea
- Sean Heelan
- Daniel Neville
- Daniel Kroening
eprint: '1805.03450'
layout: paper
primaryclass: cs.SE
read: true
readings:
- 2021-02-10
title: Evaluating manual intervention to address the challenges of bug finding with KLEE
year: 2018
notes:
- symbolic execution
- KLEE verifier
papers:
- bornholt:oopsla:2018
---

This paper looks at how to find and fix verification performance bugs
encountered with KLEE; builds a bug corpus for the evaluation; and
categorizes different kinds of problem.

This is good to read in conjunction with [bornholt:oopsla:2018].

They build a bug corpus of 130 bugs in 8 real world applications for evaluation
– based on
searching for security fixes in public code repos;
using known concrete test cases to find the changes that introduced the security bugs;
and constructing 19 min-sets that contain all those known bugs.
(Unknown bugs also exist and are detected later in the paper.)

They start by establishing a baseline using KLEE's default settings and the 
covnew and random-path search strategies.
They also implemented  a modified strategy ‘rspf’.

- KLEE struggled to find bugs and coverage seems low (but no good coverage baseline to compare against
  so it is hard to know whether coverage really is low)
- Covnew (or all strategies?) often have a single program location responsible for almost all state forks.

Categorization of software problems that cause problems for symbolic execution

- They locate problem pieces of code
  using klee-stats and klee-replay, some custom logging extensions, warning messages. A critical measure seems to be the number of forks at a given program location.
- Methodology is to run 60 minute experiment, make some changes, evaluate (in parallel?), repeat
- Common problems
  - Avoidable library code: Printing/formatting code → replace with a ‘low fidelity model’
  - Avoidable application code: two alternative implementations (one higher performance but more branchy) → insert assumption to force choice
  - Input discarding code - skips over input characters looking for delimiter/terminator → insert assumption that code does not have trailing whitespace, etc.
  - Parsing code → write a verification harness that calls interesting code directly
  - Initialization of static data
    - → lift initialization to before the first state fork
    - or → replace initialization code with a statically calculated table
    - or → write a verification harness that bypasses the code
    - Interesting coverage problem found in this: the locale is concrete by default so, if you want to test with different locale’s need to make it symbolic.
      They do this by enumerating locales to test with and using a symbolic variable to select from this enumeration.
  - Metaproperties of input data such as input length that have an indirect data-flow dependency on input data.
    - Problem when passed to malloc (say) that concretizes its arguments. → Enumerating interesting ranges lets you steer coverage.
      (Note that this concretization can cause soundness issues as well.)
    - Problem in loop that searches for zero values in a histogram table: dependency is so complex that resulting table index is effectively concrete
      (This reminded me of verifying crypto code where the function is effectively irreversible so solving for interesting
      input values is not possible.)
    - Inefficient environment models - eg memcpy creates 2n states when n is symbolic → mitigate by adding model to KLEE (using an otherwise inaccessible API?) or by constraining range of symbolic variables

Evaluation of manual mitigations

- Some mitigations decreased coverage metrics (by removing ‘uninteresting’ paths)
- More bugs and more coverage overall
- Some assumptions added would either conflict (always false) or would not add anything (always true).
- Overall, coverage increases were modest (average of 3%).
- Out of the 130 known bugs, the number found increased from 3 to 9 and the number of unknown bugs found increased from 78 to 162. Almost all of the increase in unknown bugs is in 2 of the 8 applications.

The related work has a good discussion of techniques used to increase bug-finding efficiency.

{% include links.html %}
