# Question 8

*UGC NET CS · 2013 Dec Paper 3 · Software Testing · Boundary and Equivalence Limitations*

One weakness of boundary value analysis and equivalence partitioning is

- **A.** they are not effective.
- **B.** they do not explore combinations of input circumstances.
- **C.** they explore combinations of input circumstances.
- **D.** none of the above.

> [!TIP]
> **Correct answer: B. they do not explore combinations of input circumstances.**

## Solution

Equivalence partitioning selects representatives from input classes, and boundary-value analysis targets values at class edges. Applied one variable at a time, neither systematically covers interactions among several input conditions. Combination-oriented methods such as decision tables, pairwise testing or cause-effect graphs address that gap.

## Key Points

- Equivalence and boundary tests cover individual input domains well but may miss multi-input interactions.

## Why the other options are incorrect

The techniques are effective for their intended purpose, so A is too broad. C states the opposite of the weakness. Therefore 'none' is false.
