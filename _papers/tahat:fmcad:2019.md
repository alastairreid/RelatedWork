---
ENTRYTYPE: article
doi: 10.23919/FMCAD.2019.8894252
added: 2019-10-12
authors:
- Amer Tahat
- Sarang Joshi
- Pronnoy Goswami
- Binoy Ravindran
layout: paper
read: true
readings:
- 2019-10-12
title: Scalable translation validation of unverified legacy OS code
year: 2019
topics:
- os
- verification
notes:
- translation validation
- Arm architecture
- ASL
- PVS theorem prover
papers:
---

Describes a toolchain for translation validation of radere2 reverse engineering
tool using the [ASL] specification of the [Arm architecture] based on the PVS7 theorem prover.

Uses multiple techniques to validate translation of ASL to PVS7.
Tested using 370 functions extracted from Linux and Google's Zircon OS.
Limited to loop-free leaf functions.

{% include links.html %}
