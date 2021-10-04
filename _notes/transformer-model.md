---
layout: note
notes:
- neural network
- auto-encoder model
- attention function
- RNN
- LSTM
- NLP
wiki: https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)
papers:
- vaswani:arxiv:2017
title: Transformer machine learning model
---

In natural language processing ([NLP]), transformers replace sequential RNN/LSTM models
with more parallel models by using [attention function]s.
This solves the problem seen in LSTMs that the first words of the sentence
are often lost. In LSTMs, this is solved by adding an attention mechanism;
the idea of transformers is that the attention mechanism is enough and you
don't need the LSTM.

The attention mechanism weights the importance of each token on every other token.
This is used to reduce the number of operations required to relate signals from two arbitrary
input or output positions from linear in their distance to constant which makes it easier to
learn dependencies between distant positions.




There can be multiple "attention heads": one that weights nearby words, one that weights
the impact of the verb, ...

Used in pretrained models such as GPT-2, GPT-3, BERT, XLNet and ROBERTa.



{% include links.html %}
