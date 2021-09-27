---
layout: note
notes:
- machine learning
- neural network
- gating network
papers:
- shazeer:arxiv:2017
title: Mixture of experts
---

A technique used in [machine learning] where a larger model is composed of multiple
sub-models plus a [gating network] (e.g., a [neural network]) to calculate a relative weight
for the outputs of the sub-models.

When the weights are often zero, it is possible to exploit sparsity as in [shazeer:arxiv:2017].


{% include links.html %}
