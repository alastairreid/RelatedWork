---
ENTRYTYPE: inproceedings
added: 2020-09-19
authors:
- Andrew Macvean
- John Daughtry
- Luke Church
- Craig Citro
booktitle: Proceedings of the 26th annual workshop of the Psychology of Programming Interest Group
layout: paper
read: true
readings:
- 2020-09-21
title: API usability at scale
year: 2016
notes:
- google
- friction diagram
papers:
- rieman:chi:1995
---

How can you evaluate the usability of web APIs?
They gather usage data from the [Google API explorer](https://developers.google.com/apis-explorer) for 26 APIs
looking for explorations that produce 4xx (i.e., HTTP error codes).
They find that three particular APIs are especially error prone.

The next problem is gathering data about number of parameters, number of
methods in API, etc. and try to correlate with how error prone an API is.
The "coefficient of determination (R^2) score" is just "0.256".

To communicate with developers, they observe users and generate [friction
diagrams] and then use a cognitive walkthrough ([rieman:chi:1995]) to explain
the problem to the API designers.

Evolving APIs is hard when you can't get hold of all the clients.

A common metric to optimize is the "Time to Hello World" (TTHW): the time to
get a trivial example working.
Within Google, they instead use "Pain to Hello World" (PTHW) in order to focus
more on long-term success.

One possible way to make evolving APIs easier is to auto-generate libraries
for many different languages. Those libraries can support both the old and
new APIs and can switch over to the new API when ready.
Alas, it seems that hand-written libraries are more idiomatic and easier to
use.

{% include links.html %}
