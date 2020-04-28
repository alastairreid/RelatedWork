---
layout: note
title: Permission logic
examples:
- chalice-verifier
- viper-verifier
---

Permission logic is a generalization of [separation logic].
All permission logics have

- a notion of resource
- resources follow rules of [linear logic] wrt replication / consumption

Permission logics include
- many variants of [separation logic]
- [implicit dynamic frames]

Systems based on permission logic:

- [Chalice]
- [Viper]

## Papers about permission logic

{% include paperlist.html %}

[Chalice]: {{ "notes/chalice-verifier" | relative_url }}
[Separation logic]: {{ "notes/separation-logic" | relative_url }}
[Implicit dynamic frames]: {{ "notes/implicit-dynamic-frames" | relative_url }}
[Viper]: {{ "notes/viper-verifier" | relative_url }}
[linear logic]: {{ "notes/linear-logic" | relative_url }}
