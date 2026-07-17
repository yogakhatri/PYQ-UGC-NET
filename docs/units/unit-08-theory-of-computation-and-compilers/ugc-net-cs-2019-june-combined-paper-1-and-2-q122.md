# Question 122

*UGC NET CS · 2019 June Paper 1 And 2 · Intermediate Code Generation · Three-Address Code and Quadruples*

On translating the expression (i*j) + (e+f)*(a*b+c) into quadruple representation, how many operations are required?

- **1.** 5
- **2.** 6
- **3.** 3
- **4.** 7

> [!TIP]
> **Correct answer: 2. 6**

## Solution

Generate one quadruple per binary operation: t1=i*j (1), t2=e+f (2), t3=a*b (3), t4=t3+c (4), t5=t2*t4 (5), and t6=t1+t5 (6). The expression therefore requires six operations and six corresponding quadruples.

## Key Points

- For a binary expression represented by ordinary three-address code, count its operator nodes: one quadruple per operator.

## Why the other options are incorrect

The expression contains three multiplications and three additions. Counts 3 and 5 omit operators, while 7 introduces an operation that is not present; assigning a result to a temporary is part of each quadruple, not an extra arithmetic operation.
