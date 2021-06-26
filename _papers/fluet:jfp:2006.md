---
ENTRYTYPE: article
added: 2021-06-19
authors:
- Matthew Fluet
- Riccardo Pucella
doi: 10.1017/S0956796806006046
journal: Journal of Functional Programming
layout: paper
number: '6'
pages: 751-791
publisher: Cambridge University Press
read: true
readings:
- 2021-06-26
title: Phantom types and subtyping
volume: '16'
year: 2006
notes:
- phantom types
- foreign function interface
papers:
- reppy:att:1996
- finne:icfp:1999
- blume:babel:2001
---

When creating a safe interface to code in another language, you want
to encode the type system of the other language.
This paper describes a general encoding of subtyping hierarchies
in the Hindley-Milner type system using [phantom types]
and generalizes [reppy:att:1996], [finne:icfp:1999]
and [blume:babel:2001].

The essence of the encoding is as follows (see section 5.4 for a worked example)

1. To define a dummy datatype corresponding to each sort within the type
   hierarchy. For example given "A > B, A > C, C > D, C > E", you create[^haskell-syntax]

   [^haskell-syntax]:
       Note that the paper uses ML syntax but I have switched it to Haskell syntax.

   ```
   datatype A a
   datatype B a
   datatype C a
   datatype D a
   datatype E a
   ```

   The type parameter 'a' is used to encode subtyping

2. Represent each concrete subtype by the path from the root to that subtype
   and ending in '()'.

   ```
   type A_conc = A ()
   type B_conc = A (B ())
   type C_conc = A (C ())
   type D_conc = A (C (D ()))
   type E_conc = A (C (E ()))
   ```


3. Represent each abstract subtype by the path from the root to that subtype
   and ending in a type variable 'a'

   ```
   type A_abs a = A a
   type B_abs a = A (B a)
   type C_abs a = A (C a)
   type D_abs a = A (C (D a))
   type E_abs a = A (C (E a))
   ```

   Note that a concrete subtype 'c' unifies with an abstract subtype 'a' only
   if 'c' is a subtype of 'a'.

4. Use these types as 'phantom' type parameters when defining the mapping to
   the other language.  For example, if the representation in C is a
   32-bit value, that has the above 5 subsorts, we might define

   ```
   newtype T a = T Word32
   mkA :: IO (T A_conc)
   mkB :: IO (T B_conc)
   mkC :: IO (T C_conc)
   mkD :: IO (T D_conc)
   mkE :: IO (T E_conc)
   addB :: T (C_abs a) -> T (C_abs a) -> T C_conc
   ```

   Which (if I got this example right) lets you add values that are
   any subtype of C and return something with the type C and prevents
   you from accidentally adding values of subtype A or B.

Type hierarchies that are not trees (i.e., that have multiple inheritance)
can be encoded as an embedding into powerset lattices created using 
the product of two phantom types.
And that leads to a more flexible but less readable alternative type encoding
with types that look like "(T (T a), (b, c))"

Extending this approach to a form of bounded polymorphism is restricted
by ML's use of "prenex parametric polymorphism". That is, all type quantifiers
go on the outside of the type.

{% include links.html %}
