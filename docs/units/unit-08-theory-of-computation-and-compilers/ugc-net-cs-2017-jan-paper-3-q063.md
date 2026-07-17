# Question 63

*UGC NET CS · 2017 Jan Paper 3 · Recursive and Recursively Enumerable Languages · Countability and Closure Properties*

Which of the following statements is false ?

- **1.** Every context-sensitive language is recursive.
- **2.** The set of all languages that are not recursively enumerable is countable.
- **3.** The family of recursively enumerable languages is closed under union.
- **4.** The families of recursively enumerable and recursive languages are closed under reversal.

> [!TIP]
> **Correct answer: 2. The set of all languages that are not recursively enumerable is countable.**

## Solution

There are only countably many Turing machines and therefore only countably many recursively enumerable languages. Over any nonempty finite alphabet, the set of all languages is the power set of the countably infinite set of strings, so it is uncountable. Removing the countable RE languages leaves uncountably many non-RE languages. Hence statement 2, which calls that set countable, is false.

## Key Points

- Machines are countable but languages are uncountable; consequently almost all languages are not recursively enumerable.

## Why the other options are incorrect

Statement 1 is true because an LBA has a finite configuration space on a fixed input, so context-sensitive membership is decidable. RE languages are closed under union by dovetailing recognizers, and both RE and recursive languages are closed under reversal by reversing the finite input before simulation.
