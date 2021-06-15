---
ENTRYTYPE: inproceedings
added: 2020-11-01
address: New York, NY, USA
authors:
- Ana Nora Evans
- Bradford Campbell
- Mary Lou Soffa
booktitle: Proceedings of the ACM/IEEE 42nd International Conference on Software Engineering
doi: 10.1145/3377811.3380413
isbn: '9781450371216'
layout: paper
link: https://doi.org/10.1145/3377811.3380413
location: Seoul, South Korea
numpages: '12'
pages: 246-257
publisher: Association for Computing Machinery
read: true
readings:
- 2021-06-15
series: ICSE '20
title: Is Rust used safely by software developers?
url: https://doi.org/10.1145/3377811.3380413
year: 2020
notes:
- Rust language
- Rust unsafe code
papers:
---

Empirical study of unsafe annotations in open source Rust crates.
Uses a tool to count different forms of unsafe annotation
in the crates and the transitive dependencies of safe functions
on other functions that contain unsafe annotations.

Code studied:

1. All crates on crates.io that still build. (Around 15,000 crates)
2. Crates that account for 90% of all downloads from crates.io. (Around 500 crates)
3. All crates that Mozilla's Servo depends on. (Around 400 crates, overlapping with group 2)

29% of (1) use unsafe directly; rising to over 50% in (2) and (3).
Mostly as unsafe blocks, not unsafe functions or unsafe traits like Sync and Send.
There is a long tail mostly due to auto-generated code.

On average, a crate depends on 12 other crates.
38% of crates do not directly contain unsafe annotations but transitively depend
on crates that do.
(There are lots of other stats in the paper.)

The most common reason for an unsafe annotation is calling an unsafe function (64--89%).
These unsafe functions are 65% Rust functions, 22.5% C functions and Rust intrinsics.
Roughly half the unsafe calls to Rust functions are to Rust's Core library of which
36% are in the ptr module and 40% are to SIMD instructions and architecture-specific
intrinsics.[^but-why-is-SIMD-unsafe]

[^but-why-is-SIMD-unsafe]:
    From my own use of Rust's SIMD libraries, I know that the vast majority of SIMD
    library functions just perform arithmetic and 
    do not cause any type, memory or thread safety issues but
    they are marked 'unsafe' anyway.
    This distorts the numbers a bit: if we were to ignore these unproblematic
    SIMD instructions, all the other numbers would rise: 60% of unsafe Core calls
    would be to ptr, 50% of unsafe function calls would be to Rust functions
    and 30% would be to C functions and Rust intrinsics.




{% include links.html %}
