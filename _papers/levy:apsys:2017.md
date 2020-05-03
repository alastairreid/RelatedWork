---
ENTRYTYPE: inproceedings
added: 2020-01-17
address: New York, NY, USA
articleno: Article 1
authors:
- Amit Levy
- Bradford Campbell
- Branden Ghena
- Pat Pannuto
- Prabal Dutta
- Philip Levis
booktitle: Proceedings of the 8th Asia-Pacific Workshop on Systems
doi: 10.1145/3124680.3124717
isbn: '9781450351973'
layout: paper
location: Mumbai, India
numpages: '7'
publisher: Association for Computing Machinery
read: true
readings:
- 2020-01-16
series: "APSys'17"
title: The case for writing a kernel in Rust
url: https://doi.org/10.1145/3124680.3124717
year: 2017
topics:
- os
notes:
- rust-language
papers:
---

The Rust language is increasingly being proposed as a safe
replacement for C in systems programming.
This paper (by the authors of TockOS) explores some of the
key challenges in doing so.
In particular, they are interested in how they can write
low-level code without having to weaken Rust's
safety story by using the "unsafe" feature of Rust.

The introduction talks about very minimal OSes that
rely heavily on the language guarantees as part of
the security story.
(While they talk about Spin and Singularity, I was
surprised that they did not talk about Java OSes
which were briefly popular in the late '90s.)

One of the challenges in using Rust to write an OS is that
objects have to be shared by multiple parts of the system.
They don't use the terminology but I think they mean
"top half" and "bottom half" code and, of course
device accesses.
Rust provides the "Cell" wrapper that can be used to share
mutable scalar values in a safe way.
They extend this with the "TakeCell" wrapper that provides
for atomic updates of non-scalar values (in particular, references to objects).
TakeCell uses a nice trick for this of specifying the atomic
operation to be performed using a closure (that the Rust
compiler supports as a zero-cost abstraction). 
TakeCell does not appear to be interrupt-safe or MP-safe (MP
support is future work).

The paper then discusses three challenges in building a kernel:

- DMA access.
  The challenge they discuss is that the DMA engine shares
  a buffer with the software world and so the ownership
  and lifetime of the buffer is a concern.

- USB.
  This is an example of interacting with a complex hardware
  device that requires particular memory layouts,
  has particular control requirements, etc.
  
- Doubly linked lists and other complex data structures.
  The aliasing caused by doubly linked lists is a well
  known challenge for Rust's typesystem.
  They use what I suspect is a standard trick for
  sneaking these past Rust's typesystem.
  It is not clear to me whether this merely suppresses
  Rust's warnings or is able to preserve useful safety
  guarantees.
  
  

  {% include links.html %}
