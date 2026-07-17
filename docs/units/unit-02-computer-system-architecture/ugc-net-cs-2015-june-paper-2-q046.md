# Question 46

*UGC NET CS · 2015 June Paper 2 · Parallel Computer Architecture · Amdahl's Law and Speedup*

For parallelization, Amdahl's law states that P is the parallelizable proportion and (1-P) is the non-parallelizable proportion. What maximum speed-up can be achieved with N processors?

- **1.** 1/[(1-P)+NP]
- **2.** 1/[(N-1)P+P]
- **3.** 1/[(1-P)+(P/N)]
- **4.** 1/[P+((1-P)/N)]

> [!TIP]
> **Correct answer: 3. 1/[(1-P)+(P/N)]**

## Solution

Normalize the original single-processor running time to 1. The serial fraction `(1-P)` cannot be reduced, while the parallel fraction `P` is ideally shared among `N` processors and takes `P/N`. The parallel running time is therefore `(1-P) + P/N`, and speedup is old time divided by new time: `S(N) = 1 / [(1-P) + P/N]`. This is option 3.

## Key Points

- Amdahl speedup = `1 / (serial fraction + parallel fraction / processor count)`.

## Why the other options are incorrect

Option 1 multiplies the parallel work by `N` instead of dividing it. Option 2 does not include the serial fraction correctly. Option 4 treats `P` as the serial portion, reversing the definitions supplied in the question.
