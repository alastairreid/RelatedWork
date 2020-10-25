---
layout: note
notes:
- test driven development
- testability
wiki: https://en.wikipedia.org/wiki/Test_double
papers: {}
title: Test doubles (fakes, mocks and stubs)
---

Replacement for a software component.
Terminology is apparently inconsistent about which is which but the three choices are

- A simplified, but accurate implementation of a component (e.g., an in-memory database)
- An empty shell that can be preprogrammed with a canned sequence of expected method calls
  and results to return in response to those calls.
  If the call sequence does not match the expectation, a test failure is reported.

{% include links.html %}
