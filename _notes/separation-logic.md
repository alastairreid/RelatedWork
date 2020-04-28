---
layout: note
title: Separation logic
wiki: https://en.wikipedia.org/wiki/Separation_logic
isa: permission-logic
---

Separation logic is an extension of Hoare logic that adds the
ability to reason about heap-based data structures and,
in particular, about aliasing.
It does this using ideas from linear logic to model
resources that cannot be duplicated.

Variations on the theme of separation logic have been developed
and are collectively referred to as [permission logic].


[Chalice]: {{ "notes/chalice-verifier" | relative_url }}
[Permission logic]: {{ "notes/permission-logic" | relative_url }}
[Viper]: {{ "notes/viper-verifier" | relative_url }}
