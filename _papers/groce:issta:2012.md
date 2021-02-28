---
ENTRYTYPE: inproceedings
abstract: Swarm testing is a novel and inexpensive way to improve the diversity of test cases generated during random testing. Increased diversity leads
  to improved coverage and fault detection. In swarm testing, the usual practice of potentially including all features in every test case is abandoned.
  Rather, a large "swarm" of randomly generated configurations, each of which omits some features, is used, with configurations receiving equal resources.
  We have identified two mechanisms by which feature omission leads to better exploration of a system's state space. First, some features actively prevent
  the system from executing interesting behaviors; e.g., "pop" calls may prevent a stack data structure from executing a bug in its overflow detection logic.
  Second, even when there is no active suppression of behaviors, test features compete for space in each test, limiting the depth to which logic driven
  by features can be explored. Experimental results show that swarm testing increases coverage and can improve fault detection dramatically; for example,
  in a week of testing it found 42\% more distinct ways to crash a collection of C compilers than did the heavily hand-tuned default configuration of a
  random tester.
added: 2021-02-26
address: New York, NY, USA
authors:
- Alex Groce
- Chaoqiang Zhang
- Eric Eide
- Yang Chen
- John Regehr
booktitle: Proceedings of the 2012 International Symposium on Software Testing and Analysis
doi: 10.1145/2338965.2336763
isbn: '9781450314541'
layout: paper
link: https://doi.org/10.1145/2338965.2336763
location: Minneapolis, MN, USA
numpages: '11'
pages: 78-88
publisher: Association for Computing Machinery
read: true
readings:
- 2021-02-27
series: ISSTA 2012
title: Swarm testing
url: https://doi.org/10.1145/2338965.2336763
year: 2012
notes:
- swarm verification
papers:
- holzmann:ieeetse:2011
---

This paper adapts the ideas of [swarm verification] ([holzmann:ieeetse:2011])
in a testing context.
Like [swarm verification], the idea is to use a diverse range of configurations
to get better coverage than you would get with a single configuration (even if
it is carefully chosen).
Swarm testing makes better use of a fixed time budget and reduces the
effort needed to tune testing configurations.

Unlike swarm verification, parallelism is not a significant motivation: presumably
because testing tends to be based on many small tests that could already be
parallelized.

Some sources of different configurations are

- Omitting some subset of an API from testing.
  e.g., omitting the `pop` operation from a data-structure test -
  which may make it easier for tests to hit overflow behaviour.

- Omitting input features such as language features (in compiler testing),
  input file features (when testing media libraries), etc.

Exploiting "feature omission diversity" in this way is the only technique used
in swarm testing.
(Although they do not evaluate it in this paper, they suggest that
this would also be useful in model checking under a fixed time budget.)

**The key insight of the paper is that features can suppress bugs.**

> including a feature in a test does not always improve the ability of the test
> to cover behavior and expose faults: some features can actively suppress the
> exhibition of some behaviors.

The explanation is that different features tend to affect different parts
of the system state so executing those features more tends to be better at
exploring “deep” values of state variables.

The meat of the paper is three case studies that test this theory in practice:
a flash file system (using random mutations), C compilers and a red-black tree.

For the flash file system, improvements are seen in all coverage metrics and,
for mutants that are hard to "kill" (i.e., that pass most tests), significantly
increases detection rates. Interestingly, testing with all features enabled
tends towards "overkill": those mutants that are killed are killed by
significantly more tests. This confirms the idea that traditional random testing
is not as random as we would like.

An interesting side-effect of swarm-testing is that, after finding the same bug in multiple
configurations, you can calculate the relevance of each feature to the bug - possibly
helping you to find the bug.
(This is easy in the first experiment because you know that each mutant has just
one bug that would cause any failure but they are able to revisit it during
the second experiment by using the text of assertion failure error messages
in the compiler for bug triage.)

It also allows them to examine the idea of features being bug triggers or bug
suppressors. Interestingly, they find that some significant triggers are also
suppressors and vice-versa: reinforcing the idea that there is no such thing
as a best configuration.

The third experiment is a bit harder to interpret. There is a benefit
but they also show that bad choices about what to discard and test size
can make things worse than traditional testing.

The related work section is a good survey of many types of testing.

{% include links.html %}
