---
layout: note
title: Magic wand
papers:
- astrauskas:oopsla:2019
- blom:ijsttt:2015
- schwerhoff:ecoop:2015
notes:
- Permission logic
- Rust language
- Separation logic
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

{% include links.html %}
