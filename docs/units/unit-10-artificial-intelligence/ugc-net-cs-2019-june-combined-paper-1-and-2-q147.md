# Question 147

*UGC NET CS · 2019 June Paper 1 And 2 · Genetic Algorithms · Genetic Operators*

Consider (a) evolution, (b) selection, (c) reproduction, and (d) mutation. Which are operational components found in genetic algorithms?

- **A.** (b), (c) and (d) only
- **B.** (b) and (d) only
- **C.** (a), (b), (c) and (d)
- **D.** (a), (b) and (d) only

> [!TIP]
> **Correct answer: A. (b), (c) and (d) only**

## Solution

A genetic algorithm repeatedly selects fitter individuals, reproduces offspring—commonly through crossover—and introduces variation through mutation. Thus selection, reproduction and mutation are mechanisms in the algorithm. Evolution describes the overall population process that results from those mechanisms, not an additional genetic operator in the listed sense. Therefore (b), (c) and (d) only are selected.

## Key Points

- The standard GA cycle is fitness evaluation, selection, reproduction/crossover and mutation.

## Why the other options are incorrect

B omits reproduction. C and D count evolution as a separate operator, and D also omits reproduction.
