# Question 11

*UGC NET CS · 2014 Dec Paper 2 · Programming in C · Post-Increment Expression Evaluation*

What is the output of this C code? main() { int x=128; printf("\n%d", 1+x++); }

- **A.** 128
- **B.** 129
- **C.** 130
- **D.** 131

> [!TIP]
> **Correct answer: B. 129**

## Solution

Post-increment yields the old value of x for the current expression, then increments x as a side effect. Thus x++ contributes 128 to 1+x++, making the printed expression 1+128=129. After evaluation x itself becomes 129, but that new value is not substituted back into the already evaluated addition.

## Key Points

- x++ returns the old value, then increments x; ++x increments first and would contribute the new value.

## Why the other options are incorrect

128 omits the explicit +1. 130 effectively treats post-increment as if both the increment and +1 affected the expression. 131 adds yet another nonexistent increment.
