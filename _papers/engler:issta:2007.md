---
ENTRYTYPE: inproceedings
added: 2021-04-18
address: New York, NY, USA
authors:
- Dawson Engler
- Daniel Dunbar
booktitle: Proceedings of the 2007 International Symposium on Software Testing and Analysis
doi: 10.1145/1273463.1273464
isbn: '9781595937346'
keywords: bug finding, dynamic analysis, symbolic execution
layout: paper
link: https://doi.org/10.1145/1273463.1273464
location: London, United Kingdom
numpages: '4'
pages: 1-4
publisher: Association for Computing Machinery
read: true
readings:
- 2021-04-18
series: ISSTA '07
title: 'Under-constrained execution: Making automatic code destruction easy and scalable'
url: https://doi.org/10.1145/1273463.1273464
year: 2007
notes:
- EXE verifier
- lazy initialization
papers:
- calcagno:popl:2009
- ramos:sec:2015
- khurshid:tacas:2003
- xie:popl:2005
---

Extends the [EXE verifier] with support for under-constrained variables.
Any errors detected by symbolic execution are only reported if the path condition does
not depend on the value of an under-constrained variable.
For example, if a pointer is dereferenced, we add a constraint that the pointer
is non-null and a new under-constrained variable is created for the value read.
This idea apparently originates in Java PathFinder (JPF) ([khurshid:tacas:2003],
[xie:popl:2005]).

I'm not clear how this is different from abduction ([calcagno:popl:2009]) which
seems to operate in a similar way.

Under-constrained variables are used for function inputs to let us infer
function preconditions for each path executed avoiding the need to specify the
precondition explicitly.

Under-constrained variables can also be used when a function calls an external function:
a symbolic unconstrained return value is created.

This approach allowed them to analyze a lot of Linux device drivers relatively easily.

One tricky detail is that they track under-constrained variables through a form of taint-tracking.
The subtle thing is that if you compare a normal "exactly-constrained" variable 's' against
an under-constrained variable 'u', then 's' gains a constraint that depends on 'u' so
's' is now also under-constrained. That is, we can't use a conventional taint tracking but,
instead have to consider an equivalence class of all variables that are transitively
related to any under-constrained variable.

{% include links.html %}
