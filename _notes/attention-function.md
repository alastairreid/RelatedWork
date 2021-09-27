---
layout: note
notes:
- neural network
- NLP
- transformer model
- sparse model
papers:
- vaswani:arxiv:2017
title: Attention function
---

From [vaswani:arxiv:2017]

> An attention function can be described as mapping a query and a set of key-value pairs to an output
> where the query, keys, values and output are all vectors.
> The output is computed as the weighted sum of the values, where the weight assigned to
> each value is computed by a compatibility function of the query with the corresponding key.

Multi-head attention consists of having multiple attention functions.
For example, in [NLP] weighting nearby words, verbs, etc.


{% include links.html %}
