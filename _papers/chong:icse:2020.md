---
ENTRYTYPE: inproceedings
added: 2020-07-06
authors:
- Nathan Chong
- Byron Cook
- Konstantinos Kallas
- Kareem Khazem
- Felipe R. Monteiro
- Daniel Schwartz-Narbonne
- Serdar Tasiran
- Michael Tautschnig
- Mark R. Tuttle
booktitle: Proceedings of the 2020 International Conference on Software Engineering (ICSE)
doi: 10.1145/3377813.3381347
title: Code-level model checking in the software development workflow
month: June
read: true
readings:
- 2020-07-06
year: 2020
notes:
- model checking
- CBMC verifier
---

This very readable paper describes the successful introduction of a formal
verification flow into the development of the Amazon C Common library.  Anyone
trying to introduce formal verification into a traditional development team
should read this paper!

The most important aspect of the paper is probably their focus on getting
developer buy in. This resulted in the developers writing a lot of the function
contracts as well as reviewing contracts, proofs and bugfixes written by the
verification team.  In part, this was due to finding bugs that the developers
considered worth fixing although the verification team's goal was not just to
find bugs but to prove absence of bugs.

They highlight four lessons that they learned:

- Make specifications explicit in source code
- Write proofs-harnesses in declarative style
- Integrate proof artifacts into the development workflow
- Fix bugs instead of just reporting them

that they credit with:

- Increased proof speed (i.e., reduced human effort)
- Increased rate of bugs found and fixed
- Active developer engagement with proofs
- Increase in lines of specifications written by developers


One surprising thing is the notion of proof which, in their case,
is the verification harness used to invoke each verified function
with appropriately constrained symbolic inputs and appropriate assertions
about the results.
This harness allows them to use the [CBMC verifier] to verify that
each function meets its contract.

The properties verified (and bugs found) are mostly low-level safety properties
(integer overflow, null pointer dereference and memory safety) together with
some functional properties.

The paper is full of stories about how they interacted with and gained the
trust of the developers and graphs showing the rate at which proofs, bugs, etc.
were created/found/etc.
