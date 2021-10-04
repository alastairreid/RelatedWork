---
ENTRYTYPE: misc
added: 2021-09-30
archiveprefix: arXiv
authors:
- Trevor Gale
- Erich Elsen
- Sara Hooker
eprint: '1902.09574'
layout: paper
primaryclass: cs.LG
read: true
readings:
- 2021-10-04
title: The state of sparsity in deep neural networks
year: 2019
notes:
- neural network
- sparse model
- google
papers:
---

About techniques for learning [sparse model]s either by learning a model and then
making it sparse or by modifying how the initial model is learned
or by using a sparse architecture for the model.

They reimplement three techniques and do a massive analysis of the different techniques at
different sparsity levels.

Main takeaway seems to be that magnitude pruning is the winner.
Also, there is a lot of "tuning hyperparameters" in some of the other techniques.

{% include links.html %}
