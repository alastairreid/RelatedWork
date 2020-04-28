---
layout: note
title: Magic wand
---

"Magic wand" is the somewhat whimsical name for the intuitionistic implication
operator "—∗" used in [Separation logic] and its generalization [Permission
logic].

I get the impression that magic wands were largely ignored because use of magic
wands hit decidability problems.
Some more recent papers that changed that are:
[schwerhoff:ecoop:2015],
[blom:ijsttt:2015].
They get round the decidability problems by introducing witnesses for
magic wands.

Magic wands are useful for modelling partial data structures such as
all the parts of a tree from the root down except for the bit that is
currently being processed.

Magic wands are also used to model borrow semantics in the [Rust language] by
[astrauskas:oopsla:2019].

[Permission logic]: {{ "notes/permission-logic" | relative_url }}
[Rust language]: {{ "notes/rust-language" | relative_url }}
[Separation logic]: {{ "notes/separation-logic" | relative_url }}
[astrauskas:oopsla:2019]: {{ "papers/astrauskas:oopsla:2019" | relative_url }}
[blom:ijsttt:2015]: {{ "papers/blom:ijsttt:2015" | relative_url }}
[schwerhoff:ecoop:2015]: {{ "papers/schwerhoff:ecoop:2015" | relative_url }}
