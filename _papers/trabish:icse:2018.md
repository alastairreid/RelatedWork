---
ENTRYTYPE: inproceedings
abstract: Symbolic execution is a powerful program analysis technique that systematically explores multiple program paths. However, despite important technical
  advances, symbolic execution often struggles to reach deep parts of the code due to the well-known path explosion problem and constraint solving limitations.In
  this paper, we propose chopped symbolic execution, a novel form of symbolic execution that allows users to specify uninteresting parts of the code to
  exclude during the analysis, thus only targeting the exploration to paths of importance. However, the excluded parts are not summarily ignored, as this
  may lead to both false positives and false negatives. Instead, they are executed lazily, when their effect may be observable by code under analysis. Chopped
  symbolic execution leverages various on-demand static analyses at runtime to automatically exclude code fragments while resolving their side effects,
  thus avoiding expensive manual annotations and imprecision.Our preliminary results show that the approach can effectively improve the effectiveness of
  symbolic execution in several different scenarios, including failure reproduction and test suite augmentation.
added: 2021-02-24
address: New York, NY, USA
authors:
- David Trabish
- Andrea Mattavelli
- Noam Rinetzky
- Cristian Cadar
booktitle: Proceedings of the 40th International Conference on Software Engineering
doi: 10.1145/3180155.3180251
isbn: '9781450356381'
keywords: symbolic execution, static analysis, program slicing
layout: paper
link: https://doi.org/10.1145/3180155.3180251
location: Gothenburg, Sweden
numpages: '11'
pages: 350-360
publisher: Association for Computing Machinery
read: false
readings: []
series: ICSE '18
title: Chopped symbolic execution
url: https://doi.org/10.1145/3180155.3180251
year: 2018
notes:
- symbolic execution
- KLEE verifier
papers:
---
{% include links.html %}
