---
ENTRYTYPE: inproceedings
abstract: Many architects believe that major improvements in cost-energy-performance must now come from domain-specific hardware. This paper evaluates a
  custom ASIC--called a Tensor Processing Unit (TPU) -- deployed in datacenters since 2015 that accelerates the inference phase of neural networks (NN).
  The heart of the TPU is a 65,536 8-bit MAC matrix multiply unit that offers a peak throughput of 92 TeraOps/second (TOPS) and a large (28 MiB) software-managed
  on-chip memory. The TPU's deterministic execution model is a better match to the 99th-percentile response-time requirement of our NN applications than
  are the time-varying optimizations of CPUs and GPUs that help average throughput more than guaranteed latency. The lack of such features helps explain
  why, despite having myriad MACs and a big memory, the TPU is relatively small and low power. We compare the TPU to a server-class Intel Haswell CPU and
  an Nvidia K80 GPU, which are contemporaries deployed in the same datacenters. Our workload, written in the high-level TensorFlow framework, uses production
  NN applications (MLPs, CNNs, and LSTMs) that represent 95\% of our datacenters' NN inference demand. Despite low utilization for some applications, the
  TPU is on average about 15X - 30X faster than its contemporary GPU or CPU, with TOPS/Watt about 30X - 80X higher. Moreover, using the CPU's GDDR5 memory
  in the TPU would triple achieved TOPS and raise TOPS/Watt to nearly 70X the GPU and 200X the CPU.
added: 2021-09-29
address: New York, NY, USA
authors:
- Norman P. Jouppi
- Cliff Young
- Nishant Patil
- David Patterson
- Gaurav Agrawal
- Raminder Bajwa
- Sarah Bates
- Suresh Bhatia
- Nan Boden
- Al Borchers
- Rick Boyle
- Pierre-luc Cantin
- Clifford Chao
- Chris Clark
- Jeremy Coriell
- Mike Daley
- Matt Dau
- Jeffrey Dean
- Ben Gelb
- Tara Vazir Ghaemmaghami
- Rajendra Gottipati
- William Gulland
- Robert Hagmann
- C. Richard Ho
- Doug Hogberg
- John Hu
- Robert Hundt
- Dan Hurt
- Julian Ibarz
- Aaron Jaffey
- Alek Jaworski
- Alexander Kaplan
- Harshit Khaitan
- Daniel Killebrew
- Andy Koch
- Naveen Kumar
- Steve Lacy
- James Laudon
- James Law
- Diemthu Le
- Chris Leary
- Zhuyuan Liu
- Kyle Lucke
- Alan Lundin
- Gordon MacKean
- Adriana Maggiore
- Maire Mahony
- Kieran Miller
- Rahul Nagarajan
- Ravi Narayanaswami
- Ray Ni
- Kathy Nix
- Thomas Norrie
- Mark Omernick
- Narayana Penukonda
- Andy Phelps
- Jonathan Ross
- Matt Ross
- Amir Salek
- Emad Samadiani
- Chris Severn
- Gregory Sizikov
- Matthew Snelham
- Jed Souter
- Dan Steinberg
- Andy Swing
- Mercedes Tan
- Gregory Thorson
- Bo Tian
- Horia Toma
- Erick Tuttle
- Vijay Vasudevan
- Richard Walter
- Walter Wang
- Eric Wilcox
- Doe Hyun Yoon
booktitle: Proceedings of the 44th Annual International Symposium on Computer Architecture
doi: 10.1145/3079856.3080246
isbn: '9781450348928'
keywords: domain-specific architecture, deep learning, RNN, GPU, MLP, TPU, neural network, accelerator, TensorFlow, DNN, LSTM, CNN
layout: paper
link: https://doi.org/10.1145/3079856.3080246
location: Toronto, ON, Canada
numpages: '12'
pages: 1-12
publisher: Association for Computing Machinery
read: true
readings:
- 2021-09-29
series: ISCA '17
title: In-datacenter performance analysis of a tensor processing unit
url: https://doi.org/10.1145/3079856.3080246
year: 2017
notes:
- neural network
- MLP
- CNN
- RNN
- tensor
- TensorFlow
- hardware
- google
- TPU
- decoupled access execute
- roofline performance model
papers:
- jouppi:micro:2018
---

Describes the design and development of [Google]'s [TPU] in 15 months.

The [TPU] consists of a massive (256 x 256) systolic array supporting 8-bit multiplications.
(It can also support 8x16 and 16x16 multiplications.)
Most databuses are 256 *bytes* wide (except accumulators that are 1024 bytes wide).
Memory is explicitly managed, uses double buffering, etc.

Being a systolic array, each multiplier can store weights used to multiply by
(2 weights: one to use now, one double buffer).
The array can perform a convolution ([CNN]) or a matrix multiply.

In the control logic, some ideas from the [decoupled access execute] philosophy are used with
the multiplier stalling if operands are not ready.

The chip is half the size of Haswell, 30% the clock rate, 30% the power, 35x
the performance (on 8 bit multiplies), half the memory bandwidth, half the
on-chip memory.

Comparison with a Haswell x86 part and an Nvidia K80 part is based on using
the [roofline performance model] which shows that the benchmarks are
hitting the roofline on the TPU for all but one benchmark. (Most are memory
bandwidth limited.)
The ridge points are at 1350 ops/byte (TPU), 13 ops/byte (Haswell) and 9 ops/byte (K80)
(where lower numbers are better).
An analysis of MAC utilization shows that it is often running at 10-25% utilization
in part because tall-thin or short-wide tensors don't fit the big square
multiplier.
For Haswell and K80, most benchmarks are far below the roofline.
(But note that Haswell and K80 use F32 whereas the TPU uses I8 or I16 data.)

They emphasize that the TPU has few features to improve the average case
because they are interested in tail latency.

The TPU has poor energy proportionality (it uses similar power whether idle or busy)
because the short design cycle did not give them time to include energy-saving features.

[MLP]s and [LSTM]s are bandwidth limited while [CNN]s are compute bound.  The
large systolic array seems to be a mixed benefit: making it larger gives you
more compute but it also takes longer to feed in all of the data.








{% include links.html %}
