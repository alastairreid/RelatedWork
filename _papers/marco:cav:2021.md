---
ENTRYTYPE: inproceedings
abstract: Most existing program verifiers check trace properties such as functional correctness, but do not support the verification of hyperproperties,
  in particular, information flow security. In principle, product programs allow one to reduce the verification of hyperproperties to trace properties and,
  thus, apply standard verifiers to check them; in practice, product constructions are usually defined only for simple programming languages without features
  like dynamic method binding or concurrency and, consequently, cannot be directly applied to verify information flow security in a full-fledged language.
  However, many existing verifiers encode programs from source languages into simple intermediate verification languages, which opens up the possibility
  of constructing a product program on the intermediate language level, reusing the existing encoding and drastically reducing the effort required to develop
  new verification tools for information flow security.
added: 2021-09-22
address: Cham
authors:
- Marco Eilers
- Severin Meier
- Peter Müller
booktitle: Computer Aided Verification
editor: Silva, Alexandra and Leino, K. Rustan M.
isbn: 978-3-030-81685-8
layout: paper
pages: 718-741
publisher: Springer International Publishing
read: false
readings: []
title: 'Product programs in the wild: Retrofitting program verifiers to check information flow security'
year: 2021
notes:
- information flow
- self composition
papers:
---
{% include links.html %}
