---
layout: note
title: Contract driven development
wiki: https://en.wikipedia.org/wiki/Design_by_contract
---

Contract driven development
is a development methodology where you write a contract for a function/method/class
before implementing it.

Name comes from Bertrand Meyer's paper [meyer:fase:2007].

In a formal verification context, this is often synonymous with [modular verification].

The approach of defining the desired behaviour before implementing the
behaviour bears some resemblance to [test driven development].

Formal verification papers:
[logozzo:vmcai:2011],
[fahndrich:foveoos:2010]

[modular verification]: {{ "notes/modular-verification" | relative_url }}
[test driven development]: {{ "notes/test-driven-development" | relative_url }}
[meyer:fase:2007]: https://doi.org/10.1007/978-3-540-71289-3_2
[logozzo:vmcai:2011]: {{ "papers/logozzo:vmcai:2011" | relative_url }}
[fahndrich:foveoos:2010]: {{ "papers/fahndrich:foveoos:2010" | relative_url }}
