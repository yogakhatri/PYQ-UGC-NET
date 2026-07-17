# Question 59

*UGC NET CS · 2020 Nov With Answers · Performance Analysis and Recurrences · Iterated Multiplication and Logarithms*

Given integers a and b with a>1 and a<b, assume no overflow: `x=0; p=1; while (p<b) { p=p*a; x=x+1; }`. What is x when the loop terminates?

- **1.** a^b
- **2.** b^a
- **3.** ⌊log_a b⌋
- **4.** ⌈log_a b⌉

> [!TIP]
> **Correct answer: 4. ⌈log_a b⌉**

## Solution

Initially p=1=a^0 and x=0. Each iteration multiplies p by a and increments x, so after x iterations the invariant is p=a^x. The loop stops at the first integer x for which p≥b, that is, the smallest x satisfying a^x≥b. Taking base-a logarithms gives x≥log_a b, and the smallest integer meeting this inequality is ⌈log_a b⌉. Thus option 4.

## Key Points

- Establish p=a^x as a loop invariant; termination asks for the smallest integer exponent reaching b.

## Why the other options are incorrect

a^b and b^a describe huge values unrelated to the loop counter. The floor is wrong whenever b lies strictly between consecutive powers of a; another multiplication is then required. Ceiling also handles the exact-power case correctly.
