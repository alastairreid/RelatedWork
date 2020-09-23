---
ENTRYTYPE: article
abstract: Google's monolithic repository provides a common source of truth for tens of thousands of developers around the world.
added: 2020-09-19
address: New York, NY, USA
authors:
- Rachel Potvin
- Josh Levenberg
doi: 10.1145/2854146
issn: 0001-0782
issue_date: July 2016
journal: Communications of the ACM
layout: paper
link: https://doi.org/10.1145/2854146
month: June
number: '7'
numpages: '10'
pages: 78-87
publisher: Association for Computing Machinery
read: true
readings:
- 2020-09-21
title: Why Google stores billions of lines of code in a single repository
url: https://doi.org/10.1145/2854146
volume: '59'
year: 2016
notes:
- google
papers:
- corbett:tocs:2013
- sadowski:icse:2015
- sadowski:cacm:2018
- sadowski:icse-seip:2018
---

This paper describes Google's monorepo approach to managing source code in
a single repository, the pros, the cons and what was needed to support this
approach.

Since there is a lot of code (1 billion lines in January 2015) Google developed
"Piper" – their own source code version control system (because Perforce was no
longer scaling).
Piper is built on top of the Spanner database ([corbett:tocs:2013]).

Google practices "trunk based development": there are (virtually) no branches
(apart from a few release branches), all new code is merged into the trunk.
This focus on a single trunk avoids the diamond-import problem, lets them focus
testing in one place, ensures that there is only one "true" copy of code, etc.
Besides "piper", some of the tools that take advantage of or support this are

- Critique ([sadowski:icse-seip:2018]) code review system

- CodeSearch

- TriCorder ([sadowski:cacm:2018]) static analysis tools

- automated testing infrastructure

- Clipper to find dead code. (Or maybe to find dependencies?)

The monorepo is organized hierarchially with different owners for different
subtrees of the code. These owners review all code changes affecting their
code.
To support some of the global cleanups that are a strength of monorepos, the
"Rosie" tool splits changes up into separate review requests for each owner.

A key usage pattern with a huge monorepo with many subowners seems to be
accepting that getting all the reviews simultaneously is not going to happen.
So changes to an API (say) are made by first adding support for the new API
with conditional compilation; then gradually turning off all uses of the old
API; then, eventually, deleting the old API and all the inactive calls to it.

{% include links.html %}
