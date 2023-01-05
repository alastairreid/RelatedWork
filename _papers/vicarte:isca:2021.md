---
ENTRYTYPE: inproceedings
abstract: Microarchitectural attacks have plunged Computer Architecture into a security crisis. Yet, as the slowing of Moore's law justifies the use of
  ever more exotic microarchitecture, it is likely we have only seen the tip of the iceberg.To better anticipate this security crisis, this paper performs
  a systematic security-centric analysis of the Computer Architecture literature. Our rationale is that when implementing current and future processors,
  microarchitects will (quite reasonably) look to previously-proposed ideas. Our study uncovers seven classes of microarchitectural optimization with novel
  security implications, proposes a conceptual framework through which to study them and demonstrates several proofs-of-concept to show their efficacy.
  The optimizations we study range from those that leak as much privacy as Spectre/Meltdown (but without exploiting speculative execution) to those that
  otherwise undermine security-critical programs in a variety of ways. Many have storied histories- ranging from industry patents to media/3rd party speculation
  regarding current implementation status to recent renewed interest in the academic community. This paper's goal is to perform an early (hopefully not
  too late) analysis to inform their development moving forward.
added: 2022-08-20
authors:
- Jose Rodrigo Sanchez Vicarte
- Pradyumna Shome
- Nandeeka Nayak
- Caroline Trippel
- Adam Morrison
- David Kohlbrenner
- Christopher W. Fletcher
booktitle: 2021 ACM/IEEE 48th Annual International Symposium on Computer Architecture (ISCA)
doi: 10.1109/ISCA52012.2021.00035
issn: 2575-713X
keywords: ''
layout: paper
month: June
number: ''
pages: 347-360
read: true
readings:
- 2022-08-20
title: 'Opening Pandora''s box: A systematic study of new ways microarchitecture can leak private data'
volume: ''
year: 2021
notes:
- weak memory
- CPU verification
- ISA specification
- side-channel
- speculative execution
- uspec
papers:
---

Looks at more recent microarchitectural optimizations to see whether any are as bad as
speculative execution. Spoiler alert: yes.

The optimizations they look at are

- computation simplification
- pipeline compression
- silent stores
- computation reuse
- value prediction
- register-file compression
- data memory-dependent prefetches

Implementing some of these in gem5 lets them show that these can leak data at
a high rate.

An interesting thing in this paper is the terminology "transmitter" for instructions
that leak, "amplifiers" for instructions that make a uarch difference more obvious,
and "receivers" for instructions that can observe the difference.

{% include links.html %}
