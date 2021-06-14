---
ENTRYTYPE: inproceedings
abstract: We present a multi-lingual type inference system for checking type safety across a foreign function interface. The goal of our system is to prevent
  foreign function calls from introducing type and memory safety violations into an otherwise safe language. Our system targets OCaml's FFI to C, which
  is relatively lightweight and illustrates some interesting challenges in multi-lingual type inference. The type language in our system embeds OCaml types
  in C types and vice-versa, which allows us to track type information accurately even through the foreign language, where the original types are lost.
  Our system uses representational types that can model multiple OCaml types, because C programs can observe that many OCaml types have the same physical
  representation. Furthermore, because C has a low-level view of OCaml data, our inference system includes a dataflow analysis to track memory offsets and
  tag information. Finally, our type system includes garbage collection information to ensure that pointers from the FFI to the OCaml heap are tracked properly.
  We have implemented our inference system and applied it to a small set of benchmarks. Our results show that programmers do misuse these interfaces, and
  our implementation has found several bugs and questionable coding practices in our benchmarks.
added: 2021-06-14
address: New York, NY, USA
authors:
- Michael Furr
- Jeffrey S. Foster
booktitle: Proceedings of the 2005 ACM SIGPLAN Conference on Programming Language Design and Implementation
doi: 10.1145/1065010.1065019
isbn: '1595930566'
keywords: OCaml, multi-lingual type inference, foreign function calls, representational type, flow-sensitive type system, FFI, multi-lingual type system,
  dataflow analysis, foreign function interface
layout: paper
link: https://doi.org/10.1145/1065010.1065019
location: Chicago, IL, USA
numpages: '11'
pages: 62-72
publisher: Association for Computing Machinery
read: true
readings:
- 2021-06-14
series: PLDI '05
title: Checking type safety of foreign function calls
url: https://doi.org/10.1145/1065010.1065019
year: 2005
notes:
- foreign function interface
- dependent type
- type inference
papers:
- condit:esop:2007
---

Checks [foreign function interface] calls between O'Caml and C.
The important code (i.e., where the bugs happen) is the C code.
They use a flow-sensitive type system based on the data representation
to detect shape errors and they use an effect system to detect
when calls from C to O'Caml (that could cause a GC) are
made without appropriate precautions.

{% include links.html %}
