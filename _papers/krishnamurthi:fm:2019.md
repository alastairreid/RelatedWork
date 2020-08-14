---
ENTRYTYPE: inproceedings
abstract: Formal methods are invaluable for reasoning about complex systems. As these techniques and tools have improved in expressiveness and scale, their
  adoption has grown rapidly. Sustaining this growth, however, requires attention to not only the technical but also the human side. In this paper (and
  accompanying talk), we discuss some of the challenges and opportunities for human factors in formal methods.
added: 2020-08-14
address: Cham
authors:
- Shriram Krishnamurthi
- Tim Nelson
booktitle: Formal Methods - The Next 30 Years
editor: ter Beek, Maurice H. and McIver, Annabelle and Oliveira, José N.
isbn: 978-3-030-30942-8
layout: paper
pages: 3-10
publisher: Springer International Publishing
read: true
readings:
- 2020-08-14
title: The Human in Formal Methods
year: 2019
notes:
- SAT solver
- SMT solver
- Alloy verifier
- Model checking
- Human factors
papers:
---

This invited talk looks at "how to bring the other 90%
into the fold" of formal methods with a focus on
education, comfort with formal methods and effectiveness with formal methods.
This focus leads to emphasizing model finding such as the [Alloy verifier], [SAT
solver]s and [SMT solver]s over deductive methods.

User experience is briefly discussed – mentioning that model finders are "often
integrated into higher-level tools (with their output presented in
a domain-specific way)".

The main focus is on education and especially creating specifications which is
based on an analogy to the author's "How to design programs" book that breaks
creating a program into seven steps starting with designing I/O data structures and
examples and ending with testing.
Each of these steps leads to distinct artifacts.
This builds on a lot of cognitive theory from education research and the notion
of "concreteness fading" as design goes from concrete examples to more
flexible/abstract/generalized code.

In an educational setting, they can lean on the availability of "ground truth":
the instructor already understands the problem and has a solution.  This allows
any artifacts (e.g., examples) developed during the design process to be
automatically checked against the instructors solution and feedback given in
the form of new examples for the student to consider.  (The author's have
published about this before in the context of program design.)

{% include links.html %}
