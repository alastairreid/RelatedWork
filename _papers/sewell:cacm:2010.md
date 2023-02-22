---
ENTRYTYPE: article
abstract: Exploiting the multiprocessors that have recently become ubiquitous requires high-performance and reliable concurrent systems code, for concurrent
  data structures, operating system kernels, synchronization libraries, compilers, and so on. However, concurrent programming, which is always challenging,
  is made much more so by two problems. First, real multiprocessors typically do not provide the sequentially consistent memory that is assumed by most
  work on semantics and verification. Instead, they have relaxed memory models, varying in subtle ways between processor families, in which different hardware
  threads may have only loosely consistent views of a shared memory. Second, the public vendor architectures, supposedly specifying what programmers can
  rely on, are often in ambiguous informal prose (a particularly poor medium for loose specifications), leading to widespread confusion.In this paper we
  focus on x86 processors. We review several recent Intel and AMD specifications, showing that all contain serious ambiguities, some are arguably too weak
  to program above, and some are simply unsound with respect to actual hardware. We present a new x86-TSO programmer's model that, to the best of our knowledge,
  suffers from none of these problems. It is mathematically precise (rigorously defined in HOL4) but can be presented as an intuitive abstract machine which
  should be widely accessible to working programmers. We illustrate how this can be used to reason about the correctness of a Linux spinlock implementation
  and describe a general theory of data-race freedom for x86-TSO. This should put x86 multiprocessor system building on a more solid foundation; it should
  also provide a basis for future work on verification of such systems.
added: 2021-11-22
address: New York, NY, USA
authors:
- Peter Sewell
- Susmit Sarkar
- Scott Owens
- Francesco Zappa Nardelli
- Magnus O. Myreen
doi: 10.1145/1785414.1785443
issn: 0001-0782
issue_date: July 2010
journal: Communications of the ACM
layout: paper
link: https://doi.org/10.1145/1785414.1785443
month: jul
number: '7'
numpages: '9'
pages: 89-97
publisher: Association for Computing Machinery
read: false
readings: []
title: 'x86-TSO: A rigorous and usable programmer''s model for x86 multiprocessors'
url: https://doi.org/10.1145/1785414.1785443
volume: '53'
year: 2010
notes:
- weak memory
- TSO
- x86 architecture
papers:
---
{% include links.html %}
