---
ENTRYTYPE: inproceedings
abstract: Modern static bug finding tools are complex. They typically consist of hundreds of thousands of lines of code, and most of them are wedded to
  one language (or even one compiler). This complexity makes the systems hard to understand, hard to debug, and hard to retarget to new languages, thereby
  dramatically limiting their scope. This paper reduces checking system complexity by addressing a fundamental assumption, the assumption that checkers
  must depend on a full-blown language specification and compiler front end. Instead, our program checkers are based on drastically incomplete language
  grammars ("micro-grammars") that describe only portions of a language relevant to a checker. As a result, our implementation is tiny-roughly 2500 lines
  of code, about two orders of magnitude smaller than a typical system. We hope that this dramatic increase in simplicity will allow people to use more
  checkers on more systems in more languages.We implement our approach in \mu chex, a language-agnostic framework for writing static bug checkers. We use
  it to build micro-grammar based checkers for six languages (C, the C preprocessor, C++, Java, JavaScript, and Dart) and find over 700 errors in real-world
  projects.
added: 2021-04-29
address: New York, NY, USA
authors:
- Fraser Brown
- Andres Nötzli
- Dawson Engler
booktitle: Proceedings of the Twenty-First International Conference on Architectural Support for Programming Languages and Operating Systems
doi: 10.1145/2872362.2872364
isbn: '9781450340915'
keywords: bug finding, micro-grammars, parsing, static analysis
layout: paper
link: https://doi.org/10.1145/2872362.2872364
location: Atlanta, Georgia, USA
numpages: '15'
pages: 143-157
publisher: Association for Computing Machinery
read: false
readings: []
series: ASPLOS '16
title: How to build static checking systems using orders of magnitude less code
url: https://doi.org/10.1145/2872362.2872364
year: 2016
notes:
papers:
---
{% include links.html %}
