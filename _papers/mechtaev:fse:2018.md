---
ENTRYTYPE: inproceedings
abstract: Symbolic execution systematically explores program paths by solving path conditions -- formulas over symbolic variables. Typically, the symbolic
  variables range over numbers, arrays and strings. We introduce symbolic execution with existential second-order constraints -- an extension of traditional
  symbolic execution that allows symbolic variables to range over functions whose interpretations are restricted by a user-defined language. The aims of
  this new technique are twofold. First, it offers a general analysis framework that can be applied in multiple domains such as program repair and library
  modelling. Secondly, it addresses the path explosion problem of traditional first-order symbolic execution in certain applications. To realize this technique,
  we integrate symbolic execution with program synthesis. Specifically, we propose a method of second-order constraint solving that provides efficient proofs
  of unsatisfiability, which is critical for the performance of symbolic execution. Our evaluation shows that the proposed technique (1) helps to repair
  programs with loops by mitigating the path explosion, (2) can enable analysis of applications written against unavailable libraries by modelling these
  libraries from the usage context.
added: 2021-02-25
address: New York, NY, USA
authors:
- Sergey Mechtaev
- Alberto Griggio
- Alessandro Cimatti
- Abhik Roychoudhury
booktitle: Proceedings of the 2018 26th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering
doi: 10.1145/3236024.3236049
isbn: '9781450355735'
keywords: Library modelling, Program repair, Program synthesis
layout: paper
link: https://doi.org/10.1145/3236024.3236049
location: Lake Buena Vista, FL, USA
numpages: '11'
pages: 389-399
publisher: Association for Computing Machinery
read: false
readings: []
series: ESEC/FSE 2018
title: Symbolic execution with existential second-order constraints
url: https://doi.org/10.1145/3236024.3236049
year: 2018
notes:
- symbolic execution
papers:
---
{% include links.html %}
