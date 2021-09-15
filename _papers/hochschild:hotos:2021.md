---
ENTRYTYPE: inbook
abstract: We are accustomed to thinking of computers as fail-stop, especially the cores that execute instructions, and most system software implicitly relies
  on that assumption. During most of the VLSI era, processors that passed manufacturing tests and were operated within specifications have insulated us
  from this fiction. As fabrication pushes towards smaller feature sizes and more elaborate computational structures, and as increasingly specialized instruction-silicon
  pairings are introduced to improve performance, we have observed ephemeral computational errors that were not detected during manufacturing tests. These
  defects cannot always be mitigated by techniques such as microcode updates, and may be correlated to specific components within the processor, allowing
  small code changes to effect large shifts in reliability. Worse, these failures are often "silent" - the only symptom is an erroneous computation.We refer
  to a core that develops such behavior as "mercurial." Mercurial cores are extremely rare, but in a large fleet of servers we can observe the disruption
  they cause, often enough to see them as a distinct problem - one that will require collaboration between hardware designers, processor vendors, and systems
  software architects.This paper is a call-to-action for a new focus in systems research; we speculate about several software-based approaches to mercurial
  cores, ranging from better detection and isolating mechanisms, to methods for tolerating the silent data corruption they cause.
added: 2021-09-10
address: New York, NY, USA
authors:
- Peter H. Hochschild
- Paul Turner
- Jeffrey C. Mogul
- Rama Govindaraju
- Parthasarathy Ranganathan
- David E. Culler
- Amin Vahdat
booktitle: Proceedings of the Workshop on Hot Topics in Operating Systems
isbn: '9781450384384'
layout: paper
link: https://doi.org/10.1145/3458336.3465297
numpages: '8'
pages: 9-16
publisher: Association for Computing Machinery
read: true
readings:
- 2021-09-10
title: Cores that don't count
url: https://doi.org/10.1145/3458336.3465297
year: 2021
notes:
- Google
- hardware faults
papers:
- dixit:arxiv:2021
---

Silent Corrupt Execution Errors (CEEs) due to minor
manufacturing defects in CPUs cause infrequent corruption of
output while otherwise appearing to be fine. (The infrequent aspect
is what makes them "silent".)
Google and Facebook are both seeing a few "mercurial" cores
per several thousand machines (not clear if they mean CPUs).

Suspected to be caused by smaller feature sizes, more complex design,
and increasing difficulty testing (esp. for corner cases and post-deployment aging).

Detection

- pre/post-deployment screening (testing)
- offline/online screening (testing idle cores or testing during idle moments)
- infrastructure-level vs application-level screening (ie generic or application specific testing)

Mitigations - both hardware and software. Mostly an opportunity for future research.





{% include links.html %}
