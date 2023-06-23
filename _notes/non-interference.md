---
wiki: https://en.wikipedia.org/wiki/Non-interference_(security)
layout: note
title: Non-interference
notes:
- information flow
- hyperproperty
- non-leakage
papers:
- goguen:secpriv:1982
- goguen:secpriv:1984
- rushby:sri:1992
- bowman:icfp:2015
- costanzo:pldi:2016
- ferraiuolo:sosp:2017
- nelson:sosp:2019
- nelson:osr:2020
- tiwari:isca:2009
---

A good intro is the first few pages of [nelson:osr:2020] --- but after that,
it gets a bit denser.

Some key decisions in choosing a non-interference framework to use are:

- do you want to support downgrading (transfer of information
  under restricted conditions). If so, you probably need an intransitive policy.
  An alternative approach is to verify non-interference for the non-downgrading
  part of the system and verify the declassifier separately.
  A final alternative is to add preconditions or axioms on those operations
  that downgrading applies to.

- do you want to restrict transfer of data (eg memory/file contents) or do
  you also want to restrict transfer of metadata (eg how much memory is being used).
  To restrict data, specify restrictions on what *states* can be distinguished
  and to restrict metadata, specify restrictions on what *traces* can be distinguished.

{% include links.html %}
