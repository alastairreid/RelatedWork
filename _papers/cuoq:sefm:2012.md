---
ENTRYTYPE: inproceedings
added: 2019-10-16
authors:
- Pascal Cuoq
- Florent Kirchner
- Nikolai Kosmatov
- Virgile Prevosto
- Julien Signoles
- Boris Yakobowski
- Patrick Baudin
- Richard Bonichon
- Bernard Botella
- Loïc Correnson
- Zaynah Dargaye
- Philippe Herrmann
- Benjamin Monate
- Yannick Moy
- Anne Pacalet
- Armand Puccetti
- Muriel Roger
- Nicky Williams
booktitle: International Conference on Software Engineering and Formal Methods
doi: 10.1007/s00165-014-0326-7
layout: paper
organization: Springer
pages: 233-247
read: true
readings:
- 2019-12-02
title: "Frama-C: A software analysis perspective"
year: 2012
topics:
- tools
- verification
notes:
- abstract interpretation
- Frama-C verifier
- Why3 verifier
papers:
---

Frama-C is a platform for verifying C programs.
This foundational article describes the architecture of this platform,
the analyses built into Frama-C and the additional plugins that can be used
with it and provides references to those other plugins.
The paper cites many related papers about individual plugins and
case studies.

The core of Frama-C is the ACSL specification language that can be used for
classic Hoare-logic like statements (first order logic + arith + pointers/separation).
In addition, functions can state which locations they modify.

The kernel of Frama-C consists of support for generating messages, logging user actions for later audit (and replay?), running independent transforms in parallel (e.g., to analyse with different parameters).
In addition, there are three key analyses that lay a foundation for other analyses:
* Value is a forwards abstract interpreter that tracks whether a location is initialized, dangling and anything known about the value (e.g., its range or "x%4 == 3").
* WP is a deductive verification plug-in that calculates weakest preconditions and discharges the resulting verification conditions using the Alt-Ergo SMT solver, Coq or Why (which can invoke several different backends).  WP provides a choice of memory models based on how complex the pointer dereferencing and casting/unions are in the code being analyzed.
* PathCrawler is a concolic testing plugin that enumerates paths and explores them using bounds on loop iterations to prune the number of paths.

The Value analysis also generates information about dependencies, write sets, etc. that other plugins can use to determine which statements are affected by or could affect some other statement and to generate program srlices either as a diagnostic aid or for more refined analyses.

Some additional plugins are
* Aoraï converts LTL formulae about function call sequences into ACSL annotations that are inserted into the program.
* Sante uses testing to confirm that any alarms are true bugs and not false alarms.  This uses a combination of Value to generate alarms, slicing to reduce the program to the parts needed by each alarm and PathCrawler to explore the paths within each slice.

{% include links.html %}
