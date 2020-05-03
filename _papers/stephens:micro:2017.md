---
ENTRYTYPE: article
abstract: In this paper we describe the ARM Scalable Vector Extension (SVE). Several goals guided the design of the architecture. First was the need to
  extend the vector processing capability associated with the ARM AArch64 execution state to better address the compute requirements in domains such as
  high performance computing (HPC), data analytics, computer vision and machine learning. Second was the desire to introduce an extension that can scale
  across multiple implementations, both now and into the future, allowing CPU designers to choose the vector length most suitable for their power, performance
  and area targets. Finally, the architecture should avoid imposing a software development cost as the vector length changes and where possible reduce it
  by improving the reach of compiler auto-vectorization technologies.  We believe SVE achieves these goals. It allows implementations to choose a vector
  register length between 128 and 2048 bits. It supports a vector length agnostic programming model which allows code to run and scale automatically across
  all vector lengths without recompilation. Finally, it introduces several innovative features that begin to overcome some of the traditional barriers to
  auto-vectorization.
added: 2019-06-01
affiliation: ARM Ltd
ar_shortname: IEEE Micro
authors:
- Nigel Stephens
- Stuart Biles
- Matthias Boettcher
- Jacob Eapen
- Mbou Eyole
- Giacomo Gabrielli
- Matt Horsnell
- Grigorios Magklis
- Alejandro Martinez
- Nathanael Premillieu
- Alastair Reid
- Alejandro Rico
- Paul Walker
doi: 10.1109/MM.2017.35
journal: IEEE Micro
layout: paper
month: March
number: '2'
pages: 26-39
read: false
readings: []
title: The ARM scalable vector extension
volume: '37'
year: 2017
topics:
notes:
- arm-architecture
- instruction-set-architecture
papers:
---

{% include links.html %}
