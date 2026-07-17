# Question 52

*UGC NET CS · 2018 July Paper 2 · Memory Management · Average Memory Access Time*

In a paged memory, the page hit ratio is 0.40. The time required to access a page in secondary memory is equal to 120 ns. The time required to access a page in primary mem ory is 15 ns. The average time required to access a page is ________.

- **1.** 105
- **2.** 68
- **3.** 75
- **4.** 78

> [!TIP]
> **Correct answer: 4. 78**

## Solution

Use the weighted average of hit and miss access times. A hit occurs with probability 0.40 and costs 15 ns; a miss occurs with probability 0.60 and, under the question's stated convention, costs 120 ns. Hence average time=0.40×15+0.60×120=6+72=78 ns. Therefore option 4 is correct.

## Key Points

- Expected access time is Σ(probability of case × time for that case).

## Why the other options are incorrect

The other values do not use both probabilities with their corresponding times. In some architectures a miss cost may be written as secondary-access time plus a later primary-memory access, but the choices clearly treat the stated 120 ns as the complete secondary-page access cost.
