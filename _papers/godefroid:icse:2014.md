---
ENTRYTYPE: inproceedings
abstract: 'Micro execution is the ability to execute any code fragment without a user-provided test driver or input data. The user simply identifies a function
  or code location in an exe or dll. A runtime Virtual Machine (VM) customized for testing purposes then starts executing the code at that location, catches
  all memory operations before they occur, allocates memory on-the-fly in order to perform those read/write memory operations, and provides input values
  according to a customizable memory policy, which defines what read memory accesses should be treated as inputs. MicroX is a first prototype VM allowing
  micro execution of x86 binary code. No test driver, no input data, no source code, no debug symbols are required: MicroX automatically discovers dynamically
  the Input/Output interface of the code being run. Input values are provided as needed along the execution and can be generated in various ways, e.g.,
  randomly or using some other test-generation tool. To our knowledge, MicroX is the first VM designed for test isolation and generation purposes. This
  paper introduces micro execution and discusses how to implement it, strengths and limitations, applications, related work and long-term goals.'
added: 2021-06-14
address: New York, NY, USA
authors:
- Patrice Godefroid
booktitle: Proceedings of the 36th International Conference on Software Engineering
doi: 10.1145/2568225.2568273
isbn: '9781450327565'
keywords: Virtual Machine, Program Execution, Testing
layout: paper
link: https://doi.org/10.1145/2568225.2568273
location: Hyderabad, India
numpages: '11'
pages: 539-549
publisher: Association for Computing Machinery
read: false
readings: []
series: ICSE 2014
title: Micro execution
url: https://doi.org/10.1145/2568225.2568273
year: 2014
notes:
- lazy initialization
papers:
---
{% include links.html %}
