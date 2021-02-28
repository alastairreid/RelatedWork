---
ENTRYTYPE: inproceedings
abstract: Rust is a promising systems programming language that embraces both high-level memory safety and low-level resource manipulation. However, the
  dark side of Rust, unsafe Rust, leaves a large security hole as it bypasses the Rust type system in order to support low-level operations. Recently, several
  real-world memory corruption vulnerabilities have been discovered in Rust's standard libraries.We present XRust, a new technique that mitigates the security
  threat of unsafe Rust by ensuring the integrity of data flow from unsafe Rust code to safe Rust code. The cornerstone of XRust is a novel heap allocator
  that isolates the memory of unsafe Rust from that accessed only in safe Rust, and prevents any cross-region memory corruption. Our design of XRust supports
  both single-and multi-threaded Rust programs. Our extensive experiments on real-world Rust applications and standard libraries show that XRust is both
  highly efficient and effective in practice.
added: 2021-02-28
address: New York, NY, USA
authors:
- Peiming Liu
- Gang Zhao
- Jeff Huang
booktitle: Proceedings of the ACM/IEEE 42nd International Conference on Software Engineering
doi: 10.1145/3377811.3380325
isbn: '9781450371216'
layout: paper
link: https://doi.org/10.1145/3377811.3380325
location: Seoul, South Korea
numpages: '12'
pages: 234-245
publisher: Association for Computing Machinery
read: false
readings: []
series: ICSE '20
title: Securing unsafe Rust programs with XRust
url: https://doi.org/10.1145/3377811.3380325
year: 2020
notes:
- Rust language
papers:
---
{% include links.html %}
