---
ENTRYTYPE: inproceedings
abstract: The Rust programming language has a safe memory model that promises to eliminate critical memory bugs. While the language is strong in doing so,
  its memory guarantees are lost when any unsafe blocks are used. Unsafe code is often needed to call library functions written in an unsafe language inside
  a Rust program. We present Fidelius Charm (FC), a system that protects a programmer-specified subset of data in memory from unauthorized access through
  vulnerable unsafe libraries. FC does this by limiting access to the program's memory while executing unsafe libraries. FC uses standard features of Rust
  and utilizes the Linux kernel as a trusted base for splitting the address space into a trusted privileged region under the control of functions written
  in Rust and a region available to unsafe external libraries. This paper presents our design and implementation of FC, presents two case studies for using
  FC in Rust TLS libraries, and reports on experiments showing its performance overhead is low for typical uses.
added: 2021-03-05
address: New York, NY, USA
authors:
- Hussain M. J. Almohri
- David Evans
booktitle: Proceedings of the Eighth ACM Conference on Data and Application Security and Privacy
doi: 10.1145/3176258.3176330
isbn: '9781450356329'
keywords: isolation, sandboxing, compartmentalization, rust
layout: paper
link: https://doi.org/10.1145/3176258.3176330
location: Tempe, AZ, USA
numpages: '8'
pages: 248-255
publisher: Association for Computing Machinery
read: false
readings: []
series: CODASPY '18
title: 'Fidelius Charm: Isolating unsafe Rust code'
url: https://doi.org/10.1145/3176258.3176330
year: 2018
notes:
- Rust language
- Rust unsafe code
papers:
---

Uses dynamic enforcement (memory protection?) to prevent unsafe code from
accessing protected regions of memory.

{% include links.html %}
