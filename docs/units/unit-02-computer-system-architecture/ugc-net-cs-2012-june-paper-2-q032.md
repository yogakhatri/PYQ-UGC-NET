# Question 32

*UGC NET CS · 2012 June Paper 2 · Memory Hierarchy · Cache and Interleaved Memory*

Cached and interleaved memories are ways of speeding up memory access between CPU’s and slower RAM. Which memory models are best suited (i.e. improves the performance most) for which programs ? (i) Cached memory is best suited for small loops. (ii) Interleaved memory is best suited for small loops (iii) Interleaved memory is best suited for large sequential code. (iv) Cached memory is best suited for large sequential code.

- **A.** (i) and (ii) are true.
- **B.** (i) and (iii) are true.
- **C.** (iv) and (ii) are true.
- **D.** (iv) and (iii) are true.

> [!TIP]
> **Correct answer: B. (i) and (iii) are true.**

## Solution

A small loop repeatedly executes the same instructions and often revisits the same data, giving strong temporal and spatial locality; once the working set enters cache, most accesses hit. Large sequential code offers little temporal reuse but generates a stream of consecutive addresses. Interleaved memory maps consecutive words to different banks, allowing overlapped or parallel accesses and higher bandwidth. Therefore (i) and (iii) are true.

## Key Points

- Cache exploits locality and reuse; bank interleaving accelerates sustained sequential access.

## Why the other options are incorrect

Interleaving gives little special benefit to a tiny repeatedly reused loop compared with a cache. A large one-pass sequential stream can exceed cache capacity and has limited reuse, so caching is not the best of the two models for statement (iv).
