---
ENTRYTYPE: inproceedings
abstract: Applications targeting digital signal processors (DSPs) benefit from fast implementations of small linear algebra kernels. While existing auto-vectorizing
  compilers are effective at extracting performance from large kernels, they struggle to invent the complex data movements necessary to optimize small kernels.
  To get the best performance, DSP engineers must hand-write and tune specialized small kernels for a wide spectrum of applications and architectures. We
  present Diospyros, a search-based compiler that automatically finds efficient vectorizations and data layouts for small linear algebra kernels. Diospyros
  combines symbolic evaluation and equality saturation to vectorize computations with irregular structure. We show that a collection of Diospyros-compiled
  kernels outperform implementations from existing DSP libraries by 3.1\texttimes  on average, that Diospyros can generate kernels that are competitive
  with expert-tuned code, and that optimizing these small kernels offers end-to-end speedup for a DSP application.
added: 2021-09-22
address: New York, NY, USA
authors:
- Alexa VanHattum
- Rachit Nigam
- Vincent T. Lee
- James Bornholt
- Adrian Sampson
booktitle: Proceedings of the 26th ACM International Conference on Architectural Support for Programming Languages and Operating Systems
doi: 10.1145/3445814.3446707
isbn: '9781450383172'
keywords: Equality Saturation, Vectorization, DSPs, Program Synthesis
layout: paper
link: https://doi.org/10.1145/3445814.3446707
location: Virtual, USA
numpages: '13'
pages: 874-886
publisher: Association for Computing Machinery
read: false
readings: []
series: ASPLOS 2021
title: Vectorization for Digital Signal Processors via equality saturation
url: https://doi.org/10.1145/3445814.3446707
year: 2021
notes:
- equality saturation
papers:
---
{% include links.html %}
