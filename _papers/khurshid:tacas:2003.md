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
read: false
readings: []
series: TACAS'03
title: Generalized symbolic execution for model checking and testing
year: 2003
notes:
- lazy initialization
- Java PathFinder
papers:
---
{% include links.html %}
