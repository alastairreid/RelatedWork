---
ENTRYTYPE: inproceedings
abstract: 'Modern software systems, which often are concurrent and manipulate complex data structures must be extremely reliable. We present a novel framework
  based on symbolic execution, for automated checking of such systems. We provide a two-fold generalization of traditional symbolic execution based approaches.
  First, we define a source to source translation to instrument a program, which enables standard model checkers to perform symbolic execution of the program.
  Second, we give a novel symbolic execution algorithm that handles dynamically allocated structures (e.g., lists and trees), method preconditions (e.g.,
  acyclicity), data (e.g., integers and strings) and concurrency. The program instrumentation enables a model checker to automatically explore different
  program heap configurations and manipulate logical formulae on program data (using a decision procedure). We illustrate two applications of our framework:
  checking correctness of multi-threaded programs that take inputs from unbounded domains with complex structure and generation of non-isomorphic test inputs
  that satisfy a testing criterion. Our implementation for Java uses the Java PathFinder model checker.'
added: 2021-04-18
address: Berlin, Heidelberg
authors:
- Sarfraz Khurshid
- Corina S. Păsăreanu
- Willem Visser
booktitle: Proceedings of the 9th International Conference on Tools and Algorithms for the Construction and Analysis of Systems
isbn: '3540008985'
layout: paper
location: Warsaw, Poland
numpages: '16'
pages: 553-568
publisher: Springer-Verlag
read: true
readings:
- 2021-04-22
series: TACAS'03
title: Generalized symbolic execution for model checking and testing
year: 2003
notes:
- lazy initialization
- Java PathFinder
- Omega library
- symbolic execution
- separation logic
papers:
- xie:popl:2005
- engler:issta:2007
- calcagno:popl:2009
---

Introduced the idea of [lazy initialization] to allow pointer-manipulating programs to be
verified using [symbolic execution] without having to construct a data structure for the program to
symbolically execute.

As the name suggests, instead of constructing an input data structure first and then symbolically
executing the code, the data structure is constructed *on demand*: each dereference of an uninitialized pointer
either constructs a fresh object or chooses one of the previously constructed objects that the pointer
could potentially refer to.

This approach was used as the basis of [xie:popl:2005] and [engler:issta:2007] except that I think
both of them just created a fresh object and did not consider previously initialized objects
at the cost of ignoring possible structure sharing or cycles.

I think it is also similar to the biabduction technique used in [calcagno:popl:2009] (again, with restrictions on sharing
based on [separation logic]).

The implementation technique is also interesting: unlike most approaches (e.g.,
[xie:popl:2005]) that build the solver, etc into their tools, they use a
preprocessor that replaces all concrete variables and operations with symbolic
variables and operations. The only thing they need is a model checker capable
of forking execution and backtracking.

{% include links.html %}
