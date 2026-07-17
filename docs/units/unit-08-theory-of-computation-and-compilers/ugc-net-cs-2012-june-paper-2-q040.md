# Question 40

*UGC NET CS · 2012 June Paper 2 · Turing Machines · Expressive Equivalence of Machine Models*

Consider the following statements : I. Recursive languages are closed under complementation. II. Recursively enumerable languages are closed under union. III. Recursively enumerable languages are closed under complementation. Which of the above statements are true ?

- **A.** I only
- **B.** I and II
- **C.** I and III
- **D.** II and III

> [!TIP]
> **Correct answer: B. I and II**

## Solution

I is true: a decider halts on all inputs, so swapping its accept and reject outcomes decides the complement. II is true: two recognizers can be dovetailed in parallel and accept when either accepts, recognizing the union. III is false: recursively enumerable languages are not generally closed under complement; if both a language and its complement are RE, the language is recursive.

## Key Points

- Recursive languages are complement-closed; RE languages are union-closed but not complement-closed.

## Why the other options are incorrect

A omits the valid union closure. C accepts the false complement closure and omits II. D also accepts III while rejecting the true recursive-complement statement I.
