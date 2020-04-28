---
layout: note
title: Prusti verifier
papers:
- schwerhoff:ecoop:2015
- astrauskas:oopsla:2019
---

Prusti is a verifier for the [Rust language]
based on 
[permission logic] and using the [Viper verifier] as
an [intermediate verification language].
Prusti was developed by ETH Zurich.

An unusual part of its design is that it makes use of
[magic wands] to model reference borrowing.

[Intermediate verification language]: {{ "notes/intermediate-verification-language" | relative_url }}
[Permission logic]: {{ "notes/permission-logic" | relative_url }}
[Prusti verifier]: {{ "notes/prusti-verifier" | relative_url }}
[Rust language]: {{ "notes/rust-language" | relative_url }}
[magic wands]: {{ "notes/magic-wand" | relative_url }}
[Viper verifier]: {{ "notes/viper-verifier" | relative_url }}
