# Question 101

*UGC NET CS · 2019 June Paper 1 And 2 · Software Design · Defect cost, cohesion and coupling*

Which statements are true? P: In software engineering, defects discovered earlier are more expensive to fix. Q: A software design is good if its components are strongly cohesive and weakly coupled.

- **1.** P only
- **2.** Q only
- **3.** P and Q
- **4.** Neither P nor Q

> [!TIP]
> **Correct answer: 2. Q only**

## Solution

P is false because the cost of correcting a defect generally increases the later it is discovered: an early requirements error is cheaper to repair than the same error after implementation or release. Q is true because good modular design aims for high cohesion within components and low coupling between components. Therefore only Q is true.

## Key Points

- Find defects early; design modules for strong internal cohesion and weak external coupling.

## Why the other options are incorrect

Options 1 and 3 accept the reversed defect-cost statement P. Option 4 incorrectly rejects the established cohesion/coupling principle.
