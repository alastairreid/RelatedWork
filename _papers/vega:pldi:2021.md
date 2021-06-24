---
ENTRYTYPE: inproceedings
abstract: 'Modern field-programmable gate arrays (FPGAs) have recently powered high-profile efficiency gains in systems from datacenters to embedded devices
  by offering ensembles of heterogeneous, reconfigurable hardware units. Programming stacks for FPGAs, however, are stuck in the past-they are based on
  traditional hardware languages, which were appropriate when FPGAs were simple, homogeneous fabrics of basic programmable primitives. We describe Reticle,
  a new low-level abstraction for FPGA programming that, unlike existing languages, explicitly represents the special-purpose units available on a particular
  FPGA device. Reticle has two levels: a portable intermediate language and a target-specific assembly language. We show how to use a standard instruction
  selection approach to lower intermediate programs to assembly programs, which can be both faster and more effective than the complex metaheuristics that
  existing FPGA toolchains use. We use Reticle to implement linear algebra operators and coroutines and find that Reticle compilation runs up to 100 times
  faster than current approaches while producing comparable or better run-time and utilization.'
added: 2021-06-24
address: New York, NY, USA
authors:
- Luis Vega
- Joseph McMahan
- Adrian Sampson
- Dan Grossman
- Luis Ceze
booktitle: Proceedings of the 42nd ACM SIGPLAN International Conference on Programming Language Design and Implementation
doi: 10.1145/3453483.3454075
isbn: '9781450383912'
keywords: FPGAs, compilers
layout: paper
link: https://doi.org/10.1145/3453483.3454075
location: Virtual, Canada
numpages: '16'
pages: 756-771
publisher: Association for Computing Machinery
read: false
readings: []
series: PLDI 2021
title: 'Reticle: A virtual machine for programming modern FPGAs'
url: https://doi.org/10.1145/3453483.3454075
year: 2021
notes:
- hardware
papers:
---
{% include links.html %}
