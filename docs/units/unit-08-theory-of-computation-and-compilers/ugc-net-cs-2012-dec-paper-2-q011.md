# Question 11

*UGC NET CS · 2012 Dec Paper 2 · Code Generation and Optimization · Strength reduction*

In compiler design, reducing the strength refers to:

- **1.** reducing the range of values of input variables
- **2.** code optimization using cheaper machine instructions
- **3.** reducing program efficiency
- **4.** none of the above

> [!TIP]
> **Correct answer: 2. code optimization using cheaper machine instructions**

## Solution

Strength reduction is a code-optimization transformation that replaces an expensive operation with an equivalent cheaper one. Examples include replacing multiplication by a power of two with a shift, or replacing repeated index multiplication inside a loop with incremental addition. The program's meaning is preserved while execution cost is reduced.

## Key Points

- Strength reduction changes operation cost, not program meaning: expensive arithmetic is replaced by cheaper equivalent instructions.

## Why the other options are incorrect

It does not restrict the permitted values of input variables and certainly does not aim to reduce program efficiency. Since option 2 states the standard definition, 'none' is false.
