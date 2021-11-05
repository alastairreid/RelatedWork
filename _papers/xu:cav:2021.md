---
ENTRYTYPE: inproceedings
abstract: Verification of instruction encoders and decoders is essential for formalizing manipulation of machine code. The existing approaches cannot guarantee
  the critical consistency property, i.e., that an encoder and its corresponding decoder are mutual inverses of each other. We observe that consistent encoder-decoder
  pairs can be automatically derived from bijections inherently embedded in instruction formats. Based on this observation, we develop a framework for writing
  specifications that capture these bijections, for automatically generating encoders and decoders from these specifications, and for formally validating
  the consistency and soundness of the generated encoders and decoders by synthesizing proofs in Coq and discharging verification conditions using SMT solvers.
  We apply this framework to a subset of X86-32 instructions to illustrate its effectiveness in these regards. We also demonstrate that the generated encoders
  and decoders have reasonable performance.
added: 2021-11-05
address: Cham
authors:
- Xiangzhe Xu
- Jinhua Wu
- Yuting Wang
- Zhenguo Yin
- Pengfei Li
booktitle: Computer Aided Verification
editor: Silva, Alexandra and Leino, K. Rustan M.
isbn: 978-3-030-81688-9
layout: paper
pages: 728-751
publisher: Springer International Publishing
read: false
readings: []
title: Automatic generation and validation of instruction encoders and decoders
year: 2021
notes:
- ISA specification
papers:
---
{% include links.html %}
