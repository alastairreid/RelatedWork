---
ENTRYTYPE: inbook
abstract: A program verifier is a tool that allows developers to prove that their
  code satisfies its specification for every possible input and every thread schedule.
  These lecture notes describe a verifier for concurrent programs called Chalice.
added: 2020-02-11
address: Berlin, Heidelberg
authors:
- K. Rustan M. Leino
- Peter Müller
- Jan Smans
booktitle: 'Foundations of Security Analysis and Design V: FOSAD 2007/2008/2009 Tutorial Lectures'
doi: 10.1007/978-3-642-03829-7_7
editor: 'Aldini, Alessandro and Barthe, Gilles and Gorrieri, Roberto'
isbn: 978-3-642-03829-7
layout: paper
pages: 195-222
publisher: Springer Berlin Heidelberg
read: true
readings:
- 2020-02-15
title: Verification of concurrent programs with Chalice
url: https://doi.org/10.1007/978-3-642-03829-7_7
year: 2009
topics:
- tools
- verification
notes:
- permission logic
- modular verification
- contract driven development
- fractional permissions
- permission accounting
- Chalice verifier
- ghost code
papers:
---

This is a tutorial on the Chalice object-oriented language and verifier.
Methods have contracts, loops have invariants,
pointers have ownership annotations,
there are threads, locks and fractional ownership,
there are lock orderings to detect deadlock
and there are ghost variables and fold/unfold ghost statements.

The language seems to have had more attention paid
to usability than normal.

- For example, fractional permissions get the job done – but
  they are a slightly obscure way to say that something is "read only"
  so Chalice has notation to say that something is read only.

- There are command line options to reduce the amount of
  annotation required:

  - unfolding and folding predicates at the start/end of each method

  - automatically trying to fold when a predicate is required

The conclusions section is great: it explains the influences,
where ideas came from, who did what and where the reader might
find more about the concepts in this language/tool.

{% include links.html %}
