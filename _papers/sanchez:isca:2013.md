---
ENTRYTYPE: inproceedings
abstract: Architectural simulation is time-consuming, and the trend towards hundreds of cores is making sequential simulation even slower. Existing parallel
  simulation techniques either scale poorly due to excessive synchronization, or sacrifice accuracy by allowing event reordering and using simplistic contention
  models. As a result, most researchers use sequential simulators and model small-scale systems with 16-32 cores. With 100-core chips already available,
  developing simulators that scale to thousands of cores is crucial.We present three novel techniques that, together, make thousand-core simulation practical.
  First, we speed up detailed core models (including OOO cores) with instruction-driven timing models that leverage dynamic binary translation. Second,
  we introduce bound-weave, a two-phase parallelization technique that scales parallel simulation on multicore hosts efficiently with minimal loss of accuracy.
  Third, we implement lightweight user-level virtualization to support complex workloads, including multiprogrammed, client-server, and managed-runtime
  applications, without the need for full-system simulation, sidestepping the lack of scalable OSs and ISAs that support thousands of cores.We use these
  techniques to build zsim, a fast, scalable, and accurate simulator. On a 16-core host, zsim models a 1024-core chip at speeds of up to 1,500 MIPS using
  simple cores and up to 300 MIPS using detailed OOO cores, 2-3 orders of magnitude faster than existing parallel simulators. Simulator performance scales
  well with both the number of modeled cores and the number of host cores. We validate zsim against a real Westmere system on a wide variety of workloads,
  and find performance and microarchitectural events to be within a narrow range of the real system.
added: 2022-03-01
address: New York, NY, USA
authors:
- Daniel Sanchez
- Christos Kozyrakis
booktitle: Proceedings of the 40th Annual International Symposium on Computer Architecture
doi: 10.1145/2485922.2485963
isbn: '9781450320795'
layout: paper
link: https://doi.org/10.1145/2485922.2485963
location: Tel-Aviv, Israel
numpages: '12'
pages: 475-486
publisher: Association for Computing Machinery
read: false
readings: []
series: ISCA '13
title: 'ZSim: Fast and accurate microarchitectural simulation of thousand-core systems'
url: https://doi.org/10.1145/2485922.2485963
year: 2013
notes:
- Intel
- x86 architecture
- ISA specification
papers:
---
{% include links.html %}
