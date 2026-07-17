# Question 33

*UGC NET CS · 2009 Dec Paper 2 · Intermediate Code Generation · Translation of Declarations*

A shift-reduce parser carries out the actions specified within braces immediately after reducing with the corresponding rule of the grammar. S → x x W [ print “1”] S → y [print “2”] W → S 2 [print “3”], what is the translation of “ x x x x y z z” ?

- **A.** 1 1 2 3 1
- **B.** 1 1 2 3 3
- **C.** 2 3 1 3 1
- **D.** 2 3 3 2 1

> [!TIP]
> **Correct answer: C. 2 3 1 3 1**

## Solution

The intended third production is W→Sz (the scan resembles 'S2'). Reduce the input xxxxyzz bottom-up: y→S prints 2; Sz→W prints 3; xxW→S prints 1; the next Sz→W prints 3; and the outer xxW→S prints 1. The translation is 2 3 1 3 1.

## Key Points

- For bottom-up parsing, record actions in reduction order, not production-expansion order.

## Why the other options are incorrect

The other sequences print actions in top-down derivation order or reorder reductions. A shift-reduce parser executes semantic actions when each handle is reduced, from the innermost phrase outward.
