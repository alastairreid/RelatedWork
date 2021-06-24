---
ENTRYTYPE: article
added: 2020-03-04
address: New York, NY, USA
articleno: Article 19
authors:
- Lau Skorstengaard
- Dominique Devriese
- Lars Birkedal
doi: 10.1145/3290332
issue_date: January 2019
journal: Proc. ACM Program. Lang.
keywords: linear capabilities, fully abstract overlay semantics, secure compilation,
  well-bracketed control flow, stack frame encapsulation, fully abstract compilation,
  capability machines
layout: paper
month: January
number: POPL
numpages: '28'
publisher: Association for Computing Machinery
read: true
readings:
- 2020-03-03
title: 'StkTokens: Enforcing well-bracketed control flow and stack encapsulation using
  linear capabilities'
url: https://doi.org/10.1145/3290332
volume: '3'
year: 2019
topics:
- security
- verification
notes:
- hardware
- CHERI architecture
- capabilities
papers:
- skorstengaard:esop:2018
---

This paper follows on from
[an earlier paper by the same authors][skorstengaard:esop:2018]
that looked at how mutually distrusting pieces of code could safely call each other.
In particular, it was concerned about whether the stack and return address were what the caller expected when they called the function.

The earlier paper relied on capability machines that provided “local capabilities” and a primitive for clearing the stack on function return.
This paper relies on capability machines that provide “linear capabilities”.
Linear capabilities are interesting because they cannot be duplicated: if you attempt to copy a linear capability then the source copy is erased.
A consequence of this is that linear capabilities support two extra operations: “split” to partition the memory region accessible by a capability and “splice” to merge two adjacent capabilities back into a single capability.
They make essential use of “splice” as part of enforcing that a callee has returned the entire stack when it returns.

The earlier paper showed how to reason about some example code.
This paper develops “fully abstract overlay semantics” which is an alternative semantics for machine code that has an explicit stack and restricts the code to only use the stack in the way that a compiler might expect.
By doing this, they define what they mean by “well bracketed control flow” and they explicitly link the property that they prove to the requirements that a compiler might have on the code.
Nice!

{% include links.html %}
