---
ENTRYTYPE: inproceedings
abstract: All modern web browsers -- Internet Explorer, Firefox, Chrome, Opera, and Safari -- have a core rendering engine written in C++. This language
  choice was made because it affords the systems programmer complete control of the underlying hardware features and memory in use, and it provides a transparent
  compilation model. Unfortunately, this language is complex (especially to new contributors!), challenging to write correct parallel code in, and highly
  susceptible to memory safety issues that potentially lead to security holes.Servo is a project started at Mozilla Research to build a new web browser
  engine that preserves the capabilities of these other browser engines but also both takes advantage of the recent trends in parallel hardware and is more
  memory-safe. We use a new language, Rust, that provides us a similar level of control of the underlying system to C++ but which statically prevents many
  memory safety issues and provides direct support for parallelism and concurrency.In this paper, we show how a language with an advanced type system can
  address many of the most common security issues and software engineering challenges in other browser engines, while still producing code that has the
  same performance and memory profile. This language is also quite accessible to new open source contributors and employees, even those without a background
  in C++ or systems programming. We also outline several pitfalls encountered along the way and describe some potential areas for future improvement.
added: 2021-04-17
address: New York, NY, USA
authors:
- Brian Anderson
- Lars Bergstrom
- Manish Goregaokar
- Josh Matthews
- Keegan McAllister
- Jack Moffitt
- Simon Sapin
booktitle: Proceedings of the 38th International Conference on Software Engineering Companion
doi: 10.1145/2889160.2889229
isbn: '9781450342056'
keywords: parallelism, browser engine, servo, concurrency, Rust
layout: paper
link: https://doi.org/10.1145/2889160.2889229
location: Austin, Texas
numpages: '9'
pages: 81-89
publisher: Association for Computing Machinery
read: false
readings: []
series: ICSE '16
title: Engineering the Servo web browser engine using Rust
url: https://doi.org/10.1145/2889160.2889229
year: 2016
notes:
- Rust language
papers:
---
{% include links.html %}
