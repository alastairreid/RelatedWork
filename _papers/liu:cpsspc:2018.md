---
layout: paper
added: 2019-10-06
title: Secure autonomous cyber-physical systems through verifiable information flow control
authors:
- Jed Liu
- Joe Corbett-Davies
- Andrew Ferriauolo
- Alexander Ivanov
- Mulong Luo
- G. Edward Suh
- Andrew C. Myers
- Mark Campbell
venue: CPS-SPC
year: 2018
doi: 10.1145/3264888.3264889
booktitle: Proceedings of the 2018 Workshop on Cyber-Physical Systems Security and Privacy,
read: true
readings:
- 2019-10-06
series: CPS-SPC '18
pages: 48-59
publisher: ACM
topics:
- hardware
- security
notes:
- information flow
papers:
---

This paper ties together several different threads to create a CPS system (autonomous vehicle) that is resistant to many forms of attack.
Builds on Jif (Java with security labels), SecVerilog (HDL with security labels), Hyperflow (processor with security labels) and statistical detection of attack based on sensor fusion (sensors plus map data).
The Hyperflow processor is not used in the experiment at this stage because they need to port Java/Jif to that architecture.
Statistics try to distinguish noise (Gaussian) from attack (uniform) — not clear to me that this is sufficiently robust.


{% include links.html %}
