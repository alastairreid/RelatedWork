---
ENTRYTYPE: inproceedings
abstract: High-throughput, low-power Software Defined Radio(SDR) solutions require multi-core SIMD DSP processors to meet real-time performance requirements.
  Given the difficulty in programming traditional DSPs, these new multi-core signal processors provide even greater challenges for programmers and compilers.
  In this paper, we describe SPEX, a programming language which is aimed at narrowing the semantic gap between the description of complex SDR systems and
  their implementations. SPEX supports three different types of programming semantics, allowing SDR solutions to be developed with a divide-and-conquer
  approach. For DSP algorithm kernels, SPEX is able to support DSP arithmetics and first-class vector and matrix variables with sequential language semantics.
  From wireless protocol channels, it is able to support sequences of data-processing computations with dataflow language semantics. And for protocol systems,
  it is able to support real-time deadlines and concurrent executions with synchronous language semantics. The design choices are motivated by our experience
  implementing W-CDMA protocol on a reprogrammable substrate. In the paper, we also briefly explain SPEX's compilation strategies.
added: 2019-06-01
affiliation: ARM Ltd and University of Michigan
ar_shortname: SDR 06
authors:
- Yuan Lin
- Robert Mullenix
- Mark Woh
- Scott Mahlke
- Trevor Mudge Alastair Reid
- Krisztián Flautner
booktitle: Software Defined Radio Technical Conference and Product Exposition
day: 13-17
layout: paper
location: Orlando, FL, USA
month: November
read: false
readings: []
title: 'SPEX: A programming language for software defined radio'
year: 2006
topics:
---
