---
ENTRYTYPE: article
abstract: For a static analysis project to succeed, developers must feel they benefit from and enjoy using it.
added: 2020-09-10
address: New York, NY, USA
authors:
- Caitlin Sadowski
- Edward Aftandilian
- Alex Eagle
- Liam Miller-Cushon
- Ciera Jaspan
doi: 10.1145/3188720
issn: 0001-0782
issue_date: April 2018
journal: Communications of the ACM
layout: paper
link: https://doi.org/10.1145/3188720
month: March
number: '4'
numpages: '9'
pages: 58-66
publisher: Association for Computing Machinery
read: true
readings:
- 2020-09-23
title: Lessons from building static analysis tools at Google
url: https://doi.org/10.1145/3188720
volume: '61'
year: 2018
notes:
- google
papers:
- potvin:cacm:2016
- chou:bugs:2005
- wright:icsm:2013
- sadowski:icse:2015
- babic:fse:2019
---

This paper is an update on their earlier paper ([sadowski:icse:2015]) that
brings the story up to date and fills in some of the background stories about
previous failures that informed their later approach and some of the successes.
Despite the overlap, it is worth reading both of them because the
two articles have a different emphasis and the overlap is not too severe.

Some key things are

- The earlier failed attempt with BugBot tried
  1. A bug dashboard – that was ignored
  2. Filing bugs found by the tool – this did not scale and 84% of bugs were
     not fixed.
  3. Integrating the tool into code review – False positives and allowing
     individuals to customize their warning settings killed it off.
- Integrating checks into the compiler can be highly effective if errors
  fail the build.
  You need a dedicated team who will file fixes against the entire
  Google codebase (which is large [potvin:cacm:2016]) before you can
  enable the check. But, once you can enable the check, it ratchets up
  code quality permanently.
  Can only be used for checks that are
  - easily understood
  - actionable and easy to fix
  - no effective false positives
  - only check for correctness not style or best practice.
    (Because, engineers temporarily deviate while debugging or developing
    new code and we don't want to slow that down).
- Code review checks should have less than 10% effective false positives
  (but still need to be understandable, actionable and easy to fix).
- None of the static analyses are compositional and
  they are not convinced that techniques that work for multi-million line
  repos will scale to multi-billion line repos.
- As long as finding bugs is easy, it is hard to justify investing more
  in deeper analyses.
  (Though Google has since been very active in fuzzing – see [babic:fse:2019]
  for example.)
- "Developer happiness is key"
- "For a static analysis project to succeed, developers must feel they
  benefit from and enjoy using it."
- "Do not just find bugs, fix them": reports must be acted on.
- "Lower the bar to developer-contributed checks"
- "To overcome warning blindness, we have worked to regain the trust
  of Google engineers, ..."

{% include links.html %}
