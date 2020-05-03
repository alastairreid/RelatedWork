---
ENTRYTYPE: inproceedings
added: 2020-01-08
address: New York, NY, USA
authors:
- David Walker
booktitle: Proceedings of the 27th ACM SIGPLAN-SIGACT Symposium on Principles of Programming
  Languages
doi: 10.1145/325694.325728
isbn: '1581131259'
layout: paper
location: Boston, MA, USA
numpages: '14'
pages: 254–267
publisher: Association for Computing Machinery
read: true
readings:
- 2020-01-13
series: "POPL'00"
title: A type system for expressive security policies
url: https://doi.org/10.1145/325694.325728
year: 2000
topics:
- security
- types
notes:
- typed assembly language
---

These days, many people define security properties based on
some form of intransitive information flow specification.
But in the '90s, Fred Schneider and others were working on
security automata that would monitor the execution of the
program and terminate it if the program violated
the security specification.
For example, a specification might say that if a program
has read a file containing a secret, it cannot then
open a network connection.

This paper builds on work on [Typed Assembly Language]({{ "papers/morrisett:wcsss:1999" | relative_url }})
to develop rich, expressive type systems to capture
security properties in a type system instead of via
some more ad hoc approach.

At first sight, this merely repeats the work of Schneider
in a different formalism:
they enforce the security policy by inserting the automata
and the checks into the code and then they optimize away
any of the checks that they can show will not fail.
But the key benefit of doing this within a typesystem
is that the transformed code and each step in the optimization can be
typechecked to show that it still enforces the security
policy.
That is, when a check is removed, the system is required to leave enough of
a residue in the code that you can see why the check was
not required.
As a result of this, anyone who receives the code can confirm
that the code will obey the security policy just by
typechecking the code.

{% include links.html %}
