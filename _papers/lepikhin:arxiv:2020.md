---
ENTRYTYPE: misc
added: 2021-09-27
archiveprefix: arXiv
authors:
- Dmitry Lepikhin
- HyoukJoong Lee
- Yuanzhong Xu
- Dehao Chen
- Orhan Firat
- Yanping Huang
- Maxim Krikun
- Noam Shazeer
- Zhifeng Chen
eprint: '2006.16668'
layout: paper
primaryclass: cs.CL
read: true
readings:
- 2021-09-27
title: 'GShard: Scaling giant models with conditional computation and automatic sharding'
year: 2020
notes:
- neural network
- transformer model
- sparse model
- Mixture of Experts
- NLP
- google
papers:
- fedus:arxiv:2021
- shazeer:arxiv:2017
---

> GShard enabled us to scale up multilingual neural machine translation
> [Transformer model] with Sparsely-Gated [Mixture of Experts] beyond
> 600 billion parameters using automatic sharding.
> We demonstrate that such a giant model can efficiently be trained
> on 2048 TPU v3 accelerators in 4 days to achieve far superior
> quality for translation from 100 languages to English compared
> to the prior art.

The paper starts by enumerating challenges in scaling beyond the capacity
limit of a single accelerator memory.

GShard only requires annotation of a few critical tensors with partitioning policies.
The compiler automatically partitions based on these annotations and some heuristics
by propagating sharding decisions across tensorflow operators.
Sharding is done using an SPMD (MPI-style) programming model.

Although it uses a sparsely gated [mixture of experts], it only uses top-2 experts: a halfway point between
[shazeer:arxiv:2017] that used top-4 experts and [fedus:arxiv:2021] (Switch transformers) that
only uses the top-1 expert.

The training data is noisy and for some language pairs there are less than
10,000 examples to work with.

On small models (128 experts), they achieve 70% of the (optimistic) roofline performance;
on large models (2048 experts), they achieve 48% of roofline.



{% include links.html %}
