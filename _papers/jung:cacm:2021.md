---
ENTRYTYPE: article
added: 2021-02-28
authors:
- Ralf Jung
- Jacques-Henri Jourdan
- Robbert Krebbers
- Derek Dreyer
hal_id: hal-03021536
hal_version: v1
journal: Communications of the ACM
keywords: type systems ; control ; programming language ; Rust ; safety
layout: paper
link: https://hal.archives-ouvertes.fr/hal-03021536
pdf: https://hal.archives-ouvertes.fr/hal-03021536/file/jung2020safe.pdf
publisher: Association for Computing Machinery
read: true
readings:
- 2021-03-05
title: 'Safe systems programming in Rust: The promise and the challenge'
url: https://hal.archives-ouvertes.fr/hal-03021536
year: 2021
notes:
- Rust language
- Rust unsafe code
papers:
- jung:popl:2017
- jung:popl:2020
- tofte:inco:1997
- grossman:pldi:2002
---

This is a good introduction for PL researchers of the [Rust language], it's
type system and its approach to safety.  It reuses explanations from the
authors' earlier works ([jung:popl:2017], [jung:popl:2020]) but with more space
dedicated to explanation making this the best place to start in exploring their
work as well as a good way for PL people to map Rust concepts onto their existing
concepts.

The bulk of the paper explains how Rust's type system controls aliasing in
order to make mutation, memory management and concurrency safe based on ideas
from region-based memory allocation in [tofte:inco:1997] and
[grossman:pldi:2002].

The really interesting thing about Rust is that, alongside that decidable,
explainable type system, it allows ["unsafe code"][Rust unsafe code] that may
break the rules internally but is expected to provide a safe API to the rest of
Rust. (See [jung:popl:2020].)

*[Note that this summary is based on the PDF submitted to CACM for publication --
the final version has a slightly different title, etc.]*

{% include links.html %}
