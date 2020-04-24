---
ENTRYTYPE: inproceedings
added: 2020-03-14
address: New York, NY, USA
articleno: Article 1
authors:
- Stefan Heule
- K. Rustan M. Leino
- Peter Müller
- Alexander J. Summers
booktitle: Proceedings of the 13th Workshop on Formal Techniques for Java-Like Programs
doi: 10.1145/2076674.2076675
isbn: '9781450308939'
keywords: static verification, concurrency, fractional permissions
layout: paper
location: Lancaster, United Kingdom
numpages: '6'
publisher: Association for Computing Machinery
read: true
readings:
- 2020-03-14
series: FTfJP '11
title: Fractional permissions without the fractions
url: https://doi.org/10.1145/2076674.2076675
year: 2011
topics:
- permission-logic
- tools
- verification
notes:
- permission-logic
- chalice-verifier
- fractional-permissions
- permissions-accounting
---

The standard way of distinguishing read and write permissions
in separation logic is with
[fractional permissions]({{ "papers/bornat:popl:2005" | relative_url }})
in which you can write a resource if you have 100% of the resource
read a resource if you have some fraction of the resource
and you have no access if you have 0% of the resource.
When you replicate references to a resource, you split the
fraction into some smaller parts and when you are done with those
references, you recombine (sum) all their fractions.

Whilst this is intuitively appealing, in practice you find yourself
making arbitrary choices about the size of each fraction
and, if you add another use of a resource, you might need to update
the existing choice of fractions from "p/2" (say) to "p/3".

This paper describes an experimental version of the [Chalice verifier] which
directly encodes the notion of "read permission" as a read
instead of having to encode it as a fraction of an access.
They end up with six different forms of permission:

- 1 - a full permission (allowing both reads and writes)
- rd - read permission
- rd(tok) - a token read permission (used for asynchronous method calls)
- rd(o) - monitor read permission (used for monitor calls)
- P1 + P2 - combining permissions
- P1 - P2 - removing permissions

[Chalice verifier]: {{ "notes/chalice-verifier" | relative_url }}
