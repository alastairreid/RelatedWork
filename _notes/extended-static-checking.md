---
layout: note
title: Extended static checking (ESC)
wiki: https://en.wikipedia.org/wiki/Extended_static_checking
notes:
- SeaHorn verifier
- SMACK verifier
- SV competition
- AoRTE
---

> ESC can be thought of as an extended form of type checking.
> [...]
> it promotes practicality over soundness, in that it aims to dramatically
> reduce the number of false positives (overestimated errors that are not real
> errors, that is, ESC over strictness) at the cost of introducing some false
> negatives (real ESC underestimation error, but that need no programmer's
> attention, or are not targeted by ESC).
> ESC can identify a range of errors which are currently outside the scope of
> a type checker, including division by zero, array out of bounds, integer
> overflow and null dereferences.
> <br>--- [Wikipedia](https://en.wikipedia.org/wiki/Extended_static_checking)

Extended static checking achieves ["Absence of RunTime Exceptions"][AoRTE]
(AoRTE) which is things like

- No division by zero
- No integer overflow
- Memory safety
  - All array accesses in bounds
  - No null dereferences
  - No buffer overflows
  - No use after free
  - No memory leaks
- Lock safety of concurrent code

The nice thing about extended static checking is that you don't have
to write specifications or proofs.

The software verification competition [SV-COMP][SV competition] mostly checks
properties like this.

{% include links.html %}
