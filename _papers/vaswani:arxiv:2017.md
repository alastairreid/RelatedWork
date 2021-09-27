---
ENTRYTYPE: misc
added: 2021-09-27
archiveprefix: arXiv
authors:
- Ashish Vaswani
- Noam Shazeer
- Niki Parmar
- Jakob Uszkoreit
- Llion Jones
- Aidan N. Gomez
- Lukasz Kaiser
- Illia Polosukhin
eprint: '1706.03762'
layout: paper
primaryclass: cs.CL
read: true
readings:
- 2021-09-27
title: Attention is all you need
year: 2017
notes:
- neural network
- encoder-decoder model
- transformer model
- attention function
- LSTM
- BLEU
- google
papers:
---

Introduced the [transformer model] and replacing the recurrent layers
entirely with [attention][attention function]
to improve efficiency.

Uses multi-head [attention][attention function] in [encoder-decoder][encoder-decoder model]
layers, self-attention layers in the encoder
and attention layers that avoid leftward information flow.
Uses sin/cos functions of varying frequencies to encode position.

Evaluated on English-French and English-German translation tasks and
improving the previous best [BLEU] score by 2.0%
and on English constituency parsing.

{% include links.html %}
