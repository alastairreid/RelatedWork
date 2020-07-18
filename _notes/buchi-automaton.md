---
layout: note
wiki: https://en.wikipedia.org/wiki/Büchi_automaton
notes:
- model checking
- Kripke structure
- temporal logic
papers: {}
title: Büchi automaton
---

A Büchi automaton is like a finite state machine (FSM) except that it
accepts infinite inputs.
An FSM accepts an input if it enters an accepting state _once_;
a Büchi automaton accepts an input if it passes through an accepting
state infinitely many times.

As with FSMs, there are deterministic and non-determistic variants of Büchi
automata but, unlike FSMs, not all non-deterministic automata can be converted
to deterministic Büchi automata.
(See [Wikipedia page] for details/alternatives.)

Büchi automata are used for [model checking] by converting linear [temporal
logic] formulae to automata.
They can accept any ω-regular language.

{% include links.html %}
