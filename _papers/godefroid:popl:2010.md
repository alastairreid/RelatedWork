---
ENTRYTYPE: inproceedings
abstract: 'Program analysis tools typically compute two types of information: (1) may information that is true of all program executions and is used to
  prove the absence of bugs in the program, and (2) must information that is true of some program executions and is used to prove the existence of bugs
  in the program. In this paper, we propose a new algorithm, dubbed SMASH, which computes both may and must information compositionally . At each procedure
  boundary, may and must information is represented and stored as may and must summaries, respectively. Those summaries are computed in a demand driven
  manner and possibly using summaries of the opposite type. We have implemented SMASH using predicate abstraction (as in SLAM) for the may part and using
  dynamic test generation (as in DART) for the must part. Results of experiments with 69 Microsoft Windows 7 device drivers show that SMASH can significantly
  outperform may-only, must-only and non-compositional may-must algorithms. Indeed, our empirical results indicate that most complex code fragments in large
  programs are actually often either easy to prove irrelevant to the specific property of interest using may analysis or easy to traverse using directed
  testing. The fine-grained coupling and alternation of may (universal) and must (existential) summaries allows SMASH to easily navigate through these code
  fragments while traditional may-only, must-only or non-compositional may-must algorithms are stuck in their specific analyses.'
added: 2021-05-16
address: New York, NY, USA
authors:
- Patrice Godefroid
- Aditya V. Nori
- Sriram K. Rajamani
- Sai Deep Tetali
booktitle: Proceedings of the 37th Annual ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages
doi: 10.1145/1706299.1706307
isbn: '9781605584799'
keywords: software model checking, directed testing, abstraction refinement
layout: paper
link: https://doi.org/10.1145/1706299.1706307
location: Madrid, Spain
numpages: '14'
pages: 43-56
publisher: Association for Computing Machinery
read: false
readings: []
series: POPL '10
title: 'Compositional may-must program analysis: Unleashing the power of alternation'
url: https://doi.org/10.1145/1706299.1706307
year: 2010
notes:
- model checking
- under-approximation
- over-approximation
papers:
---
{% include links.html %}
