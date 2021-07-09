---
ENTRYTYPE: inproceedings
abstract: snmalloc is an implementation of malloc aimed at workloads in which objects are typically deallocated by a different thread than the one that
  had allocated them. We use the term producer/consumer for such workloads. snmalloc uses a novel message passing scheme which returns deallocated objects
  to the originating allocator in batches without taking any locks. It also uses a novel bump pointer-free list data structure with which just 64-bits of
  meta-data are sufficient for each 64 KiB slab. On such producer/consumer benchmarks our approach performs better than existing allocators. Snmalloc is
  available at https://github.com/Microsoft/snmalloc.
added: 2021-07-06
address: New York, NY, USA
authors:
- Paul Liétar
- Theodore Butler
- Sylvan Clebsch
- Sophia Drossopoulou
- Juliana Franco
- Matthew J. Parkinson
- Alex Shamis
- Christoph M. Wintersteiger
- David Chisnall
booktitle: Proceedings of the 2019 ACM SIGPLAN International Symposium on Memory Management
doi: 10.1145/3315573.3329980
isbn: '9781450367226'
keywords: Memory allocation, message passing
layout: paper
link: https://doi.org/10.1145/3315573.3329980
location: Phoenix, AZ, USA
numpages: '14'
pages: 122-135
publisher: Association for Computing Machinery
read: true
readings:
- 2021-07-06
series: ISMM 2019
title: 'snmalloc: A message passing allocator'
url: https://doi.org/10.1145/3315573.3329980
year: 2019
notes:
papers:
---

snmalloc is an efficient multiprocessor memory allocator optimized
for the asymmetric allocation / deallocation pattern found in
pipelined programs.

It uses lock-free data structures,
uses radix-trees to collect
objects so that they can be sent in batches of 1MB by a curious
multi-hop communication scheme,
distinguish large (16MB+), medium (64kB+) and small objects.

Linked lists of free objects are added to input queues of other allocators
which are checked on malloc/free calls.
These objects are tagged with the destination allocator; if this is 
different from the allocator that receives them, it queues them
to be sent to another allocator. It can take up to 7 hops to get to the
true destination.
(In practice, there is probably one allocator per thread and the number
of threads is low enough that most objects just take one hop.)


{% include links.html %}
