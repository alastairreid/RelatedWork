---
ENTRYTYPE: inproceedings
added: 2020-08-11
address: New York, NY, USA
authors:
- Pietro Braione
- Giovanni Denaro
- Andrea Mattavelli
- Mauro Pezzè
booktitle: 'Proceedings of the 40th International Conference on Software Engineering: Companion Proceeedings'
doi: 10.1145/3183440.3183472
isbn: '9781450356633'
keywords: search-based software engineering, symbolic execution, automatic test case generation
layout: paper
link: https://doi.org/10.1145/3183440.3183472
location: Gothenburg, Sweden
numpages: '4'
pages: 21-24
publisher: Association for Computing Machinery
read: true
readings:
- 2020-08-11
series: ICSE '18
title: 'SUSHI: A test generator for programs with complex structured inputs'
url: https://doi.org/10.1145/3183440.3183472
year: 2018
notes:
- search based test generation
- symbolic execution
- fuzz testing
- test generation
- unit tests
papers:
---

[Search based test generation] alone is unable to generate inputs that
have complex structures such as dependencies between different data structures.

This paper uses symbolic execution to capture the missing dependencies and
then transforms this into a fitness function to guide the search for inputs
satisfying the dependencies.

SUSHI implements this for Java and is based on JBSE.

It is evaluated on benchmarks: avl, treemap, caching, tsafe, gantt, clos01, clos72.
And compared against JBSE, Seeker and EvoSuite.
Results with SUSHI seem to be dramatically better.

Future work is automatic synthesis of invariants.

{% include links.html %}
