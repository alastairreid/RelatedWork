---
ENTRYTYPE: inproceedings
abstract: The advent of Deep Learning (DL) has radically transformed the computing industry across the entire spectrum from algorithms to circuits. As myriad
  application domains embrace DL, it has become synonymous with a genre of workloads across vision, speech, language, recommendations, robotics, and games.
  The key compute kernel within most DL workloads is general matrix-matrix multiplications (GEMMs), which appears frequently during both the forward pass
  (inference and training) and backward pass (training). GEMMs are a natural choice for hardware acceleration to speed up training, and have led to 2D systolic
  architectures like NVIDIA tensor cores and Google Tensor Processing Unit (TPU). Unfortunately, emerging GEMMs in DL are highly irregular and sparse, which
  lead to poor data mappings on systolic architectures. This paper proposes SIGMA, a flexible and scalable architecture that offers high utilization of
  all its processing elements (PEs) regardless of kernel shape and sparsity. Within SIGMA includes a novel reduction tree microarchitecture named Forwarding
  Adder Network (FAN). SIGMA performs 5.7x better than systolic array architectures for irregular sparse matrices, and roughly 3x better than state-of-the-art
  sparse accelerators. We demonstrate an instance of SIGMA operating at 10.8 TFLOPS efficiency across arbitrary levels of sparsity, with a 65.10 mm\^{}2
  and 22.33 W footprint on a 28 nm process.
added: 2021-09-28
authors:
- Eric Qin
- Ananda Samajdar
- Hyoukjun Kwon
- Vineet Nadella
- Sudarshan Srinivasan
- Dipankar Das
- Bharat Kaul
- Tushar Krishna
booktitle: 2020 IEEE International Symposium on High Performance Computer Architecture (HPCA)
doi: 10.1109/HPCA47549.2020.00015
issn: 2378-203X
keywords: ''
layout: paper
month: Feb
number: ''
pages: 58-70
read: true
readings:
- 2021-09-28
title: 'SIGMA: A sparse and irregular GEMM accelerator with flexible interconnects for DNN training'
volume: ''
year: 2020
notes:
- neural network
- sparse model
- hardware
- ReLU
- Benes network
papers:
---

An accelerator for sparse matrix-matrix multiplies that achieves
10.8 TFLOPS (at multiple levels of sparsity) at 22.33W and 65.10mm^2
on a 28nm process.

Sources of sparsity include [ReLU], pooling and dropout and varies
through the training runs and both weights and activations can be sparse
with sparsity levels of 70-90% and sparsity tends to increase with
model size.
Matrices need not be square and their size need not be a multiple of the
SIMD size of your hardware.

Flexible dot-product engines (Flex-DPEs) use a rich interconnect fabric
to give fast data loading/collection times.
Flexible dot-product units (Flex-DPUs) combine multiple Flex-DPEs.

The main source of their flexibility is a [Benes network] for distributing values
to MACs and a "Forwarding Adder Network" (FAN) that adds extra connections ("forwarding links")
(and FP Adders?) to a conventional reduction tree to let it perform multiple
irregular reductions at once. [Or maybe it gives one result per cycle? Not sure.]

They use a bitmap for their sparse encoding and a comparison with other representations
(for FP32 data)
shows that it is never terrible and sometimes the best representation.
(They also make the point that this design choice is largely orthogonal to other
choices.)

Comparing PPA with a TPU-like systolic engine at same frequency, and number of multipliers,
(therefore the same peak TFLOPs), their design uses almost twice the power and 38% more area
but (in their evaluation) 6 times higher effective TFLOPS and 3 times effective TFLOPS/W.

The evaluation compares against 7 other accelerators over 10 KxMxN matrix multiplication sizes
with K,M,N dimensions ranging from 1 to 500,000 with common values in the range 128-2048.
Compared with the TPU (with its 128x128 grid), they win on matrices where one of the dimensions
is less than 128.
On average, SIGMA is 2x faster than TPUs on dense GEMMs because of higher utilization and faster reduction.
And 6x faster than TPUs on sparse GEMMs.

{% include links.html %}
