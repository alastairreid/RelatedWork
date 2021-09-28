---
ENTRYTYPE: misc
added: 2021-09-27
archiveprefix: arXiv
authors:
- William Fedus
- Barret Zoph
- Noam Shazeer
eprint: '2101.03961'
layout: paper
primaryclass: cs.LG
read: true
readings:
- 2021-09-27
title: 'Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity'
year: 2021
notes:
- mixture of experts
- transformer model
- machine learning
- neural network
- sparse model
- NLP
- google
papers:
- shazeer:arxiv:2017
---

Observes that the [mixture of experts] approach suffers from problems in
complexity, communication costs and training instabilities.
Simplifies it by replacing the "top-k" approach from the [mixture of experts]
(where the results from k experts are combined) with a switch
that selects just one expert. That is, it uses k=1.
This preserves model quality, reduces routing computation and performs better.

*[Does the improvement come at the cost of needing more experts so that there is
more redundancy/overlap between experts?]*

When implemented on a TPU, all tensor shapes must be determined at compile time
and all matrix operations are dense
but the routing decisions are dynamic.

An important tradeoff between precision and efficiency is that values sent
between devices are represented using bfloat16 but values used within devices
are represented using float32.

Switch transformers scale well (wrt number of parameters) because you can have many
different experts without increasing computational cost much.
The only cost of more experts is choosing which expert to use.
And the extra capacity (more parameters) means that you get better results
from a [sparse][sparse model] switch-transformer model than from a dense model.
But, you have to limit the size of each expert so that it fits in a single
device.

Figure 9 (page 16) gives a nice picture of five ways that model weights and data can be
split over cores. The impact of these on compute patterns, communication patterns
and various capacities are then discussed.









{% include links.html %}
