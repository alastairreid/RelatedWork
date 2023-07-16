---
ENTRYTYPE: article
abstract: 'Sanitizers are widely used compiler features that detect undefined behavior and resulting vulnerabilities by injecting runtime checks into programs.
  For better performance, sanitizers are often used in conjunction with optimization passes. But doing so combines two compiler features with conflicting
  objectives. While sanitizers want to expose undefined behavior, optimizers often exploit these same properties for performance. In this paper, we show
  that this clash can have serious consequences: optimizations can remove sanitizer failures, thereby hiding the presence of bugs or even introducing new
  ones. We present LookUB, a differential-testing based framework for finding optimizer transformations that elide sanitizer failures. We used our method
  to find 17 such sanitizer-eliding optimizations in Clang. Next, we used static analysis and fuzzing to search for bugs in open-source projects that were
  previously hidden due to sanitizer-eliding optimizations. This led us to discover 20 new bugs in Linux Containers, libmpeg2, NTFS-3G, and WINE. Finally,
  we present an effective mitigation strategy based on a customization of the Clang optimizer with an overhead increase of 4\%.'
added: 2023-07-02
address: New York, NY, USA
articleno: '143'
authors:
- Raphael Isemann
- Cristiano Giuffrida
- Herbert Bos
- Erik van der Kouwe
- Klaus von Gleissenthall
doi: 10.1145/3591257
issue_date: June 2023
journal: Proc. ACM Program. Lang.
keywords: Fuzzing, Sanitizers, Optimizations
layout: paper
link: https://doi.org/10.1145/3591257
month: jun
number: PLDI
numpages: '21'
publisher: Association for Computing Machinery
read: false
readings: []
title: 'Don''t look UB: Exposing sanitizer-eliding compiler optimizations'
url: https://doi.org/10.1145/3591257
volume: '7'
year: 2023
notes:
- undefined behaviour
- sanitizer
papers:
---

This is about the conflict between compiler optimizations and
sanitizers.
Compiler optimizations exploit UB behavior to optimize code and,
in the process, they can transform UB code to well-defined code
by picking an arbitrary interpretation for the code.
Sanitizers introduce additional runtime checks into code
to detect UB behavior.
Obviously, sanitizers cannot detect UB that has been elided by
a compiler optimization.

This paper uses differential testing to understand where this happens
in LLVM.

{% include links.html %}
