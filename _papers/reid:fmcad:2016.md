---
ENTRYTYPE: inproceedings
abstract: 'Processor specifications are of critical importance for verifying programs, compilers, operating systems/hypervisors, and, of course, for verifying
  microprocessors themselves.  But to be useful, the scope of these specifications must be sufficient for the task, the specification must be applicable
  to processors of interest and the specification must be trustworthy.  This paper describes a 5 year project to change ARM''s existing architecture specification
  process so that machine-readable, executable specifications can be automatically generated from the same materials used to generate ARM''s conventional
  architecture documentation.  We have developed executable specifications of both ARM''s A-class and M-class processor architectures that are complete
  enough and trustworthy enough that we have used them to formally verify ARM processors using bounded model checking.  In particular, our specifications
  include the semantics of the most security sensitive parts of the processor: the memory and register protection mechanisms and the exception mechanisms
  that trigger transitions between different modes.  Most importantly, we have applied a diverse set of methods including ARM''s internal processor test
  suites to improve our trust in the specification using many other expressions of the architectural specification such as ARM''s simulators, testsuites
  and processors to defend against common-mode failure.  In the process, we have also found bugs in all those artifacts: testing specifications is very
  much a two-way street.  While there have been previous specifications of ARM processors, their scope has excluded the system architecture, their applicability
  has excluded newer processors and M-class, and their trustworthiness has not been established as thoroughly.  Our focus has been on enabling the formal
  verification of ARM processors but, recognising the value of this specification for verifying software, we are currently preparing a public release of
  the machine-readable specification.'
added: 2019-06-01
affiliation: ARM Ltd
ar_shortname: FMCAD 16
authors:
- Alastair D. Reid
booktitle: Proceedings of Formal Methods in Computer-Aided Design (FMCAD 2016)
isbn: 978-0-9835678-6-8
layout: paper
link: https://alastairreid.github.io/papers/fmcad2016-trustworthy.pdf
location: Mountain View, CA, USA
month: October
pages: 161-168
read: false
readings: []
title: Trustworthy specifications of ARM v8-A and v8-M system level architecture
url: https://alastairreid.github.io/papers/fmcad2016-trustworthy.pdf
year: 2016
topics:
notes:
- Arm architecture
- ISA specification
- instruction set architecture
- dependent type
- type inference
- ASL
papers:
---

{% include links.html %}
