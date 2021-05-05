---
ENTRYTYPE: inbook
abstract: 'Side-channel attacks such as Spectre rely on properties of modern CPUs that permit discovery of microarchitectural state via timing of various
  operations. The Weird Machine concept is an increasingly popular model for characterization of emergent execution that arises from side-effects of conventional
  computing constructs. In this work we introduce Microarchitectural Weird Machines (\mathrm{\mu}WM): code constructions that allow performing computation
  through the means of side effects and conflicts between microarchitectual entities such as branch predictors and caches. The results of such computations
  are observed as timing variations. We demonstrate how \mathrm{\mu}WMs can be used as a powerful obfuscation engine where computation operates based on
  events unobservable to conventional anti-obfuscation tools based on emulation, debugging, static and dynamic analysis techniques. We demonstrate that
  \mathrm{\mu}WMs can be used to reliably perform arbitrary computation by implementing a SHA-1 hash function. We then present a practical example in which
  we use a \mathrm{\mu}WM to obfuscate malware code such that its passive operation is invisible to an observer with full power to view the architectural
  state of the system until the code receives a trigger. When the trigger is received the malware decrypts and executes its payload. To show the effectiveness
  of obfuscation we demonstrate its use in the concealment and subsequent execution of a payload that exfiltrates a shadow password file, and a payload
  that creates a reverse shell.'
added: 2021-05-05
address: New York, NY, USA
authors:
- Dmitry Evtyushkin
- Thomas Benjamin
- Jesse Elwell
- Jeffrey A. Eitel
- Angelo Sapello
- Abhrajit Ghosh
booktitle: Proceedings of the 26th ACM International Conference on Architectural Support for Programming Languages and Operating Systems
isbn: '9781450383172'
layout: paper
link: https://doi.org/10.1145/3445814.3446729
numpages: '15'
pages: 758-772
publisher: Association for Computing Machinery
read: false
readings: []
title: 'Computing with time: Microarchitectural weird machines'
url: https://doi.org/10.1145/3445814.3446729
year: 2021
notes:
papers:
---
{% include links.html %}
