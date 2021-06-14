---
ENTRYTYPE: inproceedings
abstract: Symbolic execution has become a popular technique for software testing and vulnerability detection. Most implementations transform the program
  under analysis to some intermediate representation (IR), which is then used as a basis for symbolic execution. There is a multitude of available IRs,
  and even more approaches to transform target programs into a respective IR.When developing a symbolic execution engine, one needs to choose an IR, but
  it is not clear which influence the IR generation process has on the resulting system. What are the respective benefits for symbolic execution of generating
  IR from source code versus lifting machine code? Does the distinction even matter? What is the impact of not using an IR, executing machine code directly?
  We feel that there is little scientific evidence backing the answers to those questions. Therefore, we first develop a methodology for systematic comparison
  of different approaches to symbolic execution; we then use it to evaluate the impact of the choice of IR and IR generation. We make our comparison framework
  available to the community for future research.
added: 2021-06-13
address: New York, NY, USA
authors:
- Sebastian Poeplau
- Aurélien Francillon
booktitle: Proceedings of the 35th Annual Computer Security Applications Conference
doi: 10.1145/3359789.3359796
isbn: '9781450376280'
keywords: symbolic execution, intermediate representation
layout: paper
link: https://doi.org/10.1145/3359789.3359796
location: San Juan, Puerto Rico, USA
numpages: '14'
pages: 163-176
publisher: Association for Computing Machinery
read: false
readings: []
series: ACSAC '19
title: 'Systematic comparison of symbolic execution systems: Intermediate representation and its generation'
url: https://doi.org/10.1145/3359789.3359796
year: 2019
notes:
- symbolic execution
- hybrid testing
papers:
- poeplau:usenix:2020
---
{% include links.html %}
