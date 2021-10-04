---
layout: note
notes:
- neural network
wiki: https://en.wikipedia.org/wiki/Autoencoder
url: https://www.deeplearningbook.org/contents/autoencoders.html
papers: {}
title: Auto-encoder model
---

A pair of [neural network]s f and g such that g(f(x)) is kinda similar to x.
The range of f is usually much smaller than its domain so that f is
required to capture the most useful/salient properties of x.
That is, they are "undercomplete" and are used for dimensionality reduction.


{% include links.html %}
