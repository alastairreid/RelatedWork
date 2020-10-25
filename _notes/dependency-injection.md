---
layout: note
title: Dependency injection
wiki: https://en.wikipedia.org/wiki/Dependency_injection
url: https://martinfowler.com/articles/injection.html
date: 2020-10-25
notes:
- testability
- test driven development
- test double
papers:
---

Technique to make code more flexible mostly used for testing.
Consists of replacing hardcoded dependencies with parameters
so that the caller/creator has control over which object/function
is called.
e.g., instead of writing to stdout, pass a file handle to write to
or, better yet, pass an object that the code can write to.

See also [Dependency inversion principle (wikipedia)](https://en.wikipedia.org/wiki/Dependency_inversion_principle).

{% include links.html %}
