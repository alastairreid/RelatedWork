---
ENTRYTYPE: inproceedings
abstract: Recent program synthesis techniques help users customize CAD models(e.g., for 3D printing) by decompiling low-level triangle meshes to Constructive
  Solid Geometry (CSG) expressions. Without loops or functions, editing CSG can require many coordinated changes, and existing mesh decompilers use heuristics
  that can obfuscate high-level structure. This paper proposes a second decompilation stage to robustly "shrink" unstructured CSG expressions into more
  editable programs with map and fold operators. We present Szalinski, a tool that uses Equality Saturation with semantics-preserving CAD rewrites to efficiently
  search for smaller equivalent programs. Szalinski relies on inverse transformations, a novel way for solvers to speculatively add equivalences to an E-graph.
  We qualitatively evaluate Szalinski in case studies, show how it composes with an existing mesh decompiler, and demonstrate that Szalinski can shrink
  large models in seconds.
added: 2023-06-21
address: New York, NY, USA
authors:
- Chandrakana Nandi
- Max Willsey
- Adam Anderson
- James R. Wilcox
- Eva Darulova
- Dan Grossman
- Zachary Tatlock
booktitle: Proceedings of the 41st ACM SIGPLAN Conference on Programming Language Design and Implementation
doi: 10.1145/3385412.3386012
isbn: '9781450376136'
keywords: Equality Saturation, Program Synthesis, Decompilation, Computer-Aided Design
layout: paper
link: https://doi.org/10.1145/3385412.3386012
location: London, UK
numpages: '14'
pages: 31-44
publisher: Association for Computing Machinery
read: false
readings: []
series: PLDI 2020
title: Synthesizing structured CAD models with equality saturation and inverse transformations
url: https://doi.org/10.1145/3385412.3386012
year: 2020
notes:
- egraphs
papers:
---
{% include links.html %}
