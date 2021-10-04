---
ENTRYTYPE: misc
added: 2021-10-04
archiveprefix: arXiv
authors:
- Erich Elsen
- Marat Dukhan
- Trevor Gale
- Karen Simonyan
eprint: '1911.09723'
layout: paper
primaryclass: cs.CV
read: true
readings:
- 2021-10-04
title: Fast sparse ConvNets
year: 2019
notes:
- neural network
- sparse model
- TensorFlow
- XNNPACK
- google
papers:
---

Describes the motivation and implementation of sparse
convolution operations in XNNPACK (implemented in Arm NEON).
Can be used with the [TensorFlow] lite model pruning library
that learns sparse representations.

At sparsity levels of 85-90%, runtime of models increases by about 30-50% (for
MobileNet and EfficientNet).


Three observations

1. Although the weights are sparse, the activations are dense.
   So they can perform vector loads from the activation matrix.

2. It is possible to keep the working set smaller than the L1$.
   (Is this just a corollary of the ability to use
   vector loads?)

3. If you don't have too many channels, you can prefetch activations.
   (todo: I thought "channel" was just red-green-blue in images - now
   I think I have that wrong).


{% include links.html %}
