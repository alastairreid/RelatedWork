---
ENTRYTYPE: inproceedings
added: 2020-09-10
address: New York, NY, USA
authors:
- Caitlin Sadowski
- Emma Söderberg
- Luke Church
- Michal Sipko
- Alberto Bacchelli
booktitle: 'Proceedings of the 40th International Conference on Software Engineering: Software Engineering in Practice'
doi: 10.1145/3183519.3183525
isbn: '9781450356596'
layout: paper
link: https://doi.org/10.1145/3183519.3183525
location: Gothenburg, Sweden
numpages: '10'
pages: 181-190
publisher: Association for Computing Machinery
read: true
readings:
- 2020-09-23
series: ICSE-SEIP '18
title: 'Modern code review: A case study at Google'
url: https://doi.org/10.1145/3183519.3183525
year: 2018
notes:
- google
- usability
papers:
- potvin:cacm:2016
- sadowski:cacm:2018
---

Code review goes back to heavyweight practices in the '70s but this paper looks
at modern, lightweight review as practiced at Google since the early days.
Modern code review is

- informal
- tool-based
- asynchronous
- focused on reviewing code changes

Although finding bugs is important, much more important are

- normative effects: bringing consistency to the codebase
- educational effects: making sure that more than one person
  knows the code
- improving test quality
- accident prevention
- gatekeeping to protect other team's codebases

The paper highlights the importance of the relationship between the author of
a change and the reviewer. Several relationships can exist and affect the
expectations of the review.

- Project lead: education, maintaining norms
- New team members: education, maintaining norms
- Other team members: education, accident prevention
- Readability reviewers: maintaining norms
- Other teams: gatekeeping

Some distinctive features of Google's approach and tools (compared
with OSS, Microsoft and other review processes)

- the first review comments come fast
- changes are smaller
- often just one reviewer (most other processes have two)
- clearly defined expectations from review
- the tool recommends reviewer choice based on ownership,
  review load, availability, etc.
- integration of static analysis checks ([sadowski:cacm:2018])


One thing I did not understand about the paper was why they used
[snowball sampling](https://en.wikipedia.org/wiki/Snowball_sampling)
for the interviews they performed.
Wikipedia says that this is normally used for hidden populations
like drug addicts that are hard to identify but it is easy to generate
a list of reviewers, change authors, etc.

{% include links.html %}
