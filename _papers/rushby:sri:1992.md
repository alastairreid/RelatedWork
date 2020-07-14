---
ENTRYTYPE: techreport
layout: paper
added: 2019-10-06
title: Noninterference, transitivity, and channel-control security policies
author: Rushby, John
year: 1992
publisher: SRI International, Computer Science Laboratory Menlo Park
topics:
- security
read: true
readings:
- 2019-10-11
notes:
- information flow
papers:
- goguen:secpriv:1982
---

This very highly cited report provides (what I think is) the accepted extension of [Goguen and Meseguer's notion of interference][goguen:secpriv:1982] to handle intransitive security policies.

The report is written in the style of a tutorial that discusses a range of competing/contributing ideas from the time, combines them into a consistent framework, proves results about the definitions and illustrates strengths/weaknesses with examples.
Some important results relate their definitions to multilevel security policies (MLS).

One of the key examples for intransitivity involves a 4-level security policy with a component that is able to downgrade top-secret documents to confidential.
Clearly, it is ok for top-secret documents to be sent to the downgrader and for the downgrader to send documents to confidential locations but it is not ok to send top-secret documents directly to confidential locations.

In addition to the basic definitions, they provide the "unwinding conditions" required to prove that a system satisfies a given security policy and all formal statements are backed up by mechanised proofs (in a companion report).

One purpose of the report to provide a definition of intransitive interference for which it is easy to show that transitive interference is a special case.

{% include links.html %}
