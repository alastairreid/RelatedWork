---
ENTRYTYPE: article
abstract: Unsafe programming systems are still very popular, despite the shortcomings due to several published memory-corruption vulnerabilities. Toward
  defending memory corruption, compilers have started to employ advanced software hardening such as Control-flow Integrity (CFI) and SafeStack. However,
  there is a broad interest for realizing compilers that impose memory safety with no heavy runtime support (e.g., garbage collection). Representative examples
  of this category are Rust and Go, which enforce memory safety primarily statically at compile time.Software hardening and Rust/Go are promising directions
  for defending memory corruption, albeit combining the two is questionable. In this article, we consider hardened mixed binaries, i.e., machine code that
  has been produced from different compilers and, in particular, from hardened C/C++ and Rust/Go (e.g., Mozilla Firefox, Dropbox, npm, and Docker). Our
  analysis is focused on Mozilla Firefox, which outsources significant code to Rust and is open source with known public vulnerabilities (with assigned
  CVE). Furthermore, we extend our analysis in mixed binaries that leverage Go, and we derive similar results.The attacks explored in this article do not
  exploit Rust or Go binaries that depend on some legacy (vulnerable) C/C++ code. In contrast, we explore how Rust/Go compiled code can stand as a vehicle
  for bypassing hardening in C/C++ code. In particular, we discuss CFI and SafeStack, which are available in the latest Clang. Our assessment concludes
  that CFI can be completely nullified through Rust or Go code by constructing much simpler attacks than state-of-the-art CFI bypasses.
added: 2021-03-05
address: New York, NY, USA
articleno: '7'
authors:
- Michalis Papaevripides
- Elias Athanasopoulos
doi: 10.1145/3418898
issn: 2471-2566
issue_date: February 2021
journal: ACM Transactions on Privacy and Security
keywords: Memory safety, Go, SafeStack, Rust, CFI
layout: paper
link: https://doi.org/10.1145/3418898
month: January
number: '2'
numpages: '29'
publisher: Association for Computing Machinery
read: false
readings: []
title: Exploiting mixed binaries
url: https://doi.org/10.1145/3418898
volume: '24'
year: 2021
notes:
- Rust language
- Rust unsafe code
papers:
---


{% include links.html %}
