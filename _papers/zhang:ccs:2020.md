---
ENTRYTYPE: inproceedings
abstract: As a young programming language designed for systems software development, Rust aims to provide safety guarantees like high-level languages and
  performance efficiency like low-level languages. Lifetime is a core concept in Rust, and it is key to both safety checks and automated resource management
  conducted by the Rust compiler. However, Rust's lifetime rules are very complex. In reality, it is not uncommon that Rust programmers fail to infer the
  correct lifetime, causing severe concurrency and memory bugs. In this paper, we present VRLifeTime, an IDE tool that can visualize lifetime for Rust programs
  and help programmers avoid lifetime-related mistakes. Moreover, VRLifeTime can help detect some lifetime-related bugs (i.e., double locks) with detailed
  debugging information. A demo video is available at https://youtu.be/L5F_XCOrJTQ.
added: 2021-02-28
address: New York, NY, USA
authors:
- Ziyi Zhang
- Boqin Qin
- Yilun Chen
- Linhai Song
- Yiying Zhang
booktitle: Proceedings of the 2020 ACM SIGSAC Conference on Computer and Communications Security
doi: 10.1145/3372297.3420024
isbn: '9781450370899'
keywords: concurrency bugs, Rust
layout: paper
link: https://doi.org/10.1145/3372297.3420024
location: Virtual Event, USA
numpages: '3'
pages: 2085-2087
publisher: Association for Computing Machinery
read: false
readings: []
series: CCS '20
title: VRLifeTime - An IDE tool to avoid concurrency and memory bugs in Rust
url: https://doi.org/10.1145/3372297.3420024
year: 2020
notes:
- Rust language
papers:
---
{% include links.html %}
