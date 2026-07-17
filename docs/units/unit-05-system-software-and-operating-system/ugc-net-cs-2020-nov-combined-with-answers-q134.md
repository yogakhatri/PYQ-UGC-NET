# Question 134

*UGC NET CS · 2020 Nov With Answers · Processes and System Calls · Counting Processes and Output after fork*

Assuming fork() never fails, consider two C programs on UNIX/Linux. P1: int main(){ fork(); fork(); fork(); printf("Happy\n"); } P2: int main(){ fork(); printf("Happy\n"); fork(); printf("Happy\n"); fork(); printf("Happy\n"); } Statement I: P1 displays Happy 8 times. Statement II: P2 displays Happy 12 times.

- **1.** Both statements are true
- **2.** Both statements are false
- **3.** Statement I is true but Statement II is false
- **4.** Statement I is false but Statement II is true

> [!TIP]
> **Correct answer: 3. Statement I is true but Statement II is false**

## Solution

In P1, each of the three fork calls doubles the number of running processes: 1→2→4→8. All eight reach the single printf, so Statement I is true. In P2, the first fork creates 2 processes and the first printf executes twice; the second fork creates 4 processes and the next printf executes four times; the third creates 8 processes and the last printf executes eight times. The total is 2+4+8=14, not 12, so Statement II is false. The answer is option 3.

## Key Points

- After each unconditional fork, double the process count; for interleaved output, add the number of processes present at each printf.

## Why the other options are incorrect

Options 1 and 4 accept the incorrect total of 12, while option 2 rejects the correct 2^3=8 count for P1. The intended exam model counts each reached printf once; it abstracts away unusual output-buffer duplication when stdout is redirected.
