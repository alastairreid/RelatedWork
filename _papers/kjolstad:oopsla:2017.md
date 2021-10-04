---
ENTRYTYPE: article
abstract: Tensor algebra is a powerful tool with applications in machine learning, data analytics, engineering and the physical sciences. Tensors are often
  sparse and compound operations must frequently be computed in a single kernel for performance and to save memory. Programmers are left to write kernels
  for every operation of interest, with different mixes of dense and sparse tensors in different formats. The combinations are infinite, which makes it
  impossible to manually implement and optimize them all. This paper introduces the first compiler technique to automatically generate kernels for any compound
  tensor algebra operation on dense and sparse tensors. The technique is implemented in a C++ library called taco. Its performance is competitive with best-in-class
  hand-optimized kernels in popular libraries, while supporting far more tensor operations.
added: 2021-10-04
address: New York, NY, USA
articleno: '77'
authors:
- Fredrik Kjolstad
- Shoaib Kamil
- Stephen Chou
- David Lugato
- Saman Amarasinghe
doi: 10.1145/3133901
issue_date: October 2017
journal: Proc. ACM Program. Lang.
keywords: tensor algebra, linear algebra, sparse data structures, iteration graphs, parallelism, performance, code generation, merge lattices, tensors
layout: paper
link: https://doi.org/10.1145/3133901
month: October
number: OOPSLA
numpages: '29'
publisher: Association for Computing Machinery
read: true
readings:
- 2021-10-04
title: The tensor algebra compiler
url: https://doi.org/10.1145/3133901
volume: '1'
year: 2017
notes:
- tensor
- tensorflow
- neural network
- sparse model
papers:
---

The Tensor Algebra COmpiler (TACO) is a compiler for tensor index notation
for sparse tensor code (with dense tensors as an easy special case).
This early paper about the system
introduces a format that generalizes existing sparse
formats such as CSR, CSC or DCSR; 
introduces iteration graphs for capturing the structure of the loop nest
that will be generated;
and
the use of merge lattices for capturing the constraints on iteration
due to use of addition or multiplication, etc.

TACO generated code is fast (better than most of the libraries/tools
it is compared against).

Around 10 further papers and theses by the same group improve representation,
distributed computing, transposition and format conversion.

Later tools by other groups claim significant improvements.


{% include links.html %}
