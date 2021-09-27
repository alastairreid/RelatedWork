---
layout: note
notes:
- neural network
- activation function
wiki: https://en.wikipedia.org/wiki/Softmax_function
papers: {}
title: Soft max
---

Smooth approximation to the one-hot argmax function

    argmax (z_1, ... ,z_n) = (y_1, ... ,y_n) = (0, ... , 0, 1, 0, ... , 0)

that copes with having k equal max values by distributing the
weight evenly across all k max values.

    softargmax (z_1, ... ,z_n) = (y_1, ... ,y_n) = (... , 1, ... , 1, ...) / k

or

    softargmax (z_1, ... ,z_n) = (y_1, ... ,y_n) = (... , 1/k, ... , 1/k, ...)

Often used in the final layer of a neural network-based classifier.

{% include links.html %}
