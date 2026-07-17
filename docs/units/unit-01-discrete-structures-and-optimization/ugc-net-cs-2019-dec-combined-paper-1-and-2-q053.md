# Question 53

*UGC NET CS · 2019 Dec Paper 1 And 2 · Boolean Algebra · Boolean Functions and their Representation*

The Boolean expression AB + A(not B) + (not A)C + AC is unaffected by the value of which Boolean variable?

- **1.** A
- **2.** B
- **3.** C
- **4.** A,B and C

> [!TIP]
> **Correct answer: 2. B**

## Solution

Group the first two terms and the last two terms: AB+A¬B=A(B+¬B)=A, while ¬AC+AC=C(¬A+A)=C. The whole expression simplifies to A+C. Variable B has disappeared, so changing B cannot affect the result. Therefore option 2 is correct.

## Key Points

- Use X+¬X=1 after factoring complementary terms; a variable absent from the simplified expression is irrelevant to the output.

## Why the other options are incorrect

A and C remain in the simplified function A+C, so changing either can change the output; for example A=C=0 gives 0, while setting either to 1 gives 1. Thus the function is not independent of A, C, or all three variables.
