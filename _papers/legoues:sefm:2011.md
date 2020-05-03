---
ENTRYTYPE: inproceedings
abstract: The Boogie Verification Debugger (BVD) is a tool that lets users explore
  the potential program errors reported by a deductive program verifier. The user
  interface is like that of a dynamic debugger, but the debugging happens statically
  without executing the program. BVD integrates with the program-verification engine
  Boogie. Just as Boogie supports multiple language front-ends, BVD can work with
  those front-ends through a plug-in architecture. BVD plugins have been implemented
  for two state-of-the-art verifiers, VCC and Dafny.
added: 2020-03-04
address: Berlin, Heidelberg
authors:
- Claire Le Goues
- K. Rustan M. Leino
- Michał Moskal
booktitle: Software Engineering and Formal Methods
editor: 'Barthe, Gilles
  and Pardo, Alberto
  and Schneider, Gerardo'
isbn: 978-3-642-24690-6
layout: paper
pages: 407-414
publisher: Springer Berlin Heidelberg
read: true
readings:
- 2020-03-03
title: The Boogie verification debugger
year: 2011
topics:
- tools
- verification
notes:
- Boogie verifier
- Dafny verifier
- VCC verifier
papers:
- barnett:fmco:2005
- leino:lpair:2010
- cohen:cav:2010
- cohen:cav:2010
- barnett:cacm:2011
- jacobs:nfm:2011
---

A critical part of any verification tool is a debugger that helps you understand and localise any errors detected.
For dynamic verification (i.e., testing), we typically use a debugger like gdb/lldb to halt the program at interesting points and inspect the state of the system.
For static verification (i.e., formal verification), it initially seems quite different because the verification tool typically does not run the program from the beginning and does not generate concrete values for all variables.
I think the message of this paper is that it is not as hard as it seems.

The ingredients of their solution are:
- The language specific part of the verifier generates canonical names for heap objects. e.g., for nodes of type T, it might call them T'0, T'1, etc.
- Allowing you to step through the code and showing values accessible in either the previous state or the next state as you step.  (I guess conventional dynamic debuggers do this too?)
- Supporting search for aliases (other pointers to the same location)
- Breadth first conversion of SMT solver states to source-language states
- <something> for Skolem constants
- A standard plugin interface to the language front end.  For VCC, this is 1000 lines, for Dafny, it is 400 lines.

As the title implies, this is implemented in
[Boogie][barnett:fmco:2005]
and they have implemented the frontend support for both
[Dafny][leino:lpair:2010]
and
[VCC][cohen:cav:2010].

The paper has a useful list of other work in
ESC/Modula-3,
ESC/Java,
[VCC][cohen:cav:2010],
[Spec#][barnett:cacm:2011],
[VeriFast][jacobs:nfm:2011]
and
CBMC.
This topic is not discussed often so it is super-useful to find a list of what little has been reported.


{% include links.html %}
