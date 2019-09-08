Title: Theoretical analysis of gate-level information flow tracking
Author: Jason Oberg and Wei Hu and Ali Irturk and Mohit Tiwari and Timothy Sherwood and Ryan Kastner
Venue: DAC10
Year: 2010
---

GLIFT (Gate Level Information Flow Tracking) calculates a precise "taint" bit for every signal indicating whether the signal depends on some input signals.  GLIFT is added by calculating taint for each primitive gate type (and, or, XOR, not) with an assumption of linearity.  This paper looks at how the number of midterms grows with circuit complexity for 1-8 bit adder, multiplier, comparator, shifter and multiplexer.  All costs are exponential and quite high.

Questions: Can linearity assumption be justified?  Is number of midterms the right metric?