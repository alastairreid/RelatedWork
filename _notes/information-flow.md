---
layout: note
title: Information flow
wiki: https://en.wikipedia.org/wiki/Information_flow_(information_theory)
notes:
- self-composition
---

todo: refactor this note

Information flow checks are a form of security checks that track where
information is flowing from and to and under which circumstances.
It can be performed as a dynamic check on a single execution ("taint tracking")
or as a static analysis that typically compares results on two or more
executions.

A distinction is often made before "explicit" information flow (e.g., "x = y;")
and "implicit" information flow (e.g., "if y then x = 1;" which has an
information flow from y to x even if y is False).  This distinction reflects
a classic weakness of taint tracking approaches that dynamically tag values
with metadata during an execution and, because they are based on a single
execution, are unable to accurately track information flows in the paths that
are not executed.

Some topics are

-  Declassification
-  Cryptography
-  Operating Systems
-  Languages
   - Type-based information flow checking
   - Self-composition
-  Hardware
-  Systems
-  Quantitative

## Papers about information flow

{% include paperlist.html %}

{% include links.html %}
