---
layout: note
title: Concurrent separation logic
---

todo:

Concurrent separation logic is an extension of [separation logic] to handle concurrency.
Since the [frame rule] already takes care of most of the work, the
main extension is how to reason about locks, mutexes, and other synchronization
mechanisms.
Often the answer is that the synchronization mechanism logically owns the
resource when the lock (or whatever) is not held.

[Separation logic]: {{ "notes/separation-logic" | relative_url }}
