---
ENTRYTYPE: inproceedings
abstract: Separation logic is a powerful tool for reasoning about structured, imperative programs that manipulate pointers. However, its application to
  unstructured, lower-level languages such as assembly language or machine code remains challenging. In this paper we describe a separation logic tailored
  for this purpose that we have applied to x86 machine-code programs.The logic is built from an assertion logic on machine states over which we construct
  a specification logic that encapsulates uses of frames and step indexing. The traditional notion of Hoare triple is not applicable directly to unstructured
  machine code, where code and data are mixed together and programs do not in general run to completion, so instead we adopt a continuation-passing style
  of specification with preconditions alone. Nevertheless, the range of primitives provided by the specification logic, which include a higher-order frame
  connective, a novel read-only frame connective, and a 'later' modality, support the definition of derived forms to support structured-programming-style
  reasoning for common cases, in which standard rules for Hoare triples are derived as lemmas. Furthermore, our encoding of scoped assembly-language labels
  lets us give definitions and proof rules for powerful assembly-language 'macros' such as while loops, conditionals and procedures.We have applied the
  framework to a model of sequential x86 machine code built entirely within the Coq proof assistant, including tactic support based on computational reflection.
added: 2021-11-22
address: New York, NY, USA
authors:
- Jonas B. Jensen
- Nick Benton
- Andrew Kennedy
booktitle: Proceedings of the 40th Annual ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages
doi: 10.1145/2429069.2429105
isbn: '9781450318327'
keywords: proof assistants, separation logic, machine code
layout: paper
link: https://doi.org/10.1145/2429069.2429105
location: Rome, Italy
numpages: '14'
pages: 301-314
publisher: Association for Computing Machinery
read: false
readings: []
series: POPL '13
title: High-level separation logic for low-level code
url: https://doi.org/10.1145/2429069.2429105
year: 2013
notes:
- Separation logic
- ISA specification
- Instruction Set Architecture
- x86 Architecture
papers:
- kennedy:ppdp:2013
---
{% include links.html %}
