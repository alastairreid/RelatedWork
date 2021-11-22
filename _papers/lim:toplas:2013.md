---
ENTRYTYPE: article
abstract: 'This article describes the design and implementation of a system, called TSL (for Transformer Specification Language), that provides a systematic
  solution to the problem of creating retargetable tools for analyzing machine code. TSL is a tool generator--that is, a metatool--that automatically creates
  different abstract interpreters for machine-code instruction sets.The most challenging technical issue that we faced in designing TSL was how to automate
  the generation of the set of abstract transformers for a given abstract interpretation of a given instruction set. From a description of the concrete
  operational semantics of an instruction set, together with the datatypes and operations that define an abstract domain, TSL automatically creates the
  set of abstract transformers for the instructions of the instruction set. TSL advances the state-of-the-art in program analysis because it provides two
  dimensions of parameterizability: (i) a given analysis component can be retargeted to different instruction sets; (ii) multiple analysis components can
  be created automatically from a single specification of the concrete operational semantics of the language to be analyzed.TSL is an abstract-transformer-generator
  generator. The article describes the principles behind TSL, and discusses how one uses TSL to develop different abstract interpreters.'
added: 2021-11-22
address: New York, NY, USA
articleno: '4'
authors:
- Junghee Lim
- Thomas Reps
doi: 10.1145/2450136.2450139
issn: 0164-0925
issue_date: April 2013
journal: 'ACM Transactions on Programming Languages and Systems (TOPLAS)'
keywords: Abstract interpretation, dataflow analysis, dynamic analysis, static analysis, symbolic analysis, machine-code analysis
layout: paper
link: https://doi.org/10.1145/2450136.2450139
month: apr
number: '1'
numpages: '59'
publisher: Association for Computing Machinery
read: false
readings: []
title: 'TSL: A system for generating abstract interpreters and its application to machine-code analysis'
url: https://doi.org/10.1145/2450136.2450139
volume: '35'
year: 2013
notes:
- ISA specification
- Abstract interpretation
papers:
---
{% include links.html %}
