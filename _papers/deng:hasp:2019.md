---
added: 2019-10-06
layout: paper
title: "SecChisel: Language and tool for practical and scalable security verification of security-aware hardware architectures"
authors:
- Shuwen Deng
- Doğuhan Gümüşoğlu
- Wenjie Xiong
- Sercan Sari
- Y. Serhan Gener
- Corine Lu
- Onur Demir
- Jakub Szefer
year: 2019
booktitle: Proceedings of the 8th International Workshop on Hardware and Architectural Support for Security and Privacy
pages: 7:1-7:8
doi: 10.1145/3337167.3337174
publisher: ACM
read: true
readings:
- 2019-10-06
topics:
- hardware
- security
- tools
notes:
- information flow
papers:
- demoura:tacas:2008
---

Extends Chisel with security labels to track information flow.
Uses [the Z3 SMT solver][demoura:tacas:2008]
to check but check is based on syntactic structure, not on semantic analysis.
That is, it just propagates labels.
Suggests this is important for performance.

Sketches several optimisations — I would have liked to have had more detail here.
There seem to be several strategies for labelling each module: explicitly label all flops; explicitly label inputs and outputs of module and scan internal connectivity to check for flow; programmer sketches abstract connectivity by specifying which inputs are connected to which outputs as a matrix.  It is not clear whether hybrids of these are supported.
The paper seems like an early report with many unimplemented features (dynamic labelling, nested modules, Chisel 3 support) and no case study to demonstrate/test/evaluate design choices.
Related work discusses a lot of other security related hardware description languages.

{% include links.html %}
