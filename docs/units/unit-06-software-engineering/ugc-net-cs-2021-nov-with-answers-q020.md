# Question 20

*UGC NET CS · 2021 Nov With Answers · Software Testing · Limits of Exhaustive Testing*

Given below are two statements, one is labelled as Assertion A and the other is labelled as Reason R Assertion A : Software developers donot do exhaustive software testing in practice. Reason R : Even for small inputs, exhaustive testing is too computationally intensive (e.g., takes too long) to run all the tests. In light of the above statements, choose the correct answer from the options given below

- **1.** Both A and R are true and R is the correct explanation of A
- **2.** Both A and R are true but R is NOT the correct explanation of A
- **3.** A is true but R is false
- **4.** A is false but R is true

> [!TIP]
> **Correct answer: 1. Both A and R are true and R is the correct explanation of A**

## Solution

Exhaustive testing would have to cover all input values, input sequences, states, paths, timing combinations, and environmental conditions. Even small-looking domains grow combinatorially, making the total number of tests too large to execute in practical time. Hence developers do not perform exhaustive testing in practice, and the computational explosion stated in R directly explains A. Both are true with R the correct explanation: option 1.

## Key Points

- The state/input space grows combinatorially, so practical testing samples strategically instead of enumerating everything.

## Why the other options are incorrect

Options 2–4 either break the genuine cause-and-effect link or declare a true statement false. Testing uses representative partitions, boundaries, risk priorities, and coverage criteria precisely because exhaustive enumeration is infeasible.
