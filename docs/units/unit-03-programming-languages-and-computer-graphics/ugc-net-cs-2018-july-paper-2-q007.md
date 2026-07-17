# Question 7

*UGC NET CS · 2018 July Paper 2 · Language Design and Translation Issues · Static and Strong versus Weak Type Systems*

Which statements are true? P: C has a weak type system with static types. Q: Java has a strong type system with static types.

- **1.** P only
- **2.** Q only
- **3.** Both P and Q
- **4.** Neither P nor Q

> [!TIP]
> **Correct answer: 3. Both P and Q**

## Solution

Under the conventional programming-language taxonomy used by the question, both statements are true. C is statically typed because types are checked largely at compile time, but is often called weakly typed because casts, pointer reinterpretation, promotions, and unchecked low-level operations can bypass abstractions. Java is also statically typed and is classed as strongly typed because it enforces stricter type compatibility and runtime safety checks. Therefore option 3 is correct.

## Key Points

- Static/dynamic describes when types are checked; strong/weak informally describes how strictly incompatible representations and operations are prevented.

## Why the other options are incorrect

Options 1 and 2 reject one of the standard textbook classifications, while option 4 rejects both. 'Strong' and 'weak' are informal terms without one universally formal boundary, so learn the concrete safety features behind the exam's labels rather than treating them as mathematical categories.
