# Question 43

*UGC NET CS · 2017 Jan Paper 2 · Software Design · Cohesion and Coupling*

Which of the following statement(s) is/are true with respect to software architecture ? S1 : Coupling is a measure of how well the things grouped together in a module belong together logically. S2 : Cohesion is a measure of the degree of interaction between software modules. S3 : If coupling is low and cohesion is high then it is easier to change one module without affecting others.

- **1.** Only S1 and S2
- **2.** Only S3
- **3.** All of S1, S2 and S3
- **4.** Only S1

> [!TIP]
> **Correct answer: 2. Only S3**

## Solution

S1 is false because it defines cohesion—the logical relatedness of responsibilities within one module—not coupling. S2 is false because interaction or dependence between different modules is coupling, not cohesion. S3 is true: high cohesion localizes related work inside modules, while low coupling limits dependencies, so changing one module is less likely to affect others. Hence only S3 is true, option 2.

## Key Points

- Cohesion is within a module; coupling is between modules.
- Prefer high cohesion and low coupling.

## Why the other options are incorrect

Options 1, 3, and 4 accept S1 or S2 even though the two definitions have been swapped. The desired design combination is explicitly the one in S3.
