---
ENTRYTYPE: inproceedings
abstract: Both static and dynamic program verification approaches have significant disadvantages when considered in isolation. Inspired by research on gradual
  typing, we propose gradual verification to seamlessly and flexibly combine static and dynamic verification. Drawing on general principles from abstract
  interpretation, and in particular on the recent Abstracting Gradual Typing methodology of Garcia et al., we systematically derive a gradual verification
  system from a static one. This approach yields, by construction, a gradual verification system that is compatible with the original static system, but
  overcomes its rigidity by resorting to dynamic verification when desired. As with gradual typing, the programmer can control the trade-off between static
  and dynamic checking by tuning the (im)precision of pre- and postconditions. The formal semantics of the gradual verification system and the proofs of
  its properties, including the gradual guarantees of Siek et al., have been fully mechanized in the Coq proof assistant.
added: 2020-11-09
address: Cham
authors:
- Johannes Bader
- Jonathan Aldrich
- Éric Tanter
booktitle: Verification, Model Checking, and Abstract Interpretation
editor: Dillig, Isil and Palsberg, Jens
isbn: 978-3-319-73721-8
layout: paper
pages: 25-46
publisher: Springer International Publishing
read: false
readings: []
title: Gradual program verification
year: 2018
notes:
papers:
---
{% include links.html %}
