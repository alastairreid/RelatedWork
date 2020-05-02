---
layout: note
title: Fractional permissions
papers:
- bornat:popl:2005
- heule:ftfjp:2011
notes:
- separation logic
- permission logic
- permission accounting
---

Fractional permissions
is trick used in [separation logic]
and its generalization [permission logic] to
for [permission accounting].
That is, to track the notion of sharing a resource.
The idea is to distinguish between

- owning 100% of a resource that allows you to do anything with it: read/write/delete.
- having several owners of a resource that might each own 50%, 25% and 25%
  (say) of the resource and can only read the resource.

Adapted for [separation logic] by [bornat:popl:2005].
Later, [heule:ftfjp:2011] developed a variation that avoids the sometimes ad hoc
choice of what fractions to use.



{% include links.html %}
