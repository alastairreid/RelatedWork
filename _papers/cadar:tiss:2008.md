---
ENTRYTYPE: article
abstract: 'This article presents EXE, an effective bug-finding tool that automatically generates inputs that crash real code. Instead of running code on
  manually or randomly constructed input, EXE runs it on symbolic input initially allowed to be anything. As checked code runs, EXE tracks the constraints
  on each symbolic (i.e., input-derived) memory location. If a statement uses a symbolic value, EXE does not run it, but instead adds it as an input-constraint;
  all other statements run as usual. If code conditionally checks a symbolic expression, EXE forks execution, constraining the expression to be true on
  the true branch and false on the other. Because EXE reasons about all possible values on a path, it has much more power than a traditional runtime tool:
  (1) it can force execution down any feasible program path and (2) at dangerous operations (e.g., a pointer dereference), it detects if the current path
  constraints allow any value that causes a bug. When a path terminates or hits a bug, EXE automatically generates a test case by solving the current path
  constraints to find concrete values using its own co-designed constraint solver, STP. Because EXE''s constraints have no approximations, feeding this
  concrete input to an uninstrumented version of the checked code will cause it to follow the same path and hit the same bug (assuming deterministic code).EXE
  works well on real code, finding bugs along with inputs that trigger them in: the BSD and Linux packet filter implementations, the dhcpd DHCP server,
  the pcre regular expression library, and three Linux file systems.'
added: 2021-06-13
address: New York, NY, USA
articleno: '10'
authors:
- Cristian Cadar
- Vijay Ganesh
- Peter M. Pawlowski
- David L. Dill
- Dawson R. Engler
doi: 10.1145/1455518.1455522
issn: 1094-9224
issue_date: December 2008
journal: ACM Trans. Inf. Syst. Secur.
keywords: constraint solving, symbolic execution, attack generation, dynamic analysis, test case generation, bug finding
layout: paper
link: https://doi.org/10.1145/1455518.1455522
month: December
number: '2'
numpages: '38'
publisher: Association for Computing Machinery
read: false
readings: []
title: 'EXE: Automatically Generating Inputs of Death'
url: https://doi.org/10.1145/1455518.1455522
volume: '12'
year: 2008
notes:
papers:
---
{% include links.html %}
