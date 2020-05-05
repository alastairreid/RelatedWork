---
layout: note
title: Arm Architecture Specification Language (ASL)
wiki: https://en.wikipedia.org/wiki/Abstract_interpretation
notes:
- Arm architecture
- ISA specification
papers:
- reid:cav:2016
- reid:fmcad:2016
- reid:oopsla:2017
- reid:phd:2019
---

ASL is the [ISA specification] language used by Arm to
specify their A-, R- and M-profile processor architectures ([reid:fmcad:2016]).
Those specifications have been extensively tested,
formally validated ([reid:oopsla:2017])
and have been used to formally validate Arm's
processor implementations ([reid:cav:2016]).

> ASL is an executable, strongly-typed, imperative language with support for
> [dependent type]s and for throwing and catching exceptions.  For the first
> 20–25 years of Arm’s history, specifications were created after the
> corresponding implementation as documentation of what had been built.  [...]
> specifications are now written and tested before implementation starts.
>
> The ASL language was created by reverse engineering a specification language
> from the pseudocode notation used in Arm’s existing documentation, fixing the
> pseudocode in the documentation and evolving that pseudocode into a formal
> specification.
> <br>--- Alastair Reid ([reid:phd:2019])

{% include paperlist.html %}

{% include links.html %}
