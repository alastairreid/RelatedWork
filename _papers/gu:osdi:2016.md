---
ENTRYTYPE: inproceedings
added: 2019-11-10
authors:
- Ronghui Gu
- Zhong Shao
- Hao Chen
- Xiongnan Newman Wu
- Jieung Kim
- Vilhelm Sjöberg
- David Costanzo
booktitle: 12th USENIX Symposium on Operating Systems Design and Implementation (OSDI 16)
layout: paper
pages: 653-669
read: true
readings:
- 2019-11-29
title: 'CertiKOS: An extensible architecture for building certified concurrent OS
  Kernels'
year: 2016
topics:
- os
- verification
---

This is one of a steady stream of papers from the FLINT group at Yale on creating a formally verified OS.
Some distinguishing features of CertiKOS are the completeness of the verification (cf. seL4), the way that the C code and the proofs are split into more than 30 very small layers each adding one feature at a time and greatly simplifying the proof of each layer and their use of an extended version of the CompCert C compiler. The layered structure is strongly reminiscent of Bryan Ford's work on Recursive Virtual Machines – unsurprising since Bryan was an early contributor to this project.
The use of CompCert avoids the need to perform translation validation (cf. seL4 work).
This paper adds concurrency with fine-grained locking and progress guarantees to CertiKOS.

The key result in this paper is Contextual Refinement: that if the kernel K is a refinement of the specification then, for any user program P, KxP is a refinement of SxP.
Showing this result for a concurrent system requires a proof that kernel calls are linearizable and of a progress property such as starvation freedom.
A consequence of this result is that they can also derive _behavior equivalence_ of P under either S or K.

Most of the paper describes the proof with particular focus on how the layered structure determines the structure of the proof.
The layers are:

* Concurrent layer interface. A notion of shared objects supporting a number of primitives and ghost state maintaining a log of past primitive calls. Objects can be "private" or "atomic".  Atomic objects are shared so the name indicates a requirement that they be accessed atomically.
* Machine model with hardware scheduler.  This layer introduces an oracle to decide whether to perform a context switch after each instruction.
* Machine model with local copy of shared memory.  This layer introduces a notion of ownership of a shared object by introducing "pull" actions to take ownership and "push" actions to release ownership.  (These are ghost code, updating ghost state.). This lets them talk about Data Race Freedom.
* Partial machine with environment contexts.  This layer lets them reason separately about the code running on different CPUs.
* CPU-local machine model.  This layer introduces a "log cache" in order to delay when primitive actions are considered to happen through shuffling and merging of events in a log.  I think this is where serializability comes into play.

It is worth mentioning what is not verified:

* TLB shootdown code (because they don't have a spec for the TLB)
* The ELF loader (this seems like a significant omission!)
* The boot loader
* A PreInit module that initialises the CPU and the devices.
Also, the concurrency results assume a sequentially consistent memory model – that is, a strict interleaving semantics.
The paper says that the proof should remain valid for the x86 TSO model but that is not done in this paper.

The introduction suggests that one of the benefits of the layered approach is that it decomposes the verification task into many simple _and easily automated ones_.  The paper makes a good case for the simplicity of this approach but it seems that the proof itself is around 40,000 lines of definitions and 50,000 lines of proof so the argument that this is easily automated is less clear.

Since the code itself is only 6500 lines of C and assembly code, the total proof+specification overhead is around 15x for this part.
The paper suggests that one third of the overhead is redundant and semi-automatically generated.  However, it still has to be maintained so I think that this remains a serious issue for more widespread adoption.

The paper is not clear but my suspicion is that part of the reason for the size of the proof and auxiliary definitions is the layered structure.
My guess is that, for each layer, you have to state and re-prove any properties that carry over from the layer below – even if that proof is fairly trivial.

As far as I can tell, the sizes stated in the paper are the size of the new concurrency related proof – I don't think that it includes the size of the proof about the previous sequential version that is reused.  (The paper does not explicitly mention the size of the CompCert changes and proofs but I assume that those are part of the 90,000 lines.)

Since one of the key differences from seL4 is the support of fine-grained locking (instead of seL4's single big lock), the evaluation focussed on absolute and relative performance as the number of CPUs grows.
The L4 family has always focussed on very fast IPC so, as one might expect, seL4 is significantly faster (50-100%).
They do not directly compare multiprocessor scaling with seL4 but they do compare use of a single big-lock version of CertiKOS with the fine-grained locking version and see that the big lock adds around 40% overhead on 3 cores compared with finer locks.


A second evaluation uses mC2 (the particular version of CertiKOS in this paper) as a hypervisor.
In this experiment, they are able to run Ubuntu in the guest VMs and they compare against the KVM hypervisor.
The big performance difference here comes from limitations of the disk driver interface.


One question that I am left with is whether the layered structure brings any flexibility to the code (as it did in Ford's Recursive Virtual Machines).
That is, can we replace, omit or reorder layers to get interesting variations on CertiKOS?
It is possible that the hypervisor configuration does this – but it is not clear from the paper.

