# Question 33

*UGC NET CS · 2016 July Paper 2 · Code Generation and Optimization · Loop Jamming (Loop Fusion)*

In _______, the bodies of the two loops are merged together to form a single loop provided that they do not make any references to each other.

- **1.** Loop unrolling
- **2.** Strength reduction
- **3.** Loop concatenation
- **4.** Loop jamming

> [!TIP]
> **Correct answer: 4. Loop jamming**

## Solution

Loop jamming, also called loop fusion, combines two adjacent loops into one loop when their iteration spaces are compatible and the transformation preserves data dependences. The merged body performs the work of both original bodies in each iteration. This reduces loop-control overhead and can improve locality, so option 4 is correct.

## Key Points

- Loop jamming/fusion merges compatible adjacent loops; legality depends on bounds and data-dependence preservation.

## Why the other options are incorrect

Loop unrolling duplicates a loop body to perform several iterations per test. Strength reduction replaces an expensive operation with a cheaper equivalent. 'Loop concatenation' is not the standard name intended by this compiler-optimization definition; the named transformation is loop jamming or loop fusion.

## References

- [LLVM Loop Fusion documentation](https://llvm.googlesource.com/llvm-project/llvm/+/refs/heads/main/docs/LoopFusion.rst)
