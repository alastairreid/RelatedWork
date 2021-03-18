---
layout: note
notes:
- symbolic execution
- angr verifier
papers:
- coppa:ase:2017
title: Symbolic memory
---

In symbolic execution tools, there is a choice about what to do with symbolic memory addresses.
They can be concretized on all accesses, concretized on writes but not reads, on reads but not writes or kept symbolic.
Additionally, they can be concretized if they fall outside a certain range [angr verifier].

[coppa:ase:2017] describes a fully symbolic approach and compares against other tools that use more concretization.

It is not clear whether this is worse for binary analysis tools since they have less type information
to work with?

{% include links.html %}
