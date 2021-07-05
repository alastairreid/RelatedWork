---
ENTRYTYPE: misc
added: 2021-07-05
archiveprefix: arXiv
authors:
- Alex Shamis
- Peter Pietzuch
- Miguel Castro
- Edward Ashton
- Amaury Chamayou
- Sylvan Clebsch
- Antoine Delignat-Lavaud
- Cedric Fournet
- Matthew Kerner
- Julien Maffre
- Manuel Costa
- Mark Russinovich
eprint: '2105.13116'
layout: paper
primaryclass: cs.DC
read: true
readings:
- 2021-07-05
title: 'PAC: Practical Accountability for CCF'
year: 2021
notes:
papers:
---

Permissioned ledgers that use Byzantine fault tolerance can detect misbehaviour
provided that there is enough diversity between machines
but, if there are only a few cloud providers, you don't get much
diversity.

This paper proposes a mechanism to assign blame based on verifiable
receipts that allow the ledger to be audited which creates
a strong disincentive to misbehaviour at low cost (they can support
48k transactions per second).

{% include links.html %}
