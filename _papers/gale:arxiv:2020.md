---
ENTRYTYPE: misc
added: 2021-10-04
archiveprefix: arXiv
authors:
- Trevor Gale
- Matei Zaharia
- Cliff Young
- Erich Elsen
eprint: '2006.10901'
layout: paper
primaryclass: cs.LG
read: true
readings:
- 2021-10-04
title: Sparse GPU kernels for deep learning
year: 2020
notes:
- neural network
- sparse model
- google
papers:
---

Scientific sparse matrices tend to be 99% sparse and have  many short rows (eg 4-16 elements)
while ML matrices tend to be 60-99% sparse and have many moderate length rows (eg 64-256 elements)
with much less variability in row lengths.

This paper describes in detail how to implement SpMM and SDDMM efficiently on CUDA resulting in significantly
faster inference than if dense models were used instead.
Figure 12 shows that you can get 1% more accuracy at the same throughput 
or 20% higher framerates at the same accuracy.

{% include links.html %}
