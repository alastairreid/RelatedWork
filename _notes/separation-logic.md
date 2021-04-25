---
layout: note
title: Separation logic
wiki: https://en.wikipedia.org/wiki/Separation_logic
isa:
- permission logic
notes:
- alias analysis
- shape analysis
- abstract interpretation
- symbolic execution
- VeriFast verifier
papers:
- calcagno:sas:2006
- calcagno:popl:2009
---

Separation logic is an extension of [Hoare
logic](https://en.wikipedia.org/wiki/Hoare_logic)
that adds the
ability to reason about heap-based data structures and,
in particular, about aliasing.
It does this using ideas from linear logic to model
resources that cannot be duplicated.

Variations on the theme of separation logic have been developed
and are collectively referred to as [permission logic].

Many tools that use separation logic only use a subset because
some parts of separation logic like "magic wands" (linear implication)
have poor complexity/decidability
properties.
In particular, tools often keep the linear and the classical
parts of a term separate.

Automatic tools that use separation logic (e.g., [calcagno:sas:2006] and
related papers) often use [abstract interpretation] and use an even smaller
subset of separation logic as their abstract domains together with more
conventional widening operators, fixpoints, etc.  This lets them construct a
[shape analysis] where separation logic terms are used to capture what is known
about the shape of a data structure.  And it lets them move back and forth
between precise reasoning using [symbolic execution] outside of loops and
deliberately dropping information using abstract interpretation when
generalizing loop bodies into loops / loop invariants.

Auto-active tools like the [VeriFast verifier] typically use more of the logic
(but still not all of it) and require the user to provide loop invariants.

{% include links.html %}
