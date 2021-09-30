---
ENTRYTYPE: misc
added: 2021-09-29
archiveprefix: arXiv
authors:
- Martín Abadi
- Ashish Agarwal
- Paul Barham
- Eugene Brevdo
- Zhifeng Chen
- Craig Citro
- Greg S. Corrado
- Andy Davis
- Jeffrey Dean
- Matthieu Devin
- Sanjay Ghemawat
- Ian Goodfellow
- Andrew Harp
- Geoffrey Irving
- Michael Isard
- Yangqing Jia
- Rafal Jozefowicz
- Lukasz Kaiser
- Manjunath Kudlur
- Josh Levenberg
- Dan Mane
- Rajat Monga
- Sherry Moore
- Derek Murray
- Chris Olah
- Mike Schuster
- Jonathon Shlens
- Benoit Steiner
- Ilya Sutskever
- Kunal Talwar
- Paul Tucker
- Vincent Vanhoucke
- Vijay Vasudevan
- Fernanda Viegas
- Oriol Vinyals
- Pete Warden
- Martin Wattenberg
- Martin Wicke
- Yuan Yu
- Xiaoqiang Zheng
eprint: '1603.04467'
layout: paper
primaryclass: cs.DC
read: true
readings:
- 2021-09-30
title: 'TensorFlow: Large-scale machine learning on heterogeneous distributed systems'
year: 2016
notes:
- TensorFlow
- tensor
- neural network
- stochastic gradient descent
- google
papers:
---

Language for expressing machine learning computations using stateful dataflow graphs
increasing portability by avoiding leaky abstractions.
Replaces an earlier model called DistBelief.

[TensorFlow] computations are directed graphs that extend dataflow by
allowing nodes to maintain/update persistent state, with branching
and looping control and control-dependence edges used to express
happens-before relationships (also to limit/schedule resource usage).
(cf. Arvind's work in the '80s).
Operations tend to be polymorphic
with element types (sometimes) inferred at graph construction time.
Kernels implement operations on particular platforms.
Graphs are constructed in Python or C++ within a "Session" that can be
extended or "Run". (Typically, each such graph is run thousands of times.)

Uniprocessor execution is easy enough: scheduling tasks as their inputs become
available and reference counting tensors.

Distributed execution requires data transfers and considering where each task can
run fastest (given the cost of data xfer).
This is scheduled using a greedy algorithm with some hinting (and plans for
improvement).
Checkpointing can be used to cope with failures.

There is built in support for calculating gradients to support [stochastic gradient descent]
by calculating the derivative of any tensor wrt any(?) of the tensors that it transitively
depends on.
Many TensorFlow operations support calculation of derivatives and
TensorFlow uses the chain rule to trace back from a tensor to any of its transitive inputs.
This introduces a lot of backward edges that make it hard to reclaim memory used by
tensors.
Also requires a bit of book-keeping about control-flow nodes.

Besides common subexpression elimination, a key optimization is to delay
data transfers as late as possible to avoid tying up memory in constrained
devices from the earliest moment that the data is available.

Data transfers are often optimized by dropping the bottom 16 bits of F32
values. (Is this where the bfloat16 (Brain Float) representation
comes from?)

Having a language supports the creation of tools to visualize graphs;
to observe the evolution of values during a training run;
performance traces/metrics that show tasks and dependencies;
optimizers;
etc.

{% include links.html %}
