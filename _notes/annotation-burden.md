---
layout: note
title: Annotation burden
papers:
- calcagno:popl:2009
- cohen:cav:2010
- gu:osdi:2016
- mangano:crisis:2016
- morrisett:wcsss:1999
- vasudevan:usenix:2016
- vogels:fmoods:2011
- costanzo:pldi:2016
- klein:sosp:2009
- leroy:cacm:2009
notes:
- ghost code
- VeriFast verifier
- interactive theorem prover
- auto-active verification
---

Program verification using
[auto-active verifiers][auto-active verification] and
[interactive theorem prover]s requires writing annotations,
proof scripts or [ghost code] to assist the verification.

Some reported numbers are

| Prover         | System            | Paper                   | Burden |
| -------------- | ----------------- | ----------------------- | -----: |
| VCC            | Hyper-V           | [cohen:cav:2010]        | 100%   |
| Frama-C        | Contiki           | [mangano:crisis:2016]   | 110%   |
| Frama-C        | überSpark         | [vasudevan:usenix:2016] | 110%   |
| Coq            | CertiKOS          | [gu:osdi:2016]          | 1500%  |
| -------------- | ----------------- | ----------------------- | ------ |

todo: collect more data

[vogels:fmoods:2011] describes some techniques to infer annotations in
the [VeriFast verifier].
[calcagno:popl:2009] describes the Infer system used to infer function
contracts for various systems including parts of the Linux kernel.

{% include links.html %}
