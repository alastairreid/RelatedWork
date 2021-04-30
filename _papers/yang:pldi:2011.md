---
ENTRYTYPE: inproceedings
abstract: Compilers should be correct. To improve the quality of C compilers, we created Csmith, a randomized test-case generation tool, and spent three
  years using it to find compiler bugs. During this period we reported more than 325 previously unknown bugs to compiler developers. Every compiler we tested
  was found to crash and also to silently generate wrong code when presented with valid input. In this paper we present our compiler-testing tool and the
  results of our bug-hunting study. Our first contribution is to advance the state of the art in compiler testing. Unlike previous tools, Csmith generates
  programs that cover a large subset of C while avoiding the undefined and unspecified behaviors that would destroy its ability to automatically find wrong-code
  bugs. Our second contribution is a collection of qualitative and quantitative results about the bugs we have found in open-source C compilers.
added: 2021-04-30
address: New York, NY, USA
authors:
- Xuejun Yang
- Yang Chen
- Eric Eide
- John Regehr
booktitle: Proceedings of the 32nd ACM SIGPLAN Conference on Programming Language Design and Implementation
doi: 10.1145/1993498.1993532
isbn: '9781450306638'
keywords: compiler defect, random program generation, automated testing, compiler testing, random testing
layout: paper
link: https://doi.org/10.1145/1993498.1993532
location: San Jose, California, USA
numpages: '12'
pages: 283-294
publisher: Association for Computing Machinery
read: false
readings: []
series: PLDI '11
title: Finding and understanding bugs in C compilers
url: https://doi.org/10.1145/1993498.1993532
year: 2011
notes:
- differential testing
papers:
---
{% include links.html %}
