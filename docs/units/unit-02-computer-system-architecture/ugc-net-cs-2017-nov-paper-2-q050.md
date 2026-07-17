# Question 50

*UGC NET CS · 2017 Nov Paper 2 · Parallel Computer Architecture · Amdahl's Law and Maximum Speedup*

Which speed up could be achieved according to Amdahl’s Law for infinite number of processes if 5% of a program is sequential and the remaining part is ideally parallel ?

- **1.** Infinite
- **2.** 5
- **3.** 20
- **4.** 50

> [!TIP]
> **Correct answer: 3. 20**

## Solution

Amdahl's law gives speedup S(N)=1/[f+(1−f)/N], where f is the sequential fraction. Here f=0.05. As the number of processors N tends to infinity, the parallel term tends to zero, so Smax=1/0.05=20. Therefore option 3 is correct.

## Key Points

- With infinitely many processors, Amdahl's maximum speedup is the reciprocal of the serial fraction: Smax=1/f.

## Why the other options are incorrect

Speedup is not infinite because the sequential 5% remains a hard bottleneck. A speedup of 5 or 50 would correspond to different sequential fractions. Even perfect parallelization of the other 95% cannot reduce the serial execution time.
