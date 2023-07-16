---
ENTRYTYPE: article
abstract: We introduce indexed streams, a formal operational model and intermediate representation that describes the fused execution of a contraction language
  that encompasses both sparse tensor algebra and relational algebra. We prove that the indexed stream model is correct with respect to a functional semantics.
  We also develop a compiler for contraction expressions that uses indexed streams as an intermediate representation. The compiler is only 540 lines of
  code, but we show that its performance can match both the TACO compiler for sparse tensor algebra and the SQLite and DuckDB query processing libraries
  for relational algebra.
added: 2023-07-02
address: New York, NY, USA
articleno: '154'
authors:
- Scott Kovach
- Praneeth Kolichala
- Tiancheng Gu
- Fredrik Kjolstad
doi: 10.1145/3591268
issue_date: June 2023
journal: Proc. ACM Program. Lang.
keywords: streams, operational semantics, functional programming, contractions
layout: paper
link: https://doi.org/10.1145/3591268
month: jun
number: PLDI
numpages: '25'
publisher: Association for Computing Machinery
read: false
readings: []
title: 'Indexed streams: A formal intermediate representation for fused contraction programs'
url: https://doi.org/10.1145/3591268
volume: '7'
year: 2023
notes:
- tensor
- sparse model
- loop fusion
- Lean theorem prover
papers:
---

Takes operators from "positive algebra" (that includes relational algebra),
shows that they work for tensor algebra,
uses to perform operator fusion on access patterns that are
hierarchical (ie multidimensional) and may skip value (ie sparse).

Compilation is in two steps:
(1) a "contraction language" expression is compiled to the indexed stream intermediate representation;
and
(2) the indexed stream representation is compiled to imperative C code.

The result is concise (the transformations are implemented in only 540 lines of Lean code);
matches (for performance) TACO (sparse operations), SQLite (relational operators) and DuckDB (relational operators);
and is proved correct in the [Lean theorem prover].


The contraction language consists of variables, addition, multiplication, contraction, expansion and renaming.
Contraction aggregates (sums) values across a dimension/attribute.
Expansion repeats a value across a dimension/attribute.

Indexed streams have four operators:

- ready - is there a value at the current index
- skip - advance index according to an index value
- index - current index value. This is a lower bound on the next ready index state.
- value - index at current index

Streams are monotone: "index(q) <= index(skip(q, (i,r)))"

{% include links.html %}
