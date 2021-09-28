---
ENTRYTYPE: inproceedings
abstract: Generalized tensor algebra is a prime candidate for acceleration via customized ASICs. Modern tensors feature a wide range of data sparsity, with
  the density of non-zero elements ranging from 10-6\% to 50\%. This paper proposes a novel approach to accelerate tensor kernels based on the principle
  of hierarchical elimination of computation in the presence of sparsity. This approach relies on rapidly finding intersections--situations where both operands
  of a multiplication are non-zero--enabling new data fetching mechanisms and avoiding memory latency overheads associated with sparse kernels implemented
  in software.We propose the ExTensor accelerator, which builds these novel ideas on handling sparsity into hardware to enable better bandwidth utilization
  and compute throughput. We evaluate ExTensor on several kernels relative to industry libraries (Intel MKL) and state-of-the-art tensor algebra compilers
  (TACO). When bandwidth normalized, we demonstrate an average speedup of 3.4\texttimes , 1.3\texttimes , 2.8\texttimes , 24.9\texttimes , and 2.7\texttimes  on
  SpMSpM, SpMM, TTV, TTM, and SDDMM kernels respectively over a server class CPU.
added: 2021-09-28
address: New York, NY, USA
authors:
- Kartik Hegde
- Hadi Asghari-Moghaddam
- Michael Pellauer
- Neal Crago
- Aamer Jaleel
- Edgar Solomonik
- Joel Emer
- Christopher W. Fletcher
booktitle: Proceedings of the 52nd Annual IEEE/ACM International Symposium on Microarchitecture
doi: 10.1145/3352460.3358275
isbn: '9781450369381'
keywords: Hardware Acceleration, Tensor Algebra, Sparse Computation
layout: paper
link: https://doi.org/10.1145/3352460.3358275
location: Columbus, OH, USA
numpages: '15'
pages: 319-333
publisher: Association for Computing Machinery
read: true
readings:
- 2021-09-28
series: MICRO '52
title: 'ExTensor: An accelerator for sparse tensor algebra'
url: https://doi.org/10.1145/3352460.3358275
year: 2019
notes:
- hardware
- neural network
- sparse model
papers:
- qin:hpca:2020
---

The key idea in this paper is to exploit hierarchy based on
the observation that "0 * x == 0" not just for scalar zeros
but for tensor zeros. So they can exploit "hyper-sparsity" (sparsity at the
level of entire rows, columns or tiles) and avoid fetching large amounts of data.
And they can potentially avoid computing data that would
only have been multiplied by zero.

To support this, they decouple metadata processing from
data processing allowing metadata processing to run ahead.

They view an N-dimensional tensor as an N-level tree where
each level represents one of the dimensions.
(Tiling is treated is adding additional dimensions/levels.)
Various operations (e.g., dot product) correspond to different
ways of intersecting the nodes in the two input trees.

A lot of the paper is dedicated to efficiently intersecting
coordinate streams from the trees of the input operands.
The sequencers and scanners required to do this are placed
right next to DRAM to maximize lookahead.
Content addressable memories seem to be an important part
in some optimizations.


Evaluation compares against a server-class CPU (not a TPU)
for different matrix/vector/sparse/dense combinations
(GEMM, TTV, TTM, SDDMM).
Evaluation uses a partial simulator written in Python
that models DRAM burst/rows, NoC, multicast/unicast, ...

They get speedups (against a CPU) in the range 1.3x-25x 
across the different benchmarks and approach the CPU roofline
and ExTensor rooflines on many benchmarks.
The improvement comes from the higher DRAM utilization
achieved.

Further analysis looks at exactly where the benefit comes
by adding/removing parts of the design and sweeping over the design space.

A partial hardware implementation of the novel parts yielded
PPA estimates and showed that the novel hardware (the intersection
and coordination units) are a small fraction (2.5%) of area.


{% include links.html %}
