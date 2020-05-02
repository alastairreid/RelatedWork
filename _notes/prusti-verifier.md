---
layout: note
title: Prusti verifier
papers:
- schwerhoff:ecoop:2015
- astrauskas:oopsla:2019
notes:
- intermediate verification language
- permission logic
- Rust language
- viper verifier
- Prusti verifier
- magic wand
---

Prusti is a verifier for the [Rust language]
based on 
[permission logic] and using the [Viper verifier] as
an [intermediate verification language].
Prusti was developed by ETH Zurich.

An unusual part of its design is that it makes use of
[magic wand]s to model reference borrowing.

{% include links.html %}
