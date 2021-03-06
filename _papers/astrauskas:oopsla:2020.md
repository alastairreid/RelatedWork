---
ENTRYTYPE: inproceedings
added: 2020-11-01
authors:
- Vytautas Astrauskas
- Christoph Matheja
- Federico Poli
- Peter Müller
- Alexander J. Summers
booktitle: Object-Oriented Programming Systems, Languages, and Applications (OOPSLA)
journal: Proc. ACM Program. Lang.
volume: 4
pages: 136:1-136:27
doi: 10.1145/3428204
layout: paper
publisher: ACM
read: true
readings:
- 2021-06-16
title: How do programmers use unsafe Rust?
month: November
year: 2020
pages: 27
notes:
- Rust language
- Rust unsafe code
papers:
- evans:icse:2020
- qin:pldi:2020
---

This is an empirical study of unsafe Rust code.
It differs from [evans:icse:2020] by doing a more detailed measurement and analysis
of the different reasons that unsafe code is being used
and that they consider direct uses of unsafe annotations, not indirect uses
via dependencies. It is also based on code that is 18 months younger.


It identifies six reasons for using unsafe.

1. To overcome sharing restrictions (e.g., to create cyclic data structures, linked lists, etc.)
   and mutability restrictions (e.g., in read-only cache structures).

2. To overcome incompleteness restrictions.
   e.g., the compiler cannot recognize that two slices of an array do not overlap and
   therefore do not alias.

3. To document function contracts (preconditions?) and invariants.

4. Foreign function calls.

5. Use of the LLVM compiler's concurrency intrinsics.

6. Performance.
   e.g., using unchecked access functions and avoiding data copying.

Their analysis considers the frequency, size, 'self-containedness', encapsulation, and
motivation (wrt the six reasons above).
To  investigate this, they built a general purpose query tool "QRATES" for Querying
Rust Crates that can look for particular annotations, syntactic features, etc.
and they propose a set of specific queries to use to identify particular motivations, etc.

Unlike [evans:icse:2020], they study all crates on crates.io without separating out the
popular crates. This results in over 31,000 crates (roughly double the largest category
considered by [evans:icse:2020]). *[It is not clear whether this is better or worse.]*

They find

- 75% of crates do not use unsafe and that most usage is either unsafe blocks (in 20% of crates)
  or unsafe function declarations (13%).

- Most unsafe blocks are small but there are some huge outliers caused by macros or
  machine-generated code

- Surprisingly, unsafe code is more likely to invoke closures than safe code
  due to parameterization of safe wrappers to increase reuse.
  (e.g., the `sort_by` function)

- 52% of standard (non-closure, non trait-method) function calls from unsafe blocks are to the standard library,
  15% are to `-sys` libraries and 26% are to the same crate.
  Only 7% are to other crates.
  This shifts only slightly when restricted to standard *unsafe* calls.

  > This suggests that programmers hesitate to call *unsafe* functions that reach
  > out to other crates unless they explicitly wish to interact with system libraries.

  *[The pattern may be even stronger since they found that the `-sys` suffix naming
  convention was not consistently applied.]*

- Encapsulation: There is a strong bimodal distribution of crates that make unsafe functions
  public: either almost 100% of the unsafe functions they define are
  public or close to 0% are public.
  59% of the crates that export all their functions provide bindings to foreign functions
  or are a foreign export of Rust functions.
  Some examples are bindings to system libraries, OpenGL bindings, and microcontroller APIs.

  > ... for unsafe functions *implemented in Rust alone*, programmers avoid
  > making at least the vast majority publicly visible.


- Table 3 breaks down the reasons why blocks and functions need to be declared unsafe.
  Almost 90% call unsafe functions with dereferencing raw pointers and accessing
  mutable static variables making up most of the remainder.
  (Dereferencing raw pointers is sometimes an indication of FFI usage and
  sometimes an indication of limitations due to the borrow checker and
  ownership discipline.)

  ![Table 3]({{site.baseurl}}/images/astrauskas:oopsla:2020-3.png)

  In addition, 7% of all crates dereference at least one raw pointer.

- Type system limitations:
  Using use of 'transmute' as a proxy for limitations of the type system,
  they find 9% of unsafe blocks call 'transmute' functions.
  Most crates use these three times or less but some autogenerated
  code uses them a lot more.

- Use as documentation:
  36% of unsafe functions are written in completely safe Rust.
  This was partly from auto-generated code
  and possibly some accidents due to legacy reasons.
  Only rarely did it seem to be done to document properties such as invariants that
  the function might potentially break.[^unsafe-scope] [^unsafe-functions-that-are-safe]

[^unsafe-scope]:
    See Ralf Jung's [The scope of unsafe](https://www.ralfj.de/blog/2016/01/09/the-scope-of-unsafe.html)
    for a discussion of such invariants and how adding a function that
    does not use unsafe can break an otherwise correct module that uses
    unsafe elsewhere. In particular, he makes the point that *the following
    statement is not true*

    > in order to detect bugs in data structures like Vec it suffices to check functions involving unsafe code.

  [^unsafe-functions-that-are-safe]:
      [qin:pldi:2020] contains an example of `String::from_utf8_unchecked` as a function that is marked
      as 'unsafe' but that performs no unsafe operations.
      However, it is unsafe because the rest of the module relies on the fact that the string is
      correct utf8.
      An alternative choice would be to mark most/all other functions unsafe but it is considered
      better to focus on the creation of strings.:


- Intrinsics: Compiler intrinsics (core::intrinsics and std::intrinsics) are marked experimental/unstable
  and are not widely used.

- 5% of all crates provide bindings to foreign libraries.
  (Many such libraries do not adhere to the '-sys' name suffix convention.)

- Inline assembly is not common.

- Performance: 4.3% of all crates contain calls to unchecked functions

In the conclusions, they mention that many public, unsafe functions
that are not FFI functions do not document the requirements imposed
on their callers and suggest that development practice should be changed
and testers should highlight these cases.


{% include links.html %}

