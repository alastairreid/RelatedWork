---
ENTRYTYPE: inproceedings
abstract: 'This paper presents component techniques essential for converting executables to a high-level intermediate representation (IR) of an existing
  compiler. The compiler IR is then employed for three distinct applications: binary rewriting using the compiler''s binary back-end, vulnerability detection
  using source-level symbolic execution, and source-code recovery using the compiler''s C backend. Our techniques enable complex high-level transformations
  not possible in existing binary systems, address a major challenge of input-derived memory addresses in symbolic execution and are the first to enable
  recovery of a fully functional source-code.We present techniques to segment the flat address space in an executable containing undifferentiated blocks
  of memory. We demonstrate the inadequacy of existing variable identification methods for their promotion to symbols and present our methods for symbol
  promotion. We also present methods to convert the physically addressed stack in an executable (with a stack pointer) to an abstract stack (without a stack
  pointer). Our methods do not use symbolic, relocation, or debug information since these are usually absent in deployed executables.We have integrated
  our techniques with a prototype x86 binary framework called SecondWrite that uses LLVM as IR. The robustness of the framework is demonstrated by handling
  executables totaling more than a million lines of source-code, produced by two different compilers (gcc and Microsoft Visual Studio compiler), three languages
  (C, C++, and Fortran), two operating systems (Windows and Linux) and a real world program (Apache server).'
added: 2021-11-25
address: New York, NY, USA
authors:
- Kapil Anand
- Matthew Smithson
- Khaled Elwazeer
- Aparna Kotha
- Jim Gruen
- Nathan Giles
- Rajeev Barua
booktitle: Proceedings of the 8th ACM European Conference on Computer Systems
doi: 10.1145/2465351.2465380
isbn: '9781450319942'
layout: paper
link: https://doi.org/10.1145/2465351.2465380
location: Prague, Czech Republic
numpages: '14'
pages: 295-308
publisher: Association for Computing Machinery
read: false
readings: []
series: EuroSys '13
title: A compiler-level intermediate representation based binary analysis and rewriting system
url: https://doi.org/10.1145/2465351.2465380
year: 2013
notes:
- binary lifter
- binary analysis
- reverse engineering
- secondwrite tool
- x86 architecture
- LLVM compiler
papers:
---
{% include links.html %}
