---
ENTRYTYPE: article
added: 2019-10-12
authors:
- Felipe R. Monteiro
- Mikhail R. Gadelha
- Lucas C. Cordeiro
journal: arXiv preprint arXiv:1904.06152
layout: paper
read: true
readings:
- 2019-10-16
title: Boost the impact of continuous formal verification in industry
year: 2019
topics:
- verification
papers:
---

Proposes a way to use model checking on large codebases when CI is used and lots of regression tests are available (at least one per C function).
Like fb-infer, focusses on verifying changes.
Approach is to use equivalence checking to find which functions may have changed, select regression tests relevant to those functions and then to generalise inputs of regression tests to increase their coverage.

I think this differs from fb-infer by using tests and model checking - but similar goals in terms of where it fits in developer workflow.

Final sentences say that they are working with AWS and Samsung to evaluate/apply their approach and tools.

{% include links.html %}
