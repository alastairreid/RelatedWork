---
ENTRYTYPE: article
added: 2020-01-15
address: New York, NY, USA
articleno: Article 147
authors:
- Vytautas Astrauskas
- Peter Müller
- Federico Poli
- Alexander J. Summers
doi: 10.1145/3360573
issue_date: October 2019
journal: Proc. ACM Program. Lang.
keywords: heap-manipulating programs, type systems, Rust, concurrency
layout: paper
month: October
number: OOPSLA
numpages: '30'
publisher: Association for Computing Machinery
read: true
readings:
- 2020-02-10
title: Leveraging Rust types for modular specification and verification
url: https://doi.org/10.1145/3360573
volume: '3'
year: 2019
topics:
- tools
- types
- verification
notes:
- permission logic
- Rust language
- viper-verifier
- permission accounting
- cactus-plot
papers:
- heule:ftfjp:2011
- bornat:popl:2005
papers:
- ohearn:cacm:2019
- muller:vmcai:2016
- jacobs:nfm:2011
---

This paper exploits the close similarity between
Rust's type system
and
permission based reasoning approaches such as
[separation logic][ohearn:cacm:2019]
and
implicit dynamic frames logic.
Specifically, they describe the embedding of Rust programs
into the [Viper intermediate verification language][muller:vmcai:2016]
in a way that exploits the properties of Rust's
borrow-based type system.
This embedding is (partially?) implemented in the _Prusti_
verification tool that translates Rust to Viper
and translates any errors back from Viper to Rust.
Their focus at the moment is on "safe" code: code that
obeys the Rust type system.

Prusti is a plugin into rustc (the Rust compiler) and
it is able to use some of the type information available
inside the Rust typechecker although some of the internal
detail is hard to obtain and must be reconstructed
and some of the detail is only expressed as negative facts
instead of as positive witnesses.
Their goal is to construct Viper annotated with enough
annotations that no human intervention is required for
type-level proofs so Prusti has to reconstruct any
missing information.

One of the challenges with Rust's type system is the
notion of mutable reborrows.
This makes it hard for them to express some post-conditions
in the standard way and they propose a system of
"pledges" that talk not just about "old" values
(from before a function was called)
and the current values (from immediately after
when a function was called) but, when a function
returns a mutable reference, they must also talk about
the value that reference has after the reference's
lifetime ends.
This was a bit hard for me to get my head around because I
was still thinking of the reference as "just a pointer"
which may be how it is implemented but it is not how
the semantics works.

Another interesting detail is how they model immutable
references.
It seems that they really want to use
[counting permissions][bornat:popl:2005]
but, instead, they model them as fractional
permissions (an approach they attribute to [Heule][heule:ftfjp:2011]).

Their evaluation is in two parts

1. Verifying functions for undefined behaviour such as
   panics, assert failures, etc. – without adding
   specifications of the functions under test.
   They harvested 11,791 functions
   from 500 Rust crates (after discarding functions that
   use unimplemented features and very large functions
   that cause their translation to blow up.
   They report the time taken to verify functions (with the
   usual cactus plot)
   and the number of potential/actual errors found.
   It is not clear to me how many of these are confirmed
   bugs and have been reported/fixed.
   They also had problems with timeouts (mostly in non-linear
   arithmetic).
   Average verification time was 1 second but there was
   significant variation (median time was 0.16 seconds).


2. Verifying functional correctness of functions for
   which they added specifications.
   For this, they gathered code from [Rosetta
   Code](http://www.rosettacode.org/wiki/Rosetta_Code)
   and from [Matsakis' blog](http://smallcultfollowing.com/babysteps/),
   rewrote the examples to
   avoid unimplemented syntax, added functional
   specifications.
   Average verification time was over 30 seconds per
   function with a median time of around 20 seconds.
   (They don't report the average/median so those
   numbers come from me eyeballing the tables.)
   This is a bit slow (especially since I have recently been
   using the "very fast"
   [VeriFast][jacobs:nfm:2011]
   tool), but this is clearly early days in the tool
   development and they say there is a lot of opportunity
   for optimisation.
   
   

{% include links.html %}
