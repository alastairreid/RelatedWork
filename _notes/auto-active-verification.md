---
layout: note
title: Auto active verification
notes:
- Boogie verifier
- Dafny verifier
- VeriFast verifier
papers:
- nelson:sosp:2019
---

A term coined by Leino and Moskal

> [...] all interaction with the program verifier [is] done with annotations
> supplied in the program text [...]. This was made possible by powerful automatic
> satisfiability-modulo-theories (SMT) solvers.
> <br>--- [Usable auto-active verification], [Usable Verification Workshop 2010].

though I think they are retroactively naming what the [ESC report] did.

A more recent description

> In contrast to interactive theorem provers, auto-active theorem provers ask
> developers to write proof annotations on implementation code, such as
> preconditions, postconditions, and loop invariants. The prover translates
> the annotated code into a verificationcondition and invokes a constraint
> solver to check its validity.
> <br>--- [nelson:sosp:2019]

Some examples are the [Dafny verifier], the [Boogie verifier] and the [VeriFast verifier].

[ESC report]: https://scholar.google.co.uk/scholar?q=extended+static+checking
[Usable Verification Workshop 2010]: http://fm.csl.sri.com/UV10/
[Usable auto-active verification]: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.295.2080&rep=rep1&type=pdf

{% include links.html %}
