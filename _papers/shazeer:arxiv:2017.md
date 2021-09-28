---
ENTRYTYPE: misc
added: 2021-09-27
archiveprefix: arXiv
authors:
- Noam Shazeer
- Azalia Mirhoseini
- Krzysztof Maziarz
- Andy Davis
- Quoc Le
- Geoffrey Hinton
- Jeff Dean
eprint: '1701.06538'
layout: paper
primaryclass: cs.LG
read: true
readings:
- 2021-09-27
title: 'Outrageously large neural networks: The sparsely-gated mixture-of-experts layer'
year: 2017
notes:
- mixture of experts
- machine learning
- neural network
- gating network
- CNN
- LSTM
- NLP
- google
papers:
---

Achieves efficiency (and, hence, scaling) by using a [mixture of experts] approach
with thousands of experts and exploiting sparsity in the [gating network] where
at most k experts are selected.

There are tricks in how the work is distributed and implemented to make learning efficient
that exploit the nature of [CNN]s.

They use two loss functions.
One encourages all experts to have equal importance.
The other encourages load balancing across experts.

They evaluate on a "billion word language model" consisting of shuffled unique
sentences from news articles containing 829 million words and a vocabulary of
793,471 words.  They trained models consisting of two stacked [LSTM] layers
with a [mixture of experts] layer between them and vary the sizes of layers and
the number of experts from 4 to 4096 where each expert consists of around 8 million MACs per
training example per timestep in the forward pass and 4 experts are active per
input.
Comparing models by size (number of parameters), this method gives similar perplexity compared
with a straight LSTM approach.
Comparing models by computational complexity, this method gives 24% lower (better) perplexity
for the same computational effort.

The also evaluated on a "100 billion word" news corpus, bilingual machine translation, multilingual machine translation,

{% include links.html %}
