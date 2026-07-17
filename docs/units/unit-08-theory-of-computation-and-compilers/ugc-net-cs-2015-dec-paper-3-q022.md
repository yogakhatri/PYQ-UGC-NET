# Question 22

*UGC NET CS · 2015 Dec Paper 3 · Context-Sensitive Languages · Closure under Union and Reversal*

The family of context sensitive languages is __________ under union and __________ under reversal.

- **1.** closed, not closed
- **2.** not closed, not closed
- **3.** closed, closed
- **4.** not closed, closed

> [!TIP]
> **Correct answer: 3. closed, closed**

## Solution

Context-sensitive languages are closed under union: linear-bounded automata can nondeterministically choose which component recognizer to simulate. They are also closed under reversal: reverse the input and simulate an LBA for the original language, or equivalently reverse an appropriate context-sensitive construction. Thus both blanks are ‘closed’.

## Key Points

- CSL is closed under union and reversal (and, more deeply, complement).

## Why the other options are incorrect

Options 1, 2, and 4 deny one or both valid closure properties. Do not confuse context-sensitive languages with context-free languages, whose closure behavior is different for some operations.
