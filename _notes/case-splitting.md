---
layout: note
title: Case splitting
notes:
- symbolic execution
- model checking
- symbolic evaluation
- state merging
- swarm verification
papers:
- goodman:ndss:2018
- bornholt:oopsla:2018
- holzmann:ieeetse:2011
---

In formal verification, case splitting consists of separately considering
different cases.

In [symbolic evaluation], case splitting introduces multiple paths where some
variable has a different concrete value on each path.
This allows more efficient reasoning about concrete values and can work
past issues that would be hard for a solver to handle such as non-linearity, etc.

{% include links.html %}
