---
Title: SecChisel: Language and Tool for Practical and Scalable Security Verification of Security-Aware Hardware Architectures
Authors: Shuwen Deng and Doguhan Gumusoglu and Wenjie Xiong and Y. Serbian Gener and Onur Demir and Jakob Szefer
Venue:
Year: 
Topics:
  - information-flow
---

As BibTeX (trimmed of useless fields)

inproceedings{Deng:2019:SFS:3337167.3337174,
 author = {Deng, Shuwen and G\"{u}m\"{u}\c{s}o\u{g}lu, Do\u{g}uhan and Xiong, Wenjie and Sari, Sercan and Gener, Y. Serhan and Lu, Corine and Demir, Onur and Szefer, Jakub},
 title = {SecChisel Framework for Security Verification of Secure Processor Architectures},
 booktitle = {Proceedings of the 8th International Workshop on Hardware and Architectural Support for Security and Privacy},
 series = {HASP '19},
 year = {2019},
 pages = {7:1--7:8},
 doi = {10.1145/3337167.3337174},
 publisher = {ACM},

Author names with accents (this looks like UTF-8 and may need to be re-encoded both for BibTeX and for Jekyll)
 
Authors:	Shuwen Deng	Yale University, New Haven, CT, USA
Doğuhan Gümüşoğlu	Yeditepe Üniversitesi, Ataşehir/İstanbul, Turkey
Wenjie Xiong	Yale University, New Haven, CT, USA
Sercan Sari	Yeditepe Üniversitesi, Ataşehir/İstanbul, Turkey
Y. Serhan Gener	Yeditepe Üniversitesi, Ataşehir/İstanbul, Turkey
Corine Lu	Yale University, New Haven, CT, USA
Onur Demir	Yeditepe Üniversitesi, Ataşehir/İstanbul, Turkey
Jakub Szefer	Yale University, New Haven, CT, USA

Extends Chisel with security labels to track information flow.
Uses Z3 to check but check is based on syntactic structure, not on semantic analysis.  That is, it just propagates labels.  Suggests this is important for performance.
Sketches several optimisations - I would have liked to have had more detail here.
There seem to be several strategies for labelling each module: explicitly label all flops; explicitly label inputs and outputs of module and scan internal connectivity to check for flow; programmer sketches abstract connectivity by specifying which inputs are connected to which outputs as a matrix.  It is not clear whether hybrids of these are supported.
The paper seems like an early report with many unimplemented features (dynamic labelling, nested modules, Chisel 3 support) and no case study to demonstrate/test/evaluate design choices.
Related work discusses a lot of other security related hardware description languages.