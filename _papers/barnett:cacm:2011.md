---
ENTRYTYPE: article
added: 2020-02-16
address: New York, NY, USA
authors:
- Mike Barnett
- Manuel Fähndrich
- K. Rustan M. Leino
- Peter Müller
- Wolfram Schulte
- Herman Venter
doi: 10.1145/1953122.1953145
issn: 0001-0782
issue_date: June 2011
journal: Communications of the ACM
layout: paper
month: June
number: '6'
numpages: '11'
pages: 81-91
publisher: Association for Computing Machinery
read: true
readings:
- 2020-02-16
title: 'Specification and verification: The Spec# experience'
url: https://doi.org/10.1145/1953122.1953145
volume: '54'
year: 2011
topics:
- tools
- verification
notes:
- spec-sharp-project
- Boogie verifier
- contract driven development
papers:
- barnett:cassis:2004
- chatterjee:tacas:2007
- fahndrich:foveoos:2010
- logozzo:vmcai:2011
- barnett:fmco:2005
- leino:tacas:2010
- demoura:tacas:2008
---

[Spec#][barnett:cassis:2004]
was a Microsoft Research project that added automated verification
to C# through the addition of method contracts, class invariants and
loop invariants.
This was all integrated into the Visual Studio IDE to make for a very
different user experience from normal verification: they wanted verification
to be integrated into the development flow.
This paper gives a retrospective on the project with a particular focus
on efforts to get the techniques adopted.

Spec# was an ambitious project with many different parts:

- Frontend: Visual Studio integration so that verification errors
  show up as "squigglies" under the offending code.

- Language: it was a superset of C# which brought advantages of a large
  codebase and userbase to try things on but tracking a large language
  as it evolves is hard and the language brings several problems of its
  own.

  ([HAVOC][chatterjee:tacas:2007]
  was a spinoff that applied some Spec# ideas to low-level C code.)

- Platform: their work built on Microsoft's .NET framework which gave
  them even more potential impact but also meant that Spec# code could
  be linked against programs written in other languages that did not
  have contracts.
  This lead to the development of a
  [language-neutral contract library][fahndrich:foveoos:2010],
  [see also logozzo:vmcai:2011][logozzo:vmcai:2011].

- Contracts that could be used for dynamic checking or static verification.
  An early goal was to integrate with established programming practice
  so a subset of their contract language can be checked dynamically.

  (Although different, this reminds me of [Executable
  ACSL](http://www.open-do.org/wp-content/uploads/2011/05/e-acsl.pdf).)

- One of the most frequent things stated in function contracts is whether
  a pointer can be null or not.
  So, by default, object references in Spec# are non-null and you have
  to explicitly request a nullable type.
  They strongly urge language designers to follow this model.

- Compiler integration: instead of extending the parser for C#, they
  verify the MSIL bytecode.  This requires them to reverse engineer
  some of the transformations that the compiler made and they would
  have benefited from having the compiler provide extra information
  to make this easier.

- Verification backend: the
  [Boogie Intermediate Verification Language][barnett:fmco:2005]
  was created to support Spec# but has been used in many other projects.
  (See also: [Boogie2][leino:tacas:2010].)
  And Boogie builds on [Z3][demoura:tacas:2008].

I have probably missed out a lot of important stuff – read the paper!

{% include links.html %}
