---
layout: note
title: FShell Query Language (FQL)
notes:
- SV competition
papers:
- holzer:cav:2008
- holzer:hvc:2010
---

FQL is a query language for describing code coverage criteria.
It consists of

- structural constraints specified as path automata
- quality constraints such as
  - block coverage
  - condition coverage
  - predicate coverage

The syntax of FQL is defined in [holzer:hvc:2010].
An FQL spec has the form

    in G cover C passing P

where

- "in G" and "passing P" are optional
- G is a filter functon
  - "@BASICBLOCKENTRY"
  - "@FUNC(<name>)" ("@CALL" in later work)
  - "@CONDITIONEDGE" ("@DECISIONEDGE" in later work)
- C is a coverage specification
    - A regexp like syntax
        - line specifications @4, @7, etc.
        - conditions "{ x == 42 }", etc.
        - wildcards "ID"
        - quoted regexps
        - Normal regexp syntax: ".", "*", "+", "^" and "$" ("*" can only occur inside quotes)
    - Which are used in
        - edges using "EDGES(regex)"
        - nodes (i.e., statements) using "NODES(regex)"
        - paths using "PATHS(T, k)" where "T" is a filter function and "k"
          is a bound on how many times "T" appears.

- P is a "passing clause": a path pattern that every test case must satisfy
  - For example, "^NOT(@CALL(unimplemented))*$"
  - For example, "^(ID.{x >= 0})*$" specifies tests where x never becomes
    negative.

The syntax "in @FUNC(foo) cover EDGES(@DEF(x))" is equivalent to
"cover EDGES(COMPOSE(@DEF(x), @FUNC(foo)))".

Sugar:

- "->" == ".ID*"


{% include links.html %}
